from selenium import webdriver

# The URL of the page you want to crawl
url = 'https://chicor.com/goods?dscatNo=1&hrchyLv=1'

# Create a new instance of the Firefox driver
driver = webdriver.Firefox()

# Navigate to the page
driver.get(url)

# Find all product elements on the page
products = driver.find_elements_by_css_selector('div.product')

# Loop through each product and extract the relevant information
for product in products:
    # Extract the product name
    name = product.find_element_by_css_selector('div.product-name').text.strip()
    
    # Extract the product description
    description = product.find_element_by_css_selector('div.product-description').text.strip()
    
    # Extract the product price
    price = product.find_element_by_css_selector('div.product-price').text.strip()
    
    # Extract the product image URL
    image_url = product.find_element_by_css_selector('img.product-image').get_attribute('src')
    
    # Print the extracted information
    print(f'Product Name: {name}')
    print(f'Description: {description}')
    print(f'Price: {price}')
    print(f'Image URL: {image_url}')
    print('---')

# Close the browser window
driver.quit()