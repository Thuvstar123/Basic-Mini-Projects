import sys
import subprocess

subprocess.check_call([sys.executable,"-m","pip","install","selenium"])

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By

#get url links
websave=open("Websave.txt")
web_content=websave.read()
url_links = web_content
websave.close()

#automation requirements
url = 'https://www.ncsc.gov.uk/section/about-this-website/report-scam-website'
input_label = 'Enter the website link or URL'
more_info = 'Tell more'
dropdown_name = 'How did you receive it?'
dropdown_option_to_select = 'Social media'
cookie_button_class = 'pcf-button.button.button--normalised.button--secondary.pull-right.cookie-button'
button_class="field__btn"

#incognito mode
chrome_options = Options()
chrome_options.add_argument('--incognito')
driver = webdriver.Chrome(options=chrome_options)
driver.get(url)

#automation of cookie acception
button_element = driver.find_element(By.CLASS_NAME,cookie_button_class)
button_element.click()

#automation of url inputs
input_field = driver.find_element(By.NAME, input_label)
input_field.send_keys(url_links)

#automation of recieval dropdown
dropdown_element=driver.find_element(By.NAME,dropdown_name)
dropdown=Select(dropdown_element)
dropdown.select_by_visible_text(dropdown_option_to_select)

#automation of extra info inputs
more_info_field = driver.find_element(By.NAME, more_info)
more_info_field.send_keys("")

#automation of submition
button_element=driver.find_element(By.CLASS_NAME,button_class)
button_element.click()

