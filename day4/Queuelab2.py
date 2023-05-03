import QueueOutOfRangeException
class Queue:
    objs = {}  
    def __init__(self, name, size=10):
        self.name = name
        self.myList = []
        self.size = size
        Queue.objs[name] = self  #set the obj in the dictionary #the key will be the name and the value is the obj

    def insert(self, value):
        num_items=len(self.myList)
        if(num_items < self.size):
            self.myList.append(value)
            print(f"{value} has been added Successfully")
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
            # print("The Queue is Empty ")
            return True
        else:
            # print(f"The Queue is Not Empty and The number of its items is {len(self.myList)} ")
            return False    

    @classmethod
    def get_obj(cls, name):
        return cls.objs.get(name, "NOT FOUND")
    
q=Queue("obj1",3)
q.insert(1)
q.insert(2)

# print(q.get_obj("obj1"))
# print(q.get_obj("obj2"))

q.insert(3)
#q.insert(4)
"""-------------------------------------"""

