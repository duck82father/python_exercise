import cal_sum
import cal_sub
import cal_mul
import cal_div

if __name__ == '__main__':
    a = cal_sum.isthis(1, 2)
    b = cal_sub.isthis(2, 1)
    c = cal_mul.isthis(2, 2)
    d = cal_div.isthis(2, 1)
    print("a = {}, b = {}, c = {}, d = {}".format(a,b,c,d))

