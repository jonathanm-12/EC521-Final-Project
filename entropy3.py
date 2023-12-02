import math
import string
import re

def calculate_entropy(s):
    """
    Calculate the Shannon entropy of a string.
    """
    if not s:
        return 0
    entropy = 0.0
    for x in dict.fromkeys(list(s)):
        p_x = float(s.count(x)) / len(s)
        if p_x > 0:
            entropy += (p_x * math.log(p_x, 2))
    return -entropy

def is_high_entropy(s, threshold=3.5):
    """
    Check if a string has high entropy, typically above a certain threshold.
    """
    return calculate_entropy(s) > threshold

def find_high_entropy_strings(file_path, threshold=3.0, min_length=10):
    high_entropy_strings = []

    with open(file_path, 'r') as file:
        for line in file:
            words = re.findall(r'"([^"]*)"', line)

            for word in words:
                if len(word) >= min_length and all(c in string.ascii_letters + string.digits + "-_=" for c in word):
                    entropy = calculate_entropy(word)
                    if entropy > threshold:
                        high_entropy_strings.append(word)

    return high_entropy_strings

file_path = '/Users/jueunkang/test.py'
high_entropy_strings = find_high_entropy_strings(file_path)
print("High entropy strings (potential API keys):", high_entropy_strings)
