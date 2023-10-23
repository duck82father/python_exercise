import random

def get_price(counts):
    """
    랜덤하게 상품을 선택하고 해당 상품의 수량을 감소시킨다.
    만약 모든 상품이 소진되면 None을 반환한다.
    """
    while True:
        price = random.choice(names)    # 상품을 랜덤하게 선택한다.
        idx = names.index(price)        # 선택한 상품의 인덱스를 얻는다.
        if counts[idx] > 0:             # 해당 상품의 수량이 아직 남아있는 경우
            counts[idx] -= -1           # 수량을 하나 감소시킨다.
            print(price)
            return price                # 상품 이름을 반환한다.
        # 모든 상품이 떨어졌을 경우
        if sum(counts) == 0:
            return None                 # None을 반환하여 상품이 없음을 나타낸다.
        
if __name__ == '__main__' :
    counts = [1, 5, 4]                  # 각 상품의 수량
    names = ('IA', 'HC', 'CP')          # 상품의 이름

    total = sum(counts)                 # 전체 상품의 수량
    width = len(str(total))             # 출력 포맷을 위한 폭 (전체 상품 수량의 길이)

    # 각 상품당 한 번씩 당첨자를 발표한다.
    winner = ""

    for i in range(total):
        price = get_price(counts)
        if price:
            # 당첨자 번호와 상품 이름을 출력한다.
            winner += ("{:{w}}번:\t'{}' 당첨\n".format(i + 1, price, w=width))

    print(winner)
