# program to implement Queue using array.
class Queue:
    def __init__(self):
        self.queue = []
    
    def enqueue(self, item):
        self.queue.append(item)
    
    def dequeue(self):
       
        if self.is_empty():
            raise IndexError("dequeue from empty queue")
        return self.queue.pop(0)
    
    def peek(self):
        if self.is_empty():
            raise IndexError("peek from empty queue")
        return self.queue[0]
    
    def is_empty(self):
        return len(self.queue) == 0
    
    def size(self):
        return len(self.queue)

# Example Usage:
if __name__ == "__main__":
    queue = Queue()
    
    # Enqueue items to the queue
    queue.enqueue(10)
    queue.enqueue(20)
    queue.enqueue(30)
    
    # Print queue size
    print(f"Queue size: {queue.size()}")
    
    # Peek at the front item
    print(f"Front item: {queue.peek()}")
    
    # Dequeue items from the queue
    print(f"Dequeued item: {queue.dequeue()}")
    print(f"Dequeued item: {queue.dequeue()}")
    
    # Check if the queue is empty
    print(f"Is queue empty? {queue.is_empty()}")
    
    # Try to dequeue from an empty queue
    try:
        queue.dequeue()
    except IndexError as e:
        print(e)
