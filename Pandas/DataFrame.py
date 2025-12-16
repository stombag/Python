from pandas import DataFrame

data = {
    "종가" : [157000,51300,68800,140000],
    "PER" : [39.88, 8.52,10.03,228.38],
    "PBR" : [4.36,1.45,0.87,2.16]

}
index = ['NAVER', '삼성전자','LG전자','카카오']

df = DataFrame(data, index)
print(df)


index1 = ['비트코인','리플','이더리움']
Data = {

    "시가" : [980,200,300],
    "고가" : [990,300,500],
    "저가" : [920,180,300],
    "종가" : [930,180,400],
}
Df = DataFrame(Data,index1)
print(Df)


data1 = []
data1.append([980,990,920,930])
data1.append([200,320,120,180])
data1.append([280,990,300,400])
print(data1)
