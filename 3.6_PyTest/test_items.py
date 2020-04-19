import time
def test_items(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
    browser.get(link)
    #time.sleep(15)#раскоментировать для визуальной проверки языка страницы
    assert browser.find_element_by_class_name("btn-add-to-basket")\
        , "Error: element btn-add-to-basket NOT FOUND!"
