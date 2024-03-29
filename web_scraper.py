import requests
from bs4 import BeautifulSoup
from selenium import webdriver

def get_html(servery):
    URL = "https://dining.rice.edu/"+servery

    chromedriver_path = './chromedriver'
    driver = webdriver.Chrome(executable_path=chromedriver_path)
    driver.get(URL)
    driver.refresh()
    html_content = driver.page_source
    driver.quit()

    return html_content

def lunch_or_dinner(meal):
    soup = BeautifulSoup(str(meal), "html.parser")
    meal_title = soup.find("h2")
    if meal_title is not None:
        return meal_title.text
    else:
        return ""

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

def get_all_dishes():
    serveries = [
                "south-servery",
                "seibel-servery", 
                "west-servery", 
                "north-servery", 
                "baker-college-kitchen"
                ]

    all_dishes = {}
    for servery in serveries:
        html = get_html(servery)
        soup = BeautifulSoup(html, "html.parser")
        meals = soup.find_all("div", class_="views-element-container",attrs={'style':'display: block;'})
        all_dishes[servery] = combine(meals)
        print(servery, "done")

    return all_dishes

