import requests
from bs4 import BeautifulSoup
import telegram
import time

# Telegram bot token
bot_token = 'YOUR_BOT_TOKEN'
# Chat ID of the recipient
chat_id = 'YOUR_CHAT_ID'

# URL of the Trendyol page with discounted products
url = 'https://www.trendyol.com/butik/liste/1/kadin'

# Initialize the Telegram bot
bot = telegram.Bot(token=bot_token)

while True:
    try:
        # Send a request to the URL and get the page content
        response = requests.get(url)
        soup = BeautifulSoup(response.content, 'html.parser')

        # Find all the products on the page
        products = soup.find_all('div', class_='product-card')

        # Iterate over the products and send the ones with a discount percentage greater than 50%
        for product in products:
            discount_tag = product.find('span', class_='discount-rate')
            if discount_tag is not None and int(discount_tag.text.strip('%')) >= 50:
                # Get the product title and URL
                title = product.find('a', class_='prdct-desc-cntnr-name hasRatings').text.strip()
                product_url = 'https://www.trendyol.com' + product.find('a', class_='prdct-desc-cntnr-name hasRatings')['href']
                
                # Send a message to the recipient
                message = f'{title}\n{product_url}'
                bot.send_message(chat_id=chat_id, text=message)

        # Wait for 10 minutes before checking the page again
        time.sleep(600)

    except Exception as e:
        print(e)
