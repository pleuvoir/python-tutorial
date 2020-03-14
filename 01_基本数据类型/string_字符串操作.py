#!/usr/bin/env python3
# -*- coding: utf-8 -*-


# 转义字符
print("hello\npleuvoir\ngood")

print('1\t2\t3\t4\t')  # \t就是tab
print(r'c:\a.txt')
print('c:\\a.txt')

"""会换行"""
print("""i am 
    you 
    d""")

print("""i am your's "" a """)  # i am your's "" a

"""不会换行"""
print("i am "
      "you d")

# 切片操作

text = 'abcdefg'

"""按照索引取值"""
print(text[0])  # a
print(text[1])  # b

"""当然也可以按照倒序来获取"""
print(text[-7])  # a
print(text[-6])  # b

print(text[:])  # 截取全部字符串 abcdefg

"""左包右不包"""
print(text[0:1])  # 第一位不包含右边 a
print(text[:6])  # 从最左边到第六位之前 abcdef
print(text[0:])  # 从开始到最后一位 相当与 text[0:7]  abcdefg

print(text[-1:])  # g  从最后一位到结尾
print(text[-2:])  # fg  从倒数第二位到结尾
print(text[-3:-1])  # ef 从倒数第三位到倒数第一位
print(text[-3:6])  # ef  最好别这么用
print(text[-3:])  # efg 从倒数第三位到最右边包含最后一位

# 高级一点的用法

"""其实可以使用步长 这两个是一样的，最后一位是步长"""
print(text[::1])  # 全部 abcdefg
print(text[::])  # 全部 abcdefg
print(text[0:1:1])  # 从最左到第一位前，即第一位 a
print(text[0:1])  # 不写步长则为1 从最左到第一位前，即第一位 a

"""反向步长"""
print(text[3:0:-1])  # dcb  最后一位到第一位，步长为-1 从右到左 !!!但是记住后面的不包，所以结果为dcb

# 需要设置到最左，也不能设置为-1，-1代表的是最后一位，那么就不设置，python会自己根据步长 得到末位是最左端还是最右端
print(text[3::-1])  # dcba  从索引为3的位置从右向左全都有

"""翻转字符串"""
print(text[::-1])  # gfedcba

# join操作

"""list元素用！连接起来成为一个新的字符串"""
join = "!".join(['1', '2', '3'])
print(join)  # 1!2!3
print(''.join(['4', '5', '3']))  # 453

# split 切分

"""将上面的字符串按照！切分，会变成一个list"""
join_split = join.split('!')
print(join_split)  # ['1', '2', '3']

# 格式化字符串的几种方式
print('i come from {}, and my age is {}'.format('china', 18))  # 这种的就像输入日志一样
print('i come from {1}, and my age is {0}'.format(18, 'china'))  # 可以绑定位置，注意，一定要从0开始，后面的实际值索引和括号内对应
print('i come from {0:>10}, and my age is {1:<50}'.format('china', 18))  # 这个可以调整位置，请自己尝试

for i in range(1, 3):
    print("{0}的平方={1}，{0}的立方={2}".format(i, i ** 2, i ** 3))

# 文本  a，文本b
string1 = "hello "
string2 = "world! "
string3 = "pleuvoir"
string4 = ''

print(string1 + string2)
print(len(string1 + string2))  # 13
print("hello " "world! ")
print(len("hello " "world! "))  # 13
print('是空吗？', string4 == ' ')  # False
print('是空吗？', string4 == '')  # True
print(string1.replace('h', 'a'))

print("he" in string1)  # True
print(" " in string1)  # True
print("" in string3)  # 永远是True
print(string1 * 5)  # 打印5次

# 一些常用的函数
game = "ABc_Def呵呵ß"  # 最后一个是德语
print(game.capitalize())  # Abc_def呵呵ß
print(game.upper())  # ABC_DEF呵呵SS
print(game.lower())  # 不能正确转换德语为小写，所以用下面的就妥了
print(game.casefold())  # 最后一个是德语 小写为ss
# 把前面或者结尾的干掉，注意：部分也可以不一定是连续的才起作用
text = 'abcdEFa'
print(text.strip('ac'))  # bcdEF
print(text.strip('fab'))  # cdEF
print(text.split())  # ['abcdEFa']  注意这里是什么也不传，传 ''的话什么也不返回
