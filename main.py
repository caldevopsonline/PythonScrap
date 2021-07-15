import requests

request_data = requests.get('https://www.bbc.co.uk/')
generate_text = request_data.text
sys_status = request_data.status_code
print(generate_text,sys_status)
