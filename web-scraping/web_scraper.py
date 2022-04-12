# needed to install and import these 2 libaries to make this work

import requests
from bs4 import BeautifulSoup as bs

# define variable github user

github_user = input('Input Github User: ')
url = 'https://github.com/' +github_user

# send request to the page

r = requests.get(url) 

# pull the HTML content of the requested page

soup = bs(r.content, 'html.parser')

# define new variable as the search result of these specific identifiers

profile_image = soup.find('img', {'alt' : 'Avatar'})['src']

#print the URL of the  profile image for the user chosen

print(profile_image)
