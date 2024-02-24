names=[]
phonenumber=[]
num=3
for i in range(num):
    name=input("enter name:")
    phone_number=input("enter a phone number: ")
    names.append(name)
    phonenumber.append(phone_number)
print("\tname\t\t\tphonenumber")
for i in range(num):
    print(f'\t{names[i]}\t\t\t{phone_number[i]}')
s=input("enter the name to search:")   
if s in names:
    index=names.index(s)
    name=names[index]
    phone_number=phone_number[index]
    print(f"name:{name},phonenumber:{phone_number}")
else:
    print("Oops! name not found")
