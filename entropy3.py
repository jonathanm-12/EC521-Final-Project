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

def matches_api_pattern(s):
    """
    Check if the string matches known API key patterns.
    """
    return any(re.match(pattern, s) for pattern in api_key_patterns)

def find_high_entropy_strings(source, is_url=False, threshold=3.0, min_length=10):
    high_entropy_strings = []

    if is_url:
        req = requests.get(source)
        content = req.text.splitlines()
    else:
        with open(source, 'r') as file:
            content = file.readlines()


    with open(file_path, 'r') as file:
        for line in file:
            words = re.findall(r'"([^"]*)"', line)

            for word in words:
                if len(word) >= min_length and all(c in string.ascii_letters + string.digits + "-_=" for c in word):
                    if is_high_entropy(word, threshold) or matches_api_pattern(word):
                        high_entropy_strings.append(word)

    return high_entropy_strings


"""
for testing entropy
file_path = '/Users/jueunkang/test.py'
high_entropy_strings = find_high_entropy_strings(file_path)
print("High entropy strings (potential API keys):", high_entropy_strings)
"""


""""
in scan.py:
from entropy import find_high_entropy_strings

inside "def fetch_github_data"
high_entropy_strings = find_high_entropy_strings(repo_url)
output_area.insert('end', f"\nHigh Entropy Strings (potential API keys):\n{high_entropy_strings}\n")
"""
