# 1. Rectangles Measurement

from datetime import date, datetime
import math
from random import randint


class Point: # Point object (x,y) coordinates in pixels
    def __init__(self, x,y):
        self.xCoordinate = x
        self.yCoordinate = y

    
class Rectangle: # define rectangle object
    def __init__(self, w, h, x=0,y=0):
        self.rWidth = w
        self.rHeight = h
        #generate bottom right corner coordinates (x,y)
        if x==0:
            self.x = randint(w, 100)
        else:
            self.x = x
        if y==0:
            self.y = randint(h, 100)
        else:
            self.y = y

        print('New rectangle was created, width is {} and height is {}.'.format(w,h))
    
    def getSurfaceArea(self):
        return self.rWidth*self.rHeight

    def getCircumference(self):
        return (self.rWidth+self.rHeight)*2

    # return a Point object (x,y) in pixels
    def getBottomRightCorner(self): 
                
        return Point(self.x,self.y)

    #returns the overlapping area of the two rectangles as a new Rectangle object
    def getOverlappingArea(self, aRectangle):
        pass

def inputRecData(dataName):
    finalResult = 0
    while True:
        result = int(input('Input the {} of the rectangle (an interger >0): '.format(dataName)))
        if result > 0:
            finalResult = result
            break
        else:
            print('ERROR! Your input is invalid.')
    return finalResult

#main program
def createRectangle():
    w = inputRecData('width')
    h = inputRecData('height')

    myRectangle = Rectangle(w,h)

    print('Surface area is:', myRectangle.getSurfaceArea())
    print('Circumference is: ', myRectangle.getCircumference())

    bottomRightCorner = myRectangle.getBottomRightCorner()
    print ('The bottom-right corner of the rectangle is: ({},{})'.format(bottomRightCorner.xCoordinate,bottomRightCorner.yCoordinate))

#test the progam:
# createRectangle()

#==================================================================
# 2. Inrolled Students

# Define Course object
class Course:
    def __init__(self, name, num):
        self.name = name
        self.num = num


# Define Student object
class Student:
    def __init__(self, fName, lName, birthdate, adminNum):
        self.firstName = fName
        self.lastName = lName
        self.birthdate = birthdate
        self.adminNo = adminNum
        self.courses = []
    
    def enrollCourse(self, course):
        self.courses.append(course)

    def displayCourses(self):

        displayCourses = '['
        for course in self.courses:
            displayCourses += course.name
            displayCourses += ', '

        displayCourses += ']'
        return displayCourses

    def getAge(self):
        today = date.today()
        age = today.year-self.birthdate.year - ((today.month, today.day) < (self.birthdate.month, self.birthdate.day))

        return age
    
    def displayInfo(self):
        print('Student number {} - Fullname: {}{}, age: {}, courses: {}'.format(self.adminNo,self.firstName, self.lastName,self.getAge(),self.displayCourses()))


def inputData(dataName):

    data = input('Please input {}: '.format(dataName))
    data = data.strip()

    while data=='':
        data = input('Your data is empty, please input {} again: '.format(dataName))
        data = data.strip()

    return data

# input birthdate
def inputBirthdate():
    currentYear = date.today().year
    year = int(input('Please input year of birthdate (< current year): '))

    while year>currentYear:
        year = int(input('Please input year of birthdate (< current year): '))

    month = int(input('Please input month of birthdate (interger between 1-12): '))
    while month <1 or month >12:
        month = int(input('Please input month of birthdate (interger between 1-12): '))

    bDate = int(input('Please input date of birthdate (interger between 1-31): '))
    while bDate < 1 or bDate > 31:
        bDate = int(input('Please input date of birthdate (interger between 1-31): '))

    return date(year,month,bDate)

# create a course
def createCourse():
    courseName = inputData('course name')
    courseNum = inputData('course number')

    return Course(courseName,courseNum)

# Create a student
def createStudent():
    fName = inputData('student firstname')
    lName = inputData('stydent lastname')
    adminNo = inputData('student admin number')
    birthdate = inputBirthdate()

    return Student(fName,lName,birthdate,adminNo)



#main program:
def inrolledStudents():

    allCourses=[]
    allStudents=[]

    while True: #Create some courses
        course = createCourse()
        allCourses.append(course)

        getMore = input('Do you want to create another course? (y/n)')
        if getMore != 'y':
            break

    while True: # Create some students
        student = createStudent()
        allStudents.append(student)

        #enroll course?
        takeCourse = input('Do you want to take a course for this student? (y/n)' )

        while takeCourse=='y':
            
            courseNo = inputData('course number')
            for c in allCourses:
                if courseNo == c.num:
                    student.enrollCourse(c)

            takeCourse = input('Do you want to take another course for this student? (y/n)' )

        getMore = input('Do you want to create another student? (y/n)' )
        if getMore != 'y':
            break
    
    #Showing the list of available students
    print('List of all students: {}'.format(len(allStudents)))
    for s in allStudents:
        s.displayInfo()

#test the program
# inrolledStudents()

#===============================================================

# 3. Square Measurement

class Rectangle1:
    def __init__( self , x, y, w, h ):
        self.x = x
        self.y = y
        self.w = w
        self.h = h

    def area( self ):
        return self.w * self.h
    def circumference( self ):
        return 2*( self.w + self.h)

# Define Square object inherits from Rectangle:

class Square(Rectangle1):
    def __init__(self, x,y, size):
        super().__init__(x,y,size,size)

# main program
def squareMeasure():
    x = int(input('Input top-left corner x coordinate for your square (a number >0): '))
    y = int(input('Input top-left corner y coordinate for your square (a number >0): '))
    size = int(input('Input your square size (a number >0): '))

    aSquare = Square(x,y,size)
    print(aSquare.area())
    print(aSquare.circumference())

# test the program:
# squareMeasure()

# ======================================================================

# 4. Extending Measurement

class Shape:
    def __init__(self, name):
        self.name = name

class Rectangle2(Shape):
    def __init__( self ,x, y, w, h ):
        super().__init__('rectangle')
        self.x = x
        self.y = y
        self.w = w
        self.h = h

    def area( self ):
        return self.w * self.h
    def circumference( self ):
        return 2*( self.w + self.h)

class Square2(Shape):
    def __init__(self, x,y, size):
        super().__init__('square')
        self.x = x
        self.y = y
        self.size = size
    def area( self ):
        return self.size * self.size
    def circumference( self ):
        return self.size*4

class Circle(Shape):
    def __init__(self, x,y, radius):
        super().__init__('circle')
        self.x = x
        self.y = y
        self.radius = radius
    def area(self):
        return self.radius*self.radius*math.pi

    def circumference( self ):
        return self.radius*2*math.pi

    