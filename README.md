
<p align="center">
    <h1 align="center"> Company email webscraping  python</h1>
</p>
This Python script is designed to extract email addresses from a list of company names using web scraping techniques. It utilizes Selenium and BeautifulSoup libraries to automate the process of navigating to company Facebook pages and extracting email addresses.

## Author
 - Mouhamed Diouf : [@MdCode002](https://github.com/MdCode002)
## Features
- Automated web scraping for email extraction.
- Utilizes Google search to find relevant Facebook pages for companies.
- Handles cases where a Facebook page is not found gracefully.
## Installation
1. Clone the project repository:

   ```shell
     git clone https://github.com/Medzo02/web-scraping-email-extractor.git

2. Install the required dependencies:
    ```shell
        pip install selenium
        pip install beautifulsoup4
        pip install requests


3. Download and install ChromeDriver and place it in C:/chromedriver_win32/chromedriver.exe.
## Usage
Prepare a list of company names in a file named liste.txt, with one company name per line.
  
The script will perform web scraping to extract email addresses and save the results in a CSV file named resultats.csv.
On the first iteration, you will have 30 seconds to enter your Facebook login information. You will not have to log in again while the script runs.

## Legal Disclaimer

I assume no responsibility for the use of this script by third parties. The use of this script is at your own risk and discretion. Please ensure compliance with all applicable laws and regulations regarding data collection and website scraping.

