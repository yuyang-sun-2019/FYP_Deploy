import random
import string
import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.ui import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
from flask import Flask, request, jsonify
import os
app = Flask(__name__)

@app.after_request
def add_headers(response):
    response.headers['Access-Control-Allow-Origin'] = "*"
    response.headers['Access-Control-Allow-Headers'] =  "Content-Type, Access-Control-Allow-Headers, Authorization, X-Requested-With"
    response.headers['Access-Control-Allow-Methods']=  "POST, GET, PUT, DELETE, OPTIONS"
    return response

@app.route("/")
def hello():
    return "Hello World!"


@app.route("/<name>")
def hello_name(name):
    try:
        BASE_URL = "https://web.whatsapp.com/"
        CHAT_URL = "https://web.whatsapp.com/send?phone={phone}&text&type=phone_number&app_absent=1"

        chrome_options = Options()
        chrome_options.add_argument("start-maximized")
        user_data_dir = ''.join(random.choices(string.ascii_letters, k=8))
        chrome_options.add_argument("--user-data-dir=/tmp/chrome-data/" + user_data_dir)
        chrome_options.add_argument("--incognito")

        browser = webdriver.Chrome(ChromeDriverManager().install(),  options=chrome_options,)

        browser.get(BASE_URL)
        browser.maximize_window()


        phone = "86687676"   #change to sponsor number 86687676
        message = 'I need service for '+ name


        browser.get(CHAT_URL.format(phone=phone))
        time.sleep(3)


        inp_xpath = (
            '//*[@id="main"]/footer/div[1]/div/span[2]/div/div[2]/div[1]/div/div[1]'
        )
        input_box = WebDriverWait(browser, 60).until(
            expected_conditions.presence_of_element_located((By.XPATH, inp_xpath))
        )
        input_box.send_keys(message)
        input_box.send_keys(Keys.ENTER)

        time.sleep(10)
        driver.quit()
    except:
        pass
    return "Hello there, we have whatsapp your query to our Project V2D department"



if __name__ == "__main__":
    #app.run(port=8080)
    app.run(debug=True, host='127.0.0.1', port=8000)
#https://github.com/bhavaniravi/flask-tutorial/tree/master/app
