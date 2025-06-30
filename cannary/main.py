from abc import ABC, abstractmethod
import json

# ------------------------------------------------------------------------------
# 1) Abstract Base: Collection
# ------------------------------------------------------------------------------

class Collection(ABC):
    """Abstract base class defining a uniform interface for all collections."""
    
    @abstractmethod
    def add(self, value):
        """Add an element to the collection."""
        pass

    @abstractmethod
    def remove(self):
        """Remove and return an element from the collection."""
        pass

    @abstractmethod
    def __len__(self):
        """Return number of elements."""
        pass

# ------------------------------------------------------------------------------
# 2) Mixin: JSON serialization
# ------------------------------------------------------------------------------

class JsonMixin:
    """Provides to_json() to any class with a __dict__ or custom serialization."""
    
    def to_json(self):
        return json.dumps(self.__dict__)

# ------------------------------------------------------------------------------
# 3) Stack
# ------------------------------------------------------------------------------

class Stack(Collection, JsonMixin):
    """LIFO stack implementing Collection interface and JSON mixin."""
    
    def __init__(self, max_size=None):
        # Encapsulation: _items hidden internal state
        self._items = []
        self._max_size = max_size

    def add(self, value):
        """alias for push."""
        self.push(value)

    def push(self, value):
        if self._max_size is not None and len(self._items) >= self._max_size:
            raise OverflowError("Stack is full")
        self._items.append(value)

    def remove(self):
        """alias for pop."""
        return self.pop()

    def pop(self):
        if self.is_empty():
            raise IndexError("pop from empty stack")
        return self._items.pop()

    def peek(self):
        return self._items[-1] if not self.is_empty() else None

    def is_empty(self):
        return len(self._items) == 0

    # Special methods
    def __len__(self):
        return len(self._items)

    def __str__(self):
        return "Stack(" + ", ".join(repr(i) for i in self._items) + ")"

    @classmethod
    def from_iterable(cls, iterable):
        """Alternative constructor demonstrating a class method."""
        stack = cls()
        for item in iterable:
            stack.push(item)
        return stack

    @staticmethod
    def is_valid_sequence(seq):
        """Static utility: checks if it's list-like."""
        return hasattr(seq, "__iter__")

# ------------------------------------------------------------------------------
# 4) Queue
# ------------------------------------------------------------------------------

class Queue(Collection):
    """FIFO queue with same interface as Collection."""
    
    def __init__(self):
        self._items = []

    def add(self, value):
        self.enqueue(value)

    def enqueue(self, value):
        self._items.append(value)

    def remove(self):
        return self.dequeue()

    def dequeue(self):
        if not self._items:
            raise IndexError("dequeue from empty queue")
        return self._items.pop(0)

    def __len__(self):
        return len(self._items)

    def __str__(self):
        return "Queue(" + ", ".join(repr(i) for i in self._items) + ")"

# ------------------------------------------------------------------------------
# 5) LinkedList
# ------------------------------------------------------------------------------

class LinkedListNode:
    """Node used internally by LinkedList."""
    def __init__(self, value, nxt=None):
        self.value = value
        self.next = nxt

class LinkedList(Collection):
    """Singly linked list implementation."""
    
    def __init__(self):
        self._head = None
        self._size = 0

    def add(self, value):
        """Insert at head by default."""
        new_node = LinkedListNode(value, self._head)
        self._head = new_node
        self._size += 1

    def remove(self):
        """Remove from head."""
        if not self._head:
            raise IndexError("remove from empty list")
        val = self._head.value
        self._head = self._head.next
        self._size -= 1
        return val

    def __len__(self):
        return self._size

    def __iter__(self):
        node = self._head
        while node:
            yield node.value
            node = node.next

    def __str__(self):
        return "LinkedList([" + ", ".join(repr(v) for v in self) + "])"

    @property
    def is_empty(self):
        return self._size == 0

# ------------------------------------------------------------------------------
# 6) BinaryTree
# ------------------------------------------------------------------------------

class TreeNode:
    """Node for binary tree."""
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

class BinaryTree:
    """Simple binary search tree with insert and traversal."""
    
    def __init__(self):
        self._root = None

    def insert(self, value):
        """Public API—encapsulation hides recursion detail."""
        def _insert(node, val):
            if node is None:
                return TreeNode(val)
            if val < node.value:
                node.left = _insert(node.left, val)
            else:
                node.right = _insert(node.right, val)
            return node

        self._root = _insert(self._root, value)

    def contains(self, value):
        def _contains(node, val):
            if node is None:
                return False
            if val == node.value:
                return True
            if val < node.value:
                return _contains(node.left, val)
            return _contains(node.right, val)
        return _contains(self._root, value)

    def __contains__(self, value):
        """Special method enabling `value in tree`."""
        return self.contains(value)

    def inorder(self):
        """Generator for inorder traversal."""
        def _inorder(node):
            if node:
                yield from _inorder(node.left)
                yield node.value
                yield from _inorder(node.right)
        yield from _inorder(self._root)

    def __iter__(self):
        """Default iteration is inorder."""
        return self.inorder()

    def __str__(self):
        return "BinaryTree(" + ", ".join(str(v) for v in self) + ")"

# ------------------------------------------------------------------------------
# 7) Graph
# ------------------------------------------------------------------------------

class Graph:
    """Directed graph using adjacency list."""
    
    def __init__(self):
        # Encapsulation: hide adjacency list
        self._adj = {}

    def add_node(self, node):
        self._adj.setdefault(node, set())

    def add_edge(self, src, dst):
        self.add_node(src)
        self.add_node(dst)
        self._adj[src].add(dst)

    def neighbors(self, node):
        return self._adj.get(node, set())

    def remove_node(self, node):
        self._adj.pop(node, None)
        for nbrs in self._adj.values():
            nbrs.discard(node)

    def __contains__(self, node):
        return node in self._adj

    def __len__(self):
        return len(self._adj)

    def __str__(self):
        return "Graph(" + ", ".join(f"{n}->{list(v)}" for n, v in self._adj.items()) + ")"

    def bfs(self, start):
        """Breadth-first traversal."""
        visited = set([start])
        queue = [start]
        while queue:
            node = queue.pop(0)
            yield node
            for nbr in self._adj.get(node, []):
                if nbr not in visited:
                    visited.add(nbr)
                    queue.append(nbr)

# ------------------------------------------------------------------------------
# Example usage
# ------------------------------------------------------------------------------

if __name__ == "__main__":
    # Stack
    s = Stack(max_size=3)
    s.push(1); s.push(2)
    print(s, "| len:", len(s), "| peek:", s.peek())
    print("JSON:", s.to_json())

    # Queue
    q = Queue()
    q.enqueue("a"); q.enqueue("b")
    print(q, "| dequeue:", q.dequeue())

    # LinkedList
    ll = LinkedList()
    for i in [10,20,30]:
        ll.add(i)
    print(ll, "| pop:", ll.remove())

    # BinaryTree
    bt = BinaryTree()
    for x in [5,3,7,1,4]:
        bt.insert(x)
    print(bt, "| contains 4?", 4 in bt)

    # Graph
    g = Graph()
    g.add_edge("A","B"); g.add_edge("A","C"); g.add_edge("B","D")
    print(g, "| BFS:", list(g.bfs("A")))
