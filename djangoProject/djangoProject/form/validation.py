from datetime import date
import logging
import re
logging.basicConfig(filename="log.txt", filemode='a+',
                        format='%(asctime)s %(levelname)s-%(message)s',
                        datefmt='%Y-%m-%d %H:%M:%S')
logger = logging.getLogger()
logger.setLevel(logging.DEBUG)


class UserDataInput:
    '''userdata getting initialized in the constructor'''
    def __init__(self, data):
        self.data= data
        self.reason=''
        self.result = None

    def validate_first_name(self):
        """ validating the format of first name"""
        p=re.compile('[A-Za-z\s]+$')
        if re.search(p,self.data[0]):
            return True
        return False

    def validate_last_name(self):
        """ validating the format of last name"""
        p=re.compile('[A-Za-z\s]+$')
        if re.search(p,self.data[1]):
            return True
        return False

    def calculate_age(self):
        """ funtion to return age in number of years """
        p, q, r = map(int, self.data[2].split('-'))
        n = date(p, q, r)
        days_in_year = 365.2425
        age = int((date.today() - n).days / days_in_year)
        return age

    def validating_age_gender(self):
        """checking eligibility of age in years based on gender"""
        age=self.calculate_age()
        if self.data[3] == 'Male':
            if age > 21:
                return True
        if self.data[3] == 'Female':
            if age > 18:
                return True
        return False

    def validating_nation(self):
        """checking eligibility of nationality """
        if self.data[4] in ['Indian', 'American']:
            return True
        return False

    def validating_state(self):
        """checking eligibility of state based on given data"""
        if self.data[5] in ['Andhra Pradesh', 'Arunachal Pradesh', 'Assam, Bihar', \
            'Chhattisgarh', 'Karnataka', 'Madhya Pradesh', 'Odisha', 'Tamil Nadu', 'Telangana', 'West Bengal']:
            return True
        return False

    def validate_current_city(self):
        """validating the format of current city"""
        p=re.compile("[A-Za-z\s]+$")
        if re.search(p,self.data[6]):
            return True
        return False

    def validating_pin_code(self):
        """validating the format of pin code"""
        p=re.compile("[0-9]")
        if (re.search(p,self.data[7]) and len(self.data[7]))==6:
            return True
        return False

    def validating_salary(self):
        """Checking eligibilty of salary for given range"""
        p=re.compile("[0-9]")
        if  (re.search(p,self.data[9])) and (int(self.data[9])>10000 and int(self.data[9]) < 90000):
            return True
        return False

    def validating_pan_number(self):
        p=re.compile("[A-Z]{5}[0-9]{4}[A-Z]{1}")
        if (re.search(p,self.data[10]) and len(self.data[10])) == 10:
            return True
        return False

    def final_result(self):
        status=True
        if not self.validate_first_name():
            self.reason+='Invalid format for Fname--'
        if not self.validate_last_name():
            self.reason+='Invalid format for Lname--'
        if not self.validating_age_gender():
            self.reason+='Age less than expected -- '
        if not self.validating_nation():
            self.reason+="Invalid nation -- "
        if not self.validating_state():
            self.reason+="Invalid state -- "
        if not self.validate_current_city():
            self.reason+="Invalid city--"
        if not self.validating_pin_code():
            self.reason+="pin code should be six digits only -- "
        if not self.validating_salary():
            self.reason+="salary not in given range -- "
        if not self.validating_pan_number():
            self.reason+="Pan number should be of 10 characters -- "
        if self.reason == '':
            self.result="success"
        else:
            self.result="failure"
            status = False
        return status

    def validate_details(self):
        self.validate_first_name()
        self.validate_last_name()
        self.validating_age_gender()
        self.validating_nation()
        self.validating_state()
        self.validate_current_city()
        self.validating_pin_code()
        self.validating_salary()
        self.validating_pan_number()
        self.final_result()

        return True











