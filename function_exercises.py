def is_vowel(str):
    for char in str:
        if char in "aeiouAEIOU":
            return True
        else: 
            return False



def is_consonant(str):
     for char in str:
        if char in "aeiouAEIOU":
            return False
        else: 
            return True

def calculate_tip(bill,percent):
    if percent >= 1:
        return 'input error percent must be less than 1'
    else:
        return percent*bill

def get_letter_grade(grade):
    if grade>=(90):
        return 'Grade is a A'
    elif grade>=(80):
        return 'Grade is a B'
    elif grade>=(70):
        return 'Grade is a C'
    elif grade>=(60):
        return 'Grade is a D'
    elif grade<=(60):
        return 'Grade is a F'