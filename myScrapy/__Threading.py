import threading
import Queue

class ScrapyWorker(threading.Thread):
    def __init__(self, workQueue, resultQueue, **kwargs):
        super(ScrapyWorker,self).__init__(self, **kwargs)
        self.workQueue = workQueue
        self.resultQueue = resultQueue

    def run(self):
        while (not self.workQueue.empty()):
            res = self.workQueue.get(False)
            res()


class ThreadManager(object):
    def __init__(self, num_threading = 10):
        self.workQueue = Queue.Queue()
        self.resultQueue = Queue.Queue()
        self.workers = []
        self._initThread(num_threading)

    def _initThread(self, num_threading):
        for i in range(num_threading):
            works = ScrapyWorker(workQueue=self.workQueue, resultQueue=self.resultQueue)
            self.workers.append(works)

    def waitForallThreadcompelete(self):
        while len(self.workers):
            worker = self.workers.pop()
            worker.join()
            if worker.isAlive() and not self.workers.empty():
                self.workers.append(worker)


    def add_func(self, func):
        self.workQueue.put(func)

    def start_thread(self):
        for w in self.workers:
            w.start



