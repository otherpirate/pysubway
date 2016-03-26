import subway_exceptions
from configurations import Configurations
from datetime import date, timedelta
from collections import OrderedDict

def set_drop_down(driver, element_id, status):
    dd_options = driver.find_element_by_id(element_id).find_elements_by_tag_name('option')
    option = 2 if status else 1
    dd_options[len(dd_options)-option].click()

def set_vote(driver, element_name, item):
    driver.find_elements_by_name(element_name)[item].click()

def button_click(driver, button_id):
    driver.find_element_by_id(button_id).click()

def input(driver, element_id, value, click=True):
    if click:
        driver.find_element_by_id(element_id).click()
    driver.find_element_by_id(element_id).send_keys(value)

def deal_with_error_message(driver):
    error_msg = driver.find_element_by_id("popText")
    if error_msg.is_displayed():
        if '(URL)' in error_msg.text:
            driver.find_elements_by_class_name("TS_btn1")[1].click()
            raise subway_exceptions.RedirectException()
        else:
            raise ValueError("Subway error message: \n%s" % error_msg.text.encode('utf-8'))

def store_selection():
    configs = Configurations()

    store = configs.first()
    if len(configs) > 1:
        selection = raw_input('Store ID: ')
        store = int(selection) if selection else store

    config = configs.to(store)
    return store, config

def get_last_visit_date(week_frequency):
    past_days = int(7/week_frequency)
    last_visit = date.today() - timedelta(days=past_days)
    return last_visit

def format_date(date, format):
    fields  = OrderedDict((char, format.count(char)) for char in format)
    separator = fields.keys()[1]
    fields.pop(separator)

    formatter = ""
    for field in fields.items():
        char = field[0]
        if field[1] > 2:
            char = char.upper()
        formatter += "%" + char + separator
    formatter = formatter[:-1]

    return date.strftime(formatter)