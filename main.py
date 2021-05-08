"""
    File name: main.py
    Author: Raphaël GUINGOIS
    Date created: 08/05/2021
    Date last modified: 08/05/2021
    Python Version: 3.9
"""

from switch import switch

# Dict of cases
cases = {1: "one", 2: "two", 3: "three", 4: "four"}

# We test with the number 3
variable_to_test = 3

# Now we try ... (with "No match" default value)
print(switch(variable_to_test, cases, "No match"))

# We test with the number 5
variable_to_test = 5

print(switch(variable_to_test, cases, "No match"))
