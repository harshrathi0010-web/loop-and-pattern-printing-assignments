# Lambda Basics

#Q1. Write a lambda function to add two number

##add =lambda a,b:a+b
##print(add(10,50))
##print(add(33,12))

#Q2. Write a lambda function to check if a number is even or odd.

##check_even_odd=lambda num: "even" if num%2==0  else  "odd"
##print(check_even_odd(20))
##print(check_even_odd(13))


#            MAP BASICS
#Q3. Given a list of integers, use map() to create a new list with each number squared.

##square=lambda val:val**2
##list1=[1,2,4,5,6,8]
##result=list(map(square,list1))
##print(result)

#Q4. Convert a list of strings to uppercase using map().

##words=["harsh","rathi","croma","CaMpus"]
##
##upper_case=list(map(str.upper,words))
##print(upper_case)

#     filter Basics
#Q5.  Given a list of numbers, filter out only even numbers.

##numbers=[1,2,3,4,5,6,7,8]
##even_num=list(filter(lambda x: x%2==0,numbers))
##print(even_num)

#Q6. Filter words that have length greater than 5 from a list of strings.

##words=["harsh","aniket","shubham","sonu"]
##filter_word=list(filter(lambda x : len(x)>5 ,words))
##print(filter_word)


                    #Using Reduce
#Q7. Find the sum of all elements in a list using reduce().

##from functools import reduce
##
##numbers=[1,2,30,4,5]
##total_sum=reduce(lambda x,y:x+y,numbers)
##print(total_sum)

#Q8. Find the product of all numbers in a list.

##from functools import reduce
##
##numbers=[5,3,2,7]
##total_product=reduce(lambda x,y:x*y,numbers)
##print(total_product)

             #Intermediate Level

            #Combination of lambda + map

#Q9. Given a list of numbers, return a list where each number is multiplied by 10.

##numbers=[1,4,5,5,6,32]
##result=list(map(lambda x:x*10,numbers))
##print(result)


             #Combination of lambda + filter  
#Q10. From a list of numbers, filter out all numbers divisible by 3.

##numbers=[46,72,30,28,2,7]
##result=list(filter(lambda x:x%3==0,numbers))
##print(result)

                #Using reduce() for maximum

#Q11. Find the maximum number in a list using reduce().

##from functools import reduce
##
##numbers=[10,50,3,56,95]
##max_result=reduce(lambda a,b: a if a>b else b,numbers)
##print(max_result)
                       #String manipulation

#Q12. Given a list of names, use map() to return names with their first letter capitalized.

##words=["harsh","Ankit","suraj"]
##result=list(map(str.capitalize,words))
##print(result)

                       #filter palindromes
#Q13. Given a list of strings, filter out only palindrome words using filter().

##words=["madam","sir"]
##result_palin=list(filter(lambda x:x==x[::-1],words))
##print(result_palin)


                         
























