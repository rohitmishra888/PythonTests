import pytest
from selenium import webdriver
from utils.webdriver_manager import get_driver
from utils.logger import setup_logger

@pytest.fixture(scope="session")
def driver():
    """Fixture to initialize and quit WebDriver."""
    driver = get_driver()
    yield driver
    driver.quit()

@pytest.fixture(autouse=True)
def log_test_start(request):
    """Fixture to log the start and end of each test."""
    logger = setup_logger('test_logger', 'test.log')
    logger.info(f"Starting test: {request.node.name}")
    yield
    logger.info(f"Finished test: {request.node.name}")
