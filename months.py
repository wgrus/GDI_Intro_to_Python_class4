def get_age():
    age = int(input('How old are you?\n'))
    return age
    
def find_months():
    age = get_age()
    months = (age + 1) * 12
    return months

print('At your next birthday, you will have been alive for', find_months(), 'months.\n')