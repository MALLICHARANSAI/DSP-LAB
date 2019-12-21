import numpy as np                 
a=input('Enter any array:')        
b=input('Enter array to append:') 
c=a
d=b
x=np.array(c)
y=np.array(d)
e=np.append(x,y)		  
print(e)
for i in range(0,len(b)):	   	
	a.append(b[i])		   
print('The appended array using for loop:',a)
