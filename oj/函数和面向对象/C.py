class Vector:
    x, y, z = 0, 0, 0

    def __init__(self, _x, _y, _z):
        self.x = _x
        self.y = _y
        self.z = _z

    def add(self, v):
        self.x += v.x
        self.y += v.y
        self.z += v.z
    
    def sub(self, v):
        self.x -= v.x
        self.y -= v.y
        self.z -= v.z

    def mul(self, num):
        self.x *= num
        self.y *= num
        self.z *= num
    
    def div(self, num):
        self.x /= num
        self.y /= num
        self.z /= num

    def get_length(self):
        return (self.x ** 2 + self.y ** 2 + self.z ** 2) ** 0.5


str1 = input().split()
x = eval(str1[0])
y = eval(str1[1])
z = eval(str1[2])
v1 = Vector(x, y, z)
str1 = input().split()
x = eval(str1[0])
y = eval(str1[1])
z = eval(str1[2])
v2 = Vector(x, y, z)
str1 = input()
if (str1 == "add"):
    v1.add(v2)
    print(str(v1.x) + " " + str(v1.y) + " " + str(v1.z), end="")
elif (str1 == "sub"):
    v1.sub(v2)
    print(str(v1.x) + " " + str(v1.y) + " " + str(v1.z), end="")
elif (str1 == "get_length"):
    length = v1.get_length()
    print("%.2f" % length, end="")
else:
    num = eval(input())
    if (str1 == "mul"):
        v1.mul(num)
        print(str(v1.x) + " " + str(v1.y) + " " + str(v1.z), end="")
    else:
        v1.div(num)
        print("%.2f" % v1.x, end=" ")
        print("%.2f" % v1.y, end=" ")
        print("%.2f" % v1.z, end="")
