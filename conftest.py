import pytest
import requests
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.chrome.options import Options as ChromeOptions
from faker import Faker
from urls import Urls

fake = Faker()


@pytest.fixture()
def driver():
    options = ChromeOptions()
    options.add_argument("--start-maximized")
    chrome_service = ChromeService(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=chrome_service, options=options)

    yield driver
    driver.quit()


@pytest.fixture
def create_and_delete_user(driver):
    user_data = {
        "email": fake.email(),
        "password": fake.password(),
        "name": fake.name()
    }
    response = requests.post(Urls.register_api, json=user_data)
    access_token = response.json().get('accessToken')
    refresh_token = response.json().get('refreshToken')
    driver.get(Urls.home_page_url)
    driver.execute_script("window.localStorage.setItem('accessToken', arguments[0]);", access_token)
    driver.execute_script("window.localStorage.setItem('refreshToken', arguments[0]);", refresh_token)
    yield access_token
    requests.delete(Urls.delete_api, headers={"Authorization": f"{access_token}"})


@pytest.fixture
def create_order(driver, create_and_delete_user):
    access_token = create_and_delete_user
    headers = {"Authorization": access_token}
    ingredients_response = requests.get(Urls.list_of_ingredients_api)
    ingredients_data = ingredients_response.json()["data"]
    selected_ingredients = [
        ingredients_data[0]["_id"],
        ingredients_data[1]["_id"]
    ]
    order_data = {"ingredients": selected_ingredients}
    requests.post(Urls.create_order_api, json=order_data, headers=headers)
