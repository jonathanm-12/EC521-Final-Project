import json
import random
import string
import uuid
import datetime
import hashlib

def generate_api_key():
    key_formats = [
        'UUID',
        'ALPHANUMERIC_WITH_PREFIX',
        'TIMESTAMP',
        'TOKEN',
        'HASH',
        'ALPHANUMERIC_WITH_GROUPING'
    ]

    api_keys = {}
    api_keys2 = set()
    
    for i in range(1, 1500):  # Generate 5 API keys
        key_type = random.choice(key_formats)

        if key_type == 'UUID':
            key_value = 'UUID-' + str(uuid.uuid4())
        elif key_type == 'ALPHANUMERIC_WITH_PREFIX':
            key_value = 'API_KEY_' + ''.join(random.choices(string.ascii_uppercase + string.digits, k=10))
        elif key_type == 'TIMESTAMP':
            key_value = 'APIKEY-' + datetime.datetime.now().strftime('%Y%m%d%H%M%S')
        elif key_type == 'TOKEN':
            key_value = ''.join(random.choices(string.ascii_uppercase + string.digits, k=5)) + '-' + \
                        ''.join(random.choices(string.ascii_uppercase + string.digits, k=5)) + '-' + \
                        ''.join(random.choices(string.ascii_uppercase + string.digits, k=5))
        elif key_type == 'HASH':
            key_value = hashlib.md5(''.join(random.choices(string.ascii_uppercase + string.ascii_lowercase + string.digits, k=8)).encode()).hexdigest()
        elif key_type == 'ALPHANUMERIC_WITH_GROUPING':
            key_value = ''.join(random.choices(string.ascii_uppercase + string.digits, k=3)) + '-' + \
                        ''.join(random.choices(string.ascii_uppercase + string.digits, k=3)) + '-' + \
                        ''.join(random.choices(string.ascii_uppercase + string.digits, k=3)) + '-' + \
                        ''.join(random.choices(string.ascii_uppercase + string.digits, k=3))

        key_name = f'Example_API_Key{i}'
        api_keys[key_name] = key_value
        api_keys2.add(key_value)
    return api_keys2

keys = generate_api_key()
# json_keys = json.dumps(keys, indent=4)
with open('keys.json', 'w') as f:
    json.dump(list(keys), f)
# print(json_keys)