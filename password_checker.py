#password strength checker
# checks whether a password is weak, medium, or strong 
password = input("Enter your password: ")   
length = len(password) >= 8
upper = any(char.isupper() for char in password)
lower = any(char.islower() for char in password)
digit = any(char.isdigit() for char in password)
special = any(not char .isalnum() for char in password)
score = sum([length, upper, lower, digit, special])
if score <= 2:
    print("weak password")
elif score <=4:
    print("medium password")    
else:
    print("strong password")    