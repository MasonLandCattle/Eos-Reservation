from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.select import Select
from selenium.common.exceptions import ElementNotInteractableException
import sys

# Custom imports
import Child

class Eos_Reserver:
    # * XPATHS
    FORM_START = '//*[@id="cid_67"]/div/div[3]/button[2]' #From initial url path
    # Feilds
    FIRST_NAME_FIELD = '//*[@id="first_62"]'
    LAST_NAME_FIELD = '//*[@id="last_62"]'
    AGE_SELECT_DROP_DOWN = '//*[@id="input_111"]'
    # Next Btns
    MEMBER_ID_NEXT_BTN = '//*[@id="cid_68"]/div/div[3]/button[2]'
    CHILD_NAME_NEXT_BTN = '//*[@id="cid_62"]/div/div[3]/button[2]'
    AGE_NEXT_BTN = '//*[@id="cid_111"]/div/div[3]/button[2]'
    TIME_SELECT_NEXT_BTN = '//*[@id="cid_64"]/div/div[3]/button[2]'
    # Submit
    SUBMIT_BTN = '//*[@id="cid_69"]/div/div[3]/button[3]'

    # TIME SLOTS
    TIME_SLOTS = {
    "AM_8" :  '//*[@id="input_64"]/div/div/div/div[2]/div[2]/div/div[1]',
    "AM_9" :  '//*[@id="input_64"]/div/div/div/div[2]/div[2]/div/div[2]',
    "AM_10" : '//*[@id="input_64"]/div/div/div/div[2]/div[2]/div/div[3]',
    "AM_11" : '//*[@id="input_64"]/div/div/div/div[2]/div[2]/div/div[4]',
    "PM_12" : '//*[@id="input_64"]/div/div/div/div[2]/div[2]/div/div[5]',
    "PM_4" :  '//*[@id="input_64"]/div/div/div/div[2]/div[2]/div/div[6]',
    "PM_5" :  '//*[@id="input_64"]/div/div/div/div[2]/div[2]/div/div[7]',
    "PM_6" :  '//*[@id="input_64"]/div/div/div/div[2]/div[2]/div/div[8]',
    }

    def __init__(self, first_name, last_name, member_id, phone_number, email, state, location, time_preference_order, kids=[]):
        self.first_name = first_name
        self.last_name = last_name
        self.member_id = member_id
        self.phone_number = phone_number
        self.email = email
        self.state = state
        self.location = location
        self.time_preference_order = time_preference_order
        self.kids = kids

        # Set Chrome Driver
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

    def reserve_eos_kid_care(self, child_obj:Child):
        # Get Web Form - W/ Prefilled Fields
        self.driver.get(f"https://forms.alariscloud.com/202628942231957?state={self.state}&club={self.location}&guardianFirstName={self.first_name}&guardianLastName={self.last_name}&guardianEmail={self.email}&guardianPhone={self.phone_number}&memberID={self.member_id}&target=_blank")

        # (START FORM)
        # Next Button - From guardian Data
        WebDriverWait(self.driver, 15).until(EC.element_to_be_clickable((By.XPATH, self.FORM_START))).click()

        # Next Button - Member ID (Pre-filled)
        WebDriverWait(self.driver, 15).until(EC.element_to_be_clickable((By.XPATH, self.MEMBER_ID_NEXT_BTN))).click()

        # Fill in Child Name
        WebDriverWait(self.driver, 15).until(EC.element_to_be_clickable((By.XPATH, self.FIRST_NAME_FIELD))).send_keys(child_obj.first_name)
        WebDriverWait(self.driver, 15).until(EC.element_to_be_clickable((By.XPATH, self.LAST_NAME_FIELD))).send_keys(child_obj.last_name)

        # Next Button - Child Name
        WebDriverWait(self.driver, 15).until(EC.element_to_be_clickable((By.XPATH, self.CHILD_NAME_NEXT_BTN))).click()

        # Age Drop Down
        age_sel = Select(self.driver.find_element(By.XPATH, self.AGE_SELECT_DROP_DOWN))
        age_sel.select_by_visible_text(child_obj.get_eos_age_category())
        WebDriverWait(self.driver, 15).until(EC.element_to_be_clickable((By.XPATH, self.AGE_NEXT_BTN))).click()
        self.driver.implicitly_wait(3)

        # Select Time
        time_chosen = False
        for time_selection in self.time_preference_order:
            time_elem = self.driver.find_element(By.XPATH, self.TIME_SLOTS[time_selection])
            class_attrs = time_elem.get_attribute('class')
            if "disabled" not in class_attrs:
                try:
                    time_elem.click()
                except ElementNotInteractableException:
                    print("Hit an Exception")
                    continue

                time_chosen = True
                WebDriverWait(self.driver, 15).until(EC.element_to_be_clickable((By.XPATH, self.TIME_SELECT_NEXT_BTN))).click()
                self.driver.implicitly_wait(2)
                break
            else:
                continue

        if not time_chosen:
            print("No availible times")
            sys.exit()

        # Submit Form
        WebDriverWait(self.driver, 15).until(EC.element_to_be_clickable((By.XPATH, self.SUBMIT_BTN))).click()


    def reserve_all_kids(self):
        for kid in self.kids:
            print(kid)
            self.reserve_eos_kid_care(kid)
