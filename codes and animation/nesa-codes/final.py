import math
import random
import numpy as np

#定义了第一个球面类
class Spherical(object):
#初始化默认值设定
    def __init__(self, radial=1.0, polar=0.0, azimuthal=0.0):
        self.radial = radial
        self.polar = polar
        self.azimuthal = azimuthal
#位置1处的球。由求坐标系返回直角坐标系
    def toCartesian1(self):
        r = math.sin(self.azimuthal) * self.radial
        x = math.cos(self.polar) * r
        y = math.sin(self.polar) * r
        z = math.cos(self.azimuthal) * self.radial
        x = x + 0.5
        y = y + 0.5
        z = z + 0.5
        return x, y, z
#位置2处的球。由求坐标系返回直角坐标系（默认两球心距离为5）
    def toCartesian2(self):
        r = math.sin(self.azimuthal) * self.radial
        x = math.cos(self.polar) * r
        y = math.sin(self.polar) * r
        z = math.cos(self.azimuthal) * self.radial
        x = x + 5.5
        y = y + 0.5
        z = z + 0.5
        return x, y, z
#输入点数q，均匀分布在位置1处小球面上
def splotxiao1(limit):
    s = Spherical(radial=rin)#传递内部小球半径参数
    # #将整个球面分为2n个维度（一条经线包含2n个点），每条纬线点数排除两极点由0增加到4n（道包含了4n个点），可算出球面总点数为4*n^2+2
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
#输入点数Q，均匀分布在位置1处大球面上
def splotda1(limit):
    s = Spherical(radial=rout)
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
#输入点数q，均匀分布在位置2处小球面上
def splotxiao2(limit):
    s = Spherical(radial=rin)
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
#输入点数Q，均匀分布在位置2处小球面上
def splotda2(limit):
    s = Spherical(radial=rout)
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
#计算格林公式，输入两个点的直角坐标，输出其格林公式的值
def green(dot, Dot):
    d = math.sqrt((dot[0] - Dot[0]) ** 2 + (dot[1] - Dot[1]) ** 2 + (dot[2] - Dot[2]) ** 2)
    f = 300 * 10 ** 6
    k = 2 * math.pi * f / (3 * 10 ** 8)
    green = (math.e ** (1j*(-k )*d))/d
    return green
#输入两个点阵，计算每对点的格林公式值，构建输出格林值的矩阵
def gnq(zftr, qiur, nr, qr):
    g = np.zeros([nr, qr],dtype=complex)
    for i in range(nr):
        for k in range(qr):
            g[i][k] = green(zftr[i], qiur[k])
    return g
#计算误差
def erro(m1,m2):
    nmG = np.linalg.norm(m1)
    dif=m2-m1
    nmdif = np.linalg.norm(dif)
    erro = nmdif / nmG
    return erro





q=int(input('输入小球面点数：q=2+4*m^2'))
Q=int(input('输入大球面点数：Q=2+4*m^2'))
n=int(input('输入正方体点数：n='))
#大小球的半径赋值
rin=0.866
rout=2
#构建位置1处小球面点坐标，放入qmxiao1这个数组（q个点，每个点有x，y，z这3个维度的数值）。下同
qmxiao1 = np.zeros([q, 3])
i=0
for point in splotxiao1(q):
    # print("%f %f %f" % point)
    dot = [a for a in point]
    qmxiao1[i] = dot
    i += 1

qmda1 = np.zeros([Q, 3])
i=0
for point in splotda1(Q):
    # print("%f %f %f" % point)
    dot = [a for a in point]
    qmda1[i] = dot
    i+= 1
qmxiao2 = np.zeros([q, 3])
i=0
for point in splotxiao2(q):
    # print("%f %f %f" % point)
    dot = [a for a in point]
    qmxiao2[i] = dot
    i+=1
qmda2 = np.zeros([Q, 3])
i=0
for point in splotda2(Q):
    # print("%f %f %f" % point)
    dot = [a for a in point]
    qmda2[i] = dot
    i+=1
#构建位置1处正方体坐标，放入zft1这个数组（n个点，每个点有x，y，z这3个维度的数值）。下同
zft1 = np.zeros([n, 3])
for k in range(n):
    for i in range(2):
        a, b, c = random.random(), random.random(), random.random()
        zft1[k] = [a, b, c]
zft2 = np.zeros([n, 3])
for k in range(n):
    for i in range(2):
        a, b, c = random.random(), random.random(), random.random()
        zft2[k] = [a+5, b, c]
#由函数gnq生成两点阵对应的格林值矩阵，并依次相乘验证
g1=gnq(zft1, qmda1, n, Q)#正方体1到大球面1
g2=gnq(qmxiao1,qmda1,q,Q)#大球面1到小球面1
g22=np.linalg.pinv(g2)#矩阵求逆
u=np.dot(g1,g22)#矩阵点乘得到矩阵 u
g3=gnq(qmxiao1,qmxiao2,q,q)#小球面1到小球面2，即矩阵 D
g4=gnq(qmda2,qmxiao2,Q,q)#小球面2到大球面2
g44=np.linalg.pinv(g4)#求逆
g5=gnq(qmda2,zft2,Q,n)#大球面2到正方体2
v=np.dot(g44,g5)#矩阵点乘得到矩阵 V
GG=np.dot(u,g3)#矩阵 u*D
GGG=np.dot(GG,v)#矩阵 U*D*v
G=gnq(zft1,zft2,n,n)#两正方体直接作用

print('---------------------------')
print('两正方体直接作用时的矩阵：','\n',G[11])
print('---------------------------')
print('算法优化后计算得到的矩阵：','\n',GGG[11])
print('---------------------------')
print('平均二范数相对误差：',erro(G,GGG))
