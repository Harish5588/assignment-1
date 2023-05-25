#!/usr/bin/env python
# coding: utf-8

# In[3]:


numbers=(0,1,2,3,4,5,6,7,8,9,10)
count_odd=0
count_even=0
for x in numbers:
    if x%2==0:
        count_even+=1
    else:
        count_odd+=1
print("No. of even numbers :",count_even)
print("No. of odd numbers :",count_odd)


# In[ ]:




