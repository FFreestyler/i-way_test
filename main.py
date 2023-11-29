from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def test_price_difference(driver):
    WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'div.cart-sidebar__info-summary')))

    summary_coast = driver.find_element(By.CSS_SELECTOR, "div.cart-sidebar__info-summary")
    check_coast = summary_coast.find_element(By.CSS_SELECTOR, "div.info-item__value").text
    result_coast = 0
    for item in driver.find_elements(By.CSS_SELECTOR, "div.product-price__value--discount"):
        str = item.text
        new_str = str[:-1].replace(' ', '')
        new_int = int(new_str)

        result_coast += new_int

    if(result_coast == int(check_coast[:-1].replace(' ', ''))):
        print("test pass")

def driver():
    driver = webdriver.Chrome()
    driver.get("https://www.chitai-gorod.ru/")
    driver.maximize_window()

    driver.find_element(By.TAG_NAME, "input").send_keys(u"тестирование", Keys.RETURN)

    driver.execute_script("window.scrollTo(0, 250);")
    WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, "//div[@class='button action-button blue']")))

    check = 0
    for item in driver.find_elements(By.XPATH, "//div[@class='button action-button blue']"):
        if check == 3:
            break
        driver.execute_script("arguments[0].click();", item)
        check += 1

    WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, "//span[contains(text(), '3')]")))
    driver.find_element(By.XPATH, '//a[contains(@href,"/cart")]').click()

    test_price_difference(driver)
    driver.find_element(By.XPATH, "//button[@class='button cart-item__actions-button cart-item__actions-button--delete light-blue']").click()
    test_price_difference(driver)

    driver.close()


if __name__ == "__main__":
    driver()