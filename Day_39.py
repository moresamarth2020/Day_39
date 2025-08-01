#!/usr/bin/env python
# coding: utf-8

# # read-readlines-and-other-methods

# In[33]:


#Create A file
f = open('myfile_1.txt','w')
f.write('Samarth Nagesh')

#Read
f = open('myfile_1.txt','r')
contents = f.read()
print(contents)


# # readlines() method
# The readline() method reads a single line from the file. If we want to read multiple lines, we can use a loop.

# In[34]:


f = open('myfile_1.txt', 'r')
while True:
    line = f.readline()
    if not line:
        break
    print(line)


# # writelines() method
# The writelines() method in Python writes a sequence of strings to a file. The sequence can be any iterable object, such as a list or a tuple.
# Here's an example of how to use the writelines() method:

# In[37]:


f = open('myfile_2.txt','w')
lines = ['Line 1\n','Line 1\n', 'Line 3\n' ]
f.writelines(lines)
f.close()


# In[41]:


f = open('myfile_2.txt','r')
con = f.read()
print(con)


# This will write the strings in the lines list to the file myfile.txt. The \n characters are used to add newline characters to the end of each string.
# Keep in mind that the writelines() method does not add newline characters between the strings in the sequence. If you want to add newlines between the strings, you can use a loop to write each string separately:

# In[42]:


f = open('myfile_2.txt', 'w')
lines = ['line 1', 'line 2', 'line 3']
for line in lines:
    f.write(line + '\n')
f.close()


# In[44]:


f = open('myfile_2.txt','r')
con = f.read()
print(con)


# In[ ]:





# In[ ]:




