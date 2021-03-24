import pytest
import time
from selenium import webdriver

def test_AddToCartButton(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
    browser.get(link)
    time.sleep(10)
    button = len(browser.find_elements_by_css_selector(".btn-add-to-basket"))
    assert button > 0, "Кнопка добавления в корзину не найдена"
    

