import numpy as np
import matplotlib.pyplot as plt


data_file_name=input("Enter the name of your data file:")
file_Object=open('C:/Users/pooja/.spyder-py3/'+data_file_name,"r")

first_line=file_Object.readline()
first_line_array=first_line.split()
max_rows=int(first_line_array[0])
no_of_elements=int(first_line_array[1])

array1=np.zeros[max_rows,(no_of_elements+1)]
for i in range (max_rows):
    coordinates_string=file_Object.readline()
    data=coordinates_string.split("\t")
    for j in range(no_of_elements):
        array1[i,j]=float(data[j])
    array1[i,no_of_elements]=data[no_of_elements]


    
#print(feature_array)

print('''You can do a plot of any two features of the Iris Data set
The feature codes are:
0 = sepal length
1 = sepal width
2 = petal length
3 = petal width''')

horizontal_axis=int(input("Enter feature code for the horizontal axis: "))
vertical_axis=int(input("Enter feature code for the vertical axis: "))

for k in range (max_rows):
    if array1[k,no_of_elements]=='Setosa':
        plt.scatter(array1[horizontal_axis,vertical_axis],c='orange',marker='o')
    elif array1[k,no_of_elements]=='Versicolor':
        plt.scatter(array1[horizontal_axis,vertical_axis],c='blue',marker='x')
    elif array1[k,no_of_elements]=='Virginica':
        plt.scatter(array1[horizontal_axis,vertical_axis],c='yellow',marker='s')
#plt.ylabel('Y')
plt.show()

#plt.plot([2,4],[6,8],'bo')
#plt.ylabel('Y')
#plt.show()
