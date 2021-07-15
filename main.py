import requests
from bs4 import BeautifulSoup

# request_data = requests.get('https://www.bbc.co.uk/')
# generate_text = request_data.text
# sys_status = request_data.status_code
# print(generate_text,sys_status)


# Make a HTTPS request from the BBC Website
web_main = requests.get('https://www.bbc.co.uk/')

# Initialize fetch connection with the help og BeautifulSoup Library
Fetch_data = BeautifulSoup(web_main.content, 'html.parser')

# Get bbc page title
bbc_title = Fetch_data.title.text

# Get BBC Main Body
bbc_body = Fetch_data.body.text

# Create a .TXT File
data_output = open("DATA_FROM_BBC.txt", 'w')

# Push web content to the file created
data_output.write(bbc_body)

# Close the opened file
data_output.close()
