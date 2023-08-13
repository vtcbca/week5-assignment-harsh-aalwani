# INSERTING RECORDS
def insertFunct():
    import csv    #importing csv functions
    fields=['sid','sname','city','contact']
    rows=[[101,'Om','Bardoli',9999990000],
      [102,'Sai','Surat',9998888000],
      [103,'Ram','Navsari',9991110000],
      [104,'Vatsal','Vyara',9999666000],
      [105,'Harsh','Bardoli',8889900222]]     #pre-inserted records
    print("Enter the required records: ")
    for i in range(5):
        s_id=int(input("Enter Student ID: "))
        name=input("Enter Student Name: ")
        city=input("Enter their city name: ")
        contact=int(input("Enter their Contact info: "))
        srow=[s_id,name,city,contact]         #user input records
        rows.append(srow)
    with open('D:\\python\\student.csv','w',newline='') as csvfile:
        csvwriter=csv.writer(csvfile)
        csvwriter.writerow(fields)     #writing column names into csv file
        csvwriter.writerows(rows)      #writing student info into csv file

# READING RECORDS
]def readFunct():
    import csv    #importing csv file
    with open('D:\\python\\student.csv', 'r') as read_file:
        read =csv.reader(read_file)
        header=next(read)      # Skip headers from file
        for records in read:
            print(records[0], records[1],records[2],records[3])    #printing records

insertFunct()    #directly calling function
readFunct()      #directly calling function
