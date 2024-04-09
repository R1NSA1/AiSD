from queue import Queue


class MultiPump:
    def __init__(self, queues, generator):
        self.queues = queues
        self.generator = generator
        self.current_queue_index = 0

    def action(self):
        value = next(self.generator)
        self.queues[self.current_queue_index].put(value)
        self.current_queue_index = (self.current_queue_index + 1) % len(self.queues)


queues = [Queue(), Queue()]
generator = (i for i in range(10))
multi_pump = MultiPump(queues, generator)
for _ in range(10):
    multi_pump.action()
for i, queue in enumerate(queues):
    print(f"Queue {i}: {queue.queue}")
