#import os
import matplotlib.pyplot as plt


data_file_name=input("Enter the name of your data file:")
file_Object=open('C:/Users/pooja/.spyder-py3/'+data_file_name,"r")

first_line=file_Object.readline()
first_line_array=first_line.split()
max_rows=first_line_array[0]
no_of_elements=first_line_array[1]

feature_array=[]
for i in range (150):
    feature_array=file_Object.readline()
print(feature_array)

print('''You can do a plot of any two features of the Iris Data set
The feature codes are:
0 = sepal length
1 = sepal width
2 = petal length
3 = petal width''')

#horizontal_axis=int(input("Enter feature code for the horizontal axis: "))
#vertical_axis=int(input("Enter feature code for the vertical axis: "))

#plt.plot(horizontal_axis,vertical_axis,'ro')
#plt.ylabel('Y')
#plt.show()

#plt.plot([2,4],[6,8],'bo')
#plt.ylabel('Y')
#plt.show()
