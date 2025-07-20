from math import pow,sqrt

 #to find numer of count of string in sub string


# def count_substring(string, sub_string):
#     count=0
#     for i in range(len(string) - len(sub_string) + 1):
#         if string[i:i+len(sub_string)] == sub_string:
#             count += 1
#     return count
# def count_substring(string, sub_string):
#     return string.count("su")
# string = "abssudbdjkdbsusu"
# sub_string ="su"
# count = count_substring(string, sub_string)
# print(count)






# to replace " " with "-"

# def split_and_join(line):
#     line=line.split(" ")
#     line ="-".join(line)
#     return line






# check the number is pailndrome ignoring white space 

# str="A man, a plan, a canal: Panama"

# def palin(str):
    
#     list1=[c.lower() for c in str if c.isalnum()]
#     left=0
#     right=len(list1)-1
#     while left>right:
#         if list1[left]!=list1[right]:
#             return False
#         right-=1
#         left+=1
#     return True    

# print(palin(str))





# Question: Write a Python function to count the frequency of each character in a string and 
# return a disctionary with characters as keys and their counts as values. 
# For example, for "hello", return {'h': 1, 'e': 1, 'l': 2, 'o': 1}.

#s ="hellooo"

# count={}
# def count1(s):
#     for i in s:
#        res=0
#         fors j in s:
      
#             if i==j:
#                 res+=1
#             count[i]=res    
#     return count 






# def isdigitchec(s):
#     return s.isdigit()   




# anagram
# def anagram(s1,s2):
#     return s1.sorted()==s2.sorted()

# print(anagram("silent","listen"))






# largest coomon prefix in list

# def prefix(s):
#     if not s:
#         return ""
#     pre=s[0]
#     for i in s[1:]:
#         while not i.startswith(pre):
#             pre=pre[:-1]
#             if not pre:
#                 return ""
#     return pre          
# s=["floe","floewe","floewwww"]
# print(prefix(s))




# Question: Given a list of strings, group all anagrams together.
#  For example, ["eat", "tea", "tan", "ate", "nat", "bat"] 
# returns [["eat", "tea", "ate"], ["tan", "nat"], ["bat"]].

# li=["eat", "tea", "tan", "ate", "nat", "bat"]
# def group_anagram(words):
#     anagram_groups = {}

#     for word in words:
#         # Sort the word to get the key
#         sorted_word = ''.join(sorted(word))

#         # Add the word to the correct group in the dictionary
#         if sorted_word in anagram_groups:
#             anagram_groups[sorted_word].append(word)
#         else:
#             anagram_groups[sorted_word] = [word]

#     # Return all grouped anagrams as a list
#     return list(anagram_groups.values())

# print(group_anagram(li))







# remove duplicate on string


# s="abdudbhf"
# def duplicate(s):
#     result=""
#     for i in s:
#         if i not in result:
#             result+=i
#     return result
# print(duplicate(s))



#list duplicate
# def remove_duplicates(lst):
#     # Using set (order not preserved)
#     return list(set(lst))

# def remove_duplicates_ordered(lst):
#     # Using loop (preserves order)
#     seen = set()
#     result = []
#     for item in lst:
#         if item not in seen:
#             seen.add(item)
#             result.append(item)
#     return result







# def is_prime(n):
#     if n < 2:
#         return False
#     for i in range(2, int(n ** 0.5) + 1):
#         if n % i == 0:
#             return False
#     return True

# # Example
# print(is_prime(17))  # True
# print(is_prime(4))   # False





# squares = [x**2 for x in range(1, 11) if x % 2 == 0]
# print(squares)  # Output: [4, 16, 36, 64, 100]



 #def reverse_list(lst):
#     left, right = 0, len(lst) - 1
#     while left < right:
#         lst[left], lst[right] = lst[right], lst[left]
#         left += 1
#         right -= 1
#     return lst


# def reverse_list(lst):
#     return lst[::-1]

# # Example
# lst = [1, 2, 3, 4]
# print(reverse_list(lst))  # Output: [4, 3, 2, 1]










# def word_frequency(sentence):
#     words = sentence.lower().split()
#     freq = {}
#     for word in words:
#         freq[word] = freq.get(word, 0) + 1
#     return freq

# print(word_frequency("the quick brown fox the"))  
# # Output: {'the': 2, 'quick': 1, 'brown': 1, 'fox': 1}










# def odd_frequency_chars_manual(s):
#     # Count frequency using a dictionary
#     freq = {}
#     for char in s:
#         freq[char] = freq.get(char, 0) + 1
    
#     # Collect odd-frequency characters in order
#     result = []
#     seen = set()
#     for char in s:
#         if freq[char] % 2 != 0 and char not in seen:
#             result.append(char)
#             seen.add(char)
    
#     return ''.join(result)







#to uppercase without using method

# def toupper(s):
#     result=""
#     for char in s:
#         if "a" <= char <= "z":
#             result+=chr(ord(char)-32)

#     return result         
# s1="python"
# print(toupper(s1))




## return index of i non repeating string
# s="swiss"

# def returnfirstindex(s):
#     count=[0]*len(s)
#     for i in range(len(s)):
#         for j in range(len(s)):
#             if s[i]==s[j]:
#                 count[i]+=1
#     for i in range(len(count)):
#         if count[i]==1:
#             return i        
# print(returnfirstindex(s))
### 


        ###using dict
# def firstindex(s):
#     count={}
#     for i in s:
#         count[i]=count.get(i,0)+1

#     for i in range(len(s)):
#         if count[s[i]]==1:
#             return i

#     return -1        
# s="swiss"
# print(firstindex(s))







# def mostfrequent(s):
#    count={}
#    max_char=""
#    max_count=0 
#    for i in s:
#       count[i]=count.get(i,0)+1
   
#    for j,count in count.items():
#       if count > max_count:
#          max_char=j
#          max_count=count


#    return max_char



# s = "banana"
# count = {}

# for char in s:
#     count[char] = count.get(char, 0) + 1

# max_char = max(count, key=count.get)
# print("Most frequent character:", max_char)


# print(mostfrequent("uwdgabkdugaaaaaa"))
   
      
        

###########longest word 

# def longestword1(s):
#     a=s.split()
#     longestword=""
#     for i in a:
#         if len(i) > len(longestword):
#             longestword=i
#     return longestword

# print(longestword1("i loveagqyghfyucutd python,dgtydutududfcu programminif")) 




   



## compressed word
#aaabbcc==a3b2c2


# def comp(s):
#     compressed=[]
#     count=1
#     for i in range(1,len(s)):
#         if s[i]==s[i-1]:
#             count+=1
#         else:
#             compressed.append(s[i-1]+str(count))
#             count=1    
#     compressed.append(s[-1]+str(count))
#     return "".join(compressed)
# print(comp("aaabbxx"))







# print(any(c.isalnum() for c in s)) 
# print(any(c.isalpha() for c in s)) 
# print(any(c.isadigit() for c in s)) 
# print(any(c.islower() for c in s)) 
# print(any(c.isupper() for c in s)) 




# if __name__ == '__main__':
#     x = int(input())
#     y = int(input())
#     z = int(input())
#     n = int(input())
    
# a_list=[]    
# for a in range(x+1):
#     for b in range(y+1):
#         for c in range(z+1):
#             if a+b+c!=n:
#                 a_list.append([a,b,c])
# print(a_list)
            




            
# from collections import Counter

# N=int(input())
# shoes_size=list(map(int,(input().split())))

# counters=Counter(shoes_size)

# M=int(input())
# earning=0

# for i in range(M):
#     size,price=map(int,input().split())
    
#     if counters[size]>0:
#         earning+=price
#         counters[size]-=1
        
# print(earning)     





# def reverse_words_order_and_swap_cases(sentence):
#     # Write your code here
#     words = sentence.split()
#     # Reverse word order and swap case of each word
#     reversed_swapped = [word.swapcase() for word in reversed(words)]
#     # Join back to a string
#     return ' '.join(reversed_swapped)