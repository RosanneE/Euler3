# The prime factors of 13195 are 5, 7, 13 and 29.

# What is the largest prime factor of the number 600851475143 ?

# http://codepad.org/TM3xGIQq

num = 600851475143
n = num - 1
count = 2
prime = 0

#Ends when prime is given a non zero value
while prime ==0:
 
 # if the number we are currently evaluating divides into the original number, it may be a prime factor
 if num % n == 0:
  
  #starting at 2, checks to see if the number is prime
  while count <= n
  
  #if the number divides into num and is prime, it is le largest prime number
   if count == n:
    prime = n
   
   #checks to see if the number is divisable by smaller numbers
   elif count <n:
    
    #means the number is not prime, moves to check the next number
    if n % count == 0:
     
     #
    
    #not divisible by the counter, check next counter number
    elif:
     count += count
    
  
 
 #is not a factor, check next number
 else:
  num -= num
 
print(prime)

"""while prime == 0:

 if num % n == 0:
  
   while count <= n:
    if count == n:
        prime = n
    if n % count ==0:
      count = n + 1
      n -= n
    if n% count != 0:
      count += count
    count = 2
   if count == n:
      n -= n
 if num % n != 0:
      n -= n
      
print (prime)   """

#while n < num:
  
 # if num%n == 0:
    #check prime list to see if any number in it divides that number
  #  prime.append(n)
   # print (list)
    
  #n += 1
  
#print (prime)
