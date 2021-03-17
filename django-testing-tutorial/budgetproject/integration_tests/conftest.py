import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

from budget.models import Project

@pytest.fixture(scope="session", autouse=True)
def setup():
    chrome_options = Options()
    chrome_options.add_argument('--headless')   
     
    print("initiating chrome driver\n")
    web_driver = webdriver.Chrome() #if not added in PATH
    web_driver.set_window_size(1920, 1080)
    #web_driver.get("http://localhost:3000")    
    
    # session = request.node
    # for item in session.items:
    #     cls = item.getparent(pytest.Class)
    #     setattr(cls.obj,"driver", web_driver)

    yield web_driver

    web_driver.close()
