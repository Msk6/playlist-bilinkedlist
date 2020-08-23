class Node:
    def __init__(self, year, next=None, prev=None):
        self.year = year
        self.next = next
        self.prev = prev

    def get_year(self):
        return self.year
    
    def get_next(self):
        return self.next
    
    def get_prev(self):
        return self.prev
    
    def set_year(self, year):
        self.year = year

    def set_next(self, next):
        self.next = next

    def set_prev(self, prev):
        self.prev = prev


class BiLinkedlist:
    def __init__(self, year):
        node = Node(year)
        self.head = node
        self.tail = node        

    def add_tail(self, year):
        node = Node(year, prev=self.tail)
        self.tail.next = node
        self.tail = node
    
    def get_head(self):
        return self.head

    def add_between(self, current_node, year):
        node = Node(year, next=current_node.next, prev=current_node)
        current_node.next = node

    def print_bilinkedlist(self, head):
        
        current_node = head

        while current_node:
            print(current_node.year)
            current_node = current_node.next

    def remove_node(self, name):
        current_node = self.head
        while current_node: 
            if current_node.get_year() == name:
                if current_node.get_prev() == None:
                    print ("Inside remove head")
                    self.head = current_node.get_next()
                    current_node.get_next().set_prev(None)
                    current_node.set_next(None)
                    
                elif current_node.get_next() == None:
                    self.tail = current_node.get_prev()
                    current_node.get_prev().set_next(None)
                    current_node.set_prev(None)
                    
                else:
                    current_node.get_prev().set_next(current_node.get_next())
                    current_node.get_next().set_prev(current_node.get_prev())
                return
            current_node = current_node.get_next()
        print("The item is not exist")



controler = True
playlist = BiLinkedlist("1")
playlist.add_tail("10")
playlist.add_tail("11")
playlist.add_tail("12")
playlist.add_tail("13")
current_node = playlist.get_head()

while controler:
    instruction = input("next = 1, prev = 2, add = 3, remove = 4, start from here = 5, start = 6, exit = 0:\n ")
    if instruction == "1":
        if current_node.get_next():
            current_node = current_node.get_next()
            print(current_node.get_year())
        else: 
            print ("No more, You reached the end")
    elif instruction == "2":
        if current_node.get_prev():
            current_node = current_node.get_prev()
            print(current_node.get_year())
        else:
            print("No more, You reached the first track")

    elif instruction == "3":
        year = input("Enter your track name: ")
        playlist.add_tail(year)

    elif instruction == "4":
        year = input("Enter track name to remove: ")
        if current_node.get_year() == year:
            current_node = current_node.get_next()
        playlist.remove_node(year)
         

    elif instruction == "5":
        print("start the playlist from where we are: ")
        playlist.print_bilinkedlist(current_node)
    
    elif instruction == "6":
        print ("start playlis from begining: ")
        playlist.print_bilinkedlist(playlist.get_head())
    
    elif instruction == "0":
        break

    else:
        print("Enter valid option")