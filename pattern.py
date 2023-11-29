"""
def get_values(*names):
    import json
    _all_values = json.loads('''{"int_example":1,"float_example":1.0,"string_example":"string_example","options_boolean_example":"True","options_string_example":"options_string_example","options_int_example":0,"options_float_example":99.999}''')
    return [_all_values[n] for n in names]
"""

def get_values_test(*names):
    import json
    _all_values = json.loads('''{"int_example":2,"float_example":2.0,"string_example":"string_example2","options_boolean_example":"False","options_string_example":"options_string_example2","options_int_example":2,"options_float_example":100.01}''')
    return [_all_values[n] for n in names]

metadata = {
    'author': 'Opentrons <protocols@opentrons.com>',
    'source': 'Protocol Library',
    }

requirements = {
    "robotType": "Flex",
    "apiLevel": "2.15",
}


def run(protocol):

    # Instantiate and set the defaults for your variables
    # that are mapped to the protocol parameters
    # These should match the defaults defined in your parameters json
    int_example = 1
    float_example = 1.0
    string_example = "string_example"
    options_boolean_example = True
    options_string_example = "options_string_example"
    options_int_example = 0
    options_float_example = 99.999
    # TODO file_example = ""

    # if the get_values function is defined,
    # as it would be when this protocol is downloaded from the protocol library,
    # read the values from the json string there
    # overwriting the defaults defined above
    try:
        [int_example,float_example,string_example,options_boolean_example,options_string_example,options_int_example,options_float_example] = get_values("int_example","float_example","string_example","options_boolean_example","options_string_example","options_int_example","options_float_example")
    except (NameError):
        # get_values is not defined, so proceed with defaults
        print("get_values is not defined, so proceed with defaults")
    
    ################## for testing ##################
    try:
        [int_example,float_example,string_example,options_boolean_example,options_string_example,options_int_example,options_float_example] = get_values_test("int_example","float_example","string_example","options_boolean_example","options_string_example","options_int_example","options_float_example")
    except (NameError):
        # get_values_test is not defined, so proceed with defaults
        print("get_values_test is not defined, so proceed with defaults")

    print(locals())


def main():
    print("main")
    run(None)

if __name__ == "__main__":
    main()