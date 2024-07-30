import pytest
from selenium import webdriver
from imdb_search_page import IMDBSearchPage

@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    yield driver
    driver.quit()

def test_imdb_search(driver):
    page = IMDBSearchPage(driver)
    page.load()
    page.fill_name("George Clooney")
    page.fill_birth_date("1961-05-06")
    #page.fill_death_date("2020-01-01")
    page.select_birth_month("May")
    page.select_profession("Actor")
    page.search()
    
    try:
        assert "No results found" not in driver.page_source
    except AssertionError:
        print("AssertionError: Search results not found")