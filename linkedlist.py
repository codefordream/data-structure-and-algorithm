class Node:
    def __init__(self,dataval=None):
        self.dataval = dataval
        self.nextval = None

class linkedlist:
    def __init__(self):
        self.headval = None

#method to print element of list
    def listprint(self):
        printval = self.headval
        while printval is not None:
            print(printval.dataval)
            printval = printval.nextval

#method to insert element at the begining
    def InsAtBegining(self,newdata):
        New = Node(newdata)
        New.nextval = self.headval
        self.headval = New

#method to insert element at last
    def InsAtLast(self,newdata):
        New = Node(newdata)
        if self.headval is None:
            self.headval = New
            return
        last = self.headval
        while(last.nextval):
            last = last.nextval
        last.nextval = New

#length of Linkedlist
    def length(self):
        element = self.headval
        l = 1
        while(element.nextval):
            l +=1
            element = element.nextval
        return l


#method to insert element in prespecified index and index starts from 0
    def InsAtLoc(self,newdata,location):
        iter = location - 1
        l = list.length()
        if location < l:
            New = Node(newdata)
            current = self.headval
            while(iter):
                current = current.nextval
                iter -=1
            New.nextval = current.nextval
            current.nextval = New
        else:
            print("invalid Location")


#method to remove element at the begining
    def DelAtBegining(self):
        if self.headval is None:
            print("list is empty")
            return
        val = self.headval
        self.headval = self.headval.nextval
        print("Deleted element:" + str(val.dataval))

#method to remove element at last
    def DelAtLast(self):
        if self.headval is None:
            print("list is empty")
            return
        last = self.headval
        while(last.nextval):
            p = last
            last = last.nextval
        p.nextval = None
        print("Deleted element:" + str(p.dataval))

#method to remove element in prespecified index and index starts from 0
    def DelAtLoc(self,location):
        if self.headval is None:
            print("list is empty")
            return
        l = list.length()
        if location == 0:
            list.DelAtBegining()
            return
        if location == l:
            list.DelAtLast()
            return
        if location < l:
            current = self.headval
            while(location):
                p = current
                current = current.nextval
                location -=1
            val = current
            p.nextval = current.nextval
            print("Deleted element:" + str(val.dataval))
        else:
            print("invalid Location")


list = linkedlist()
list.headval = Node("Feb")
e2 = Node("Mar")
e3 = Node("Apr")

list.headval.nextval = e2
e2.nextval = e3

list.InsAtBegining('Jan') #inserting element at begining
list.InsAtLast('Dec') #inserting element at last
list.InsAtLoc('May',4) #inserting element at index 4, index starts from 0
list.DelAtBegining() #delete element at begining
list.DelAtLast() #delete element at last
list.DelAtLoc(2) #delete element at index 2, index starts from 0
list.listprint() #print list elements
