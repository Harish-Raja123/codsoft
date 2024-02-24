import random
uppercase= "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
lowercase= uppercase.lower()
digits="0123456789"
symbols="[](),{}.|:;-=/\\+.#$%^&*"
upper,lower,nums,symbol=True,True,True,True
all=""
if upper :
    all+=uppercase
if lower:
    all+=lowercase
if nums:
    all+=digits
if symbol:
    all+=symbols
password_length=int(input("enter the length:"))
password_amount=int(input("enter the amount:"))
for x in range(password_amount):
    password="".join(random.sample(all,password_length))
    print(password)    