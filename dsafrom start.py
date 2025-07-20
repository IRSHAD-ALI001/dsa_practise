
######################################DSA###########################################################################

# ### reverse
# n=786
# def rev(n):
#     num=n
#     result=0
#     while(num>0):
#         last_dig=num%10
#         result=(result*10)+last_dig
#         num=num//10

#     return result   

# print(rev(n))                                                



############pallindrone#######
#n=2324444
# def pallin(n):
    
#     num=n
#     result=0
#     while(num>0):
#         last_dig=num%10
#         result=(result*10)+last_dig
#         num=num//10

#     return result==n 

# print(pallin(n))



###########armstrong
# n=153
# def arm(n):
#     num=n
#     le=int(len(str(n)))
#     result=0
#     while(num>0):
#         las=num%10
#         result+=pow(las,le)
#         num=num//10
#     return result==n
# print(arm(n))   

################frequency in digit
# def freqq(n):
#     freq=dict()
#     num=n
#     for i in range(0,len(num)):
#         if num[i] in freq:
#             freq[num[i]]+=1
#         else:
#             freq[num[i]]=1

#     return freq

# print(freqq("123456789123456789"))



# def freqq(n):
#     freq=dict()
#     num=(n)
#     for i in range(0,len(num)):
#         freq[num[i]]=freq.get(num[i],0)+1
#     return freq


# print(freqq("123456789123456789"))



##########factors


#n=12
# def fact(n):
#     num=n
#     result=[]
#     for i in range(1,int(sqrt(num)+1)):
#         if num%i==0:
#             result.append(i)
#             if num//i!=i:
#                result.append(num//i)
    
#     result.sort()
#     return result 
# print(fact(n))           

# def fact(n):
#     num=n
#     result=[]
#     for i  in range(1,(num//2)+1):
#         if num%i==0:
#             result.append(i)
#     result.append(num)
       
# print(fact(12)) 
      





###############Recursion

#15 5 times

# def rec(i,n):
   
#     if i==0:
#         return
#     print(n) 
#     rec(i-1,n)
# rec(9,16)    



##############N to N 
###using head

# def rec(i,N):
#     if i>N:
#         return
#     print(i)
#     rec(i+1,N)
# rec(1,5)

##### N to 1
# def rec(N):
#     if N==0:
#         return
#     print(N)
#     rec(N-1)
# rec(5)



#############using tail recursion
### 1 to N
# def rec(N):
#     if N==0:
#         return
    
#     rec(N-1)
#     print(N)
# rec(5)


# #############N to 1
# def rec(i,N):
#      if i>N:
#         return
     
#      rec(i+1,N)
#      print(i)
# rec(1,5)

    
    
    ##############reveerse a string using recursion
# def reverse_string(s):
#     if len(s) == 0:
#         return s
#     else:
#         return s[-1] + reverse_string(s[:-1])###### 
# s = "hello"
# print(reverse_string(s))  # Output: "olleh" 



##################reverse a list using recursion and two pointers
# def reverse_list(lst, left, right):
#     left =0
#     right = len(lst) - 1
#     if (left =< right):
#         lst[left], lst[right] = lst[right], lst[left]
#         left += 1
#         right -= 1
#     return lst



# def reverse_list(lst, left, right):
#     if (left =< right):
#         lst[left], lst[right] = lst[right], lst[left]
#         reverse_list(lst, left + 1, right - 1)
#     return lst
# lst = [1, 2, 3, 4]
# print(reverse_list(lst, 2, 3))  # Output: [4, 3, 2, 1]    




##########pallindrone
# def is_palindrome(s,left,right):
#     for i in range(0,len(s)):
#         if s[left]!=s[right]:
#             return False
#         left+=1
#         right-=1
#     return True 



# def is_palindrome(s, left, right):
#     if left >= right:
#         return True
#     if s[left] != s[right]:
#         return False
#     return is_palindrome(s, left + 1, right - 1)
# s = "racecar"
# print(is_palindrome(s, 0 , len(s) - 1))  # Output




##########fibonacci using recursion
def fibonacci(n):
    if n<=0:
        return 0
    elif n==1:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)







# def all_fibonacci(n):
#     fib_series = []
#     a, b = 0, 1
#     for _ in range(n):
#         fib_series.append(a)
#         a, b = b, a + b
#     return fib_series

# print(all_fibonacci(10))

# # Example usage

# n = 10    
# for i in range(n):
#     print(fibonacci(i), end=" ")  # Output: 0 1 1 2 3 5 8 13 21 34  
    

    
  