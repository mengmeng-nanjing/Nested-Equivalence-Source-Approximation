import math
import random
import numpy as np
import matplotlib.pyplot as plt

fig = plt.figure()

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
    s = Spherical(radial=0.866)
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
    s = Spherical(radial=0.866)
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
    green = (math.e ** (1j * (-k) * d)) / d
    return green


def gnq(zftr, qiur, nr, qr):
    g = np.zeros([nr, qr], dtype=complex)
    for i in range(nr):
        for k in range(qr):
            g[i][k] = green(zftr[i], qiur[k])
    return g


def erro(m1, m2):
    nmG = np.linalg.norm(m1)
    dif = m2 - m1
    nmdif = np.linalg.norm(dif)
    erro = nmdif / nmG
    return erro

'''
q = int(input('输入小球面点np.zeros([q, 3])数：q=2+4*m^2'))
Q = int(input('输入大球面点数：Q=2+4*m^2'))
n = int(input('输入正方体点数：n='))
'''
ql=[]
for i in range(0,10):
    ql.append(2+4*(i+1)**2)
Ql=[]
for i in range(0,10):
    Ql.append(2+4*(i+1)**2)
errol=[]
errolln=[]
n=100


for i in range(10):
    q = ql[i]
    Q = Ql[i]

    qmxiao1 = np.zeros([q, 3])
    i = 0
    for point in splotxiao1(q):
        # print("%f %f %f" % point)
        dot = [a for a in point]
        qmxiao1[i] = dot
        i += 1
    print('点数：' + str(i))

    qmda1 = np.zeros([Q, 3])
    i = 0
    for point in splotda1(Q):
        # print("%f %f %f" % point)
        dot = [a for a in point]
        qmda1[i] = dot
        i += 1
    qmxiao2 = np.zeros([q, 3])
    i = 0
    for point in splotxiao2(q):
        # print("%f %f %f" % point)
        dot = [a for a in point]
        qmxiao2[i] = dot
        i += 1
    qmda2 = np.zeros([Q, 3])
    i = 0
    for point in splotda2(Q):
        # print("%f %f %f" % point)
        dot = [a for a in point]
        qmda2[i] = dot
        i += 1

    zft1 = np.zeros([n, 3])
    for k in range(n):
        for i in range(2):
            a, b, c = random.random(), random.random(), random.random()
            zft1[k] = [a, b, c]
    zft2 = np.zeros([n, 3])
    for k in range(n):
        for i in range(2):
            a, b, c = random.random(), random.random(), random.random()
            zft2[k] = [a + 5, b, c]

    g1 = gnq(zft1, qmda1, n, Q)
    g2 = gnq(qmxiao1, qmda1, q, Q)
    g22 = np.linalg.pinv(g2)
    u = np.dot(g1, g22)
    g3 = gnq(qmxiao1, qmxiao2, q, q)
    g4 = gnq(qmda2, qmxiao2, Q, q)
    g44 = np.linalg.pinv(g4)
    g5 = gnq(qmda2, zft2, Q, n)
    v = np.dot(g44, g5)
    GG = np.dot(u, g3)
    GGG = np.dot(GG, v)
    G = gnq(zft1, zft2, n, n)
    print(erro(G,GGG))
    errolln.append(math.log10(erro(G,GGG)))

    errol.append(erro(G,GGG))
plt.subplot(211)
plt.plot(ql,errolln)
plt.xlabel('q')
plt.ylabel('lg(erro)')
plt.subplot(212)
plt.plot(Ql,errolln)
plt.xlabel('Q')
plt.ylabel('lg(erro)')
plt.show()




