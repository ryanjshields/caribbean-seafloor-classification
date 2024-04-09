import boto3
import requests
import configparser
from bs4 import BeautifulSoup

# get latest global GEBCO dataset from URL in config file
config = configparser.ConfigParser()
config.read('config.ini')
url = config['DEFAULT']['gebco_url']

reponse = requests.get(url)
soup = BeautifulSoup(reponse.text, 'html.parser')
tables = soup.find_all('table')

# get all the urls from the tables
links = []
for table in tables:
    for link in table.find_all('a'):
        links.append(link.get('href'))

try:
    netcdf = requests.get(links[0])
    netcdf.raise_for_status()  # Raises a HTTPError if the response status code is 4xx (client error) or 5xx (server error)
except requests.exceptions.RequestException as err:
    print(f"An error occurred: {err}")
    # Handle the error as needed

# Save file to S3
# need to configure s3 bucket and credentials

# Unzip GEBCO download

# Clip to bbox found in config file

# Reproject clipped area using custom TNC prj string found in config file

# Dump everything except the reprojected, clipped COG from S3

# Retrieve layers from Felt and update