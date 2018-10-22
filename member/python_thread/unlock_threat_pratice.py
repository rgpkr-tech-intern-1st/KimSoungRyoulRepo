from threading import Thread, Lock


class Counter(object):
    def __init__(self):
        self.count = 0

    def increment(self, offset):
        self.count += offset


def worker(sensor_index, how_many, counter):
    for _ in range(how_many):
        counter.increment(1)


class LockingCounter(object):

    def __init__(self):
        self.lock = Lock()
        self.count = 0

    def increment(self, offset):
        with self.lock:
            self.count += offset


def run_thread(func, how_many, counter):
    threads = []

    for i in range(5):
        args = (i, how_many, counter)
        thread = Thread(target=func, args=args)
        threads.append(thread)
        thread.start()

    for thread in threads:
        thread.join()


how_many = 10 ** 5
counter = Counter()
run_thread(worker, how_many, counter)
print('Counter는 %d 회 실행했습니다 그러나 counter결과값은 %d 입니다 ' %
      (5 * how_many, counter.count))

counter = LockingCounter()
run_thread(worker, how_many, counter)
print('Locking Counter는 %d 회 실행했습니다 그리고  counter결과값은 %d 입니다 ' %
      (5 * how_many, counter.count))
