'''
    Time Complexity: O(N * M)
    Space Complexity: O(N)

    Where 'N' denotes size of cache and 'M' denotes the number of operations.
'''

from typing import List


class Node:
    def __init__(self, value: int = 0, index: int = 0, freq: int = 0) -> None:
        self.value = value  # Value stored in the node.
        self.index = index  # Index of the node.
        self.freq = freq    # Frequency of the node.


class LFUCache:
    def __init__(self, capacity: int) -> None:
        self.capacity = capacity   # Capacity of the cache.
        self.cache = [-1] * capacity  # Cache to store the keys.
        # Nodes representing the objects in the cache.
        self.nodes = [Node() for _ in range(capacity)]
        self.currSize = 0   # Current size of the cache.
        self.position = 0   # Current position in the cache.

    def get(self, key: int) -> int:
        self.position += 1  # Update the current number of queries.
        value = -1  # Initial value set as -1.

        # Search the entire cache.
        for i in range(len(self.cache)):
            if key == self.cache[i]:
                value = self.nodes[i].value  # Key found in the cache.
                self.nodes[i].freq += 1  # Update the frequency.
                self.nodes[i].index = self.position  # Update the position.

        return value

    def put(self, key: int, value: int) -> None:
        self.position += 1  # Update the current number of queries.

        if self.capacity == 0:
            return

        # Check if the key is already present in the cache.
        for i in range(self.capacity):
            if key == self.cache[i]:
                self.nodes[i].index = self.position  # Update the position.
                self.nodes[i].freq += 1  # Update the frequency.
                self.nodes[i].value = value  # Update the value.
                return

        # If the key is not present in the cache and the cache is not full.
        if self.currSize < self.capacity:
            self.cache[self.currSize] = key  # Add the key to the cache.
            # Add the value to the node.
            self.nodes[self.currSize].value = value
            self.nodes[self.currSize].freq = 1  # Set the frequency as 1.
            # Set the position.
            self.nodes[self.currSize].index = self.position
            self.currSize += 1  # Increment the current size.
        else:
            pos = 0  # Position of the least frequently used (LFU) node.

            # Find the LFU node in the cache.
            for j in range(self.capacity):
                if self.nodes[j].freq < self.nodes[pos].freq:
                    pos = j
                elif self.nodes[j].freq == self.nodes[pos].freq and self.nodes[j].index < self.nodes[pos].index:
                    pos = j

            # Replace the LFU node with the current key and value.
            self.cache[pos] = key
            self.nodes[pos].value = value
            self.nodes[pos].freq = 1
            self.nodes[pos].index = self.position
