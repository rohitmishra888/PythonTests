import pytest
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

@pytest.mark.smoke
@pytest.mark.describe("Example Test Suite")
@pytest.mark.it("Should contain the name Sarthak")
def test_example():
    """Example test."""
    name = "Sarthak"
    assert "Sarthak" in name

@pytest.mark.smoke
@pytest.mark.describe("Google Homepage Test")
@pytest.mark.it("Should have Google in the title")
def test_example_2(driver):
    """Example test."""
    driver.get("https://www.google.com")
    assert "Google" in driver.title

@pytest.mark.smoke
@pytest.mark.describe("Google Search Test")
@pytest.mark.it("Should search for 'speed test' on Google")
def test_search_speed_test(driver):
    """Test case to search for 'speed test' on Google."""
    # ... (rest of the test case remains the same)

#PS E:\NxtGenTesting> pytest Tests\sampletest.py --html=reports.html --self-contained-html --css=Tests\pytest-html.css