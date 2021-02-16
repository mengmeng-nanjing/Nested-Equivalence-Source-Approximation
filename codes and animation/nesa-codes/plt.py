import math
import random
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

class Spherical(object):

    def __init__(self, radial=1.0, polar=0.0, azimuthal=0.0):
        self.radial = radial
        self.polar = polar
        self.azimuthal = azimuthal

    def toCartesian1(self):
        r = math.sin(self.azimuthal) * self.radial
        x = math.cos(self.polar) * r
        y = math.sin(self.polar) * r
        z = math.cos(self.azimuthal) * self.radial
        x = x + 0.5
        y = y + 0.5
        z = z + 0.5
        return x, y, z
    def toCartesian2(self):
        r = math.sin(self.azimuthal) * self.radial
        x = math.cos(self.polar) * r
        y = math.sin(self.polar) * r
        z = math.cos(self.azimuthal) * self.radial
        x = x + 5.5
        y = y + 0.5
        z = z + 0.5
        return x, y, z


def splotxiao1(limit):
    s = Spherical(radial=0.5)
    n = int(math.ceil(math.sqrt((limit - 2) / 4)))
    azimuthal = 0.5 * math.pi / n
    for a in range(-n, n + 1):
        s.polar = 0
        size = (n - abs(a)) * 4 or 1
        polar = 2 * math.pi / size
        for i in range(size):
            yield s.toCartesian1()
            s.polar += polar
        s.azimuthal += azimuthal

def splotda1(limit):
    s = Spherical(radial=2)
    n = int(math.ceil(math.sqrt((limit - 2) / 4)))
    azimuthal = 0.5 * math.pi / n
    for a in range(-n, n + 1):
        s.polar = 0
        size = (n - abs(a)) * 4 or 1
        polar = 2 * math.pi / size
        for i in range(size):
            yield s.toCartesian1()
            s.polar += polar
        s.azimuthal += azimuthal

def splotxiao2(limit):
    s = Spherical(radial=0.5)
    n = int(math.ceil(math.sqrt((limit - 2) / 4)))
    azimuthal = 0.5 * math.pi / n
    for a in range(-n, n + 1):
        s.polar = 0
        size = (n - abs(a)) * 4 or 1
        polar = 2 * math.pi / size
        for i in range(size):
            yield s.toCartesian2()
            s.polar += polar
        s.azimuthal += azimuthal

def splotda2(limit):
    s = Spherical(radial=2)
    n = int(math.ceil(math.sqrt((limit - 2) / 4)))
    azimuthal = 0.5 * math.pi / n
    for a in range(-n, n + 1):
        s.polar = 0
        size = (n - abs(a)) * 4 or 1
        polar = 2 * math.pi / size
        for i in range(size):
            yield s.toCartesian2()
            s.polar += polar
        s.azimuthal += azimuthal

def green(dot, Dot):
    d = math.sqrt((dot[0] - Dot[0]) ** 2 + (dot[1] - Dot[1]) ** 2 + (dot[2] - Dot[2]) ** 2)
    f = 300 * 10 ** 6
    k = 2 * math.pi * f / (3 * 10 ** 8)
    green = (math.e ** (1j*(-k )*d))/d
    return green
def gnq(zft, qiu, n, q):
    g = np.zeros([n, q],dtype=complex)
    for i in range(n):
        for k in range(q):
            g[i][k] = green(zft[i], qiu[k])
    return g


q=int(input('输入q=2+4*n^2'))
n=100
qmxiao1 = np.zeros([q, 3])
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
i=0
for point in splotxiao1(q):
    # print("%f %f %f" % point)
    dot = [a for a in point]
    qmxiao1[i] = dot
    ax.scatter(dot[0], dot[1], dot[2], c='r')
    i += 1


qmda1 = np.zeros([q, 3])
i=0
for point in splotda1(q):
    # print("%f %f %f" % point)
    dot = [a for a in point]
    qmda1[i] = dot
    ax.scatter(dot[0], dot[1], dot[2], c='y')
    i+= 1
qmxiao2 = np.zeros([q, 3])
i=0
for point in splotxiao2(q):
    # print("%f %f %f" % point)
    dot = [a for a in point]
    qmxiao2[i] = dot
    ax.scatter(dot[0], dot[1], dot[2], c='r')
    i+=1
qmda2 = np.zeros([q, 3])
i=0
for point in splotda2(q):
    # print("%f %f %f" % point)
    dot = [a for a in point]
    qmda2[i] = dot
    ax.scatter(dot[0], dot[1], dot[2], c='y')
    i+=1

zft1 = np.zeros([n, 3])
for k in range(n):
    for i in range(2):
        a, b, c = random.random(), random.random(), random.random()
        zft1[k] = [a, b, c]
        ax.scatter(a, b, c, c='g')
zft2 = np.zeros([n, 3])
for k in range(n):
    for i in range(2):
        a, b, c = random.random(), random.random(), random.random()
        zft2[k] = [a+5, b, c]
        ax.scatter(a+5, b, c, c='g')
ax.set_xlabel('X Label')
ax.set_ylabel('Y Label')
ax.set_zlabel('Z Label')
plt.show()
#n = zft1.shape[0]
#q = qmxiao1.shape[0]
g1=gnq(zft1, qmda1, n, q)
g2=gnq(qmda1,qmxiao1,q,q)
g22=np.linalg.inv(g2)
u=np.dot(g1,g22)
g3=gnq(qmxiao1,qmxiao2,q,q)
g4=gnq(qmxiao2,qmda2,q,q)
g44=np.linalg.inv(g4)
g5=gnq(qmda2,zft2,q,n)
v=np.dot(g44,g5)
GG=np.dot(u,g3)
GGG=np.dot(GG,v)
G=gnq(zft1,zft2,n,n)
gjian=GGG-G
print(G[3])
print('---------------------------')
print(GGG[3])
print('---------------------------')
print(gjian[3])
