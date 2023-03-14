from selenium import webdriver
import pytest


@pytest.fixture(autouse=True)
def set():
    driver = webdriver.Chrome('C:\Users\79136\PycharmProjects\driver\chromedriver.exe')
    driver.get('http://petfriends.skillfactory.ru/login')

    yield

    driver.quit()
