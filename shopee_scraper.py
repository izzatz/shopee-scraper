from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from time import sleep
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail

chrome_options = Options()
# chrome_options.add_argument("--headless")

sendgrid_api_key = "<YOUR_SENDGRID_API_KEY>"
url = 'https://shopee.com.my/product/724335/2212828002'

driver = webdriver.Chrome(service = Service( <YOUR_CHROMEDRIVER_EXE_PATH> ))

driver.get(url)

sleep(1)

# click the english language button
driver.find_element(By.XPATH, """//*[@id="modal"]/div[1]/div[1]/div/div[3]/div[1]/button""").click()

sleep(3)

# stock reading count on the product detail section
read_stock = """//*[@id="main"]/div/div[2]/div[1]/div/div[1]/div/div[2]/div[3]/div/div[4]/div/div[4]/div/div[3]/div[2]/div[2]"""
out = driver.find_element(By.XPATH, read_stock).text

if out == "0":
    print("Product still out of stock")

else:
    print("Product is available to purchase!")

    message = Mail(
        from_email='<YOUR_SENDER_EMAIL>',
        to_emails='<YOUR_RECEIVER_EMAIL>',
        subject='Izzat Shopee Script - Your item is back in stock!',
        html_content='<strong>Buy now!</strong>')
    try:
        sg = SendGridAPIClient(sendgrid_api_key)
        response = sg.send(message)
        print(response.status_code)
        print(response.body)
        print(response.headers)
    except Exception as e:
        print(e.message)

driver.quit()
