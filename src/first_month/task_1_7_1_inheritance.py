from task_1_5_1_oop_money_class import Money


class Person:
    def __init__(self, name: str, surname: str, age: int, gender: str):
        self.__name = name
        self.__surname = surname
        self.__age = age
        self.__gender = gender

    def get_name(self):
        return self.__name

    def get_surname(self):
        return self.__surname

    def get_age(self):
        return self.__age

    def get_gender(self):
        return self.__gender

    def set_name(self, x):
        if type(x) == 'str':
            self.__name = x
        else:
            print("Type of name must be str")

    def set_surname(self, x):
        if type(x) == 'str':
            self.__surname = x
        else:
            print("Type of surname must be str")

    def set_age(self, x):
        if type(x) == 'int' and age > 0:
            self.__age = x
        else:
            print("Type of age must be positive int")

    def set_gender(self, x):
        if x == "Male" or x == "Female":
            self.__gender = x
        else:
            print("Gender must be Male or Female")

    def __repr__(self):
        return "{} {} - {}, {} years old".format(self.__name, self.__surname, self.__gender, self.__age)


class Student(Person):
    def __init__(self, name: str, surname: str, age: int, gender: str, university: str, faculty: str, course: int,
                 middle_score: int):
        super().__init__(name, surname, age, gender)
        self.__university = university
        self.__faculty = faculty
        self.__course = course
        self.__middle_score = middle_score

    def __repr__(self):
        return super().__repr__() + ", {} - {},{}, {}".format(self.__university, self.__faculty, self.__course,
                                                              self.__middle_score)

    def get_score(self):
        return self.__middle_score

    def get_course(self):
        return self.__course

    def get_faculty(self):
        return self.__faculty

    def get_university(self):
        return self.__university

    def set_score(self, x):
        if type(x) == 'int':
            self.__middle_score = x
        else:
            print("Type of score must be int")

    def set_course(self, x):
        if type(x) == 'int':
            self.__course = x
        else:
            print("Type of course must be int")

    def set_faculty(self, x):
        if type(x) == 'str':
            self.__faculty = x
        else:
            print("Type of faculty must be str")

    def set_university(self, x):
        if type(x) == 'str':
            self.__university = x
        else:
            print("Type of university must be str")


class Teacher(Person):
    def __init__(self, name: str, surname: str, age: int, gender: str, university: str, faculty: str, discipline: str,
                 experience: int, salary: Money):
        super().__init__(name, surname, age, gender)
        self.__university = university
        self.__faculty = faculty
        self.__discipline = discipline
        self.__experience = experience
        self.__salary = salary

    def __repr__(self):
        return super().__repr__() + ", {} - {},{}, {} years experience, salary - {}".format(self.__university,
                                                                                            self.__faculty,
                                                                                            self.__discipline,
                                                                                            self.__experience,
                                                                                            self.__salary)

    def get_discipline(self):
        return self.__discipline

    def get_faculty(self):
        return self.__faculty

    def get_university(self):
        return self.__university

    def get_experience(self):
        return self.__experience

    def get_salary(self):
        return self.__salary

    def set_discipline(self, x):
        if type(x) == 'str':
            self.__discipline = x
        else:
            print("Type of discipline must be str")

    def set_faculty(self, x):
        if type(x) == 'str':
            self.__faculty = x
        else:
            print("Type of faculty must be str")

    def set_university(self, x):
        if type(x) == 'str':
            self.__university = x
        else:
            print("Type of university must be str")

    def set_experience(self, x):
        if type(x) == 'int':
            self.__experience = x
        else:
            print("Type of experience must be int")

    def set_salary(self, x):
        if type(x) == '__main__.Money':
            self.__salary = x
        else:
            "Type of salary must be __main__.Money"


t = Teacher("John", "Brown", 50, "Male", "YSU", "Mathematics", "MA", 20, Money(2000, "USD"))
t.set_salary(Money(5000, "USD"))
print(t)
s = Student("Nune", "Tonoyan", 30, "Female", "YSU", "Economics", 3, 5)
print(s)
