#!/usr/bin/env python
# coding: utf-8

# In[9]:


#Calculate length of string
str=input("Enter a String: ")
count=0
for i in str:
    count=count+1
print("Length of the Input String is: ", count)


# In[11]:


#Sum of all numbers
num=[1,2,3,4,5]
sum=0;
for i in num:
    sum=sum+x;
print(sum)


# In[18]:


#largest number in a list using sort()
num=[4,546,474,45,645,435]
num.sort()
print("Largest number in the list is:", num[-1])


# In[21]:


#largest number in a list using max()
num=[4,36,345,435,5435,65]
print("Largest number in the list is: ",max(num))


# In[29]:


#print the even numbers in the list
lis1=[33,4,34,545,34,45,5,3,34,34,44,4]
for num in lis1:
    if num % 2==0:
        print(num,end=" ")


# In[ ]:




