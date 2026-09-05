# class Bike:
#     name = "" // atribute
#     gear = 0

# plusar = Bike() // object 

# plusar.name = "Pulsar 180"
# plusar.gear = 5
# # print(plusar.name)
# # print(plusar.gear)





class Room:
    length = 0
    breadth = 0
    height = 0

    def volume(self):
        print(f"Volume of Room is = {self.length * self.breadth * self.height}")
dining_room = Room()
dining_room.length = 20
dining_room.breadth = 15
dining_room.height = 10
dining_room.volume()