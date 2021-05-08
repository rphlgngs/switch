"""
    File name: switch.py
    Author: Raphaël GUINGOIS
    Date created: 08/05/2021
    Date last modified: 08/05/2021
    Python Version: 3.9
"""


def switch(variable_to_test, list_of_cases, default_value=None):
    """

    :param variable_to_test: Variable we want to test
    :param list_of_cases: Dict of all possible cases
    :param default_value: Default value to return. None if not provided
    :return: The value corresponding to the test
    """

    # We loop the dictionary
    for key, value in list_of_cases.items():
        # If there is a match, we return the corresponding value
        if variable_to_test == key:
            return value

    # Else, we return the default value
    return default_value
