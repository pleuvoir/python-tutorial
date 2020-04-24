## 如何写出更 Pythonic 的代码



### 1. PEP8 代码风格

注意对齐

```python
def context(user,password
            timeout,command)
    pass
```

注意最后一个括号的位置

```python
user_list = [
    'user1',
    'user2',
    'user3',
    'user4'
]
```

定义变量

```python
x = 1
long_variable = 3
```

命名方式

```python

import my_module # 可以使用下划线的方式，都是小写的
import mymodule  # 当然也可以使用完整词语，都是小写的

MAX_TOTAL = 100 # 常量使用全大写加下划线的格式

class MyClass(Object):
	""" this is a demo class
	"""
	
	def __init__(self):
		pass
```

### 2. 在判断语句中使用True和False



基本类型的判断

```python
false_values = [
    False,
    0,
    0.0,
    None,
    '',
    [],
    {},
    ()
]

for value in false_values:
    """这两个输出的结果都是False"""
    print('{}是否为空{}'.format(value, bool(value)))
    print(True if value else False)  # 我们一般通过这种形式来判断是否为空
    print(True if bool(value) else False)  # 上面的其实就是这个意思
```

自定义对象如何返回bool值呢？

```python
class MyType(object):

    def __init__(self):
        self.values = []

    def add(self, x):
        self.values.append(x)

    def __bool__(self):
        print('__bool__ 被调用了')
        return bool(self.values)  # 由上述的推论我们得知，当列表为空时返回的是False


m = MyType()
print(bool(m))  # False  当调用 bool 时其实调用的就是__bool__方法
m.add(1)
print(bool(m))  # True

if bool(m) == True:  # 现在MyType不为为空时返回True，我们可以按照自己的逻辑进行代码编写了，优化下格式就是 if m
    print('m is not empty')

if m:
    print('m is not empty')
```

### 3. if 条件判断较多时的优化

```python
import random
import time
from enum import Enum


class Condition(Enum):
    A = 1
    B = 2
    C = 3
    D = 4


values = [1, 2, 3, 4]
condition = Condition(random.choice(values))

# 第一种写法

begin = time.time()
for index in range(1000000):
    if condition == Condition.A or condition == Condition.B or condition == Condition.C:
        pass
    else:
        pass
print('cost {}'.format(time.time() - begin))  # cost 0.42326903343200684

# 优化后
options = [Condition.A, Condition.B, Condition.C]
begin = time.time()
for index in range(1000000):
    if condition in options:
        pass
    else:
        pass
print('cost {}'.format(time.time() - begin))  # cost 0.1031181812286377
```
### 4. 使用列表解析

```python
numbers = list(range(1, 101))
# 将所有偶数放到新列表中
numbers_new = []
for number in numbers:
    if number % 2 == 0:
        numbers_new.append(number)
print(numbers_new)

# 使用列表解析，还可以对其进行格式化 [str(item) + '-00' for item in numbers if item % 2 == 0]
numbers_new = [item for item in numbers if item % 2 == 0]
print(numbers_new)
```

### 5. 使用字典解析

```python
numbers = list(range(1, 6))
dict = {}

# 普通循环
for number in numbers:
    dict[number] = str(number)
print(dict)  # {1: '1', 2: '2', 3: '3', 4: '4', 5: '5'}

# 字典解析 左边是key，右边是value，同样可以格式化
dict_new = {number: str(number) for number in numbers}
print(dict_new)  # {1: '1', 2: '2', 3: '3', 4: '4', 5: '5'}
```

### 6. 使用yield减少内存消耗

```python
def my_range(total):
    value = 0
    while value < total:
        yield value  # 你可以把它理解为return，但是return只会返回一次，它会返回很多次，并且可以供你遍历
        value += 1


i = my_range(100)
print(i)  # 返回的就是一个生成器 <generator object my_range at 0x118cedd60>
print(dir(i))  # 可以发现里面有__iter__方法

# 注意只能使用一次
for item in i:
    print(item)  # 0 
    break

for item in i:
    print(item)  # 1
    break
```

### 7. 小心默认参数的陷阱

```python
def default_args(x, time, target=[]):
    for item in range(time):
        target.append(x)
    return target


target = default_args('a', 3)
print(target)  # ['a', 'a', 'a']

target = default_args('b', 3)
print(target)  # ['a', 'a', 'a', 'b', 'b', 'b']  可以看出如果没指定列表的话，它就会使用上次使用的，这是非常危险的

target = default_args('c', 3, target=[])
print(target)  # ['c', 'c', 'c']

target = default_args('d', 3, target=[])
print(target)  # ['d', 'd', 'd']


# 总不能每次都传递 target=[] 吧

def default_args_better(x, time, target=None):
    if not target:
        target = []
    for item in range(time):
        target.append(x)
    return target


target = default_args_better('a', 3)
print(target)  # ['a', 'a', 'a']

target = default_args_better('b', 3)
print(target)  # ['b', 'b', 'b']
```

