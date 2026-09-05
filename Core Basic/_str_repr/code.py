# class Room:
#     length = 0
#     breadth = 0
#     def __int__(self, length, breadth):
#         self.length = length
#         self.breadth = breadth

#     def __str_(self):
#         return f"Length = {self.length} Breadth = {self.breadth}"

#     def __int__(self):
#         return f"Length = {self.length} Breadth = {self.breadth}"

# dining_room = Room(20, 15)
# print(str(dining_room))
# print(int(dining_room))


class Animal:

    def __str__(self):
        return "This is an Animal"

    def display(self):
        print(self.__str__())


animal = Animal()
animal.display()