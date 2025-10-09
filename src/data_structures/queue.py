from typing import Any


class Node:
    def __init__(self, value: Any) -> None:
        self.value: Any | None = value
        self.next: Any | None = None


class Queue:
    def __init__(self) -> None:
        self.front: Any | None = None
        self.rear: Any | None = None
        self.size: int = 0

    # O(1) - constant time
    def __len__(self) -> int:
        return self.size

    # O(n) - linear time
    def __repr__(self) -> str:
        items = []
        current_item = self.front
        while current_item is not None:
            items.append(str(current_item.value))
            current_item = current_item.next
        return ", ".join(items)

    # O(1) - constant time
    def enqueue(self, value: Any) -> None:
        new_node = Node(value)
        if self.rear is None:
            self.front = self.rear = new_node
        else:
            self.rear.next = new_node
            self.rear = new_node
        self.size += 1

    # O(1) - constant time
    def dequeue(self) -> Any | IndexError:
        if self.front is None:
            raise IndexError("Queue is empty")
        dequeue_value = self.front.value
        self.front = self.front.next
        if self.front is None:
            self.rear = None
        self.size -= 1
        return dequeue_value

    # O(1) - constant time
    def peek(self) -> Any:
        if self.front is None:
            raise IndexError("Queue is empty")
        return self.front.value

    # O(1) - constant time
    def is_empty(self) -> bool:
        return self.front is None
