#George West
#23-1-15
#Student mark record

class markbook:
    def __int__(self):
        self.name = None
        self.mark = None
##new_record = markbook()
##new_record.name = input("Please enter the name: ")
##new_record.mark = int(input("Please enter a mark: "))
##print("{0} got {1} marks".format(new_record.name,new_record.mark))

records = []
for count in range(3):
    records.append(markbook())
for record in records:
    record.name = input("Please enter the name: ")
    record.mark = int(input("Please enter a mark: "))
Name = "Name"
Mark = "Mark"
print("{0:<6} {1:<4}".format(Name, Mark))
for record in records:
      print("{0:6} {1:^4}".format(record.name,record.mark))
    
