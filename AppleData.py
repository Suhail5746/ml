import pandas as pd
import numpy as np 
path="apple_quality.csv"
df=pd.read_csv(path)
# print("DataFrame :")
# print(df.head())
# print(df.tail())

# print(df.info())
# print(df.shape)
# print(df.describe())
# print(df.describe(include="all"))

                   #dataframe copy and view 
# print(df[df['Sweetness']>6])
# df[df['Sweetness']>6]['Sweetness']

# df.loc[df['Sweetness']>6,'Sweetness']=5
# print(df[df['Sweetness']>6])

# df2=df[df['Sweetness']>6].copy()

               #rename column
# df.rename(columns={'Weight':'W'},inplace=True)
# df=df.rename(columns={'Sweetness':'S'})
# print(df.head())

 
      #changing index
# df=df.set_index("A_id")
# df.index.name="New_index"
# df=df.reset_index()
# print(df.head())

       #adding and delrting columns
# df['Color']='Red'
# df=df.drop(['Color'])
# df.drop(['SweetNess'],inplace=True)


# row_1=pd.DataFrame([['4002','43','2','Sweet','Crunchy','Juicy','1','2','3']],columns=df.columns,index=[4002])
# df=df.append(row_1)
# print(df.tail())

       #concate two dataframe

df11=pd.DataFrame({'A':[1,2,3],'B':[5,6,7]})
df22=pd.DataFrame({'A':[6,9,0],'B':[0,3,6]})

print(pd.concat([df11,df22],ignore_index=True))  #by default axis=0 i.e row-wise concat

print(pd.concat([df11,df22],axis=1,ignore_index=True))