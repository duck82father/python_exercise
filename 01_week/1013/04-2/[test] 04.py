# 딕셔너리를 선언합니다.
charactor = {
    "name":"기사",
    "lever":12,
    "item":{
        "sword":"불꽃의 검",
        "armor":"풀플레이트"
    },
    "skill":["베기","세게 베기","아주 세게 베기"]
}

print(charactor["item"]["sword"])

# for 반복문을 사용합니다.
for key in charactor:
    
    # dict
    if type(charactor[key]) is dict:   
        
        for item in charactor[key]:
            print(item, ":", charactor[key][item])
    
    # list
    elif type(charactor[key]) is list:
        
        for skill in charactor[key]:
            print(key, ":", skill)
    
    # str, int
    else:
        print(key, ":", charactor[key])
        