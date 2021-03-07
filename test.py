from datetime import date

class BookInstance():
#    due_back = "2021/02/21"
    #def __init__(self, id):
    #    self.due_back = id

    def is_overdue(due_back):
        if due_back and date.today() > due_back:
            return True
        return False

    def test(id):
        if id and 23 > id:
            return True
        return False

#print(BookInstance.test(23))

datum = date(2021, 2, 21)
#datum = None
y = BookInstance.is_overdue(datum)
x = date.today()
#print(x)
#print(y)
#print(BookInstance.is_overdue(("2021-02-23"))

#x = BookInstance("2021/02/23")
#print (BookInstance.is_overdue.__get__(x)) #2

if 200 and 220 > 23:
    print(True)
else:
    print(False)