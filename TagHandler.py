from abc import ABC, abstractmethod
class TagHandler(ABC):
    def __init__(self):
        pass
    @abstractmethod
    def run(client, payload):
        pass