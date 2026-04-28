# method to add a guest

import pickle
def ADDguest():
    file=open("guest.bin","ab")
    guest_id=int(input("\n\t\t\tenter the guest_id:"))
    guest_name=input("\t\t\tenter the guest name:")
    guest_phone=input("\t\t\tenter the guest phone:")
    guest_address=input("\t\t\tenter the guest address:")
    guest=[guest_id,guest_name,guest_phone,guest_address]
    pickle.dump(guest,file)
    file.close()
    print("\n\t\t\t  we add guest successfully!")
    input("\t\t\t  press key to continue....")


# method to view guest
import pickle
def Viewguest():
    
    try:
        file=open("guest.bin","rb")
        print("\n\t\t\t  ** GUEST list **")
        while True:
            guest=pickle.load(file)
            print("\n\t\t guest ID:",guest[0])
            print("\t\t guest name:",guest[1])
            print("\t\t guest phone:",guest[2])
            print("\t\t guest address:",guest[3])
            print("\t\t -----------------------")
    except :
        print("\n\t\t here are all the guest")
            
    file.close()
    input("\t\t press key to continue....")

# method to add room

import pickle
def addroom():
    file=open("room.bin","ab")
    room_id=input("\n\t\t enter the room ID:")
    room_type=input("\t\t enter the room type (single/double):")
    room_status=input("\t\t enter the room status (cleaned,under maintenance):")
    room_duration=input("\t\t enter the room duration(24hour/48hour):")
    room_price=input("\t\t enter the room price:")
    
    room=[room_id,room_type,room_status,room_duration,room_price]
    pickle.dump(room,file)
    print("\n\t\t room has been added ")
    file.close()
    input("\t\t press key to continue....")

# method to viewrooms
import pickle
def viewrooms():   
    try:
        file=open("room.bin","rb")
        while True:
            room=pickle.load(file)
            print("\n\t\t room ID:",room[0])
            print("\t\t room type:",room[1])
            print("\t\t room status:",room[2])
            print("\t\t room duration:",room[3])
            print("\t\t room price:",room[4])
                                          
            print("\t\t ---------------------")
            
    except EOFError:
        print("\n\t\t here all the room details")
    except FileNotFoundError:
        print("\n\t\t  -------No room found!--------")
    finally:
        try:
            file.close()
        except:
            pass
    input("\n\t\t press key to continue....")
    
# Method to book rooms

import pickle
def bookrooms():
    with open("bookrooms.bin","ab") as file:
        booking_id=int(input("\n\t\t enter the booking ID:"))
        guest_id=input("\t\t enter the guest id:")
        room_id=int(input("\t\t enter the room id:"))
        check_in_date=input("\t\t enter the check in date:")
        check_out_date=input("\t\t enter the check out date:")
        duration=input("\t\t enter the duration for book  booked:")
        total_price=int(input("\t\tenter the total booking price:"))
        payment=input("\t\tenter the paymnet status( paid/pending):")
        booking=[booking_id,guest_id,room_id,check_in_date,duration,total_price,payment]
        pickle.dump(booking,file)
        
    print("\n\t\t booking saved successfully")
    
    input("\n\t\t press key to continue....")

# method to viewbooking of rooms

import pickle
def viewbookings():
    
        try:
            with open("bookrooms.bin","rb") as file:
                while True:
                    booking=pickle.load(file)
                    print("\n\t\t enter the booking ID:",booking[0])
                    print("\t\t enter the guest ID:",booking[1])
                    print("\t\t enter the room ID:",booking[2])
                    print("\t\t enter the check_in_date :",booking[3])
                    print("\t\t enter the duration:",booking[4])
                    print("\t\t enter the total price:",booking[5])
                    print("\t\t enter the payment status:",booking[6])
                    print("\t\t -----------------------------------")
                
        except EOFError:
            print("\n\t\t here all the booking details")
        except FileNotFoundError:
            print("\n\t\t NO data found")
            
            
        print("\n\t\t here all the booking details")
        input("\n\t\t press key to continue....")
        
    
    









print("\n\t\t ***HOTEL BOOKING CONSOLE***")
print("\n\t\t        ADD guest-1")
print("\t\t        VIEW guest-2")
print("\t\t        ADD  ROOM-3")
print("\t\t        VIEW rooms-4")
print("\t\t        BOOK room-5")
print("\t\t        VIEW bookings-6")
print("\t\t        EXIT-0")

while True:
    choice=int(input("\n\t\tenter the number as per requirement:"))
    if choice==0:
        print("\n\t\t\t   -----bye bye----- ")
        break

    elif choice==1:
        ADDguest()

    elif choice==2:
        Viewguest()

    elif choice==3:
        addroom()

    elif choice==4:
        viewrooms()

    elif choice==5:
        bookrooms()

    elif choice==6:
        viewbookings()
            




