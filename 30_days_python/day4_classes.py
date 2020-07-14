class Person:
    def __init__(self, initialAge):
        if initialAge > 0:
            self.age = initialAge
        else:
            self.age = 0
            print('Age is not valid, setting age to 0.')
        # Add some more code to run some checks on initialAge

    def amIOld(self):
        if self.age < 13:
            print('You are young.')
        elif 13 <= self.age < 18:
            print('You are a teenager.')
        else:
            print('You are old.')
        # Do some computations in here and print out the correct statement to the console

    def yearPasses(self):
        self.age = self.age + 1
        # Increment the age of the person in here


t = int(input())
for i in range(0, t):
    age = int(input())
    p = Person(age)
    p.amIOld()
    for j in range(0, 3):
        p.yearPasses()
    p.amIOld()
    print("")


# 1. the lesson I learned in this day that first I need the self in front of the variables so ti can be passed from one
# method to another

# 2. the second lesson is how to handle the inputs. For example as I will see in the future, when we read the input form
# the stdin we are often given the first the T or the number of lines, often the variables that we need to read in this line
# as you could see above we achieve this by the line t = int(input()). Now, we use this in our loop , for i in range(0,t)
# but we we gonna do inside the for loop. O.K now we gonna read the following inputs age = int(input()), once we have that
# then we use it our main variable which is age to create instances from the class. What we do next, do we just go ahead and
# apply all the methods of the class. No we can go ahead and apply the first method directly but for the second one we need
# to loop and then apply it

# I think I also learned how to loop in creating classes.


