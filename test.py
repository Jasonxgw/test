def fizzBuzz(n):
    print(['Fizz' * (not i % 3) + 'Buzz' * (not i % 5) or str(i) for i in range(1, n + 1)])


'''
打印一个数字1到100，3的倍数打印"fizz"来替换这个数，5的倍数打印"buzz"，对于既是3的倍数又是5的倍数的数字打印"fizzbuzz"
'''
fizzBuzz(100)

if __name__ == '__main__':
    for i in range(100):
        print([(not i % 3) + (not i % 5) or str(i)])
print('*' * 50)

import heapq
from collections import Counter

'''
计数
'''
c = Counter('hello world')  # 变字典
print(c.most_common(2))  # 打印出现2次以上的字符
print('*' * 50)

import json

'''
漂亮的打印json

'''
data = {'a': 1, 'b': 2, 'c': 3}
print(json.dumps(data, indent=2))

print('*' * 50)
'''
比较
'''
x = 2
if 3 > x > 1:
    print(x)
if 2 <= x > 0:
    print(x)
print('*' * 50)

'''
字典取元素
'''
data = {'user': 1, 'name': 2, 'three': 3}
is_user = data.get('user', False)
print(is_user)

print('*' * 50)

'''
迭代工具
所有的排列组合
'''

from itertools import combinations

teams = ['Page', '24dsa', 'ravens', 'patriots']
for game in combinations(teams, 2):
    print(game)
print('*' * 50)

'''
三层嵌套列表展开
'''
from tkinter import _flatten

s = [1, [2, [3, 4, [5]]]]
print(_flatten(s))

# 方法二
res = []


def fun(s):
    for i in s:
        if isinstance(i, list):
            fun(i)
            # res.extend(fun(i)) 或者是这个
        else:
            res.append(i)


fun(s)
print(res)

print('*' * 50)
'''
两层嵌套列表展开
'''
list_of_list = [[1, 2, 3], [4, 5, 6], [7, 8], [9]]
print([y for x in list_of_list for y in x])

print('*' * 50)

'''
排序
'''

import heapq

nums = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print(heapq.nlargest(3, nums))  # 最大排
print(heapq.nsmallest(3, nums))  # 最小排
students = [{'name': 1, 'score': 100, 'height': 180},
            {'name': 2, 'score': 90, 'height': 181},
            {'name': 3, 'score': 80, 'height': 182}]
print(heapq.nsmallest(2, students, key=lambda x: x['height']))

print('*' * 50)
'''

查询


'''
import re

list1 = ['user', 'name', 'value', 'to_pickle', 'to_sql', 'update', 'aa']
for i in filter(lambda x: x.startswith('update'), list1):
    print(i)
for j in filter(lambda x: re.findall(r'to_', x), list1):
    print(j)
list2 = [{'aa': 100}, {'bb': 101, 'cc': 102}]
for k in filter(lambda x: 'aa' in x.keys(), list2):
    print(k)

print('*' * 50)
'''
添加字典的方法
'''
option = {'code': 'utf-8'}
base_headers = {'user-Agent': 100,
                'accept-encoding': 'gzip,deflate,sdch', }
base_headers = dict(base_headers, **option)  # 新建了一个
print(base_headers)

# 方法二
base_headers.update(option)
print(base_headers)
