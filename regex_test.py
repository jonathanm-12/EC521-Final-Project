import re

regex_patterns = {
    "Google API Key": "AIza[0-9A-Za-z\\-_]{35}",
    "AWS Access Key ID": "AKIA[0-9A-Z]{16}",
    "Mailgun API Key": "key-[0-9a-zA-Z]{32}",
    "Twilio API Key": "SK[0-9a-fA-F]{32}",
    "Square Access Token": ["sqOatp-[0-9a-zA-Z]{22}", "sq0atp-[0-9a-zA-Z]{22}"],
    "Stripe API Key": ["sk_live_[0-9a-zA-Z]{24}", "pk_live_[0-9a-zA-Z]{24}"],
    "Slack Token": ["xoxb-[0-9A-Za-z]{10,48}", "xoxp-[0-9A-Za-z]{10,48}", "xoxa-2-[0-9A-Za-z]{10,48}"],
    "GitHub Token": ["ghp_[0-9a-zA-Z]{36}", "gho_[0-9a-zA-Z]{36}"],
    "Heroku API Key": "[0-9a-fA-F]{40}",
    "SendGrid API Key": "SG\\.[0-9A-Za-z\\-_]{22}\\.[0-9A-Za-z\\-_]{43}",
    "GitLab Private Token": "glpat-[0-9a-zA-Z]{20}",
    "Asana Access Token": "0\\/[0-9a-zA-Z]{32}",
    "PayPal/Braintree Access Token": "access_token\\$production\\$[0-9a-zA-Z]{16,64}",
    "Azure Shared Access Signature": "sig=[0-9a-zA-Z%]{43,}",
    "Docker Hub": "sha256:[0-9a-fA-F]{64}",
    "Atlassian": "BQA[0-9A-Za-z\\\\-_]{20,}",
    "Shopify Access Token": ["shpat_[0-9a-zA-Z]{32}", "shpca_[0-9a-zA-Z]{32}", "shpss_[0-9a-zA-Z]{32}"]
}

def search_file_for_patterns(file_path, patterns):
    # Read the contents of the file
    with open(file_path, 'r') as file:
        file_contents = file.read()

    # Search for patterns in the file contents
    matches = {}
    for key, pattern in patterns.items():
        if isinstance(pattern, list):
            for p in pattern:
                found = re.findall(p, file_contents)
                if found:
                    matches[key] = found
        else:
            found = re.findall(pattern, file_contents)
            if found:
                matches[key] = found

    return matches

# Testing
if __name__ == "__main__":
    file_path = "test_cases\codes.txt"
    patterns = regex_patterns
    results = search_file_for_patterns(file_path, patterns)
    for name,key in results.items():
        print(f"{name}: {key}")