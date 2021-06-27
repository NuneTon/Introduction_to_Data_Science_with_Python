class Room:
    def __init__(self, type, count):
        self.__type = type
        self.__count = count

    def get_type(self):
        return self.__type

    def get_count(self):
        return self.__count

    def set_count(self, x):
        if type(x) == int:
            self.__count += x
        else:
            print("Type of count must be integer")

    def reserve(self, x):
        if self.__count - x >= 0:
            self.__count -= x

    def checkout(self, x):
        self.__count += x

    def __repr__(self):
        return "There are {} {} rooms available ".format(self.get_count(), self.get_type())


class Hotel():
    def __init__(self, name):
        self.__name = name
        self.__rater_count = 0
        self.__rooms = []
        self.__rate = 0
        self.__rating=0

    def get_rating(self):
        return self.__rating

    def rate(self, x):
        if type(x) == int and self.__rater_count > 0:
            self.__rate += x
            self.__rater_count += 1
            self.__rating = self.__rate / self.__rater_count
        else:
            print("Rate with integer numbers")



    def get_rooms(self):
        return self.__rooms

    def reserve(self, type, count):
        for r in self.__rooms:
            if r.get_type() == type:
                r.reserve(count)

    def checkout(self, type, count):
        for r in self.__rooms:
            if r.get_type() == type:
                r.checkout(count)

    def add_room(self, room):  # room is object
        self.__rooms.append(room)
        # for r in self.__rooms:
        #     if r.get_type() == room.get_type():
        #         r.set_count(room.get_count())
        #     else:
        #         self.__rooms.append(room)
        # print(self.__rooms)

    def remove_room(self, room):
        self.__rooms.remove(room)


r1 = Room("Single", 8)
r2 = Room("Penthouse", 5)
r2.checkout(1)
r1.set_count("second_month")
r1.reserve(3)
print(r2)
print(r1)
h = Hotel("Sunrise")
h.rate(20)
h.rate(2)
print(h.get_rating())
r3 = Room("Single", 5)
r4 = Room("Luxe", 3)
h.add_room(r3)
h.add_room(r4)
h.reserve("Single", 2)
h.reserve("Luxe", 1)
h.checkout("Luxe", 1)
h.remove_room(r4)
h.get_rooms()
