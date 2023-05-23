from collections import Counter

def is_valid_string(s):
    # Count the frequency of each character in the string
    char_frequency = Counter(s)

    # Count the frequency of frequencies
    frequency_frequency = Counter(char_frequency.values())

    # If there is only one unique frequency, the string is valid
    if len(frequency_frequency) == 1:
        return "YES"

    # If there are exactly two unique frequencies and one frequency has a count of 1, the string is valid
    if len(frequency_frequency) == 2 and (1 in frequency_frequency.values() and frequency_frequency[1] == 1):
        return "YES"

    return "NO"

# Test case 1
s = "abc"
print(is_valid_string(s))  # Output: YES

# Test case 2
s = "abcc"
print(is_valid_string(s))  # Output: NO

# Test case 3
s = "aabbcc"
print(is_valid_string(s))  # Output: YES

# Test case 4
s = "aabbccc"
print(is_valid_string(s))  # Output: YES

## The is_valid_string function takes a string s as input.
## The frequency of each character in the string is counted using the Counter class from the collections module. The result is stored in the char_frequency dictionary, where the keys are characters and the values are their frequencies.
## The frequency of frequencies is counted by applying Counter on the values of char_frequency. The result is stored in the frequency_frequency dictionary, where the keys are the unique frequencies and the values are their counts.
## If there is only one unique frequency (i.e., len(frequency_frequency) == 1), it means all characters have the same frequency, and the string is valid. In this case, "YES" is returned.
## If there are exactly two unique frequencies (i.e., len(frequency_frequency) == 2), the string can be valid if one of the frequencies has a count of 1. This means that one character occurs only once in the string, and removing it will make all the remaining characters have the same frequency. In this case, "YES" is returned.
## If none of the above conditions are met, the string is not valid, and "NO" is returned.