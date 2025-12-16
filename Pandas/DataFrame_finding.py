import pandas as pd

data = [
    ['3R', 1520,9.10],
    ['3SOFT',1790,1.65],
    ['ACTS',1185,1.28]
]

index = ['037720','036360','005760']
columns = ['종목명', '현재가','등락률']

df = pd.DataFrame(data=data,index=index,columns=columns)
print(df)
print(df.iloc[0:1])
print(df.iloc[0,2])
print(df.loc["037720","등락률"])