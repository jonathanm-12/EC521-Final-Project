import requests


def fetch_github_data(output_area):

    pat = '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'
    repo_url = 'https://api.github.com/repos/jonathanm-12/ope-quay/contents'
    branch_url = 'https://api.github.com/repos/jonathanm-12/ope-quay/branches'
    auth = ('jonathanm-12', pat)

    #authenticate response request using github key
    req = requests.get(repo_url,auth=auth)

    file_names = [item['name'] for item in req.json()]

    req = requests.get('https://api.github.com/repos/jonathanm-12/ope-quay/branches', auth=('jonathanm-12', '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'))

    names = [item['name'] for item in req.json()]
    main_branch = requests.get(branch_url, auth=auth).json()[0]['name']

    
    output_area.insert('end', f"Main Branch: {main_branch}\n")
    output_area.insert('end', "Repository Contents:\n")
    output_area.insert('end', "\n".join(names))