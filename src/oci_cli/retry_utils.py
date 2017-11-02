from oci import exceptions
from oci import Response
from requests.exceptions import Timeout
from requests.exceptions import ConnectionError


import retrying


DEFAULT_RETRY_STRATEGY_NAME = 'default'


def retry_on_timeouts_connection_internal_server_and_throttles(exception):
    retryable = False
    if isinstance(exception, Timeout):
        retryable = True
    elif isinstance(exception, ConnectionError):
        retryable = True
    elif isinstance(exception, exceptions.ServiceError):
        # 500+ == Internal Server Error
        # -1 == Unknown
        # 429 == TooManyRequests (throttled)
        if exception.status >= 500 or exception.status == -1 or exception.status == 429:
            retryable = True

    return retryable


def list_call_get_up_to_limit_with_default_retries(list_func_ref, record_limit, page_size, **func_kwargs):
    return list_call_get_up_to_limit(list_func_ref, record_limit, page_size, DEFAULT_RETRY_STRATEGY_NAME, **func_kwargs)


def list_call_get_up_to_limit(list_func_ref, record_limit, page_size, retry_strategy_name, **func_kwargs):
    # If no limit was provided, make a single call
    if record_limit is None:
        return call_function_with_retries(list_func_ref, retry_strategy_name, **func_kwargs)

    # If we have a limit, make calls until we get that amount of data
    keep_paginating = True
    remaining_items_to_fetch = record_limit
    call_result = None
    aggregated_results = []
    while keep_paginating and remaining_items_to_fetch > 0:
        if page_size:
            func_kwargs['limit'] = min(page_size, remaining_items_to_fetch)
        elif 'limit' in func_kwargs:
            func_kwargs['limit'] = min(func_kwargs['limit'], remaining_items_to_fetch)

        call_result = call_function_with_retries(list_func_ref, retry_strategy_name, **func_kwargs)
        aggregated_results.extend(call_result.data)
        remaining_items_to_fetch -= len(call_result.data)

        if call_result.next_page is not None:
            func_kwargs['page'] = call_result.next_page

        keep_paginating = call_result.has_next_page

    # Truncate the list to the first limit items, as potentially we could have gotten more than what the caller asked for
    final_response = Response(call_result.status, call_result.headers, aggregated_results[:record_limit], call_result.request)
    return final_response


def list_call_get_all_results_with_default_retries(list_func_ref, **func_kwargs):
    return list_call_get_all_results(list_func_ref, DEFAULT_RETRY_STRATEGY_NAME, **func_kwargs)


def list_call_get_all_results(list_func_ref, retry_strategy_name, **func_kwargs):
    keep_paginating = True
    call_result = None
    aggregated_results = []

    while keep_paginating:
        call_result = call_function_with_retries(list_func_ref, retry_strategy_name, **func_kwargs)
        aggregated_results.extend(call_result.data)

        if call_result.next_page is not None:
            func_kwargs['page'] = call_result.next_page

        keep_paginating = call_result.has_next_page

    post_processed_results = aggregated_results
    if 'sort_by' in func_kwargs:
        if func_kwargs['sort_by'].upper() == 'DISPLAYNAME':
            sort_direction = 'ASC'
            if 'sort_order' in func_kwargs:
                sort_direction = func_kwargs['sort_order'].upper()

            post_processed_results = sorted(aggregated_results, key=lambda r: getattr(r, 'display_name'), reverse=(sort_direction == 'DESC'))
        elif func_kwargs['sort_by'].upper() == 'TIMECREATED':
            sort_direction = 'DESC'
            if 'sort_order' in func_kwargs:
                sort_direction = func_kwargs['sort_order'].upper()

                post_processed_results = sorted(aggregated_results, key=lambda r: getattr(r, 'time_created'), reverse=(sort_direction == 'DESC'))

    # Most of this is just dummy since we're discarding the intermediate requests
    final_response = Response(call_result.status, call_result.headers, post_processed_results, call_result.request)

    return final_response


def call_funtion_with_default_retries(func_ref, **func_kwargs):
    return call_function_with_retries(func_ref, DEFAULT_RETRY_STRATEGY_NAME, **func_kwargs)


# Generic wrapper which can be used to call with retries the function referenced by func_ref
# with the keyword arguments defined in the func_kwargs dict.
def call_function_with_retries(func_ref, retry_strategy_name, **func_kwargs):
    retry_strategy = RetryStrategies().get_retry_strategy(retry_strategy_name)
    if retry_strategy is None:
        raise RuntimeError('No retry strategy with name {} is defined'.format(retry_strategy_name))

    return retry_strategy.call(func_ref, **func_kwargs)


# A singleton which serves as a repository of retry strategies which are available to the application.
# This contains some default strategies, as well as allowing callers to define their own
# strategies and store them here so that they don't have to create the same retrying.Retry objects
# over and over again
class RetryStrategies:
    __instance = None

    # A default strategy with the following attributes:
    #
    #   - 3 attempts
    #    - Exponential back off of (2 ^ retries) seconds
    #    - Random jitter between retries of 0-2 seconds
    #    - Retry on timeouts, connection errors, internal server errors and throttles
    __default_retry_strategy = retrying.Retrying(
        stop_max_attempt_number=3,
        wait_exponential_multiplier=1000,
        wait_exponential_max=10000,
        wait_jitter_max=2000,
        retry_on_exception=retry_on_timeouts_connection_internal_server_and_throttles
    )

    # Allows us to store different retry strategies so that we don't have to create Retry objects
    # all the time
    __availabile_strategies = {
        DEFAULT_RETRY_STRATEGY_NAME: __default_retry_strategy
    }

    def __new__(cls):
        if RetryStrategies.__instance is None:
            RetryStrategies.__instance = object.__new__(cls)
        return RetryStrategies.__instance

    def add_retry_strategy(self, strategy_name, retrying_obj):
        if not strategy_name or not retrying_obj:
            raise RuntimeError('A strategy name and retry strategy object must be provided')

        if strategy_name == DEFAULT_RETRY_STRATEGY_NAME:
            raise RuntimeError('You cannot overwrite the default strategy')

        self.__availabile_strategies[strategy_name] = retrying_obj

    def get_retry_strategy(self, strategy_name):
        return self.__availabile_strategies.get(strategy_name, None)

    def get_default_retry_strategy(self):
        return self.__default_retry_strategy
