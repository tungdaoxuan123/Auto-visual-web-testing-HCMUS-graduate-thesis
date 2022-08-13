from selenium import webdriver
from time import sleep

def getscreenshot(url):
    driver = webdriver.Firefox()
    driver.get(url)
    sleep(1)

    driver.get_screenshot_as_file("screenshot.png")
    driver.quit()
    print("end...")