import requests



#private key undisclosed 
pat = ''
repo_url = 'https://api.github.com/repos/jonathanm-12/EC521-Final-Project/contents'
branch_url = 'https://api.github.com/repos/jonathanm-12/EC521-Final-Project/branches'
auth = ('jonathanm-12', pat)

#authenticate response request using github key
req = requests.get(repo_url,auth=auth)

file_names = [item['name'] for item in req.json()]

req = requests.get('https://api.github.com/repos/jonathanm-12/EC521-Final-Project/branches', auth=auth)

names = [item['name'] for item in req.json()]
main_branch = requests.get(branch_url, auth=auth).json()[0]['name']

#file_content = []

for i in file_names:
    #append file content
    #https://raw.githubusercontent.com/jonathanm-12/EC521-Final-Project/main/APIKEY_regex.txt
    file_content = requests.get(f'https://raw.githubusercontent.com/jonathanm-12/EC521-Final-Project/{main_branch}/{i}', auth=auth)
    
    if file_content.status_code != 404:
        file_content = file_content.content
    else:
        continue
    
    #output_area.insert('end', file_content)
    #output_area.insert('end', '\n')
    
    print(file_content)


