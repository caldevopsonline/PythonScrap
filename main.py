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


bbc_footer = soup.footer.text
print(bbc_footer)




