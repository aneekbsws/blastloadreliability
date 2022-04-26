def blast(r, w):
    z = float(r) / (float(w) ** (1.0 / 3.0))
    z = round(z, 4)
    po = ((1772 / z ** 3) - (114 / z ** 2) + (108 / z)) / 1000

    return round(po, 4)


w = input('Enter TNT equivalent weight in kg:')
import array as arr
import matplotlib.pyplot as plt

c = 1.83
b = arr.array('d', [])
x = 0
for i in range(1, 1000, 1):
    b.append(x)
    x += 0.01

a = arr.array('d', [])
y = 0
for i in range(1, 1000, 1):
    t = ((y ** 2) + (c ** 2)) ** 0.5
    e = blast(t, w)
    a.append(e)
    y += 0.01
plt.plot(b, a, color='r')
plt.xlabel("Stand-off distance in metres")
plt.ylabel("Peak over-pressure in MPa")
plt.show()
