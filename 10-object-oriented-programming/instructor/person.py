class Person:
    """ A class that represents a human being """

    def __init__(self, fname, lname, x, y):
        self.first_name = fname
        self.last_name = lname
        self.x_position = x
        self.y_position = y


    def __str__(self):
        return "Person object: {} positioned at {}, {}".format(self.full_name(),
                                                               self.x_position, 
                                                               self.y_position)

    def full_name(self):
        return "{} {}".format(self.first_name, self.last_name)

    def move(self, direction):
        if direction == 'N':
            self.y_position += 1
        elif direction == 'S':
            self.y_position -= 1
        elif direction == 'E':
            self.x_position += 1
        elif direction == 'W':
            self.x_position -= 1


betty = Person("Betty", "Li", 0, 0)
print(betty)
betty.move('N')
betty.move('N')
betty.move('N')
print(betty)

natalie = Person("Natalie", "Black", 1, 1)
print(natalie)
natalie.move('W')
natalie.move('S')
print(natalie)





