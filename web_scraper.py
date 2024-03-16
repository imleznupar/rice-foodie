import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium.webdriver import FirefoxOptions

serveries = ["south-servery","seibel-servery", "west-servery", "north-servery", "baker-college-kitchen"]

def get_html(servery):
    URL = "https://dining.rice.edu/"+servery

    opts = FirefoxOptions()
    opts.add_argument("--headless")
    driver = webdriver.Firefox(options=opts)
    driver.get(URL)
    html_content = driver.page_source
    driver.quit()

    return html_content

def lunch_or_dinner(meal):
    soup = BeautifulSoup(str(meal), "html.parser")
    meal_title = soup.find("h2")
    return meal_title.text

def get_dishes(meal):
    soup = BeautifulSoup(str(meal), "html.parser")
    dishes = soup.find_all('div', class_="mname")
    return [dish.text for dish in dishes]

def combine(meals):
    dic = {"LUNCH":[],"DINNER":[]}
    for meal in meals:
        title = lunch_or_dinner(meal)
        if title == "LUNCH" or title == "DINNER":
            dic[title] = dic[title]+get_dishes(meal)
    return dic

all_dishes = {}
for servery in serveries:
    html = get_html(servery)
    soup = BeautifulSoup(html, "html.parser")
    meals = soup.find_all("div", class_="views-element-container",attrs={'style':'display: block;'})
    all_dishes[servery] = combine(meals)

for key, value in all_dishes.items():
    print(key, value)

