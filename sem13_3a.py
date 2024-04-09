from queue import Queue


class Pump:
    def __init__(self, queuee, ggenerator):
        self.queue = queuee
        self.generator = ggenerator

    def action(self):
        value = next(self.generator)
        self.queue.put(value)


queue = Queue()
generator = (i for i in range(10))
pump = Pump(queue, generator)
for _ in range(10):
    pump.action()
print(queue.queue)

