from node import *

class PriorityQueue(list):
    def __init__(self, tasks=[]):
        self.tasks = tasks
        self.head = None

    def enque(self, task):
        if self.head is None:
            self.head = Node(task, None)
        current_node = self.head
        if current_node.get_priority() >= task.get_priority():
            if not current_node.has_next():
                current_node.set_next(Node(task))
            elif current_node.get_next().get_priority() < task.get_priority():
                current_node.set_next(Node(task,current_node.get_next()))
        if current_node.get_priority() < task.get_priority():



