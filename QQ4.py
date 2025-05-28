class node:
    def __init__(self,data):
        self.data = data 
        self.next = node 



class LinkedList:
    def __init__(self,data):
        self.head = node 

    def Listprint(self,data):
        printval = self.head
        while printval is not node:
            print (printval.data) 
            printval = printval.next

L1 = LinkedList ()
L1.head = node ("Toyoto")
L2 = node ("BMW")  
L3 = node ("Audi")
L4 = node ("Lombogini")
L1.head.next = L2
L2.next = L3
L3.next = L4
L3.Listprint ()