
import numpy as np
import matplotlib.pyplot as plt

data_file_name=input("Enter the name of your data file:")
file_Object=open(data_file_name,"r")

first_line=file_Object.readline()
first_line_array=first_line.split()
row=int(first_line_array[0])

def axis_label(a):
    if a==0:
        return("Sepal length")
    elif a==1:
        return("Sepal width")
    elif a==2:
        return("Petal length")
    elif a==3:
        return("Petal width")
    
coordinates=np.zeros([row,5])
for i in range (row):
    coordinates_string=file_Object.readline()
    data=coordinates_string.split("\t")
    for j in range(4):
        coordinates[i,j]=float(data[j])
    if data[4]=="Setosa\n":
      coordinates[i,4]=0
    elif data[4]=="Versicolor\n":
      coordinates[i,4]=1
    else:
      coordinates[i,4]=2
    
while True:
  print('''You can do a plot of any two features of the Iris Data set
  The feature codes are:
  0 = sepal length
  1 = sepal width
  2 = petal length
  3 = petal width''')

  horizontal_axis=int(input("Enter feature code for the horizontal axis: "))
  vertical_axis=int(input("Enter feature code for the vertical axis: "))
  flag1,flag2,flag3=1,1,1
  for k in range(row):
      if coordinates[k,4]==0:
        if flag1==1:
          plt.plot(coordinates[k,horizontal_axis],coordinates[k,vertical_axis],color='orange',marker='o',label='Setosa')
          flag1=0
        plt.plot(coordinates[k,horizontal_axis],coordinates[k,vertical_axis],color='orange',marker='o')
      elif coordinates[k,4]==1:
          if flag2==1:
            plt.plot(coordinates[k,horizontal_axis],coordinates[k,vertical_axis],c='blue',marker='x',label='Versicolor')
            flag2=0
          plt.plot(coordinates[k,horizontal_axis],coordinates[k,vertical_axis],c='blue',marker='x')
      elif coordinates[k,4]==2:
          if flag3==1:
            plt.plot(coordinates[k,horizontal_axis],coordinates[k,vertical_axis],c='yellow',marker='s',label='Virginica')
            flag3=0
          plt.plot(coordinates[k,horizontal_axis],coordinates[k,vertical_axis],c='yellow',marker='s')

  plt.legend()
  plt.xlabel(axis_label(horizontal_axis))
  plt.ylabel(axis_label(vertical_axis))
  plt.title('Iris flower plot')

  plt.show()
  option=(input("Do you want another plot(Y/N):"))
  if option=="N" or option=='n':
    break


