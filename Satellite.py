from datetime import date

def is_online(month, day):
    today = date.today()
    
    if today.month == month and today.day == day:
        return True
    else:
        return False
if is_online(9, 28):
    print("The website is currently online.")
else:
    print("The website is currently offline.")
