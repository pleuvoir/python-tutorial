#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from multiprocessing import Process
from multiprocessing import Pool
import os, time, random
import subprocess


# # 1.不跨平台
# """
# fork出一个自进程，此函数window不支持
# 注意：fork()会返回两次 0代表的是子进程的返回，非0的是父进程返回的代表子进程的PID
# """
# pid = os.fork()
#
# if pid == 0:  # 子进程返回
#     print('我是子进程PID={}的返回，父进程的PID是={}'.format(os.getpid(), os.getppid()))
# else:  # 父进程返回
#     print('我是父进程PID={}的返回，子进程的PID={}'.format(os.getpid(), pid))


# 2.跨平台

def sub_proc(name):
    start = time.time()
    time.sleep(random.random() * 3)
    print('cost {} ms，子进程代码执行了，{}'.format((time.time() - start),name))
#
#
# if __name__ == '__main__':
#     p = Process(target=sub_proc, args=('test',))  # 注意这个,很关键，没有就报错了
#     print('子进程即将启动.')
#     p.start()
#     p.join()
#     print('子进程结束了.')


# 2.1 如果一次性要创建很多个子进程可以使用进程池
# if __name__ == '__main__':
#     p = Pool(5)
#     for item in range(5):
#         p.apply_async(func=sub_proc,args=('test',))
#
#     p.close()
#     p.join()  # 会等待所有子进程执行完毕，调用join之前必须调用close

# 3.子进程的通信，如何接收输入输出参数
if __name__ == '__main__':
    # 这个就和在命令行执行 nslookup www.python.org 没有区别
    # print('$ nslookup www.python.org')
    # r = subprocess.call(['nslookup', 'www.python.org'])
    # print('Exit code:', r)

    # 持续输入模式
    # print('$ nslookup')
    # p = subprocess.Popen(['nslookup'], stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    # output, err = p.communicate(b'set q=mx\npython.org\nexit\n')
    # print(output.decode('utf-8'))
    # print('Exit code:', p.returncode)

    # 或者这样
    p = subprocess.Popen(['nslookup'], stdin=subprocess.PIPE, stdout=subprocess.PIPE
                         , stderr=subprocess.PIPE,encoding='UTF-8')

    cmds = ['set q=mx\n','python.org\n','exit\n']
    p.stdin.writelines(cmds)  #  也可以 p.stdin.write 这样输入
    output, err = p.communicate()
    print(output)
    print('Exit code:', p.returncode)