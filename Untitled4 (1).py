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


# In[9]:


from collections import Counter

with open(r"C:\Users\DELL\input.txt","r") as f:
    lines = f.read()
    list_words = (' '.join(lines.splitlines())).split()
    ar = str(dict(Counter(list_words)))
    with open('output2.txt', 'w') as s:
        s.write(ar)


# In[ ]:




