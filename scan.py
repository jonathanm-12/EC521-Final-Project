import requests

#private key undisclosed 
pat = ''
#repo_url = 'https://api.github.com/repos/jonathanm-12/EC521-Final-Project/contents'
#branch_url = 'https://api.github.com/repos/jonathanm-12/EC521-Final-Project/branches'
auth = ('jonathanm-12', pat)


def fetch_repos(user):
    repos_url =  f'https://api.github.com/users/{user}/repos'
    response = requests.get(repos_url, auth=auth)
    return [item['name'] for item in response.json()]

def fetch_contents(url):
    response = requests.get(url, auth=auth)
    return response.json()

def print_raw_file_url(user, repo, branch, path):
    raw_url = f"https://raw.githubusercontent.com/{user}/{repo}/{branch}/{path}"
    print(f"Raw URL of {path}: {raw_url}")
    print(requests.get(raw_url, auth=auth).text)

def list_files_in_repo(user, branch='main', path=""):

    repos = fetch_repos(user)    

    for repo in repos:

        api_url = f"https://api.github.com/repos/{user}/{repo}/contents/{path}"
        contents = fetch_contents(api_url)
        
        #keep track of API requests <= 100
        counter = 0

        for content in contents:

            if counter >= 100:
                print("API reached 100 requests. Stopping\n")
                break
            elif content['type'] == 'file':
                print_raw_file_url(user, repo, branch, content['path'])
                counter += 1
            elif content['type'] == 'dir':
                list_files_in_repo(user, repo, branch, content['path'])

#list_files_in_repo('jonathanm-12', 'brain-4ce')
print(fetch_repos('jonathanm-12'))