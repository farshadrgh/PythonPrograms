import requests from bs4 import BeautifulSoup

url = 'https://www.python.org/'
reqs = requests.get(url)
soup = BeautifulSoup(reqs.text, 'lxml')
print("\nChildren of the html tag (https://www.python.org):\n")
root = soup.html    
root_childs = [e.name for e in root.children if e.name is not None]
print(root_childs)
