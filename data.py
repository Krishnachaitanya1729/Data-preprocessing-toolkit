#EDITING DATA
#now let's change the column names:
print(data_frame_1.columns) #prints an array or list of column names.
old_col_names=data_frame_1.columns #let old col names be prev col names.
new_col_names=['ID', 'City_name', 'State_name', 'Country_name', 'Name', 'Employees']#define new col names as a list.
data_frame_1.columns=new_col_names #replace the old by using the command 
print(data_frame_1)#data frame with new col names
data_frame_1.columns=old_col_names#for getting back our old dataframe 
print(data_frame_1)#back to old data frame 
#print(data_frame['col_name']) allows you to print that particular column.
print(data_frame_1['Name'])# you get all the names of the dataframe.
#inoreder to transpose a matrice or dataframe we need to use .T command.
print(data_frame_1.T)# we can see transposed dataframe
#to add a new column it is very easy 
#dataframe["new_column_name"]=new values list,here new values list length should match length of the other columns.
data_frame_1['city_duplicate']=data_frame_1["City"]
print(data_frame_1)#here simply we got new column named city_duplicate.
data_frame_1["new_column"]=[1,2,3,4,5,6]#we get a new col named new_column with values corresponding values.
#data_frame_1["new_column"]=[1,2,3,4,5]---> will generate an error because length =5 which is not equal.
print(data_frame_1)
#if you want to add a row then we need to transpose the dataframe and insert a new column.
data_frame_1=data_frame_1.T
print(data_frame_1)
#new row adding:
#refer to the colnames of dataframe and add accordingly as shown below:
data_frame_1["new adress"]=[7,"new_city","new_state","new_country","new_name",0,"new_city_dup",7]
print(data_frame_1)#modified dataframe---> now transpose this one back.
data_frame_1=data_frame_1.T
print(data_frame_1)#succesfully we have add a row.
#deleting rows and columns in a dataframe 
data_frame_1=data_frame_1.drop(['new adress'],axis=0)#deletes [new address] row from the data frame.
data_frame_1=data_frame_1.drop( ['new_column'],axis=1)#deletes [new_column] column from the data frame.
data_frame_1=data_frame_1.drop(['city_duplicate'],axis=1)#deletes [city_duplicate] column from the data frame.
print(data_frame_1)# we restored our original data frame back again.
#use dataframe.values command to get values in the form of n dimensional array 
df_values=data_frame_1.values
print(df_values)
# We have to remember this point..ie..for manipulation of data or calling data from data frame "INDEX" plays the whole role.
# If we have to update cetain info in a row we need to call that row by using index.
# Enter a list of new values in place of old values by replacing them and lengths should match.
# Now if we have to delete duplicates we need to use data_frame.drop_duplicates()
# Add 3 same rows to our data_frame by performing the following operation
data_frame_1=data_frame_1.T
data_frame_1["new adress_1"]=[7,"new_city","new_state","new_country","new_name",0]
data_frame_1["new adress_2"]=[7,"new_city","new_state","new_country","new_name",0]
data_frame_1["new adress_3"]=[7,"new_city","new_state","new_country","new_name",0]
# if data_frame_1["new adress_3"]=[7,"new_city","new_state","new_country","new_name",1] then it is not a duplicate row to "new adress_1".
data_frame_1=data_frame_1.T
print(data_frame_1)#we created a dataframe with 1 original and 2 duplicate rows (different index values doesn't imply different rows).
print(data_frame_1.drop_duplicates())#deletes the 2 duplicate rows and returns a dataframe without duplicates.
print(data_frame_1.index)#to get all the index elements,and remember this print(dataframe["index_name"]) will generate an error
#now let us see how to split data from a column into 2  different new columns.
# first we will see how to create a dataframe :
data_frame_create = pd.DataFrame({'Name': ['Oliver Queen', 'Robert Junior', 'Jonny Depp'],'Age':[32, 34, 36]})
print(data_frame_create) #we have created a data frame successfully now it's time to split.
#lets split name to first_name and last_name
#in order to split we need to use data_frame_name.column_name.str.split(expand=True)
#example:
name="krishna chaitanya"
print(name.split(" "))#prints ['krishna', 'chaitanya'] ...similiarly u have to apply this for your data frame columns as shown below
[data_frame_create["f_nname"],data_frame_create["l_name"]]= [data_frame_create.Name.str.split(expand=True)[0],data_frame_create.Name.str.split(expand=True)[1]]
print(data_frame_create)#new dataframe with Name,age,f_name,l_name is created.
#lets do some little modifications to the data frame:
print(data_frame_create.columns)#u can get the columns order I have named it as old_col_order as shown below
old_col_order=['Name', 'Age', 'f_nname', 'l_name']
new_col_order=['Name','f_nname', 'l_name', 'Age']#neworder of cols
data_frame_create=data_frame_create[new_col_order]
print(data_frame_create)#u can get modified data frame now.
#if u feel like deleting the col Name as we have f_name and last_name we can simply do it in 2 simple ways that I know.
new_col_order=['f_nname', 'l_name', 'Age']
data_frame_create=data_frame_create[new_col_order]
print(data_frame_create)#we get dataframe with f_name,l_name,age....or u can use drop column to delete a column.
# by using this command --->data_frame_create= data_frame_create.drop(['Name'],axis=1)
#we will see how to form a new column by using 2 or more columns of same table.
family_data_frame =pd.DataFrame({"family_id":[1,2,3,4,5,6],"adults":[2,2,3,2,3,1],"kids":[0,1,2,3,3,4],"old_ppl": [2,0,2,2,0,1]}) 
print(family_data_frame)#prints our newly created dataframe
family_data_frame['pets']=[1,0,1,0,2,0]
print(family_data_frame)# adds a col pets
family_data_frame["total"]=family_data_frame["adults"]+family_data_frame["kids"]+family_data_frame["old_ppl"]+family_data_frame["pets"]
print(family_data_frame)#prints dataframe with a new column named total which is sum of all the other 4.
family_data_frame=family_data_frame.set_index('family_id')
print(family_data_frame)#index has been set to family_id
#lets learn how to how to break time into hours day date etc; 
# "2018-10-26 17:30:00+00:00" let this be the date we are working.
print(pd.to_datetime("2018-10-26 17:30:00+00:00").date()," is date")
print(pd.to_datetime("2018-10-26 17:30:00+00:00").time()," is time")
print(pd.to_datetime("2018-10-26 17:30:00+00:00").hour, "is hour")
print(pd.to_datetime("2018-10-26 17:30:00+00:00").minute, " minutes")
print(pd.to_datetime("2018-10-26 17:30:10+00:00").second," seconds")
print(pd.to_datetime("2018-10-26 17:30:00+00:00").day," is day")
print(pd.to_datetime("2018-10-26 17:30:00+00:00").year," is year")
print(pd.to_datetime("2018-10-26 17:30:00+00:00").month," is month")
#now let's see how to generate dummies...we can easily understand by an example as shown below:
#we can simply use pd.get_dummies()function ...
#create a new dataframe as shown..
df1=pd.DataFrame({"country":["india","usa","japan"],"population":["high","moderate","low"]})
print(df1)
df2=pd.get_dummies(df1["country"])#we can see how dummies are generated only for country column.
print(df2)#dummy matrix
frames=[df2,df1]#inorder to concat them horizontally we need to follow this way.
df_f=(pd.concat(frames,axis=1))#(axis=1 for horizontal concatenation)..
print(df_f)#prints concatenated matrix..
df_f.drop(['country'],axis=1,inplace=True)#this is useful method in machine learning and in many other things 
print(df_f)
