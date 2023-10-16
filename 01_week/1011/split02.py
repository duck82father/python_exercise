# 청주,120390,"21(일반13,소형8)",164404,5267

addr = "청주,120390,\"21(일반13,소형8)\",164404,5267"
print(addr)

# 청주
print(addr[0:2])
# 21
print(addr[11:13])

txt = "{}, {}".format(addr[:2],addr[11:13])
print(txt)

lst = addr.split(",")
print(lst)
print(lst[0])
print(lst[2])
print(lst[2][1:3])
txt2 = "{}, {}".format(lst[0],lst[2][1:3])
print(txt2)