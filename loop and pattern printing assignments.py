# loops and pattern printing assignments


# break statement= It will take exit from the current loop

##for i in range(1,6):
##    if i==3:
##        break
##    print(i)

##for i in range(1,6):
##    print(i)
##    if i==3:
##        break

# continue statement=continue will take the cursor to the next iteration
#                               or
# continue will go to the loop again

##for i in range(1,6):
##    if i==3:
##        continue  # it will skip i==3 and continue to loop again
##    print(i)

##for i in range(1,6):
##    print(i)
##    if i==3:
##        continue


# pass statement= will do do thing and take the cursor to the next line
##for i in range(1,6):
##    if i==3:
##        pass 
##        print(i)


##for i in range(1,6):
##    print(i)
##    if i==5:
##        break 
##else:
##    print(0)

##for i in range(1,9,2):
##    if i%0b110==0:       #0b110 it is called binary notation  and also start with the 0b
##                        # it is saying i%6==0:
##        break
##    print(i)


##for i in range(1,10):
##    print(i)
##else:
##    print(0) # else part will work when the loop working fully without any break

##for i in range(1,5):
##    if i==3:
##        break
##    print(i)    
##else:
##    print(0)    # here else did not work bcoz here the condtion is true(i==3).


# nested for loop

##n=int(input("enter the num:"))
##if n<2:
##    print("not prime num")
##else:
##    
##    for i in range(2,n):
##        if n%i==0:
##            print("not prime num")
##            break
##    
##    else:
##        print("prime num")

#ques. print number use a loop from 1-10

##for i in range(1,11):
##    print(i)

#ques. print even number between 1 and 20

##for i in range (1,21):
##    if i%2==0:
##        print(i)

#ques. find sum of numbers from 1-10
##sum=0
##for i in range(1,11):
##    sum+=i
##print("sum is:",sum,end=" ")

#ques..Take a number from the user and print its multiplication table up to 10.

##num=int(input("Enter the num:"))
##for i in range(1,11):
##    print(num*i)

#ques.Take a string and count the total number of characters using a for loop.

##str=input("enter the string:")
##count=0
##for ch in str:
##    count+=1
##print("total character:",count)

# Break Related Questions

#ques.Print numbers from 1 to 10 Stop the loop when the number becomes 5.

##for i in range(1,11):
##    print(i)
##    if i==5:
##        break

#ques.Search for number 25 in a list If found, print "Found" and stop the loop.
##numbers=[25,10,30,5,34]
##for num in numbers:
##    if num==25:
##        print("found",num)
##        break


#ques.Given a list of numbers print the first negative number and stop the loop.

##numbers=[25,-10,30,5,34]
##for num in numbers:
##    if num<0:
##        print("found:",num)
##        break

#       Continue Related Questions 

#ques. Print numbers from 1 to 10 Skip number 5.

##for i in range(1,11):
##    if i==5:
##        continue
##    print(i)

#ques.Print numbers from 1 to 20 Skip all even numbers.
##for i in range(1,21):
##    if i%2==0:
##        continue
##    print(i)

#ques.Print each character of the string "PYTHON" Skip the letter "O".

##word="PYTHON"
##for ch in word:
##    if ch=="O":
##        continue
##    print(ch)

#     Pass Related Questions 

#ques.Run a loop from 1 to 5 but do nothing inside the loop using pass.

##for i in range(1,6):
##    pass

#ques. Loop from 1 to 10 If number is 6, just use pass.
##
##for i in range
##(1,11):
##    if i==6:
##        pass
##else:
##    print(i)

#ques.Q14. Search Number Using for-else Search for number 100 in a list. If found, print "Found".
#If not found, print "Not Found".


#.Take a number from the user and check whether it is prime using for-else.

##num=int(input("enter the num:"))
##if num<=1:
##    print("not prime number")
##else:
##    for i in range(2,num+1):
##        if num%i==0:
##            print("not prime number")
##            break
##    else:
##        print(" prime number")


#  Pattern Questions

# pattern printing
#ques1.
# * * * * *
# * * * * *
# * * * * *
# * * * * *
# * * * * *

##for i in range(1,6):
##    for j in range(1,6):
##        print("*",end=" ")    
##    print()

#ques2.
#*
#* *
#* * *
#* * * *
#* * * * *

##for i in range(1,6):
##    for j in range(1,i+1):
##        print("*",end=" ")
##    print()

#ques3.
# * * * * *
# * * * *
# * * *
# * *
# *

##for i in range(5,0,-1):
##    for j in range(1,i+1):
##        print("*",end=" ")
##    print()

#ques4.
# 1
# 1 2
# 1 2 3
# 1 2 3 4
# 1 2 3 4 5

##for i in range(1,6):
##    for k in range(1,i+1):
##        print(k,end=" ")
##    print()

#ques5.

# 5 4 3 2 1
# 4 3 2 1
# 3 2 1
# 2 1
# 1

##for i in range(5,0,-1):
##    for j in range(i,0,-1):
##        print(j,end=" ")
##    print()


##k=1
##for i in range(1,5):
##    for j in range(1,i+1):
##        print(k, end= " ")
##        k+=1
##    print()

#ques 6.
##1
##01
##010
##1010
##10101


##k=1
##m=1
##for i in range(1,6):
##    for j in range(1,i+1):
##        print(k,end="")
##        k=k-m
##        m=-m
##    print()

 #       OR
##k=1
##for i in range(1,6):
##    for j in range(1,i+1):
##        print(k%2,end="")
##        k+=1
##    print()

#ques7.

##A
##AB
##ABC
##ABCD
##ABCDE
 

##for i in range(1,6):
##    for j in range(1,i+1):   # we used 65+ for upper case and from 97 for lowercase
##                             # and for the numeric we used from 48-57 for [0-9]
##        print(chr(j+64),end="")
##    print()

#ques8.

##A
##BB
##CCC
##DDDD
##EEEEE

##for i in range(1,6):
##    for j in range(1,i+1):
##        print(chr(i+64),end=" ")
##    print()

#ques 9.

##A
##BC
##DEF
##GHIJ
##KLMNO

 
##k=65
##for i in range(1,6):
##    for j in range(1,i+1):
##        print(chr(k),end="")
##        k+=1
##    print()

#ques10.

##    *
##   **
##  ***
## ****
##*****

##for i in range(1,6):
##    for k in range(5,i,-1):
##        print(" ",end="")
##    for j in range(1,i+1):
##        print("*",end="")
##    print()


##    *
##   * *
##  * * *
## * * * *
##* * * * *

##for i in range(1,6):
##    for k in range(5,i,-1):
##        print(" ",end="")
##    
##    for j in range(1,i+1):
##        print("* ",end="")
##    print()












    
    







#Print a star pattern Stop printing when the row number reaches 4.

##for i in range(1,6):
##  if i==4:
##      break
##    
##  for j in range(i):
##        print("*",end="")
##  print()


             #while loop
#ques.Print numbers from 1 to 10 using a while loop.

##i=0
##while i<10:
##    i+=1
##    print(i,end="  ")

#ques.Print even numbers from 1 to 20.

##i=0
##while i<=20:
##    i+=2
##    print(i)

#ques. Print odd numbers from 1 to 20.

##i=1
##while i<20:
##    print(i)
##    i+=2


#ques.Print numbers from 10 to 1 (reverse order).

##i=10
##while i>=1:
##    print(i)
##    i-=1

#ques.Print multiplication table of 5 using while loop.

##i=0
##while i<10:
##    i+=1
##    print(5*i)


                  # Intermediate Level

#ques.Find the sum of first 10 natural numbers using while loop.

##i=1
##sum=0
##while i<=10:
##    sum+=i
##    i+=1
##    
##print("sum is:",sum)

#ques.Find factorial of a number entered by user.

##num=int(input("enter the number:"))
##i=1
##fact=1
##while i<=num:
##    fact*=i
##    i+=1
##print(fact)

#ques.Count number of digits in a given number.

##n=int(input("enter the number:"))
##count=0
##while n>0:
##    n=n//10
##    count+=1
##print(count)

# ques. WAP to add the number of a digit take number from the user with while loop

##num=int(input("enter the number:"))
##add=0
##while num>0:
##    rem=num%10
##    add=add+rem
##    num=num//10
##print(add)



# ques .WAP to reverse a number

##num=int(input("enter the num:"))
##rev=0
##while num>0:
##    digit=num%10
##    rev=rev*10+digit
##    num=num//10
##print("reversed number:",rev)

# ques. WAP to check whether a number is palindrome or not.

##num=int(input("enter the num:"))
##original=num
##rev=0
##while num>0:
##    digit=num%10
##    rev=rev*10+digit
##    num=num//10
##if original==rev:
##    print("number is palindrome")
##else:
##    print("number is not palindrome")

# ques. Ask user to enter password until correct password is entered.
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

# ques. Create a number guessing game: 
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

# ques .Keep taking input numbers until user enters 0, then print total sum.

##sum=0
##while True:
##    num=int(input("enter the number:"))
##    if num==0:
##        break
##    
##    sum+=num
##print(sum)

# ques. Check whether a number is Armstrong number.
##
##num=int(input("enter the num:"))
##original=num
##digits=str(num)
##n=len(digits)
##total=0
##while num>0:
##    digit=num%10
##    total+=digit**n
##    num=num//10
##if total==original:
##    print("number is armstrong:",num)
##    
##else:
##    print("not arm strong:",num)

# ques. Print Fibonacci series up to N terms using while loop.
##a=0
##b=1
##terms=10
##for i in range(10):
##    c=a+b
##    print(c)
##    a=b
##    b=c




#ques.Print prime numbers between 1 to 50 using while loop.

##num=2
##while num<=50:
##  count=0
##  i=2
##while i<=num-1:
##    if num%2==0:
##            count+=1
##     i+=1
##   if count==0:
##       print(num,end=" ")
##  num+=1



    
            


        





















            

    
    
    
    
        
        





    











    
    
    





