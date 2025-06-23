

from core import LinkedList, Queue, Stack, BST, Graph

def main():
    linked_list = LinkedList()
    linked_list.insert_at_end(1)
    linked_list.insert_at_end(2)
    linked_list.insert_at_end(3)
    linked_list.insert_at_end(4)
    linked_list.insert_at_end(5)
    linked_list.traverse()

    queue = Queue()
    queue.enqueue(1)
    queue.enqueue(2)
    queue.enqueue(3)
    queue.enqueue(4)
    queue.enqueue(5)
    while not queue.is_empty():
        print(queue.dequeue(), end=" ")
    print()

    stack = Stack()
    stack.push(1)
    stack.push(2)
    stack.push(3)
    stack.push(4)
    stack.push(5)
    while not stack.is_empty():
        print(stack.pop(), end=" ")
    print()

    bst = BST()
    bst.insert(1)
    bst.insert(2)
    bst.insert(3)
    bst.insert(4)
    bst.insert(5)
    bst.inorder()

    graph = Graph()
    graph.add_vertex(1)
    graph.add_vertex(2)
    graph.add_vertex(3)
    graph.add_vertex(4)
    graph.add_vertex(5)
    graph.add_edge(1, 2)
    graph.add_edge(2, 3)
    graph.add_edge(3, 4)
    graph.add_edge(4, 5)
    graph.add_edge(5, 1)
    graph.print_graph()

if __name__ == "__main__":
    main()