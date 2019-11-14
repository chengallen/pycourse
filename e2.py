#!/usr/bin/env python

# bool, 整数(复数), 字符串, 元组与列表(数组), 集合，字典
# 函数

byte, int , str, tuple, list, set, dict


布尔类型真值 = True
整数类型1 = -1
浮点类型 = 1.0
字符串类型软研院 = '软研院'
元组类型 = 1, 2

元组类型[0]

列表类型 = [1, 2]
集合类型 = {1, 2}
字典类型 = {1: 'a', 'b': '软研院'}

字典类型['b']

# 函数定义 与 函数调用 

def 函数名(*args, **kwargs):
	return '函数返回值'

# 函数调用
函数名()

# 字符串, 字符集 Unicode ， UTF8
# 字节串/字节数组

字符串 = '字符串'

字节串 = 字符串.encode('utf8')

print(type(字节串))


天气 = '下雨'

if 天气 == '下雨':
	print('带伞')
elif 天气 == '下雪':
	print('多穿衣服')
else:
	print('不用带伞')

while now_time < 下班时间:
	work()
	update(now_time)


# iterable()
for 数组元素 in 数组:
	print(数组元素)

a, b = 元组

for 键 in 字典.items():
	print(键[0], 键[1])

	print('abc')

	continue

	print('hello')


class MyError(ValueError):
	pass

def 函数():
	raise EOFError('文件已读取结束')

try:
	函数()
	函数2()
except EOFError as e:
	print() # logging.
	raise
else:
	pass
finally:
	pass


print('a', 'b', 'c')

str(a)

print(f'a {a}')

print(f'1*1 = {1*1}') # end='\n' 

a = list(range(10))

for i in range(1, 10):
	print(i)