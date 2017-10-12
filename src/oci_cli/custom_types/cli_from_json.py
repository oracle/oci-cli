import click


# A datatype for the --from-json parameter. This is just a string (and so we report it is a text type in click) and will
# pass through any value given to it (in this sense it behaves like click's UNPROCESSED type).
#
# The only special behaviour it has is to store metadata information provided at construction time so it can be used when
# parsing data (either a command line string or input from a file) given by a caller.
#
# We need to decorate against the type because when the --from-json parameter is evaluated the metadata information from
# @json_skeleton_utils.json_skeleton_wrapper_metadata is not yet available. The --from-json
# parameter is eager evaluated and is also evaluated before the actual Python function for the click command is called,
# and the information from @json_skeleton_utils.json_skeleton_wrapper_metadata is only available once the command is called
class CliFromJson(click.ParamType):
    name = 'text'

    def __init__(self, json_input_metadata):
        if json_input_metadata:
            self.json_input_metadata = json_input_metadata
        else:
            self.json_input_metadata = {}

    def convert(self, value, param, ctx):
        return value

    def __repr__(self):
        return 'FROM_JSON'
