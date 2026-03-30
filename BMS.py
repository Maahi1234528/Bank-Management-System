import pandas as pd
import random

Staff={'Staff ID': ['Name', 'Age', 'Gender', 'DOB', 'Contact', 'Address', 'Designation', 'Branch', 'Access']}
Customers={'Customer ID': ['Name', 'Age', 'Gender', 'DOB', 'Contact', 'Address', 'Marital Status']}
Accounts={'Customer ID': [['Account Number', 'Account Type', 'Balance', 'Branch', 'DOO', "Account Status\n'A' for active\n'D' for dormant"]]}

def Create(CustID):
    while True:
        try:
            cacc=int(input("Account Number:-"))
            bal=float(input("Balance:-"))
            bran=input("Branch:-")
            doo=input("Date Of Opening (DD/MM/YYYY):-")
            break
        except ValueError:
            print("Invalid input\n")
    while True:
        try:
            acctype=int(input("Account type:-\n1)Savings\n2)Current\n"))
            if acctype==1:
                typ='S'
                break
            elif acctype==2:
                typ='C'
                break
            else:
                print("Invalid Choice\n")
        except ValueError:
            print("Invalid input\n")
    while True:
        try:
            sta=int(input("Account Status:-\n1)Active\n2)Dormant\n"))
            if sta==1:
                ta='A'
                break
            elif sta==2:
                ta='D'
                break
            else:
                print("Invalid Choice\n")
        except ValueError:
            print("Invalid input\n")
    details=[cacc, typ, bal, bran, doo, ta]
    if CustID not in Accounts:
        Accounts[CustID]=[details]
    else:
        Accounts[CustID].append(details)

def Add(field):
    if field=='Staff':
        try:
            no=int(input("How many staff's do you want to add:-"))
            while no > 0:
                ID=int(input("Enter Staff ID:-"))
                if ID not in Staff:
                    sname=input("Name:-")
                    sage=int(input("Age:-"))
                    sgen=input("Gender:-")
                    sdob=input("Date Of Birth (DD/MM/YYYY):-")
                    scon=int(input("Contact:-"))
                    sadd=input("Address:-")
                    sdes=input("Designation:-")
                    sbra=input("Branch:-")
                    acc='S'
                    details=[sname, sage, sgen, sdob, scon, sadd, sdes, sbra, acc]
                    Staff.setdefault(ID, details)
                    no-=1
                else:
                    print("Staff ID already exists\n")
            print("Staff added successfully\n")
        except ValueError:
            print("Invalid input\n")
            
    elif field=='Client' or field=='Customers':
        try:
            if field=='Client':
                no=1
            else:
                no=int(input("How many customers do you want to add:-"))
            while no > 0:
                ID=int(input("Enter Customer ID:-"))
                if ID not in Customers:
                    cname=input("Name:-")
                    cage=int(input("Age:-"))
                    cgen=input("Gender:-")
                    cdob=input("Date Of Birth (DD/MM/YYYY):-")
                    ccon=int(input("Contact:-"))
                    cadd=input("Address:-")
                    cmar=input("Marital Status:-")
                    details=[cname, cage, cgen, cdob, ccon, cadd, cmar]
                    Customers.setdefault(ID, details)
                    Create(ID)
                    no-=1
                else:
                    print("Customer ID already exists\n")
            print("Customer details added successfully\n")
        except ValueError:
            print("Invalid input\n")

def Displayall(field):
    df_vertical=pd.DataFrame(field)
    df_horizontal=df_vertical.T
    df_horizontal.columns=df_horizontal.iloc[0]
    df_final=df_horizontal[1:]
    print(df_final.to_markdown(tablefmt="grid", stralign="center"))

def Search(tempfield, field, index=None, search=None):
    found=False
    if search==None:
        if index in field:
            tempfield.setdefault(index, field[index])
            found=True
    else:
        for i in field:
            if str(field[i][index]).lower()==search.lower():
                tempfield.setdefault(i, field[i])
                found=True
    if found:
        Displayall(tempfield)
    else:
        print("No records found\n")

def selectcustomer():
    try:
        while True:
            tempfield={'Customer ID':['Name','Age','Gender','DOB','Contact','Address','Marital Status']}
            tempfield2={'Customer ID':[['Account Number','Account Type','Balance','Branch','DOO',"Account Status\n'A' for active\n'D' for dormant"]]}
            ch0=int(input("What do you want:-\n1)Select customers by a category\n2)Select a customer\n3)Display account details of a customer\n4)Exit\n..."))
            if ch0==1:
                ch1=int(input("Enter your choice:-\n1)Search by name\n2)Search by gender\n3)Search by address\n4)Search by marital status\n..."))
                if ch1==1:
                    cname=input("Name:-")
                    Search(tempfield,Customers,0,cname)
                elif ch1==2:
                    mgen=input("Gender:-")
                    Search(tempfield,Customers,2,mgen)
                elif ch1==3:
                    madd=input("Address:-")
                    Search(tempfield,Customers,5,madd)
                elif ch1==4:
                    msta=input("Marital Status:-")
                    Search(tempfield,Customers,6,msta)
                else:
                    print("Invalid Choice\n")
            elif ch0==2:
                tempid=int(input("Enter customer id:-"))
                Search(tempfield,Customers,tempid)
            elif ch0==3:
                tempid=int(input("Enter customer id:-"))
                if tempid in Accounts:
                    tempfield2.setdefault(tempid,Accounts[tempid])
                    Displayall(tempfield2)
            elif ch0==4:
                print("Exiting...\n",'-'*100)
                break
            else:
                print("Invalid Choice\nTry again...\n")
    except (ValueError, IndexError):
        print("Invalid input\n")

def Update(field, te_id, index, value):
    field[te_id][index]=value
    print("Updated successfully...\n")

def check(field,te_id):
    if te_id in field:
        return True
    else:
        print("No records found\n")
        return False
    
def customer_update_loop():
    try:
        while True:
            ch2=int(input("What do you want to do\n1)Update name\n2)Update age\n3)Update gender\n4)Update DOB\n5)Update contact\n6)Update address\n7)Exit\n..."))
            if ch2==1:
                tempid=int(input("Enter Customer ID:-"))
                if check(Customers,tempid):
                    newname=input("Name:-")
                    Update(Customers,tempid,0,newname)
            elif ch2==2:
                tempid=int(input("Enter Customer ID:-"))
                if check(Customers,tempid):
                    newage=int(input("Age:-"))
                    Update(Customers,tempid,1,newage)
            elif ch2==3:
                tempid=int(input("Enter Customer ID:-"))
                if check(Customers,tempid):
                    newgen=input("Gender:-")
                    Update(Customers,tempid,2,newgen)
            elif ch2==4:
                tempid=int(input("Enter Customer ID:-"))
                if check(Customers,tempid):
                    newdob=input("DOB (DD/MM/YYYY):-")
                    Update(Customers,tempid,3,newdob)
            elif ch2==5:
                tempid=int(input("Enter Customer ID:-"))
                if check(Customers,tempid):
                    newcon=input("Contact:-")
                    Update(Customers,tempid,4,newcon)
            elif ch2==6:
                tempid=int(input("Enter Customer ID:-"))
                if check(Customers,tempid):
                    newadd=input("Address:-")
                    Update(Customers,tempid,5,newadd)
            elif ch2==7:
                print("Exiting...\n",'-'*100)
                break
            else:
                print("Invalid Choice\nTry Again...\n")
    except ValueError:
        print("Invalid Input\n")

def Delete(field):
    try:
        if field=='Customers':
            tempid=int(input("Enter customer id:-"))
            if tempid in Customers:
                Customers.pop(tempid)
                Accounts.pop(tempid, None)
                print(f"Customer {tempid} deleted.")
        elif field=='Accounts':
            accno=int(input("Enter account number to close:-"))
            for key, val_list in Accounts.items():
                for val in val_list:
                    if val[0]==accno:
                        Accounts.pop(key)
                        print("Account closed.")
                        return
            print("Account not found.")
    except ValueError:
        print("Invalid input")

def aifinadvisor(accno):
    found=False
    for key in Accounts:
        for val in Accounts[key]:
            if val[0]==accno:
                found=True
                acctype=val[1]
                balance=float(val[2])
                status=val[5]

                if status=='D':
                    print("AI INSIGHT:Your account is currently Dormant. My top advice is to visit your home branch to reactivate it before planning investments.")
                    return

                if balance<5000:
                    print(f"AI INSIGHT: Your balance is ₹{balance}. It is highly recommended to set up an automated monthly deposit to build a solid emergency fund.")
                elif 5000<=balance<=50000:
                    if acctype=='S':
                        print("AI INSIGHT:You are maintaining a healthy savings balance! Consider moving 20% of these funds into a Fixed Deposit (FD) to safely beat inflation.")
                    else:
                        print("AI INSIGHT:As a Current account holder, ensure you maintain this liquidity to keep your daily business operations running smoothly.")
                else:
                    print("AI INSIGHT:You have substantial idle funds. Our AI suggests speaking to our wealth management team to diversify your portfolio into Mutual Funds or Stocks for higher returns.")
    
    if not found:
        print("AI ERROR: Could not locate account details to analyze.")

def Menu(field1, field2, mode='Staff'):
    try:
        if mode=='Client':
            while True:
                
                ch=int(input("\n1)Display personal details\n2)Deposit\n3)Withdraw\n4)Check Balance\n5)Get AI Financial Advice\n6)Exit\n..."))
                if ch==1:
                    Displayall(field1)
                elif ch==2: 
                    amt=float(input("Amount:-"))
                    accno=int(input("Enter Account Number:-"))
                    for key in Accounts:
                        for val in Accounts[key]:
                            if val[0]==accno:
                                val[2]+=amt
                                print("New Balance:", val[2])
                elif ch==3:
                    amt=float(input("Amount:-"))
                    accno=int(input("Enter Account Number:-"))
                    for key in Accounts:
                        for val in Accounts[key]:
                            if val[0]==accno:
                                val[2]-=amt
                                print("New Balance:", val[2])
                elif ch==4:
                    accno=int(input("Enter Account Number:-"))
                    for key in Accounts:
                        for val in Accounts[key]:
                            if val[0]==accno:
                                print("Balance:", val[2])
                elif ch==5:
                    accno=int(input("Enter Account Number:-"))
                    aifinadvisor(accno)
                elif ch==6: 
                    break
        else:
            while True:
                ch=int(input(f"\nAccessing {field2}\n1)Add\n2)Display All\n3)Search\n4)Update\n5)Delete\n6)Exit\n..."))
                if ch==1:
                    Add(field2)
                elif ch==2: 
                    Displayall(field1)
                elif ch==3: 
                    selectcustomer()
                elif ch==4: 
                    customer_update_loop()
                elif ch==5: 
                    Delete(field2)
                elif ch==6: 
                    break
    except ValueError:
        print("Invalid Input")

print('='*100 + '\n\t\t\tWELCOME TO BANK MANAGEMENT SYSTEM\t\t\t\n' + '='*100)

while True:
    try:
        ch=int(input("\nMain Menu:\n1)Staff\n2)Customer\n3)Quit\n..."))
        if ch==1:
            Menu(Customers, 'Customers', 'Staff')
        elif ch==2:
            Menu(Customers, 'Client', 'Client')
        elif ch==3:
            print("Quitting...")
            break
        else:
            print("Invalid Choice")
    except ValueError:
        print("Invalid Input")
