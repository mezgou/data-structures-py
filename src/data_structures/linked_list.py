from typing import Any


class Node:
    def __init__(self, value : Any) -> None:
        self.value : Any | None = value
        self.next : Any | None = None
    

class LinkedList:
    def __init__(self) -> None:
        self.head : Node | None = None

    # O(n) - linear time
    def __repr__(self) -> str:
        if self.head is None:
            return "[]"
        else:
            last = self.head
            return_string = f"[{last.value}"
            while last.next is not None:
                last = last.next
                return_string += f", {last.value}"
            return_string += "]"
        return return_string

    # O(n) - linear time
    def __contains__(self, value : Any) -> bool:
        last = self.head
        while last is not None:
            if last.value == value:
                return True
            last = last.next
        return False

    # O(n) - linear time
    def __len__(self) -> int:
        last = self.head
        counter = 0
        while last is not None:
            counter += 1
            last = last.next
        return counter

    # O(n) - linear time
    def append(self, value : Any) -> None:
        if self.head is None:
            self.head = Node(value)
        else:
            last = self.head
            while last.next:
                last = last.next
            last.next = Node(value)

    # O(1) - constant time
    def prepend(self, value: Any) -> None:
        first_node = Node(value) 
        first_node.next = self.head
        self.head = first_node

    # O(n) - linear time
    def insert(self, value : Any, index : int) -> None | ValueError:
        if index == 0:
            self.prepend(value)
        else:
            if self.head is None:
                raise ValueError("Index out of bounds")
            else:
                last = self.head
                for _ in range(index - 1):
                    if last.next is None:
                        raise ValueError("Index out of bounds")
                    last = last.next
                new_node = Node(value)
                new_node.next = last.next
                last.next = new_node

    # O(n) - linear time
    def delete(self, value : Any) -> None:
        last = self.head
        if last is not None:
            if last.value == value:
                self.head = last.next
            else:
                while last.next:
                    if last.next.value == value:
                        last.next = last.next.next
                        break
                    last = last.next

    # O(n) - linear time
    def pop(self, index : int) -> None | ValueError:
        if self.head is None:
            raise ValueError("Index out of bounds")
        else:
            last = self.head
            for _ in range(index - 1):
                if last.next is None:
                    raise ValueError("Index out of bounds")
                last = last.next
            if last.next is None:
                raise ValueError("Index out of bounds")
            else:
                last.next = last.next.next

    # O(n) - linear time
    def get(self, index : int) -> Any | ValueError:
        if self.head is None:
            raise ValueError("Index out of bounds")
        else:
            last = self.head
            for _ in range(index):
                if last.next is None:
                    raise ValueError("Index out of bounds")
                last = last.next
            return last.value
