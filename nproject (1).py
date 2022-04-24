                                                        # Bank Management System #


import pymysql
class connection:
    def __init__(self):
        try:
            self._conn=pymysql.connect(host="localhost",user="root",password="",db="bank")
        except Exception as e:
            print(e)
        else:
            print("connection successfully created:")

    
class Customer_details(connection):
    def __init__(self):
        super().__init__()
        cur=self._conn.cursor()
        n=input("Enter Name:")
        ac=int(input("Enter Account No:"))
        d=int(input("Enter DOB:"))
        a=input("Enter Address:")
        ph=input("Enter Phone No:")
        ob=int(input("Enter Opening Balance:"))
        typ=input("Enter Type of Account:")
    
        query="insert into account values(%s,%s,%s,%s,%s,%s,%s) "
        val=(n,ac,d,a,ph,ob,typ)
    
        cur.execute(query,val)
        self._conn.commit()
        print("Customer_details Entered Successfully:")
        self._conn.close()
class Deposite_amt(connection):
    def __init__(self):
        super().__init__()
        cur=self._conn.cursor()
        amt=int(input("Enter amount:"))
        ac=int(input("Enter account:"))
        a="select ob from account where ac_no=%s"
        data=(ac,)
        val=(amt,ac)
        cur.execute(a,data)
        f=cur.fetchone()
        tam=f[0]+amt
        
        query="update account set ob=%s where ac_no=%s"
        d=(tam,ac)
        cur.execute(query,d)
        self._conn.commit()
        print("Deposited Amount Has Been Successfully:")
        self._conn.close()
class Withdraw_amt(connection):
    def __init__(self):
        super().__init__()
        cur=self._conn.cursor()
        amt=int(input("Enter amount:"))
        ac=int(input("Enter account:"))
        a="select ob from account where ac_no=%s"
        data=(ac,)
        val=(amt,ac)
        cur.execute(a,data)
        f=cur.fetchone()
        tam=f[0]-amt
        
        query="update account set ob=%s where ac_no=%s"
        d=(tam,ac)
        cur.execute(query,d)
        self._conn.commit()
        print("Withdraw Amount Has Been Successfully:")
        self._conn.close()
    

class Balance_Enquiry(connection):
    def __init__(self):
        super().__init__()
           
        cur=self._conn.cursor()
        ac=int(input("Enter Account No:"))
        query="select ob from account ac_no where ac_no=%s"
        data=(ac,)
        cur.execute(query,data)
        
        result=cur.fetchone()
        if result:
            print(result)
        else:
            print("Record not found")
        self._conn.commit()
        print("Checked Balance Enquiry Has Been Successfully:")
        self._conn.close()        

    
        

class Check_Details(connection):
    def __init__(self):
        super().__init__()
           
        cur=self._conn.cursor()
        ac=int(input("Enter Account No:"))
        query="select * from account where ac_no=%s"
        data=(ac,)
        cur.execute(query,data)
       
        result=cur.fetchone()
        if result:
            print(result)
        else:
            print("Record not found")
        self._conn.commit()
        print("Checked_Details Successfully:")
        self._conn.close()

class Update_Name(connection):
    def __init__(self):
        
        super().__init__()
        
        
        a=input("Enter Name:")
        ac=int(input("Enter Account No:"))
        query="update account set name=%s where ac_no=%s"
        cur=self._conn.cursor()
        data=(a,ac)
        
        cur.execute(query,data)
        
     
        
           
        self._conn.commit()
        print("Dear Customer Your Name Has Been Updated Successfully:")
            
        self._conn.close()

            
class Update_Address(connection):
    def __init__(self):
        
        super().__init__()
        
        
        a=input("Enter Address:")
        ac=int(input("Enter Account No:"))
        query="update account set add=%s where ac_no=%s"
        cur=self._conn.cursor()
        data=(a,ac)
        
        cur.execute(query,data)
        
     
        
           
        self._conn.commit()
        print("Dear Customer Your Address Has Been Updated Successfully:")
            
        self._conn.close()            


class Update_DOB(connection):
    def __init__(self):
        
        super().__init__()
        
        
        a=int(input("Enter DOB:"))
        ac=int(input("Enter Account No:"))
        query="update account set dob=%s where ac_no=%s"
        cur=self._conn.cursor()
        data=(a,ac)
        
        cur.execute(query,data)
        
     
        
           
        self._conn.commit()
        print("Dear Customer Your DOB Has Been Updated Successfully:")
            
        self._conn.close()

class Update_Phone_No(connection):
    def __init__(self):
        
        super().__init__()
        
        
        a=int(input("Enter Phone No:"))
        ac=int(input("Enter Account No:"))
        query="update account set ph_no=%s where ac_no=%s"
        cur=self._conn.cursor()
        data=(a,ac)
        
        cur.execute(query,data)
        
     
        
           
        self._conn.commit()
        print("Dear Customer Your Phone No. Has Been Updated Successfully:")
            
        self._conn.close()

class Close_Account(connection):
    def __init__(self):
        super().__init__()
           
        cur=self._conn.cursor()
        ac=int(input("Enter Account No:"))
        query="delete from account where ac_no=%s"
        data=(ac,)
        cur.execute(query,data)
       
        result=cur.fetchone()
        if result:
            print(result)
        else:
            print("Account Close Successfully   ")
        self._conn.commit()
        print("Close_Account Has Been Successfully:")
        self._conn.close()  
    
class Display_record(connection):
    def __init__(self):
        super().__init__()
        cur=self._conn.cursor()
        query="select * from account"
        cur.execute(query)
        result=cur.fetchall()
        if result:
            print(result)
        else:
            print("Record not found")
            print("Displayed Customer Details:")
        self._conn.close()

        
while True:
    print("1.Customer_details")
    print("2.Deposite_amt")
   
    print("3.Withdraw_amt")
    print("4.Balance_Enquiry")
    print("5.Check_Details")
    print("6.Update_Name")
    print("7.Update_Addresss")
    print("8.Update_DOB")
    print("9.Update_Phone_No")
    print("10.Close_Account")
    print("11.Display_Record")
    choice=int(input("Enter choice:"))
    if choice==1:
        Customer_details()
    elif choice==2:
        Deposite_amt()
        
    elif choice==3:
        Withdraw_amt()
    elif choice==4:
        Balance_Enquiry()
        
    elif choice==5:
        Check_Details()
    elif choice==6:
        Update_Name()
    elif choice==7:
        Update_Address()
    elif choice==8:
        Update_DOB()
    elif choice==9:
        Update_Phone_No()
    elif choice==10:
        Close_Account()
    elif choice==11:
        Display_record()
        
    else:
        ("print invalid")

    ans=input("continue....y/n")
    ans=ans.lower()
    if ans!="y":
        break
    
print("///////////////////////////////////////////////////*******Bank Management System*******\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\")

        
 
