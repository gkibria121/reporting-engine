from abc import ABC, abstractmethod


class IReporter(ABC):

    @abstractmethod
    def report(self, template):
        pass

    @abstractmethod
    def set_successor(self, successor):
        pass

    @abstractmethod
    def set_data(self, data):
        pass


class IMethod(ABC):

    @abstractmethod
    def evaluate(self):
        pass

    @abstractmethod
    def set_successor(self):
        pass
