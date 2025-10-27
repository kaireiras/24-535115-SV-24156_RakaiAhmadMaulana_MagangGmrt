import math
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

def fk_3d(l1, l2, l3, theta1, theta2, theta3):
    #ubah ke radian
    t1, t2, t3 = map(math.radians, [theta1, theta2, theta3])

    #titik awalnya
    x0, y0, z0 = 0, 0, 0

    #pusat (coxa)
    x1 = 0
    y1 = 0
    z1 = 0

    #femur
    x2 = l1 * math.cos(t2) * math.cos(t1)
    y2 = l1 * math.cos(t2) * math.sin(t1)
    z2 = l1 * math.sin(t2)

    #tibia
    x3 = x2 + l2 * math.cos(t2 + t3) * math.cos(t1)
    y3 = y2 + l2 * math.cos(t2 + t3) * math.sin(t1)
    z3 = z2 + l2 * math.sin(t2 + t3)

    return [x0, x2, x3], [y0, y2, y3], [z0, z2, z3]

l1 = float(input("panjang femur: "))
l2 = float(input("panjang tibia: "))
l3 = 0  #sesuai soal, coxa dianggap 0

theta1 = float(input("sudut servo 1: "))
theta2 = float(input("sudut servo 2: "))
theta3 = float(input("sudut servo 3: "))

x, y, z = fk_3d(l1, l2, l3, theta1, theta2, theta3)

print(f"ujung kaki robot: X={x[-1]:.2f}, Y={y[-1]:.2f}, Z={z[-1]:.2f}")

#visualisasi
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

ax.plot(x, y, z, '-o', linewidth=3, markersize=8)
ax.set_title('visualisasi fk3dof', fontsize=12)
ax.set_xlabel('X-axis')
ax.set_ylabel('Y-axis')
ax.set_zlabel('Z-axis')
ax.set_box_aspect([1,1,1])
ax.grid(True)
plt.show()
