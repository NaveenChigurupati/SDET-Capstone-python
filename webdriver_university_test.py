from selenium import webdriver
from selenium.webdriver.common.by import By
import pytest
from selenium.webdriver.support.select import Select
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService


@pytest.fixture()
def driver():
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    driver.implicitly_wait(10)
    driver.delete_all_cookies()
    driver.maximize_window()
    driver.get("http://webdriveruniversity.com/index.html")
    yield driver
    driver.quit()


def test_webdriveruniversity(driver):
    webelment_title_of_page = driver.find_element(By.XPATH, "//a[@class='navbar-brand']")
    webelment_title_of_page.is_displayed()
    element_dropdown_etc = driver.find_element(By.ID, "dropdown-checkboxes-radiobuttons")
    driver.execute_script("arguments[0].scrollIntoView();", element_dropdown_etc)
    element_dropdown_etc.click()
    window_handles = driver.window_handles
    for handle in window_handles:
        driver.switch_to.window(handle)
        if driver.title.__eq__("WebDriver | Dropdown Menu(s) | Checkboxe(s) | Radio Button(s)"):
            driver.find_element(By.XPATH, "//a[@class='navbar-brand']").is_displayed()
            driver.implicitly_wait(10)
            element_dropbox = driver.find_element(By.ID, "dropdowm-menu-1")
            language_dropbox = Select(element_dropbox)
            language_dropbox.select_by_value("sql")
            selected_language = language_dropbox.first_selected_option
            assert selected_language.text == "SQL"
            driver.implicitly_wait(10)
            print(selected_language)

            checkbox1 = driver.find_element(By.XPATH, "//input[@type='checkbox' and @value='option-1']")
            checkbox2 = driver.find_element(By.XPATH, "//input[@type='checkbox' and @value='option-2']")
            checkbox3 = driver.find_element(By.XPATH, "//input[@type='checkbox' and @value='option-3']")
            checkbox4 = driver.find_element(By.XPATH, "//input[@type='checkbox' and @value='option-4']")
            checkbox1.click()
            checkbox4.click()
            checkboxlist = driver.find_elements(By.ID, "checkboxes")
            checkedcount = 0
            uncheckedcount = 0
            for CheckBoxStatus in checkboxlist:
                if CheckBoxStatus.is_selected():
                    checkedcount += 1
                else:
                    uncheckedcount += 1
            print("Checked checkboxes:", checkedcount)
            print("UnChecked checkboxes:", uncheckedcount)
            driver.implicitly_wait(10)
            radiobutton1 = driver.find_element(By.XPATH, "//input[@type='radio' and @value='green']")
            radiobutton2 = driver.find_element(By.XPATH, "//input[@type='radio' and @value='blue']")
            radiobutton3 = driver.find_element(By.XPATH, "//input[@type='radio' and @value='yellow']")
            radiobutton4 = driver.find_element(By.XPATH, "//input[@type='radio' and @value='orange']")
            radiobutton1.click()
            driver.implicitly_wait(100)
            radiobutton2.click()
            driver.implicitly_wait(100)
            radiobutton3.click()
            driver.implicitly_wait(100)
            radiobutton4.click()

            radiobuttonlist = driver.find_elements(By.ID, "radio-buttons")
            slectedcount = 0
            unselectedcount = 0
            for CheckBoxStatus in radiobuttonlist:
                if CheckBoxStatus.is_selected():
                    slectedcount += 1
                else:
                    unselectedcount += 1
            print("selected radioButtons:", slectedcount)
            print("Unselected radioButtons:", unselectedcount)
            driver.implicitly_wait(10)


