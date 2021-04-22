# coding: utf-8
# Copyright (c) 2016, 2021, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

import os
import oci
import logging

logger = logging.getLogger("{}".format(__name__))
logger.addHandler(logging.NullHandler())
logger.setLevel(logging.DEBUG)


class Metrics():

    CLI_STANDARD_PRE_INVOCATION_DELAY_VAR = "OCI_CLI_METRICS_INV_DELAY"
    CLI_STANDARD_PRE_INVOCATION_DELAY = 5  # seconds
    CLOUDSHELL_ENV_VAR = "OCI_CLI_METRICS_PATH"

    METRICS = {
        # Metric name: filename
        "NUM_INVOCATIONS": "num_invocations",
        "NUM_AUTH_FAILURES": "num_auth_failures",
        "NUM_SLOW_INVOCATIONS": "num_slow_invocations",
        "NUM_CONN_FAILURES": "num_conn_failures"
    }

    @classmethod
    def get_pre_invocation_delay(cls):
        delay = Metrics.CLI_STANDARD_PRE_INVOCATION_DELAY
        if Metrics.CLI_STANDARD_PRE_INVOCATION_DELAY_VAR in os.environ:
            try:
                delay = int(os.getenv(Metrics.CLI_STANDARD_PRE_INVOCATION_DELAY_VAR))
            except Exception:
                pass

        return max(delay, Metrics.CLI_STANDARD_PRE_INVOCATION_DELAY)

    @classmethod
    def is_metrics_enabled(cls):
        return Metrics.CLOUDSHELL_ENV_VAR in os.environ

    @classmethod
    def update_metric(cls, metric_name, debug=False):

        if not Metrics.is_metrics_enabled():
            if debug:
                logger.debug(oci.base_client.utc_now() + "Metrics is not enabled")
            return

        # this import does not work on Windows
        # Currently only being used for CloudShell instances which are not Windows instances
        import fcntl

        metric_dir = os.getenv(Metrics.CLOUDSHELL_ENV_VAR)
        metric_file = os.path.join(metric_dir, Metrics.METRICS[metric_name])

        if debug:
            logger.debug(oci.base_client.utc_now() + "Metrics is enabled with value: " + metric_dir)
            logger.debug(oci.base_client.utc_now() + "Metric being logged: " + Metrics.METRICS[metric_name])

        metric_value = 0
        try:
            with open(metric_file) as m:
                metric_value = int(m.read().strip())
        except Exception:
            pass
        except IOError:
            pass
        metric_value += 1
        if debug:
            logger.debug(oci.base_client.utc_now() + "New value of metric: " + str(metric_value))
        with open(metric_file, 'w') as m:
            try:
                fcntl.flock(m, fcntl.LOCK_EX | fcntl.LOCK_NB)
            except IOError:
                if debug:
                    logger.debug(oci.base_client.utc_now() + "Unable to write metric to file due to lock")
                return
            m.write("%d\n" % metric_value)
            fcntl.flock(m, fcntl.LOCK_UN)

        if debug:
            logger.debug(oci.base_client.utc_now() + "Metric file updated successfully")
