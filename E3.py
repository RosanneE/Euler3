# The prime factors of 13195 are 5, 7, 13 and 29.

# What is the largest prime factor of the number 600851475143 ?

# http://codepad.org/TM3xGIQq

num = 600851475143
n = num - 1
count = 2
prime = 0

while prime == 0:

 if num % n == 0:
   while count <= n:
    if count == n:
        pime = n
    if n % count ==0:
      count = n + 1
      n -= n
    if n% count != 0:
      count += count
    count = 2
   if count == n:
      n -= n
  #if
  #    n -= n
print (prime)  

#while n < num:
  
 # if num%n == 0:
    #check prime list to see if any number in it divides that number
  #  prime.append(n)
   # print (list)
    
  #n += 1
  
#print (prime)
