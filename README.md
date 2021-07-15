# PythonScrap

# PythonScrap

This project is built to capture web content from any HTTPS website using python

The project allows users to enter a website name with it domain given it is a secured connection(HTTPS)

1. The first function makes use of an input which allows a user to put in their web address

2. The web address is then Concatenate with a predefined HTTPS statement. This is then captured using python library
called the "requests"

3. The content of the captured URL is then forked with the help of a library called BeautifulSoup.

4. Now we can decide which section of the website we want to fetch.

5. The BeautifulSoup gives you room to fetch data from any section of the website say "body, footer,header etc.". In
this project the code focuses on capturing the body of the webpage.
