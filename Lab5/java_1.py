class Stack:
    def __init__(self):
        """
        Initialize an empty stack.
        """
        self.stack = []
    
    def push(self, item):
        """
        Push an item onto the stack.
        
        Parameters:
        item (any): The item to push onto the stack
        """
        self.stack.append(item)
    
    def pop(self):
        """
        Pop an item from the stack and return it.
        
        Returns:
        any: The item removed from the stack
        
        Raises:
        IndexError: If the stack is empty
        """
        if self.is_empty():
            raise IndexError("pop from empty stack")
        return self.stack.pop()
    
    def peek(self):
        """
        Return the top item of the stack without removing it.
        
        Returns:
        any: The top item of the stack
        
        Raises:
        IndexError: If the stack is empty
        """
        if self.is_empty():
            raise IndexError("peek from empty stack")
        return self.stack[-1]
    
    def is_empty(self):
        """
        Check if the stack is empty.
        
        Returns:
        bool: True if the stack is empty, False otherwise
        """
        return len(self.stack) == 0
    
    def size(self):
        """
        Return the number of items in the stack.
        
        Returns:
        int: The size of the stack
        """
        return len(self.stack)

# Example Usage:
if __name__ == "__main__":
    stack = Stack()
    
    # Push items onto the stack
    stack.push(10)
    stack.push(20)
    stack.push(30)
    
    # Print stack size
    print(f"Stack size: {stack.size()}")
    
    # Peek at the top item
    print(f"Top item: {stack.peek()}")
    
    # Pop items from the stack
    print(f"Popped item: {stack.pop()}")
    print(f"Popped item: {stack.pop()}")
    
    # Check if the stack is empty
    print(f"Is stack empty? {stack.is_empty()}")
    
    # Try to pop from an empty stack
    try:
        stack.pop()
    except IndexError as e:
        print(e)
