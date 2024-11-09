from selenium import webdriver

def get_driver():
    """Returns a WebDriver instance."""
    driver = webdriver.Chrome()  # You can parameterize this for different browsers
    driver.maximize_window()
    driver.implicitly_wait(10)
    return driver