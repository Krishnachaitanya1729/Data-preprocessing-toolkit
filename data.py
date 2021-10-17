# data pre processing :
# basics:
#1.How to read data : By using pandas we can read excel,csv,json etc type of data in python.
import pandas as pd
from pandas.core.frame import DataFrame #(import pandas library)
#name a data frame and read data from files(csv,json etc)
data_frame_1=pd.read_csv("C:\\Users\\Dell\\Downloads\\supermarkets.csv")#path of the file and  add \\ in place of \.
print(data_frame_1)# to print the data frame that u have read earlier .
#to get size shape and dimension of matrix we need to use following commands:
print("size= ",data_frame_1.size,"shape=" ,data_frame_1.shape,"n_dimensions=",data_frame_1.ndim," ie.." ,data_frame_1.ndim,"d matrix.")
#if dataset is huge we cannot see the whole dataset.In that case you have to use the following commands.
pd.options.display.max_rows=None #displays all the rows.
pd.options.display.max_columns=None #displays all the columns.
print(data_frame_1.head()) # by using dataframe.head(n),n=integer we can get top n rows (n=5,default value)
print(data_frame_1.tail()) # by using dataframe.tail(n),n=integer we can get bottom n rows (n=5, default value)
#setting index in data frame
data_frame_1.set_index('Address',inplace=True)#inplace = True makes the change permanent otherwise it would be a temporary change.
#in place of address u can use any column name.  
print(data_frame_1)# u can see the changes now.
#Using loc and iloc commands:
# loc command:
print(data_frame_1.loc["3995 23rd St"])#loc is based on label name and it gives row details of particuar index.
print(data_frame_1.loc["3995 23rd St","Employees"])#here it gives details only about employees of 3995 23rd St because we have asked only employees.
#iloc command:
print(data_frame_1.iloc[:])# prints complete dataframe 
print(data_frame_1.iloc[0:4,1:3])#here [x:y,a:b]  x:y is for row x :row y and a:b is for column a: column b.
#by default pd.read_csv assumes first row  as header. so if u declare header=None then first row is not considered as header.
data_frame_2=pd.read_csv("C:\\Users\\Dell\\Downloads\\supermarkets.csv",header=None)
print(data_frame_2)
