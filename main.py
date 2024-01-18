import selenium
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time

service = Service()
option = webdriver.ChromeOptions()
driver = webdriver.Chrome(service=service, options=option)

def login(): #logs into twitter
    url = "https://www.twitter.com/login"
    driver.get(url)
    time.sleep(3)

    user = input("user ")
    passw = input("passw ")
    

    username_field = driver.find_element(By.TAG_NAME, "input")
    username_field.click()
    time.sleep(2)
    username_field.send_keys(user)
    page_button = driver.find_elements(By.XPATH, "//div[@role='button']")
    page_button[-2].click() #as twitter uses dynamic class names, I find all clickable buttons on the page and click the second to last one, which is the button that proceeds to the next page
    
    time.sleep(2)
    pass_field = driver.find_element(By.XPATH, "//input[@type='password']")
    pass_field.send_keys(passw)
    time.sleep(2) 
    page_button = driver.find_elements(By.XPATH, "//div[@role='button']")
    page_button[-1].click()

def tweet(): #tweets
    tweet = input("tweet")
    url = "https://twitter.com/compose/tweet"
    driver.get(url)
    time.sleep(2)
    tweet_field = driver.find_element(By.XPATH, "//div[@role='textbox']")
    tweet_field.send_keys(tweet)
    time.sleep(2)
    page_button = driver.find_element(By.XPATH, "//div[@role='button' and .//span[text()='Post']]")
    page_button.click()
    input()

def main():
    login()
    tweet()

main()
