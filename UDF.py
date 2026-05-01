##USER DEFINED ASSISGNMENTS
##
##BASIC
##ques no.1 Write a function to print "Hello World".
##def greet():
##    print("hello world")
##greet()
##
##ques no 2. Create a function that takes a number and returns its square.
##def square(val):
##    return val**2
##print(square(10))
##print(square(3))
##
##ques no 3. Write a function to check whether a number is even or odd.
##
##def num(n):
##    if n%2==0:
##        print("even")
##    else:
##        print("odd")
##
##num(20)
##num(15)
##
##quesno.4Create a function that returns the sum of two numbers.
##
##def sum(a,b):
##    return a+b
##print(sum(10,20))
##print(sum(30,40))
##
##quesno.5 Write a function to find the maximum of three numbers.
##
##def maximum(a,b,c):
##    if a>=b and a>=c:
##        return " a is maximum",a
##    elif  b>=c and b>=a:
##        return "b is maxium", b
##    
##    else:
##        return "c is maximum",c
##print("maxmium",maximum(10,20,30))
##print(maximum(30,4,5))
##
##quesno .6 Create a function that takes a string and returns it in uppercase.
##
##def str1(word):
##     return word.upper()
##print(str1("harsh"))
##print(str1("rathi"))
##
##ques no .7 Create a function that checks if a number is positive, negative, or zero.
##
##def num(n):
##    if n>0:
##        return "positive"
##    elif n<0:
##        return "negative"
##    else:
##        return "zero"
##print(num(30))
##print(num(-10))
##
##ques no. 8 Write a function to count the number of vowels in a string.
##
##def count_vowels(s):
##    count=0
##    vowels="aeiouAEIOU"
##    for ch in s:
##
##        if ch in vowels:
##            count+=1
##    return count
##print(count_vowels("harsh"))
##print(count_vowels("education"))
##
##ques no.9 Create a function that returns the length of a list (without using len()).
##def count_list(l):
##    count=0
##    for i in l:
##        count+=1
##    return count
##print(count_list([1,34,45,31]))
##
##ques no .10  Write a function to calculate the factorial of a number.
##
##def factorial(n):
##    result=1
##    for i in range(1,n+1):
##        result=result*i
##    return result
##print(factorial(5))
##print(factorial(10))
##
##ques no. 11 Write a function to check whether a number is prime.
##
##def isprime(n):
##    if n<2:
##        return "not prime "
##    for i in range(2,int(n**0.5)+1):
##        if n%i==0:
##            return "not prime"
##        
##    return "prime"
##print(isprime(10))
##print(isprime(13))
##print(isprime(1))
##
##ques no.12  Create a function that returns the reverse of a string.
##
##def rev_str(s):
##    rev=""
##    for i in range(len(s)-1,-1,-1):
##        rev=rev+s[i]
##
##    return rev
##print(rev_str("harsh"))
##print(rev_str("rathi"))
##
##ques no.13  Write a function to find the sum of all elements in a list.
##
##def sum_list(li):
##    total=0
##    for i in li:
##        total+=i
##    return total
##print(sum_list([10,20,30,40]))
##
##ques no.14  Create a function that returns the second largest number in a list.
##
##
##ques no.15  Write a function to remove duplicates from a list.
##
##def rem_dup(li):
##    seen=set()
##    result=[]
##    for item in li:
##        if item not in seen:
##            seen.add(item)
##            result.append(item)
##    return result
##
##print(rem_dup([1,3,4,3,1,1,]))
##
##ques no. 16 Create a function that checks if a string is a palindrome
##
##def str_palin(str1):
##    palin=""
##    for i in range (len(str1) -1,-1,-1):
##        palin+=str1[i]
##    if palin==str1:
##        return "string is palindrome"
##    else:
##        return "string is not palindrome"
##print(str_palin("madam"))
##print(str_palin("harsh"))
##
##ques no.17  Write a function that takes a list and returns only even numbers.
##
##def even_list(li):
##    result=[]
##    for i in li:
##        if i%2==0:
##            result.append(i)
##    return result
##            
##print(even_list([10,4,5,3,20]))
##
##ques no.18 . Create a function to count frequency of each element in a list.
##
##ques no.19 . Write a function that merges two lists into one.
##
##def mer_list(li1,li2):
##   
##    return li1+li2
##print(mer_list([10,20,30],[8,9,5]))
##
##ques no.20  Create a function to calculate simple interest.
##
##def simp_int(P,R,T):
##    si=(P*R*T)/100
##    return si
##print(simp_int(1000,8,1))
##
##                 Advanced Level
##
##quesno. 21 Write a function using recursion to find factorial.

##def factorial(n):
##    if n==0:
##        return 1
##    else:
##        return n*factorial(n-1)
##print(factorial(5))
##print(factorial(3))
    




##quesno 22. Create a recursive function for Fibonacci series.


##def fibonacci(n):
##    if n==0:
##        return 0
##    elif n==1:
##        return 1
##    else:
##        return fibonacci(n-1)+fibonacci(n-2)
##
##for i in range(10):
##    print(fibonacci(i),end="")
            
##quesno 23. Write a function that accepts *args and returns their sum.

##def sum_args(*args):
##    return sum(args)
##
##print(sum_args(10,20,30))

##quesno 24.. Write a function that accepts **kwargs and prints key-value pairs

##
##def print_kwargs(**kwargs):
##    for key,value in kwargs.items():
##        print(f"{key}:{value}")
##
##print_kwargs(name="harsh rathi",role="data analyst",skill="python")
##print_kwargs(name="ankit sejwal",role="data science",skill="SQL")

#quesno.25 Create a function decorator that print "Function Started" and "Function Ended".


##def my_decorater(fun):
##    def wrapper(*args ,**kwargs):
##        print("functon started")
##        result=fun(*args,*kwargs)
##        print("function ended")
##        return result
##    return wrapper
##
##def add(a,b):
##    return a+b
##print(add(5,10))

#quesno. 26 Create a function to sort a list without using built-in sort().

##def bubble_sort(lst):
##    n=len(lst)
##    for i in range(n):
##        for j in range(0,n-i-1):
##            if lst[j]>lst[j+1]:
##                lst[j],lst[j+1]=lst[j+1],lst[j]
##    return lst
##number=[10,3,40,34,654,13]
##print(bubble_sort(number))

#quesno. 27 . Write a function that finds common elements in two lists.

##def common_element(list1,list2):
##    common=[]
##    for item in list1:
##        if item in list2:
##            if item not in common:
##                common.append(item)
##    return common
##list1=[30,20,10,5]
##list2=[45,20,5,100]
##print(common_element(list1,list2))

#quesno.28 Create a function to flatten a nested list.

##def flatten_list(nested_list):
##    flat=[]
##    for sublist in nested_list:
##        for item in sublist:
##            flat.append(item)
##    return flat
##
##nested = [[1, 2], [3, 4], [6, 7]]
##print(flatten_list(nested))

#quesno.29  Write a function that validates an email format.

##def validate_email(email):
##    if "@" in email and "." in email :
##        at_index=email.index("@")
##        dot_index=email.rindex(".")
##
##        if at_index> 0 and dot_index> at_index:
##            return True
##    return False
##
##print(validate_email("harsh12@gmail.com"))
##print(validate_email("harsh12gmail.com"))

#quesno.30  Write a function that returns another function (closure concept).

##def outer_function(x):
##    def inner_function(y):
##        return x+y
##    return inner_function
##add5=outer_function(5)
##print(add5(15))
##print(add5(10))

                                    #Challenge Level (Interview Focus)

#quesno. 31 Write a function to implement binary search.

##def binary_search(arr,target):
##    left=0
##    right=len(arr)-1
##    while left<=right:
##        mid=(left+right)//2
##        if arr[mid]==target:
##            return mid
##        elif arr[mid]<target:
##            left=mid+1
##        else:
##            right=mid-1
##    return -1
##
##numbers=[1,3,4,5,7]
##print(binary_search(numbers,7))

#ques no.31  Create a function to generate all substrings of a string.

##def generate_substring(s):
##    substrings=[]
##    for i in range(len(s)):
##        for j in range(i+1,len(s)+1):
##            substrings.append(s[i:j])
##        return substrings
##
##print(generate_substring("harsh"))


#ques no.32 . Write a function to find the first non-repeating character.

##def first_non_rept_character(s):
##    for ch in s:
##        if s.count(ch)==1:
##            return ch
##        
##    return None
##
##print(first_non_rept_character("harsh"))

#quesno .33  Create a function to find missing number in a list.

##def find_miss_num(nums):
##    n=len(nums)+1
##    expected_sum=n*(n+1)//2
##    actual_sum=sum(nums)
##    return expected_sum-actual_sum
##print(find_miss_num([1,2,3,5]))

#quesno. 34  Create a function to implement your own map() function.

##def my_map(func,iterable):
##    result=[]
##    for item in iterable:
##        result.append(func(item))
##    return result
##
##nums=[1,2,3,4]
##print(my_map(lambda x: x*2,nums))
##words=["hello","python"]
##print(my_map(str.upper,words))

#ques no. 35 . Write a function to group words by anagrams.

##def group_anagram(words):
##    anagram_group={}
##    for word in words:
##        key="".join(sorted(word))
##        if key not in anagram_group:
##            anagram_group[key]=[]
##        anagram_group[key].append(word)
##    return list(anagram_group.values())
##words=["eat","tea","tan","nat"]
##print(group_anagram(words))

#               Bonus (Real-world Practice) 

#ques no .36  Function to calculate student grade system.

##def calc_grade(marks):
##    total=sum(marks)
##    percentage=total/len(marks)
##
##    if percentage>=90:
##        grade="A+"
##
##    elif percentage>=80:
##        grade= "A"
##
##    elif percentage>=70:
##        grade= "B"
##
##    elif percentage>=60:
##        grade="C"
##
##    elif percentage>=50:
##        grade="D"
##
##    return percentage,grade
##
##marks_list=[98,84,72,66,58,43]
##percent,grade=calc_grade(marks_list)
##print(f" percentage:{percent:.2f}%|grade:{grade}")

#quesno.37  Function to simulate a login system.

##def login_system(username,password):
##    stored_username="ADMIN123"
##    stored_password="123456"
##    if username==stored_username and password==stored_password:
##        return "login successful"
##    else:
##        return "Invalid username or password"
##
##user=input("enter the username:")
##pwd=input("enter the password:")
##print(login_system(user,pwd))

#quesno. 38 Function to clean and preprocess text data.

##import re
##def clean_text(text):
##    text=text.lower()
##    text=re.sub(r'[^a-z\s]', '', text)
##    text = re.sub(r'\s+', ' ', text).strip()
##    return text
##raw_text="Hello!!! This is for preprocess text data, with Numbers 123 and symbols #@$"
##cleaned=clean_text(raw_text)
##print("before":,raw_text)
##print("after":,cleaned)


#quesno. 39  Function to calculate moving average.

##def moving_avg(nums,window_size):
##    result=[]
##    for i in range(len(nums)-window_size+1):
##        window=nums[i::i+window_size]
##        avg=sum(window)/window_size
##        result.append(avg)
##    return result
##data=[10,30,40,50]
##print(moving_avg(data,4))

#quesno. 40 . Function to split dataset into train/test (basic logic).

##def train_test_split(dataset, test_ratio=0.3):
##    split_index = int(len(dataset) * (1 - test_ratio))                                     
##    train = dataset[:split_index]
##    test = dataset[split_index:]
##    return train, test
##data = [1, 2, 3, 4, 5, 6, 7, 8, 9]
##train, test = train_test_split(data, test_ratio=0.3)
##
##print("Train set:", train)
##print("Test set:", test)






    
    
    
    









































