import pandas as pd
new_df = pd.read_csv("jonq2.csv", low_memory=False)
old_df = pd.read_csv("histqq2.csv" ,low_memory=False)

 

#common_df = new_df[new_df==old_df]

common_df=pd.merge(old_df,new_df,on=['ResponseId'],how='inner')
print("old_df: ", old_df.shape[0])
print("common_df: ", common_df.shape[1])
common_df.to_csv("DEFECTQ2.csv")
print(old_df.columns.to_list())


'''
import pandas as pd
  
# Creating Data frames
df1 = {'A': [1, 2, 3, 4],
         'B': ['Geeks', 'For', 'efg', 'ghi']} 
df2 = {'A': [1, 2, 3, 4 ],
         'B': ['Geeks', 'For', 'abc', 'cde'],
         'C':['Nikhil', 'Rishabh', 'Rahul', 'Shubham']} 
           
d1 = pd.DataFrame(df1)
d2 = pd.DataFrame(df2) 
  
# Calling merge() function
int_df = pd.merge(d1, d2, how='inner', on=['A', 'B'])
print(int_df)
'''
