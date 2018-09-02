import sys
from multiprocessing import Queue, Process

def foo(filename: str, queue: Queue):
    with open(filename) as f:
        text = f.read()

    ct = 0
    for ch in text:
        n = ord(ch.upper()) + 1
        if n == 67:
            ct += 1
    queue.put(ct)

if __name__ == '__main__':
    queue: Queue = Queue()
    ps = [Process(target = foo, args = (filename, queue))
              for filename in sys.argv[1:]]
    for p in ps:
        p.start()
    for p in ps:
        p.join()

    count = 0
    while not queue.empty():
        count += queue.get()
    print(count)







