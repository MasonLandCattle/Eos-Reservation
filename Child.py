from datetime import date, datetime

EOS_TWO_YEARS_AND_OLDER = '24 mos - 12 yrs'
EOS_UNDER_TWO_YEARS_OLD = "06 mos - 23 mos"

class Child:
    """
    Child to store data and calculate age specs per Eos
    DOB: Entered as (01/25/2021) mm/dd/yyyy
    """
    def __init__(self, first_name, last_name, dob):
        self.first_name = first_name
        self.last_name = last_name
        self.dob = self.get_age_obj(dob)

    def get_age_by_months(self):
        today = date.today()
        num_months = (today.year - self.dob.year) * 12 + (today.month - self.dob.month)
        return num_months

    def get_age_obj(self, dob_string):
        try:
            return datetime.strptime(dob_string, '%m/%d/%Y')
        except ValueError:
            print("Please Provide Valid Date format")

    def get_eos_age_category(self):
        if self.get_age_by_months() >= 24:
            return EOS_TWO_YEARS_AND_OLDER
        else:
            return EOS_UNDER_TWO_YEARS_OLD

if __name__ == "__main__":
    child_1 = Child("Bob", "Joe", "07/23/2019")
    print(child_1.get_age_by_months())
