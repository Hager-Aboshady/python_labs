class Queue:
    def __init__(self):
        self.myList = []

    def insert(self, value):
        self.myList.append(value)
        print("New Item has been added Successfully")

    def pop(self):
        if self.is_empty():
            print("Warning: The queue is empty.")
            return None
        else:
            self.myList.pop(0)
            print( "Item is popped")
            return True

    def is_empty(self):
        if len(self.myList) == 0:
            print("The Queue is Empty ")
            return True
        else:
            print(f"The Queue is Not Empty and The number of its items is {len(self.myList)} ")
            return False    


q = Queue()
q.insert(1)
q.insert(2)

# print(q.pop())  #  1
print(q.is_empty())  # False
# print(q.pop())  
# print(q.pop())  # output: Warning: The queue is empty. None
# print(q.is_empty())  # output: True
