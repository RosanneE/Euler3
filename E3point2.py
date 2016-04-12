#The prime factors of 13195 are 5, 7, 13 and 29.
#What is the largest prime factor of the number 600851475143 ?

#prime returns the largest prime number
prime = 0
#num is the number we are finding the prime of
num = 600851475143
#curr is the current number
curr = 600851475143 - 1
#count counts up to curr to check if curr is prime
count = 2

#end program when prime != 0
while prime == 0:
 if curr == 2:
  print "SO WRONG"
#If curr Goes into prime with no remainder, curr could be prime
 if curr % num ==0:
  #check if curr is prime
  while count <= curr:
 #curr is not prime
   if curr%count == 0:
    curr = cur - 1
   # Keep checking for prime
   elif count == curr:
    prime = curr
    print prime
   else:
    count = count + 1
    
    
 #If curr has a remainder
 else:
  curr = curr -1 
  
print prime 

 
 

  
 

