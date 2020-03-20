import threading
import asyncio

# 请注意，async和await是针对coroutine的新语法，要使用新的语法，只需要做两步简单的替换：
# 
# 把@asyncio.coroutine替换为async；
# 把yield from替换为await。

# @asyncio.coroutine
# def hello():
async def hello():
    print('Hello world! (%s)' % threading.current_thread())
    # yield from asyncio.sleep(1)
    await asyncio.sleep(1)
    print('Hello again! (%s)' % threading.current_thread())

loop = asyncio.get_event_loop()
tasks = [hello(), hello()]
loop.run_until_complete(asyncio.wait(tasks))
loop.close()