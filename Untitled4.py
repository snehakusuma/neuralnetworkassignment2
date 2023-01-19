#!/usr/bin/env python
# coding: utf-8

# In[1]:


def string_alternative(full_name):
    output=''
    for i in range(0,len(full_name),2):
        output+=full_name[i]
    return output

first_name=input()
last_name=input()
full_name=first_name+' '+last_name
result=string_alternative(full_name)
print(result)  


# In[2]:


string = input("Enter list of heights in inches")
L2 = string.split()
print(L2)
Output = []
for word in L2:
    Output.append(int(word)*2.54) 
print(Output)


# In[3]:


import sys

    data=file.read()
    lines=data.split()
    print(lines)
    has={}
    for i in lines:
        if i not in has:
            has[i]=1
        else:
            has[i]+=1
    for i in has:
        count=has[i]
        sys.stdout=open("output.txt","a")
        print(i+" : "+str(count)) 
        sys.stdout.close()


# In[4]:


import sys
f=open("output.txt","x")
with open(r'input.txt','r') as file:
    data=file.read()
    lines=data.split()
    print(lines)
    has={}
    for i in lines:
        if i not in has:
            has[i]=1
        else:
            has[i]+=1
    for i in has:
        count=has[i]
        sys.stdout=open("output.txt","a")
        print(i+" : "+str(count)) 
        sys.stdout.close()


# In[ ]:




