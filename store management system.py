'''store management system

customer (cid,cname,cadd,cmob)
product(pid,pname,price,pdesc)
order(cid,pdi,qty)

1-add customer
2-view all customer
3-delete customer
4-add product
5-view all product
6-update a product
7-place an order
8-view all products
9-view orders BY CID
0-exit

     '''
# Import pickle library
import pickle

# method to add a customer information
def addcustomer():
    file=open("customer.bin","ab")
    cid=input("\n\tenter the customer id:")
    cname=input("\tenter the customer name:")
    cadd=input("\tenter the customer address:")
    cmob=input("\tenter the customer mobile:")
    pickle.dump(cid,file)
    pickle.dump(cname,file)
    pickle.dump(cadd,file)
    pickle.dump(cmob,file)
    print("\n\t\tcustomer added successfully!")
    file.close()
    input("\n\t\t press enter to continue......")

# method to view all the customer information

def viewallcustomer():
    file=open("customer.bin","rb")
    try:
        while True:
            print("\n\t\t enter customer Id:",pickle.load(file))
            print("\t\t enter customer name:",pickle.load(file))
            print("\t\t enter customer address:",pickle.load(file))
            print("\t\t enter customer mobile:",pickle.load(file))
            print("\t\t ---------------------------------------")
    except:
        print("\n\t\t here is customer information!")
    file.close()
    input("\t\t press enter to continue.....")

import pickle
import os

# method to delete a customer information

def deletecustomer():
    file1=open("customer.bin","rb")
    file2=open("temp.bin","wb")
    cid=input("\t\tenter the customer Id to delete :")
    flag=0

    try:
        while True:
            data=pickle.load(file1)
            if data==cid:
                print("\t\tcustomer name:",pickle.load(file1))
                pickle.load(file1)
                pickle.load(file1)
                flag=1
                
            else:
                pickle.dump(data,file2)
    except:
        if flag==1:
            print("\n\t\t customer data deleted successfully!")
        else:
            print("\n\t customer not found")
        
    file1.close()
    file2.close()
    os.remove("customer.bin")
    os.rename("temp.bin","customer.bin")
    input("\n\t\t press enter to continue.....")

# Method to add a product information

def addproduct():
    file=open("product.bin","ab")
    pid=input("\t\tenter the product Id:")
    pname=input("\t\tenter the product name:")
    price=input("\t\tenter the product price:")
    pdesc=input("\t\tenter the product desc:")
    pickle.dump(pid,file)
    pickle.dump(pname,file)
    pickle.dump(price,file)
    pickle.dump(pdesc,file)
    print("\n\t\t product information add successfully")
    file.close()
    input("\t\tpress enter to continue......")

# method to view all product information

def viewallproducts():
    file=open("product.bin","rb")
    try:
        while True:
            print("\n\t\tproduct id:",pickle.load(file))
            print("\t\tproduct name:",pickle.load(file))
            print("\t\tproduct price:",pickle.load(file))
            print("\t\tproduct desc:",pickle.load(file))
            print("\n\t\t -----------------------")
            
    except :
        print("\n\t\t here all the product information!")
    file.close()
    input("\t\t press enter to continue!")

#method to update the product
def updateproduct():
    file1=open("product.bin","rb")
    file2=open("temp.bin","wb")
    pid=input("\n\t\t enter product ID to update:")
    flag=0
    
    try:
        while True:
            data=pickle.load(file1)
            if data==pid:
                pickle.dump(data,file2)
                name=pickle.load(file1)
                pickle.dump(name,file2)
                print("\t\t product name:",name)
                print("\t\t old price :",pickle.load(file1))
                price=input("\t\t enter the price:")
                pickle.dump(price,file2)
                pickle.dump(pickle.load(file1),file2)
                flag=1
                
                
            else:
                pickle.dump(data,file2)
    except:
        if flag==1:
            print("\t\tprice updated successfully!")
        else:
            print("\n\t\t product not found !")
        
    file1.close()
    file2.close()
    os.remove("product.bin")
    os.rename("temp.bin","product.bin")
    input("\n\t\tpress enter to continue.....")

    
    
# A method to get a customer information

import pickle
import os

def getcustomer(cid):
    cus=[]
    if not os.path.exists("customer.bin"):
        return cus
    
    file=open("customer.bin","rb")
    try:
        while True:
            data=pickle.load(file)
            if data==cid:
                cus.append(data)
                cus.append(pickle.load(file))
                cus.append(pickle.load(file))
                cus.append(pickle.load(file))
            else:
                pickle.load(file)
                pickle.load(file)
                pickle.load(file)
    except:
        pass
    file.close()
    return cus

# method to place an order

def placeanorder():
    cid=input("\n\t\t enter the Customer ID:")
    cus=getcustomer(cid)
    if len(cus)!=0:
        print("\n\t\t customer name:",cus[1])
        print("\t\t customer address:",cus[2])
        pid=input("\t\t enter the product id:")
        pro=getproduct(pid)
        if len(pro)!=0:
            print("\n\t\t  product name :",pro[1])
            print("\t\t product price:",pro[2])
            qty=input("\t\t enter quantity:")
            file=open("orders.bin","ab")
            pickle.dump(cid,file)
            pickle.dump(pid,file)
            pickle.dump(qty,file)
            file.close()
            print("\n\t\t product successful")
            print("\n\t\t bill amount:",int(qty)*int(pro[2]))
        else:
            print("\t\tproduct not found")
    else:
        print("\n\t\t customer not found")
    input("\t\t press enter to continue.....")

# method to get a product information


def getproduct(pid):
    pro=[]
    
    if not os.path.exists("product.bin"):
        return pro
    file=open("product.bin","rb")
    try:
        while True:
            data=pickle.load(file)
            if data==pid:
                pro.append(data)
                pro.append(pickle.load(file))
                pro.append(pickle.load(file))
                pro.append(pickle.load(file))
            else:
                pickle.load(file)
                pickle.load(file)
                pickle.load(file)
    except:
        pass
    file.close()
    return pro
    input("\n\tpress enter to continue")

# METHOD to view all orders

def Viewallorders():
    if not os.path.exists("orders.bin"):
        print("\n\t No orders found!")
        input("\t Press Enter To Continue...")
        return
    file = open('orders.bin','rb')
    
    try:
        n = 1001
        while True:
            cus = getcustomer(pickle.load(file))
            pro = getproduct(pickle.load(file))
            qty = pickle.load(file)
            print("\n\t Order No.",n)
            print("\t Customer Name :",cus[1])
            print("\t Customer Address :",cus[2])
            print("\t Product Name :",pro[1])
            print("\t Product Price :",pro[2])
            print("\t About Product :",pro[3])
            print("\t Total Bill :",int(pro[2])*int(qty))
            n=n+1
            print("\t ---------------------------")
    except:
        print("\n\t Here is you all orders...")
    file.close()
    input("\t Press Enter To Continue...")


# method to view order by CID

def vieworderbycid():
    cid = input("\n\t Enter Customer ID : ")
    cus = getcustomer(cid)
    print("\n\t Customer Name :",cus[1])
    print("\t Customer Address :",cus[2])
    print("\t Customer Mobile :",cus[3])
    file = open("orders.bin",'rb')
    n = 1001
    try:
        while True:
            data = pickle.load(file)
            if data==cid:
                pro = getproduct(pickle.load(file))
                qty = pickle.load(file)
                print("\n\t Order No.",n)
                print("\t Product Name :",pro[1])
                print("\t Product Price :",pro[2])
                print("\t Product Desc :",pro[3])
                print("\t Quantity :",qty)
                print("\t Total Bill :",int(pro[2])*int(qty))
                n=n+1
    except:
        print("\t Here is your all orders for cid",cid)
    file.close()
    input("\t Press Enter To Continue...")


# DASHBOARD
while True:
    print("\n\t\t **** STORE MANAGEMENT SYSTEM **** ")
    print('''
        1-add customer
        2-view all customer
        3-delete customer
        4-add product
        5-view all product
        6-update a product
        7-place an order
        8-View all orders
        9-view orders BY CID
        0-exit''')

    ch=int(input("\t\tenter your choice:"))
    if ch==0:
        print("\n\t\t\tBYE BYE ADMIN!")
        break
    
    elif ch==1:
        addcustomer()

    elif ch==2:
        viewallcustomer()

    elif ch==3:
        deletecustomer()

    elif ch==4:
        addproduct()

    elif ch==5:
        viewallproducts()

    elif ch==6:
        updateproduct()

    elif ch==7:
        placeanorder()

    elif ch==8:
        Viewallorders()

    elif ch==9:
        vieworderbycid()

    else:
        print("\n\t check your number and try again")
        

































