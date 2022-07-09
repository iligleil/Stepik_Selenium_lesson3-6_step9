from selenium.webdriver.common.by import By

def test_available_basket(browser):
    browser.get('http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/')
    result = True
    try:
        browser.find_element(By.CLASS_NAME, 'btn-add-to-basket')
        result = True
    except NoSuchElementException:
        result = False

    assert result == True, f'Кнопка добавления в корзину на странице не найдена!'
