
class Node:
    def __init__(self, task, next=None):
        """

        :param task:
        :param next:
        """
        self._task = task
        self._next = next
        self._priority = task.get_priority()

    def get_priority(self):
        """


        :return:
        """
        return self._priority

    def set_priority(self, new_priority):
        """

        :param new_priority:
        """
        self._priority = new_priority

    def get_task(self):
        """


        :return:
        """
        return self._task

    def get_next(self):
        """


        :return:
        """
        return self._next

    def set_next(self, next_node):
        """

        :param next_node:
        """
        self._next = next_node

    def has_next(self):
        """


        :return:
        """
        if self._next is None:
            return False
        else:
            return True
