class Task:
    def __init__(self, pri, name):
        self.pri = int(pri)
        self.name = str(name)

    def get_priority(self):
        return self.pri
