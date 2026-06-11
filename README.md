 Web Scraping Project (Python)


 Project Overview

This project demonstrates web scraping using Python. It extracts data from a website using the `requests` and `BeautifulSoup` libraries and stores it for further use.

 Technologies Used

- Python

- Requests library

- BeautifulSoup (bs4)

- Jupyter Notebook

- Git & GitHub


 Project Files

- `Project1.py` → Python script for scraping

- `webscraping.ipynb` → Jupyter Notebook version of the project


 What I Learned

- How to send HTTP requests using Python

- How to parse HTML using BeautifulSoup

- How to extract data from websites

- How to use Git and GitHub for version control

- How to push projects to GitHub


 How It Works

1. Send request to website using `requests`

2. Get HTML response

3. Parse HTML using BeautifulSoup

4. Extract required data (titles, links, etc.)


 Example Code

```python

import requests

from bs4 import BeautifulSoup



url = "https://example.com"

response = requests.get(url)



soup = BeautifulSoup(response.text, "html.parser")



print(soup.title.text)

