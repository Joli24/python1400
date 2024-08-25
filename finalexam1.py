#Jessica Oliveros
#Final Exam
#Purpose: To develop programs of techniques taught in class 1400


import math
import random
import tkinter as tk
from tkinter import messagebox

class Cube:
    def __init__(self, length=3.0, width=3.0, height=3.0):
        # Constructor to initialize Cube
        self.__width = width
        self.__height = height
        self.__length = length
        self.__area = self.findArea()  

    def getLength(self):
        return self.__length
    
    def getWidth(self):
        return self.__width
    
    def getHeight(self):
        return self.__height

    def setLength(self, length):
        self.__length = length

    def setWidth(self, width):
        self.__width = width

    def setHeight(self, height):
        self.__height = height

    def findArea(self):
        # Calculate and return the surface area of the cube
        return 2 * (self.__length * self.__width + self.__width * self.__height + self.__height * self.__length)

    def displayInfo(self):
        # Display information about the Cube

        #format to two decimals
        return "Cube, %.2f"%self.__area

class Square:
    def __init__(self, side=4.0):
        # Constructor to initialize Square object
        self.__side = side
        self.__area = self.findArea()  # Calculate area during initialization

    def getSide(self):
        return self.__side

    def setSide(self, side):
        self.__side = side

    def findArea(self):
        # Calculate and return the area of the square
        return self.__side * self.__side

    def displayInfo(self):
        # Display info about the Square
        return "Square, %.2f"%self.__area

class Circle:
    def __init__(self, radius=4.3):
        # Constructor to initialize Circle object
        self.__radius = radius
        self.__area = self.findArea()  # Calculate area during initialization

    def getRadius(self):
        return self.__radius

    def setRadius(self, radius):
        self.__radius = radius
    
    def findArea(self):
        # Calculate and return the area of the circle
        return math.pi * self.__radius * self.__radius

    def displayInfo(self):
        # Display information about the Circle
        return "Circle, %.2f"%self.__area

def randShape():
    # Generate a list of 10 random shapes (Circle, Square, or Cube)
    shapeObj = []
    for i in range(10):
        randomPick = random.randint(0, 2)
        #check the value of randomPick to see what shape
        if randomPick == 0:
            shapeObj.append(Circle())
        elif randomPick == 1:
            shapeObj.append(Square())
        else:
            shapeObj.append(Cube())

    return shapeObj

def main():
    choice = 0

    while choice != 4:
        print("Welcome to my Shape Generator!")
        print()
        print("Please select which option to run the program:")
        print("1. Save the results to a file")
        print("2. Print the Results on screen")
        print("3. Display the results inside a GUI window")
        print("4. Exit")
        choice = int(input("Enter your choice: "))

        shapes = randShape()

        if choice == 2:
            for shape in shapes:
                print(shape.displayInfo())
        elif choice == 1:
            filename = input("Enter the file name: ")
            outfile = open(filename, 'w')
            for shape in shapes:
                outfile.write(f"{shape.displayInfo()}\n")
            outfile.close()
            print("Results saved to file.")
        elif choice == 3:
            #create window
            window = tk.Tk()
            window.geometry('400x400')
            window.title("GUI Results")

            text = tk.Text(window)
            text.pack()

            for shape in shapes:
                text.insert(tk.END, f"{shape.displayInfo()}\n")

            window.mainloop()
        elif choice == 4:
            print("Bye! Terminating program")
        else:
            print("Invalid choice.")


main()
