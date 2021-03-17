from collections import Counter 
  
# initializing string  
test_str = "GeeksforGeeks"
  
# printing original string 
print ("The original string is : " + test_str) 
  
# using collections.Counter() + min() to get  
# Least Frequent Character in String 
res = Counter(test_str) 
print(res)
res = min(res, key = res.get)
