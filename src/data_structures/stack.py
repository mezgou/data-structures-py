from typing import Any


class Node:
    def __init__(self, value : Any) -> None:
        self.value : Any | None = value
        self.next : Any | None = None


class Stack:
    def __init__(self) -> None:
        self.top : Node | None = None
        self.size : int = 0

    # O(1) - constant time
    def __len__(self) -> int:
        return self.size
    
    # O(n) - linear time
    def __repr__(self) -> str:
        items = []
        current_item = self.top
        while current_item is not None:
            items.append(str(current_item.value))
            current_item = current_item.next
        return ", ".join(items)
    
    # O(1) - constant time
    def push(self, value : Any) -> None:
        new_node = Node(value)
        new_node.next = self.top
        self.top = new_node
        self.size += 1

    # O(1) - constant time
    def pop(self) -> Any | ValueError:
        if self.top is None:
            raise ValueError("Stack is empty")
        pop_value = self.top.value
        self.top = self.top.next
        self.size -= 1
        return pop_value

    # O(1) - constant time
    def peek(self) -> Any | ValueError:
        if self.top is None:
            raise ValueError("Stack is empty")
        return self.top.value

    # O(1) - constant time
    def is_empty(self) -> bool:
        return self.top is None
    