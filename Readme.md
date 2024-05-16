
## Description
Queues are fundamental data structure in computer science that follow the First-In-First-Out (FIFO) principle. Here are some key characteristics and uses of queues:

1. FIFO: The First-In-First-Out principle means that the first element added to the queue is the first one to be removed. This is similar to a line at a ticket counter, where people are served in the order they arrived.
2. Operations: Queues typically support three main operations: enqueue (add an element to the back of the queue), dequeue (remove and return the front element), and peek (return the front element without removing it).
3. Uses: Queues have various applications in computer science, including:
Breadth-first search: Queues are used in the breadth-first search algorithm for traversing graphs and trees.
4. Job scheduling: Queues are used in operating systems to manage the execution of processes and tasks.
5. Buffering: Queues are used to buffer data between different components of a system, such as between a producer and a consumer.
6. Asynchronous processing: Queues can be used to manage asynchronous tasks, where tasks are added to the queue and processed in the order they were added.
7. Implementation: Queues can be implemented using arrays or linked lists. Array-based implementations are simple and efficient for accessing elements, but they may require resizing and can be inefficient for enqueue and dequeue operations. Linked list-based implementations are more flexible in terms of size and can be more efficient for enqueue and dequeue operations.
8. Space complexity: The space complexity of a queue is O(n), where n is the number of elements in the queue. This is because each element in the queue requires a constant amount of space.
Queues are a versatile data structure with many applications in computer science and programming. Understanding how to use and implement queues is an important skill for any programmer.


## Application 
I have used a queue class to implement. Having the methods to do on the queue is really cool.Assuming the queue starts from the right such that the 1st item entered from the left.

1. Method enqueue for adding an item at the left side.
2. Method dequeue for removing an item from the queue at the right side.
3. Method Is empty to look through if the queue is empty.
4. Method size to look how many items there are. 
