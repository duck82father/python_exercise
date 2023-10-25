# [ 변수, 자료형, 반복문, 함수 ]

# 문제: 주어진 리스트(임의 입력값을 입력)의 모든 요소의 평균을 반환하는 함수 average를 작성하세요.

def average(lst):
    return sum(lst) / len(lst)

# ---------------------------------------------------------------------------------

# 문제: 문자열을 입력받아, 그 문자열의 모든 모음을 대문자로 변환하는 함수 capitalize_vowels를 작성하세요.
# * if * else * for * in * = [ 조건 만족 시 출력값 if 조건 else 조건 불만족 시 출력 값 for i in data] 

def capitalize_vowels(s):
    return ''.join([char.upper() if char in 'aeiou' else char for char in s])

# ---------------------------------------------------------------------------------

# 문제: 주어진 정수 n에 대해, n이 소수인지 아닌지를 판별하는 함수 is_prime를 작성하세요.
# 어떤 자연수 n이 소수임을 판정하기 위해선 'n**0.5' 까지의 수 중 1을 제외하고 그 자연수의 약수가 있는지 확인하면 된다.
def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5)+1):
        if n % i == 0:
            return False
    return True

# n=23244
# print("{}은 소수가 {}".format(n,"맞다" if is_prime(n)==True else "아니다"))

# ---------------------------------------------------------------------------------

# 문제: 주어진 리스트에서 최댓값과 최솟값을 제외한 나머지 요소의 합을 반환하는 함수 sum_without_extremes를 작성하세요.

def sum_without_extremes(lst):
    return sum(lst) - max(lst) - min(lst)

# ---------------------------------------------------------------------------------

# 문제: 피보나치 수열의 n번째 값을 반환하는 함수 fibonacci를 작성하세요.

def fibonacci(n):
    a, b = 0, 1
    for _ in range(n):
        a, b = b, a+b
    return a

# ---------------------------------------------------------------------------------

# 문제: 주어진 문자열에서 각 문자의 빈도수를 딕셔너리 형태로 반환하는 함수 char_frequency를 작성하세요.

def char_frequency_1(s):
    lst={}
    for i in range(len(s)):
        lst[s[i]] = 0
    for i in range(len(s)):
        lst[s[i]] += 1
    return lst

# s="abc123abc456"
# print(char_frequency_1(s))

def char_frequency_2(s):
    counter = {}
    for char in s:
        if char in counter:  # 딕셔너리에 key 값이 없을 경우 key 값을 1로 넣어서 생성
            counter[char] = counter[char] + 1            
        else:
            counter[char] = 1
    return counter

# print(char_frequency_2(s))

# answer
def char_frequency(s):
    freq = {}
    for char in s:
        freq[char] = freq.get(char, 0) + 1
    return freq

# s="abc123abc456"
# print(char_frequency(s))

# ---------------------------------------------------------------------------------

# 문제: 주어진 리스트를 입력받아, 리스트의 모든 연속된 부분 리스트(sublist)를 반환하는 함수 all_sublists를 작성하세요.

def all_sublists(lst):
    return [lst[i:j] for i in range(len(lst)) for j in range(i+1, len(lst)+1)]

def all_sublists_bad(lst):
    new_lst=[]
    for i in range(len(lst)):
        for j in range(i+1, len(lst)+1):
            new_lst.append(lst[i:j])
            print(new_lst)
    return new_lst

# print(all_sublists(lst = [1, 2, 3, 4]))
# print(all_sublists_bad(lst = [1, 2, 3, 4]))

# def all_sublists(lst):
#     return [for i in range(len(lst)) for j in range(j+1, len(lst)) ]


# 문제: 두 리스트를 입력받아, 두 리스트의 공통된 요소만을 가진 새로운 리스트를 반환하는 함수 common_elements를 작성하세요.

def common_elements(lst1, lst2):
    return [x for x in lst1 if x in lst2]


# 문제: 주어진 숫자의 팩토리얼을 반복문을 사용하여 계산하는 함수 factorial_iterative를 작성하세요.

def factorial_iterative(n):
    result = 1
    for i in range(1, n+1):
        result *= i
    return result

# 문제: 주어진 문자열이 회문(palindrome)인지 아닌지를 판별하는 함수 is_palindrome를 작성하세요.
# 회문(palindrome)이란 앞에서 읽었을 때와 뒤에서 읽었을 때 동일한 문자열, 숫자, 문장 등을 의미합니다. 예를 들어, "radar", "level", "121" 및 "A man, a plan, a canal, Panama!"는 모두 회문입니다. 

def is_palindrome(s):
    return s == s[::-1]

# def palindrome(n):
#     for i in range(len(n)//2+1):
#         if n[0+i]!=n[-1-i]:
#             return False
#     return True

def palindrome(n):
    return list(n) == list(reversed(n))     # reverse() x, reversed() o

# def palindrome(n):
#     return list(n) == list(n).reverse()   ( X )

sss = 'abcde'
ss = 'abcdcba'
print(palindrome(ss))
