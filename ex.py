import requests
from bs4 import BeautifulSoup

# The URL of the page you want to crawl
url = 'https://chicor.com/goods?dscatNo=1&hrchyLv=1'

# Use the requests library to download the HTML content of the page
response = requests.get(url)
html = response.text

# Print out the HTML content for debugging purposes
print(html)

# Parse the HTML using BeautifulSoup
soup = BeautifulSoup(html, 'html.parser')

# Find all product elements on the page
products = soup.find_all('div', class_='product')

# Loop through each product and extract the relevant information
for product in products:
    # Extract the product name
    name = product.find('div', class_='product-name').text.strip()
    
    # Extract the product description
    description = product.find('div', class_='product-description').text.strip()
    
    # Extract the product price
    price = product.find('div', class_='product-price').text.strip()
    
    # Extract the product image URL
    image_url = product.find('img', class_='product-image')['src']
    
    # Print the extracted information
    print(f'Product Name: {name}')
    print(f'Description: {description}')
    print(f'Price: {price}')
    print(f'Image URL: {image_url}')
    print('---')