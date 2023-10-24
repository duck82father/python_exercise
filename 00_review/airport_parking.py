# airport_parking.py

data = """
공항별,계류장면적(m2),동시주기능력(대),주차장면적(m2),동시주차능력(대)
김포,1215487,"144(일반85,소형59)",351089,10646
김해,404251,"43(일반40,소형3)",181226,6739
제주,449393,"42(일반40,소형2)",142184,3578
청주,120390,"21(일반13,소형8)",164404,5267
대구,51182,"11(일반11,소형0)",21981,1579
무안,113094,"50(일반6,소형44)",94890,3009
양양,72385,"24(일반7,소형17)",14734,534
광주,44300,"5(일반5,소형0)",38300,1191
울산,33480,"6(일반4,소형2)",26530,554
여수,41868,"5(일반5,소형0)",30867,884
포항경주,32617,"5(일반5,소형0)",17327,452
사천,13140,"2(일반2,소형0)",9893,309
군산,13758,"2(일반2,소형0)",15888,519
원주,6590,"1(일반1,소형0)",4412,178
"""

print(data)

data_row = data.strip().split('\n')
row = data_row[1].split(',')

p_area = row[0]
p_value = int(row[-1])

print("{}의 주차가능대수는 {}".format(p_area, p_value))