import cal_sum
import cal_sub
import cal_mul
import cal_div

if __name__ == '__main__':
    num1 = int(input("첫번째 숫자: "))
    num2 = int(input("두번째 숫자: "))
    a = cal_sum.isthis(num1, num2)
    b = cal_sub.isthis(num2, num1)
    c = cal_mul.isthis(num2, num2)
    d = cal_div.isthis(num2, num1)
    print("a = {}, b = {}, c = {}, d = {}".format(a,b,c,d))

