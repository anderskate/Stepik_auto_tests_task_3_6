import time


link = "http://selenium1py.pythonanywhere.com/catalogue/"


def test_check_for_add_button(browser):
    browser.get(link)
    time.sleep(10)
    try:
    	button = browser.find_element_by_css_selector(".btn-add-to-basket")
    except Exception:
    	button = False
    assert button, 'No such item "Button"'

