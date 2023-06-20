student_name = []

def readfile(filename):
    student_dict = []
    with  open(filename,"r") as fs:
        for line in fs:
            sx = Student(line)
            student_dict[sx.name] = sx 
    return student_dict 


class Student:
    def __init__(self,line):
        flds = line.split(",")
        ## name,instistute ,math,science,english,social,telugu 
        self.name = flds[0]
        self.institute = flds[1]
        self.math = int(flds[2])
        self.science = int(flds[3])
        self.english = int(flds[4])
        self.social = int(flds[5])
        self.telugu = int(flds[6])

readfile(studentFiles.txt)
    