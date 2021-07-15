import requests
from bs4 import BeautifulSoup

#request_data = requests.get('https://www.bbc.co.uk/')
#generate_text = request_data.text
#sys_status = request_data.status_code
#print(generate_text,sys_status)


# Make a request
page = requests.get(
    'https://www.bbc.co.uk/')
soup = BeautifulSoup(page.content, 'html.parser')

# Get bbc page title
bbc_title = soup.title.text
print(bbc_title)
# Get BBC Min Body
bbc_body = soup.body.text
print(bbc_body)
# Get BBC Footer
bbc_footer = soup.footer.text
print(bbc_footer )



