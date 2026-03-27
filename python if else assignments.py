#A. Python IF (Single Condition)

#1.Print "Eligible to vote" if age is 18 or above
##age=int(input("enter the age:"))
##if age>=18:
##    print("eligible to vote")
##else:
##    print("not eligible to vote")

#2.Check if a number is divisible by 7.

##num=int(input("enter the num:"))
##if num%7==0:
##    print("num is divisible by 7")

#3.Display a message if temperature exceeds 45°C.

##temp=int(input("enter the temp(in celsius):"))
##if temp>=45:
##    print("turn of switch ")

#4. Check if a string length is more than 8 characters.

##str=input("enter the string:")
##if len(str)>=8:
##    print("length is fine")

#5. Print a warning if balance is below minimum limit.

##balance=int(input("enter your balance:"))
##if bal<1000:
##    print("maintain balance of minimum of 1000")

#B. Python IF–ELSE (Two Conditions)

#6.Check whether a number is even or odd.
##num=int(input("enter the number:"))
##if num%2==0:
##    print("num is even",num)
##else:
##    print("num is odd",num)

#7. Check whether a number is positive or negative.

##num=int(input("enter the number:"))
##if num>0:
##    print("num is positive")
##else:
##    print("num is negative")

#8.Check whether a character is a vowel or consonant.

##char=input("enter the char:")
##if char in "aeiou" or "AEIOU":
##    print("vowel")
##else:
##    print("constant")

#9.Print "Valid Password" or "Invalid Password".

##password=input("enter the password:")
##if password=="Harsh@123":
##    print("valid password")
##else:
##    print("invalid password")

#10.Print "Pass" or "Fail" based on marks.

##marks=int(input("enter your marks:"))
##if marks>=33:
##    print("pass")
##else:
##    print("fail")


#C. Python NESTED IF–ELSE


#11.. Find the largest of three numbers.

##num1=int(input("enter the num1:"))
##num2=int(input("enter the num2:"))
##num3=int(input("enter the num3:"))
##if num1>num2:
##    if num1>num3:
##        print("num 1 is largest",num1)
##    else:
##        print("num3 is largest",num3)
##else:
##    if num2> num3:
##        print("num2 is largest",num2)
##    else:
##
##        print("num3 is largest",num3)

#12. Check whether a triangle is equilateral, isosceles, or scalene.
##a=int(input("enter the side1(in cm):"))
##b=int(input("enter the side2(in cm):"))
##c=int(input("enter the side3(in cm):"))
##if a==b:
##    if b==c:
##        print("traingle is equilateral")
##    else:
##        print("triangle is isoceles")
##else:
##    if b==c:
##        print("triangle is isosceles")
##    else:
##        if a==c:
##               print("triangle is isoceles")
##        else:
##            print("scalene is triangle")

#13. Assign grades: 
##● A → marks ≥ 90 
##● B → marks ≥ 75 
##● C → marks ≥ 60 
##● Fail → below 60

##marks=int(input("enter the marks:"))
##if marks>=90:
##    print("A grade")
##elif marks>=80:
##    print("B grade")
##elif marks>=70:
##    print("C grade")
##elif marks<=60:
##    print("fail ")

#14. Check whether a character is uppercase, lowercase, digit, or special character.

##char=input("enter the marks:")
##if char.isupper():
##    print("upper case")
##elif char.islower():
##    print("lowercase")
##elif char.isdigit():
##    print("is digit")
##else:
##    print("special character")

#15. Find the second largest number among three numbers.

##num1 = int(input("Enter num1: "))
##num2 = int(input("Enter num2: "))
##num3 = int(input("Enter num3: "))
##
##if (num1 <= num2 or num1 <= num3) and (num1 >= num2 or num1 >= num3):
##    print("Second largest is num1:", num1)
##
##elif (num2 <= num1 or num2 <= num3) and (num2 >= num1 or num2 >= num3):
##    print("Second largest is num2:", num2)
##
##else:
##    print("Second largest is num3:", num3)

#16. Check loan eligibility using age, salary, and credit score.
##age=int(input("Enter your age:"))
##salary=float(input("enter your salary:"))
##credit_score=int(input("enter the credit_score:"))
##if age>=21:
##    if salary>=50000:
##        if credit_score>=750:
##            print("you are eligible for the loan")
##        else:
##            print("you are not eligible for the loan because your credit score is low")
##    else:
##        if credit_score>=750:
##            print("salary is too low")
##        else:
##            print("salary and credit score is too low")
##else:
##    print("not eligible must be above 21")


# Python ELIF (Multiple Conditions)

#17. Display bonus percentage based on experience years.

##years=int(input("enter the experience years:"))
##if years<=2:
##    print("bonus is 20% ")
##elif years<=5:
##    print("bonus is 50%")
##else:
##    print("full salary bonus")

#18. Identify traffic signal meaning.


##light=input("enter the color of traffic light:")
##if light=="yellow":
##    print("ready ")
##elif light=="red":
##    print("stop")
##elif light=="green":
##    print("go")

#19. Identify number type: single-digit / double-digit / multi-digit.

##digit=int(input("enter the digit:"))
##if digit>=0 and digit<=9:
##    print("one digit")
##elif digit>=10 and digit<=99:
##    print("two digit")
##elif digit>=100 and digit<=999:
##    print("three digit")
##else:
##    print("multi digit")

#20. Assign performance rating: Poor / Average / Good / Excellent.

##n=int(input("enter the rating (out of 10) -"))
##if n<=3:
##    print("poor")
##elif n<=5:
##    print("average")
##elif n<=8:
##    print("good")
##else:
##    print("excellent")


#E. Python COMPLEX CONDITIONS (AND / OR / NOT)

#21.Check whether a number is divisible by 5 and 11.

##num=int(input("enter the number:"))
##if num%5==0 and num%11==0:
##    print("yes num is divisible by 5 and 11")
##else:
##    print("yes num is not divisible by 5 and 11")

#22. Validate login using username AND password.

##a=input("enter your username:")
##b=input("enter the password:")
##if a=="Harsh rathi" and b=="Harsh@123":
##    print("login successful")
##else:
##    print("login fail")

#23.46. Check exam eligibility: 
#● attendance ≥ 75% OR 
#● medical certificate available

##attendance=int(input("enter the attendance % :"))
##medical_certificate=input("enter in yes/no:")
##if attendance >=75 or  medical_certificate=="yes":
##    print("yes you can sit in exam")
##else:
##    print("you can't sit in exam")

#24.Check whether an email format is valid.

##email=input("enter your email:")
##if "@" in email  and "." in email:
##    if email.index("@") < email.index("."):
##        print("valid email")
##    else:
##        print("invalid e mail format")
##else:
##    print("invalid e mail")

#25.Check leap year using complete leap year logic.

##year=int(input("enter the year:"))
##if year%400==0 or year%100!=0 and  year%4==0:
##    print("leap year")
##else:
##    print("not leap year")

#F. INTERVIEW-LEVEL PYTHON LOGIC QUESTIONS

#26.Write a Python program to calculate income tax using slabs.

##income=int(input("enter your income:"))
##if income<=600000:
##    print("tax free income")
##elif income<=1000000:
##    print("tax will be 15% and tax is",income*0.15)
##elif income<=1500000:
##    print("tax will be 30% and tax is ",income *0.30)
##else:
##    print("tax will be 40% and tax is ",income*0.40)

#27. Create an ATM withdrawal program with balance checks

##balance=50000
##amount=int(input("enter the amount:"))
##if amount>balance:
##    print("insufficient balance")
##else:
##    remaining_balance=balance-amount
##    print("withdrawal succesful")
##    print("remaining balance",remaining_balance)

#28.Calculate delivery charges based on location and order amount.

##order_amount=int(input("enter the amount:"))
##location=input("enter the location(nearby/far/other town:")
##if order_amount<=500 and location=="nearby":
##    print("no charge on order")
##elif order_amount>=2000 and location=="far":
##    print("100  ruppes charge on order")
##else:
##    print("250 ruppes charge on order")

#29.Create a menu-driven program using if–elif–else.

##print(".......MENU......")
##print("1-pizza")
##print("2-burger")
##print("3-ice crea,")
##print("4-coffee")
##
##num=int(input("enter the number from the above list (from1-4):"))
##if num==1:
##    print("pizza, receive order within 10 min")
##elif num==2:
##    print("burger, receive order within 5 min")
##elif num==3:
##    print("take your ice-cream")
##elif num==4:
##    print("take your burger")
##else:
##    print("invalid number from 1-4")


#30.. Validate strong password using multiple conditions.

##password=input("enter your password:")
##
##has_upper=any(i.isupper() for i in password)
##has_lower=any(i.islower() for i in password)
##has_digit=any(i.isdigit() for i in password)
##has_special=any(i in "!@#$^&*." for i in password)
##has_length=len(password)>=8
##if has_upper and has_lower and has_digit and has_special and has_length:
##               print("valid password")
##else:
##    print("invalid passoword")

    

#            logical/scenario question


#Ask user to enter password until correct password is entered.
##print("www.harsh.com")
##password="harsh@"
##while True:
##    
##    user_input=input("enter the password:")
##
##    if user_input==password:
##        print(" access granted")
##        break
##    else:
##        print("wrong password,try again")

#Create a number guessing game: 
##• Generate a random number (1–10) 
##• Keep asking user until they guess correctly


##import random
##num=random.randint(1,10)
##while True:
##    user_input=int(input("enter the num as user:"))
##    if user_input==num:
##        print("good number is matching")
##        break
##    else:
##        print("number is not matching,try again")

#Print Fibonacci series up to N terms using while loop.
##a=0
##b=1
##terms=10
##for i in range(10):
##    c=a+b
##    print(c)
##    a=b
##    b=c

#Print prime numbers between 1 to 50 using while loop.

num=2
while num<=50:
    count=0
    i=2
    while i<=num-1:
        if num%2==0:
            count+=1
        i+=1
    if count==0:
        print(num,end=" ")
    num+=1



    
            


        

















