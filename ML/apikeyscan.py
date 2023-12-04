import re
import os


def extract_string(file_path):
    with open(file_path, 'r') as file:
        content = file.read()
    pattern = r'''(['`"])(.*?)\1'''
    matches = re.findall(pattern, content)
    combined_text = ' '.join([match[1] for match in matches])
    return combined_text.split(' ')

# Testing the function
# text = '''This is a "sample" text with 'strings' in different markers. `idk`  '''
# print(extract_string(text))


# file_path = 'sample.py'
# print(extract_string("D:\Code\BU\EC551\Program1\main.py"))


directory = os.fsencode("D:\Code\BU\SC\TestRepo")
    
strings = set()

for root, dirs, files in os.walk(directory):
    for file in files:
        # Perform actions on each file
        try:
            file_path = os.path.join(root, file)
            print(file_path)  # Example action: print the file path
            s = extract_string(file_path)

            s = set(s)
            strings = strings.union(s)
        except:
            continue


print(len(strings))
print((strings))
import json
with open('false.json', 'w') as f:
    json.dump(list(strings), f)