class Animals:
    species = 'living organisms'

    def __init__(self, name, type, age):
        self.name = name
        self.type = type
        self.age = int(age)

    def say(self,):
        print(" mew mew mew", self.name)


Uno = Animals('Una', 'lubimka', 6)
Pipa = Animals('Pipa', 'milashka', 3)

print(Uno.__dict__)
print(Pipa.__dict__)
Pipa.say()
Uno.say()
# class Person:
#     name = 'Сергей Балакирев'
#     job = 'Программист'
#     city = 'Москва'


# p1 = Person()
# if getattr(p1, 'job', False):
#     print(True)
# else:
#     print(False)
# Патерн Моносостояния
# class ThreadData:
#     __shared_attrs = {
#         'name': ' thread_1',
#         'data': {},
#         'id': 1
#     }

#     def __init__(self):
#         self.__dict__ = self.__shared_attrs


# th1 = ThreadData()
# th2 = ThreadData()
# th2.id = 43
# print(th1.id, )

# print(id(th1), id(th2))
# # Патерн проектирования Singleton   (только 1 экземпляр класса)
# class DataBase:
#     __instance = None

#     def __new__(cls, *args, **kwargs):
#         if cls.__instance is None:
#             cls.__instance = super().__new__(cls)
#         return cls.__instance

#     def __del__(self):
#         DataBase.__instance = None

#     def __init__(self, user, psw, port):
#         self.user = user
#         self.psw = psw
#         self.port = port

#     def connect(self):
#         print(f"connection with BD: {self.user}, {self.psw}, {self.port}")

#     def close(self):
#         print("close the connection with BD")

#     def read(self):
#         return ("data for BD")

#     def write(self, data):
#         print(f"write to BD {data}")


# db = DataBase('root', '1234', 80)
# print(id(db))
# print(db.connect())
# db.__del__()
# db.write('dsf')
# db2 = DataBase('root2', '1234', 30)

# print(id(db), id(db2))
# print(db.connect(), db2.connect())

# class Point:
#     "Class for representing coordinates of points on a plane"
#     collor = 'red'
#     circle = 2

#     def __new__(cls, *args, **kwargs):
#         print("call __new__ for: " + str(cls))
#         return super().__new__(cls)

#     def __init__(self, x=0, y=0):
#         print("call __init__ for: " + str(self))
#         self.x = x
#         self.y = y

#     # def __del__(self):
#     #     print("deleting a result: " + str(self))

#     # def set_coords(self, x, y):
#     #     self.x = x
#     #     self.y = y

#     # def get_coords(self):
#     #     return (self.x, self.y)


# pt = Point(1, 2)
# print(pt)

# pt2 = Point()
# pt2.set_coords(34, 23)
# pt.set_coords(12, 23)
# print(pt.__dict__)
# print(pt2.__dict__)
# print(pt.get_coords())
# f = getattr(pt, 'get_coords')
# print(f())
