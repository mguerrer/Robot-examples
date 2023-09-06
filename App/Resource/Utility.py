from robot.libraries.BuiltIn import BuiltIn
import datetime
import ibm_db_dbi
import Environment
import random
import string
from tkinter import Tk
from FrameworkKeywords import open_or_get_browser
from selenium.webdriver.common.by import By

def generate_random_number():
    var = str(datetime.datetime.today()).replace('-', '').replace(':', '').replace(' ', '').split('.')[0]
    return var

def generate_random_number_with_size( length: int):
    rand_str = ''
    for x in range(length):
        rand_str = rand_str + random.choice(string.digits)
    return rand_str

def generate_random_string( length: int):
    rand_str = ''
    for x in range(length):
        rand_str = rand_str + random.choice(string.ascii_letters)
    return rand_str

def query_database(query):
    connectionstring = "DATABASE=" + str(Environment.database[Environment.env_name]) + "; HOSTNAME=" + str(
        Environment.hostname[Environment.env_name]) + "; PORT=" + str(Environment.port[Environment.env_name]) + "; UID=" + str(
        Environment.dbuserid[Environment.env_name]) + "; PWD=" + str(Environment.dbuserpwd[Environment.env_name]) + ";AUTHENTICATION=SERVER"

    conn = ibm_db_dbi.connect(connectionstring)
    cur = conn.cursor()
    cur.execute(query)
    if "select" in query or "SELECT" in query or "Select" in query:
        allrows = cur.fetchall()
        cur.close()
        conn.close()
        return allrows
    elif "update" in query or "UPDATE" in query or "Update" in query:
        conn.commit()
        cur.close()
        conn.close()
        return True
    elif "delete" in query or "DELETE" in query or "Delete" in query:
        conn.commit()
        cur.close()
        conn.close()
        return True


def uncheck_all_checkboxes():
    driver = open_or_get_browser()
    for i in range(1, len(driver.find_elements(By.XPATH, "//input[@type='checkbox']"))):
        if driver.find_element(By.XPATH, "(//input[@type='checkbox'])[" + str(i) + "]").is_selected():
            BuiltIn().log("************************Unchecking " + str(i))
            driver.find_element(By.XPATH, "(//input[@type='checkbox']/..)[" + str(i) + "]").click()


def scroll_to_element(xpath):
    driver = open_or_get_browser()
    driver.execute_script("arguments[0].scrollIntoView();", driver.find_element(By.XPATH, xpath))

def get_clipboard_data()->str:
    attempts = 0
    clipboard = ''
    while attempts < Environment.retry_times:
        try:
            clipboard = Tk().clipboard_get()
            if clipboard != '':
                return clipboard 
        except:
            BuiltIn().sleep(1)
        attempts = attempts + 1
    return clipboard