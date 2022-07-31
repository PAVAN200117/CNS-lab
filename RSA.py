import math 
import random 
message=int(input("Enter the message to be encrypted:"))
p=int(input("Enter the p value:"))
q=int(input("Enter the q value:"))
n=p*q
phi=(p-1)*(q-1)
def gcd(a,b):
  while b:
     a,b=b,a%b
  return a
li=[]
for r in range(3,phi,2):
  while true:
    if gcd(r,phi)==1:
      li.append(r)
      break
    else:
      r+=1
print(li)
li=list(set(li))
print(li)
e=random.choice(li)
print("e=",e)
d=1
while((d*e)%phi!=1)
  d+=1
def encrypt(me):
  en=me**e
  c=en%n
  print("The encrypted is :",c)
  return c
def decrypt(c):
  de=c**d
  e=de%n
  print("The decrypted is :",e)
  return e
cypher=encrypt(message)
original=decrypt(cipher)
      
