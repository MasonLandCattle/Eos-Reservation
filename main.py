from turtle import dot
from Child import Child
import FormFiller
import os

# ! Development ONly
import dotenv
dotenv.load_dotenv("./env")

# * PARENT INFORMATION
GUARDIAN_FIRST_NAME =   os.getenv("GUARDIAN_FIRST_NAME")
GUARDIAN_LAST_NAME =    os.getenv("GUARDIAN_LAST_NAME")
MEMBER_ID =             os.getenv("MEMBER_ID")
GUARDIAN_PHONE_NUMBER = os.getenv("GUARDIAN_PHONE_NUMBER")
GUARDIAN_EMAIL =        os.getenv("GUARDIAN_EMAIL")
STATE =                 os.getenv("STATE")
LOCATION=               os.getenv("LOCATION")

# TIME OPTIONS - Order in your perfered choice, (back-up Options)
# AM_8, AM_9, AM_10, AM_11, PM_12, PM_4, PM_5, PM_6
time_preference_order = ["AM_8", "AM_9", "AM_10", "PM_4"]

# * KIDS INFORMATION
child_1 = Child(os.get("KID_1_FIRST_NAME"), os.get("KID_1_LAST_NAME"), os.get("KID_1_DOB"))
child_2 = Child(os.get("KID_2_FIRST_NAME"), os.get("KID_2_LAST_NAME"), os.get("KID_2_DOB"))
KIDS = [child_1, child_2]

eos_reserver = FormFiller.Eos_Reserver(GUARDIAN_FIRST_NAME,
                                   GUARDIAN_LAST_NAME,
                                   MEMBER_ID,
                                   GUARDIAN_PHONE_NUMBER,
                                   GUARDIAN_EMAIL,
                                   STATE,
                                   LOCATION,
                                   time_preference_order,
                                   kids=KIDS)

eos_reserver.reserve_all_kids()

