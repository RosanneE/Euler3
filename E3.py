# The prime factors of 13195 are 5, 7, 13 and 29.

# What is the largest prime factor of the number 600851475143 ?

# http://codepad.org/TM3xGIQq

n = 1
num = 600851475143
prime = 1

while n < num:
  if num%n == 0:
    prime = n
    print (prime)
  n += 1
print (prime)

#while n < num:
 # if n%num == 0:
 #   prime = n
 #   n = n+1
 # else:
 #   n = n+1
#print (prime)
