# Admin_Name = "Deneesan"
# Admin_Password = "2008"

# Admin_name = input("Enter User Name : ")
# Admin_password = input("Enter Your Password : ")

# if Admin_Name == Admin_name and Admin_Password == Admin_password :
#     with open("Admin.txt" , "w") as file :
#         file.write(f"Admin_Name : {Admin_Name}\n")
#         file.write(f"Admin_Name : {Admin_password}\n")
# else:
#     print("Please Check Your Admin Name and Admin Password")


# Hello

import random

Accounts = {}

def Create_Account():
   global Current_Account_Number
   Name = input("Welcome! Do you Want to Create New Account So Please Enter Your Account Name : ") 
   try:
     Initial_Balance = float(input("Please Enter Initial Balance : "))
     if Initial_Balance < 0:
          print("Please Enter Intial Value Not Negative ")
          return
   except ValueError:
     print("Please Enter Intial Blance in Number ")
     return
   Account_Number = str(random.randint(10000 , 99999))
   Current_Account_Number = Account_Number

   Accounts[Account_Number] = {
          "Name": Name,
          "Balance":Initial_Balance,
          "Transactions":[f"Account Create With Balance {Initial_Balance}"]
    }
   print(f"Account created successfully! Your account number is {Account_Number}")
    



def Deposite_Account():
     Account_number = str(input("Please Enter Your Account Number : " ))

     if Account_number in Accounts:
          try:
                Deposite_Money = float(input("Please Enter Your Deposite Money : "))
                if Deposite_Money < 0:
                     print("Please Enter Your Deposite Number Positive ")
                     return

          except ValueError:
               print("Please Enter Your Deposite Money In Number ")

          Accounts[Account_number]["Balance"] += Deposite_Money
          Accounts[Account_number]["Transactions"].append(f"Deposited {Deposite_Money}")
          print("Deposit successful.")
     else :
          print("Please Check Your Account Number ")
     
     


def With_Draw():
     Account_number = str(input("Please Enter Your Account Number : " ))

     if Account_number in Accounts:
          try:
               WithDraw_Money = float(input("Please Enter Your    WithDraw Money : "))
               if WithDraw_Money < 0:
                    print("Please Enter Your Deposite Number Positive ")
                    return
               elif WithDraw_Money > Accounts[Account_number]["Balance"] :
                    print("Your WithDraw Money Is Not There Your Account ")
                    return

          except ValueError:
               print("Please Enter Your WithDraw Money In Number ")
               return

          Accounts[Account_number]["Balance"] -= WithDraw_Money
          Accounts[Account_number]["Transactions"].append(f"Deposited {WithDraw_Money}")
          print("WithDarw successful.")
     else :
          print("Please Check Your Account Number ")


def Check_Balance():
     Account_number = str(input("Please Enter Your Account Number : " ))
     if Account_number in Accounts:
          print(f"Your Current Balance  {Accounts[Account_number]["Balance"]}")
     else:
          print("Please Check Your Account Number.")



while True:
     print(''' 

     ⟪⟪⟪⟪ Our Bank Menu ⟫⟫⟫⟫

     1.Create Account
     2.Deposite Money
     3.WithDraw Money
     4.Check Balance
     5.Transaction History
     6.Exit
          ''')
     Choice = int(input("Please Enter Choice Number : "))
     if Choice == 1:
          Create_Account()
     elif Choice == 2:
          Deposite_Account()
     elif Choice == 3:
          With_Draw()
     elif Choice == 4:
          Check_Balance()
     elif Choice == 5:
          print("Yes")
     elif Choice == 6:
          print("Thank you for using the banking system.")
          break
     else :
           print("Please Enter Choice Number 1 between 6")
