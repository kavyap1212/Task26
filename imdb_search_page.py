from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

class IMDBSearchPage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def load(self):
        self.driver.get("https://www.imdb.com/search/name/")
    
    def fill_name(self, name):
        try:
            name_input = self.wait.until(EC.presence_of_element_located((By.ID, "name")))
            name_input.send_keys(name)
        except TimeoutException:
            print("TimeoutException: Name input field not found")

    def fill_birth_date(self, birth_date):
        try:
            birth_date_input = self.wait.until(EC.presence_of_element_located((By.ID, "birth_date")))
            birth_date_input.send_keys(birth_date)
        except TimeoutException:
            print("TimeoutException: Birth date input field not found")
    
    def fill_death_date(self, death_date):
        try:
            death_date_input = self.wait.until(EC.presence_of_element_located((By.ID, "death_date")))
            death_date_input.send_keys(death_date)
        except TimeoutException:
            print("TimeoutException: Death date input field not found")
    
    def select_birth_month(self, month):
        try:
            birth_month_select = self.wait.until(EC.presence_of_element_located((By.ID, "birth_monthday")))
            birth_month_select.send_keys(month)
        except TimeoutException:
            print("TimeoutException: Birth month dropdown not found")
    
    def select_profession(self, profession):
        try:
            profession_select = self.wait.until(EC.presence_of_element_located((By.ID, "professions")))
            profession_select.send_keys(profession)
        except TimeoutException:
            print("TimeoutException: Profession dropdown not found")
    
    def search(self):
        try:
            search_button = self.wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "button.primary")))
            search_button.click()
        except TimeoutException:
            print("TimeoutException: Search button not found")