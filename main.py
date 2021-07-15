import requests
from bs4 import BeautifulSoup


# request_data = requests.get('https://www.bbc.co.uk/')
# generate_text = request_data.text
# sys_status = request_data.status_code
# print(generate_text,sys_status)


# Function to Request URL
def request_url():
    # Request User to enter a website Address
    web_address = input("Enter Any HTTPS Web Address\n")

    # Concatenate the web adDress with HTTPS://WWW.
    web_main = requests.get("https://www." + web_address + "/")

    # Initialize fetch connection with the help of BeautifulSoup Library
    fetch_data = BeautifulSoup(web_main.content, 'html.parser')
    return fetch_data


# Function to capture body content of URL
def display_data():
    # Get BBC Main Body
    bbc_body = request_url().body.text
    return bbc_body


# Create a .TXT File
data_output = open("DATA_FROM_URL.txt", 'w')

# Push web content to the file created
data_output.write(display_data())

# Close the opened file
data_output.close()
