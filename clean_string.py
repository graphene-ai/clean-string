# TODO: Turn this into a package

import re

def clean_string(input):
    # Make sure input is a string
    input = input if type(input) is str else ''

    # Turn everything into lower case
    input = input.lower().strip()

    # Remove unwanted characters
    input = re.sub(r"[^a-z\ ]", ' ', input, 0, re.MULTILINE)

    # Remove multiple spaces
    input = re.sub(r"\ +", ' ', input, 0, re.MULTILINE)

    # Return stripped output
    return input.strip()

# Run validation tests

tests = [
    # ["input", "expected output"]
    ["eVeRyThInG SmAlL", "everything small"],
    ["  no   extra\tspaces  ", "no extra spaces"],
    ["no 12 numbers 423", "no numbers"],
    ["holy @#$%", "holy"],
    ["no p10 characters j3j3 with 100k numbers", "no characters with numbers"],
    ["<html>no tags<html>", "no tags"],
    ["&amp; no escapes &quo;", "no escapes"],
    ["hypenated-words are okay", "hypen-words are okay"],
    ["but dashes—are–not - okay", "but dashes are not okay"],
    ["it's a small world", "its a small world"],
    ["remove 🥳 emojis", "remove emojis"],
    ["twitter @handle", "twitter"],
    ["no domains indigoresearch.xyz", "no domains"],
    ["no full links https://indigoresearch.xyz/", "no domains"],
]

total_passed = 0
total_tests = len(tests)

for test in tests:
    input = test[0]
    correct = test[1]
    output = clean_string(input)
    passed = output == correct
    passed_text = '\033[92mPASSED\033[0m' if passed else '\033[91mFAILED\033[0m'

    print(f'{passed_text}: "{input}" --> "{output}" == "{correct}"')

    if passed:
        total_passed = total_passed + 1

print(f'Passed {total_passed} out of {total_tests}')