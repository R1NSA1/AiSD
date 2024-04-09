class MultiAction:
    def __init__(self, n, cls):
        self.n = n
        self.cls = cls

    def action(self):
        for _ in range(self.n):
            self.cls.action()


class MyClass:
    def action(self):
        print("MyClass action")


multi_action = MultiAction(4, MyClass())
multi_action.action()
