import src.error as error


class Queue:
    def __init__(self):
        self.queue = []

    def enqueue(self, value):
        self.queue.append(value)

    def dequeue(self):
        if not len(self.queue):
            raise error.QueueEmptyError
        return self.queue.pop(0)

    def has(self, value):
        return value in self.queue
