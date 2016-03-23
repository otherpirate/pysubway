from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

VOTE = 9
COMPLIMENT = True
COMPLIMENT_MESSAGE = "OMG"
WARNING = False
WARNING_MESSAGE = "YYY"
FAST_FOOD_IN_MONTH = 10
SUBWAY_IN_MONTH = 5
EMAIL = "your@email.com"
RECEIVE_NEWSLETTER = False
CONTACT_ME = False

def set_drop_down(driver, element_id, status):
    dd_options = driver.find_element_by_id(element_id).find_elements_by_tag_name('option')
    option = 2 if status else 1
    dd_options[len(dd_options)-option].click()

def set_vote(driver, element_name, vote):
    driver.find_elements_by_name(element_name)[vote].click()

def main(driver, store_id):
    elem = driver.find_element_by_id("txtSearch")
    elem.send_keys(store_id)
    elem.send_keys(Keys.RETURN)
    time.sleep(1)

    error_msg = driver.find_element_by_id("popText")
    if error_msg.is_displayed():
        if '(URL)' in error_msg.text:
            print "Redirecting..."
            driver.find_elements_by_class_name("TS_btn1")[1].click()
            main(driver, store_id)
        else:
            print "Subway error message:"
            print error_msg.text
        return

    driver.find_element_by_id("agree").click()
    time.sleep(5)

    driver.find_element_by_id("answ5195").send_keys("12/03/2016")
    driver.find_element_by_id("answHour5195").send_keys("12")
    driver.find_element_by_id("answMinute5195").send_keys("45")

    set_vote(driver, "answc5197", VOTE)
    set_vote(driver, "answ5198", VOTE)
    set_vote(driver, "answ51990", VOTE)
    set_vote(driver, "answ51991", VOTE)
    set_vote(driver, "answ51992", VOTE)
    set_vote(driver, "answ51993", VOTE)
    set_vote(driver, "answ51994", VOTE)
    set_vote(driver, "answ51995", VOTE)

    set_drop_down(driver, "answ5220", COMPLIMENT)
    if COMPLIMENT:
        driver.find_element_by_id("answ5221").click()
        driver.find_element_by_id("answ5221").send_keys(COMPLIMENT_MESSAGE)

    set_drop_down(driver, "answ5222", WARNING)
    if WARNING:
        driver.find_element_by_id("answ5223").click()
        driver.find_element_by_id("answ5223").send_keys(WARNING_MESSAGE)

    driver.find_element_by_id("answ5224").click()
    driver.find_element_by_id("answ5224").send_keys(FAST_FOOD_IN_MONTH)

    driver.find_element_by_id("answ5225").click()
    driver.find_element_by_id("answ5225").send_keys(SUBWAY_IN_MONTH)

    driver.find_element_by_id("answ5218").click()
    driver.find_element_by_id("answ5218").send_keys(EMAIL)

    set_drop_down(driver, "answ5219", RECEIVE_NEWSLETTER)
    set_drop_down(driver, "DdlContact", CONTACT_ME)

    driver.find_element_by_id("btnSubmit").click()

    time.sleep(5)
    print "Your code:"
    print driver.find_element_by_id("ctl03_lblTag").text


if __name__ == "__main__":
    store_id = raw_input('Store ID: ')

    driver = webdriver.Firefox()
    driver.get("https://www.tellsubway.com/")

    main(driver, store_id)

    driver.close()