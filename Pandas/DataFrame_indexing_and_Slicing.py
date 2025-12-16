from pandas import DataFrame
index1 = ['비트코인','리플','이더리움']
Data = {

    "시가" : [980,200,300],
    "고가" : [990,300,500],
    "저가" : [920,180,300],
    "종가" : [930,180,400],
}
Df = DataFrame(Data,index1)
print(Df)

print(Df[['시가']])

print(Df.iloc[1,2])
print(Df.iloc[0:2])
print(Df.loc["비트코인":"이더리움"])