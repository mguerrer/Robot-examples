from robot.libraries.BuiltIn import BuiltIn
from robot.api import logger


# class QuickSearch:
business_name = "id=business_name"
city_name = "id=city"
state = "id=state"
zip_code = "id=zip"
telephone_1 = "id=qs_phone_1"
telephone_2 = "id=qs_phone_2"
bin_code = "id=bin"
search = "id=expanded_search_button"
clear_quicksearch = "id=clear_quicksearch"
loadingMsg = "xpath=//div[@id='quicksearch']/div[@class='yui-dt-bd']/table//div[@class='yui-dt-liner yui-dt-loading']"
tableRows = "xpath=//div[@id='quicksearch']/div[@class='yui-dt-bd']/table/tbody[@class='yui-dt-data']/tr"


def set_business_name(name):
    set_input_field(business_name, name)


def set_city(city):
    set_input_field(city_name, city)


def set_state(state_code):
    if state == '':
        return
    driver = BuiltIn().get_library_instance('SeleniumLibrary')
    driver.wait_until_element_is_visible(state)
    driver.click_element(state)
    driver.select_from_list_by_value(state, state_code)
    driver.click_element(state)
    driver.wait_until_element_is_not_visible(loadingMsg)


def set_zip_code(zip):
    set_input_field(zip_code, zip)


def set_telephone(code, number):
    set_input_field(telephone_1, code)
    set_input_field(telephone_2, number)


def set_bin(bin):
    set_input_field(bin_code, bin)


def click_search_button_and_wait_results():
    driver = BuiltIn().get_library_instance('SeleniumLibrary')
    driver.click_element(search)
    driver.wait_until_element_is_visible(loadingMsg)
    driver.wait_until_element_is_not_visible(loadingMsg)


def count_results():
    driver = BuiltIn().get_library_instance('SeleniumLibrary')
    seleniumlib = BuiltIn().get_library_instance('SeleniumLibrary') 
    title = seleniumlib.get_title()
    
    count = driver.get_element_count(tableRows)
    logger.info(f"Number of search results: {count}")
    return count


def click_clear_fields():
    driver = BuiltIn().get_library_instance('SeleniumLibrary')
    driver.click_element(clear_quicksearch)


def verify_page_loaded():
    driver = BuiltIn().get_library_instance('SeleniumLibrary')
    driver.wait_until_page_contains('Quick Search')


def set_input_field(locator, value):
    if value == '':
        return
    driver = BuiltIn().get_library_instance('SeleniumLibrary')
    driver.wait_until_element_is_enabled(locator)
    driver.clear_element_text(locator)
    driver.click_element(locator)
    driver.input_text(locator, value)
    driver.press_keys(locator, 'TAB')