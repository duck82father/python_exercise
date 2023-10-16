#
nums = ["a","b","c"]
nums_lst = [[1,2,3,],[4,5,6],[7,8,9]]

nums_lst.append(10)
nums_lst[1].append(nums)

print(nums_lst)

# nums_lst는 nums의 주소값이 연결되기에 nums 값이 변경되면 
# nums_lst에 연결된 주소의 값도 함께 변경된다.
nums.append("d")

print(nums_lst)