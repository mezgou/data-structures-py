from typing import Any, Iterable


class HashMap:
    def __init__(self, capacity: int) -> None:
        self.capacity = capacity
        self.size = 0
        self.buckets = [[] for _ in range(capacity)]

    # O(1) - constant time
    def __len__(self) -> int:
        return self.size

    # Average: O(1) - constant time
    # Worst: O(n) - linear time
    # Depends on the quality of the hash function
    def __contains__(self, key: Any) -> bool:
        index = self._hash_function(key)
        bucket = self.buckets[index]
        for k, v in bucket:
            if k == key:
                return True
        return False

    # Average: O(1) - constant time
    # Worst: O(n) - linear time
    # Depends on the quality of the hash function
    def put(self, key: Any, value: Any) -> None:
        index = self._hash_function(key)
        bucket = self.buckets[index]
        for i, (k, v) in enumerate(bucket):
            if k == key:
                bucket[i] = (key, value)
                break
        else:
            bucket.append((key, value))
            self.size += 1

    # Average: O(1) - constant time
    # Worst: O(n) - linear time
    # Depends on the quality of the hash function
    def get(self, key: Any) -> Any | KeyError:
        index = self._hash_function(key)
        bucket = self.buckets[index]
        for k, v in bucket:
            if k == key:
                return v
        raise KeyError("Key not found")

    # Average: O(1) - constant time
    # Worst: O(n) - linear time
    # Depends on the quality of the hash function
    def remove(self, key: Any) -> None | KeyError:
        index = self._hash_function(key)
        bucket = self.buckets[index]
        for i, (k, v) in enumerate(bucket):
            if k == key:
                del bucket[i]
                self.size -= 1
                break
        else:
            raise KeyError("Key not found")

    # O(n) - linear time
    def keys(self) -> Iterable[Any]:
        return [k for bucket in self.buckets for k, _ in bucket]

    # O(n) - linear time
    def values(self) -> Iterable[Any]:
        return [v for bucket in self.buckets for _, v in bucket]

    # O(n) - linear time
    def items(self) -> Iterable[tuple[Any, Any]]:
        return [(k, v) for bucket in self.buckets for k, v in bucket]

    # O(k) - linear in key length
    def _hash_function(self, key: Any) -> int:
        key_string = str(key)
        hash_result = 0
        for char in key_string:
            hash_result = (hash_result * 31 + ord(char)) % self.capacity
        return hash_result


def test_hash_map_distribution() -> None:
    import uuid
    import matplotlib.pyplot as plt

    hash_map = HashMap(500)
    for _ in range(100000):
        hash_map.put(uuid.uuid4(), "some_value")

    x = []
    y = []
    for i, bucket in enumerate(hash_map.buckets):
        x.append(i)
        y.append(len(bucket))
    plt.title("Hash Map Distribution")
    plt.xlabel("Index")
    plt.ylabel("Number of buckets")
    plt.bar(x, y)
    plt.show()
