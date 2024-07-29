import matplotlib.pyplot as plt
import numpy as np

x_train = np.array(([10, 50], [20, 30], [25, 30], [20, 60], [15, 70], [40, 40], [40, 45], [20, 45], [40, 30], [7, 35]))
y_train = np.array(([-1, 1, 1, -1, -1, 1, 1, -1, 1, -1]))

n_train = len(x_train)
w = [0, -1]
a = lambda x: np.sign(x[0] * w[0] + x[1] * w[1])
N = 50
L = 0.1
e = 0.1

last_error_index = -1

for n in range(N):
    for i in range(n_train):
        if y_train[i] * a(x_train[i]) < 0:
            w[0] = w[0] + L * y_train[i]
            last_error_index = i

    Q = sum([1 for i in range(n_train) if y_train[i] * a(x_train[i]) < 0])
    if Q == 0:
        break
if last_error_index > - 1:
    w[0] = w[0] + e * y_train[last_error_index]

print(w)

line_x = list(range(max(x_train[:, 0])))
line_y = [w[0] * x for x in line_x]

x_0 = x_train[y_train == 1]
x_1 = x_train[y_train == - 1]
print("X0:", x_0, '\n', "X1:", x_1)

plt.scatter(x_0[:, 0], x_0[:, 1], color='red')
plt.scatter(x_1[:, 0], x_1[:, 1], color='blue')
plt.plot(line_x, line_y, color='green')

plt.xlim([0, 45])
plt.ylim([0, 75])
plt.ylabel('Длина')
plt.xlabel('Ширина')
plt.grid(True)
plt.show()
