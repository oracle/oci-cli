from prompt_toolkit.key_binding.bindings import named_commands
from prompt_toolkit import key_binding
from interactive.utils import REQUIRED_PARAM_EXCEPTION
from interactive.error_messages import get_error_message
from prompt_toolkit.application import get_app


# find cmd name "oci os ns get" from buffer text
def find_command_name(text):
    cmd = "oci " + text.split("-")[0]
    return cmd.strip()


# buffer.text can have optional params
# buffer.text can have either -c or --compartment-id
def find_all_typed_params_on_command_line(text):
    cmd = text.split()
    params = []
    for p in cmd:
        if p.startswith("-"):
            params.append(p)
    return params


def all_required_param_selected(text, list_of_required_params):
    missing_required_param = []
    cmd = find_command_name(text)
    exception = REQUIRED_PARAM_EXCEPTION
    if cmd in exception:
        return missing_required_param

    typed_params = find_all_typed_params_on_command_line(text)
    for param_opts in list_of_required_params:
        found = False
        # param_opts is a tuple ('--compartment-id', '-c')
        for param in param_opts:
            if param in typed_params:
                found = True
        if not found:
            missing_required_param.append(param_opts[0])

    return missing_required_param


def override_key_binding(**kwargs):
    kb = key_binding.KeyBindings()

    @kb.add("backspace")
    def _backspace(event) -> None:
        # Normal backspace event
        named_commands.backward_delete_char(event)
        # Empty string is inserted to invoke completer
        event.current_buffer.insert_text("")

    @kb.add("c-d")
    def _quit_interactive(event) -> None:
        # Quit Interactive CLI when user presses [CTRL + D]
        get_app().exit()

    @kb.add("enter")
    def _enter_key(event) -> None:
        # the main purpose of this function is, pressing enter chooses the option then pressing enter again executes the
        # command
        buffer = event.current_buffer
        missing_required_param = all_required_param_selected(
            buffer.text, kwargs["completer"].list_of_required_params
        )
        if (
            not buffer.text or not buffer.complete_state
        ):  # If in the beginning or no menu(meaning menu is already chosen)
            if not missing_required_param:
                named_commands.accept_line(event)
            else:
                kwargs["toolbar"].set_toolbar_text(
                    get_error_message(
                        "missing_required_params", str(missing_required_param)
                    ),
                    is_error=True,
                )
        else:  # Copy the current selection and append it a new document
            document_with_selection, _ = buffer.document.cut_selection()
            buffer.reset()
            buffer.document = document_with_selection

    @kb.add("f7")
    def _clear_history(event) -> None:
        buffer = event.current_buffer

        # Clear history when user presses [F7] shortcut keys
        try:
            # Clear Command History
            cli_interactive_history = buffer.history
            cli_interactive_history.delete_history_file()

            # Clear Cache
            buffer.reset()

        # Notify User
        except Exception as e:
            kwargs["toolbar"].set_toolbar_text(
                get_error_message("try_again"),
                is_error=True,
            )
        else:
            kwargs["toolbar"].set_toolbar_text(
                get_error_message("history_clear"),
                is_error=False,
            )

    return kb
