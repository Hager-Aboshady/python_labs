import QueueOutOfRangeException
class Queue:
    def __init__(self,name,size):
        self.name=name
        self.size=size
        self.myList = []

    def insert(self, value):
        num_items=len(self.myList)
        if(num_items < self.size):
            self.myList.append(value)
            print("New Item has been added Successfully")
        else:
            raise QueueOutOfRangeException("QueueOutOfRangeException !!  You've exceded the size of the Queue !! ")


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


q=Queue("my q",3)
q.insert(0)
q.insert(1)
q.insert(2)
q.insert(2)