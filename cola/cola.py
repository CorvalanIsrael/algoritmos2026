class Queue:
from typing import Any

def __init__(self):
    self.__elements = []

def arrive(self, value:Any) -> None:
    self.__elements.append(value)
def attend(self) -> Any:
    self.__elements.pop(0)
def size(self) -> int:
    return len(self.__elements)
def move_to_end(self, value:Any) -> Any:
    value = self.attend()
    self.arrive(value)
    return value

def show(self):
    print(self.__elements)
