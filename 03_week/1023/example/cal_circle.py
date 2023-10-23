import cal_sum, cal_sub, cal_mul, cal_div

def like(len_txt, nums, cal, solv):
    if len_txt <= 3:
        for j in range(len_txt-2):
            solv = cal[j](nums[j],nums[j+1])
    else:
        like(len_txt-2, nums, cal, solv)
    return solv

if __name__ == "__main__":

    len_txt = 5
    nums = [1,2,3]
    cal = [cal_sum.like]
    solv = 0

    print(like(len_txt, nums, cal, solv))
    