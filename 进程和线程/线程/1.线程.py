'''
在一个进程的内部，要同时干多件事儿，就需要同时运行多个’子任务‘，我们把进程内的这些子任务叫做线程

线程通常叫做轻型的进程，线程是共享空间的并发执行的多任务，每一个线程都共享要给进程的资源

线程是最小的执行单元，而进程由至少一个线程组成，如何调度进程和线程，完全由操作系统决定，程序员不能决定
什么时候执行，执行多长时间

模块：
__thread:低级模块

threading:高级模块，对_thread进行封装
'''
from _dummy_thread import start_new_thread