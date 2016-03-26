from selenium import webdriver

import time
import utils
from subway_exceptions import RedirectException

def access_store(driver, store_id):
    utils.input(driver, "txtSearch", store_id)
    utils.button_click(driver, "SubmitText")
    time.sleep(1)

    try:
        utils.deal_with_error_message(driver)
        utils.button_click(driver, "agree")
        time.sleep(5)
        return True
    except RedirectException:
        return access_store(driver, store_id)

def get_cookie(driver, store_id, config):

    if access_store(driver, store_id):
        date = utils.get_last_visit_date(config["week_frequency"])
        formatted = utils.format_date(date, driver.find_element_by_id("answ5195").get_attribute("placeholder"))
        utils.input(driver, "answ5195", formatted, False)

        utils.input(driver, "answHour5195", config["hour"], False)
        utils.input(driver, "answMinute5195", config["minute"], False)

        utils.set_vote(driver, "answc5197", config["recommend_to_friend"])
        utils.set_vote(driver, "answ5198", config["general_experience"])
        utils.set_vote(driver, "answ51990", config["food_quality"])
        utils.set_vote(driver, "answ51991", config["food_quality"])
        utils.set_vote(driver, "answ51992", config["polite_staff"])
        utils.set_vote(driver, "answ51993", config["cleaning"])
        utils.set_vote(driver, "answ51994", config["comfort"])
        utils.set_vote(driver, "answ51995", config["general_experience"])

        utils.set_drop_down(driver, "answ5220", config["compliment"])
        if config["compliment"]:
            utils.input(driver, "answ5221", config["compliment_message"])

        utils.set_drop_down(driver, "answ5222", config["warning"])
        if config["warning"]:
            utils.input(driver, "answ5223", config["warning_message"])

        utils.input(driver, "answ5224", config["fast_food_in_month"])
        utils.input(driver, "answ5225", config["subway_in_month"])
        utils.input(driver, "answ5218", config["my_email"])

        utils.set_drop_down(driver, "answ5219", config["receive_newsletter"])
        utils.set_drop_down(driver, "DdlContact", config["contact_me"])

        utils.button_click(driver, "btnSubmit")
        time.sleep(1)

        utils.deal_with_error_message(driver)
        time.sleep(5)

        return driver.find_element_by_id("ctl03_lblTag").text


if __name__ == "__main__":
    store, config = utils.store_selection()

    driver = webdriver.Firefox()
    driver.get("https://www.tellsubway.com/")

    code = get_cookie(driver, store, config)
    if code:
        driver.close()
        print code