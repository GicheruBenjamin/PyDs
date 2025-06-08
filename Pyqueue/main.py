
from .que import Queue

bus_line = Queue()
bus_line.enqueue(1)
bus_line.enqueue(2)
bus_line.enqueue("John")
bus_line.enqueue({"name": "King", "age": 30})
bus_line.enqueue(True)
bus_line.enqueue(["curls", "lifts", "langes"])

def main():
    print(bus_line.size())

if __name__ == "__main__":
    main()