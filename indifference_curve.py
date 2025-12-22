import numpy as np 
import matplotlib.pyplot as plt 


# Indifference curve
alpha = 1/3
beta = 1/2

# U1 = sqrt(x1 * x2)
def indifference_curve_1(x1):
    U = 5
    return (U / (x1 ** alpha)) ** (1 / beta)

def indifference_curve_2(x1):
    U = 4
    return (U / (x1 ** alpha)) ** (1 / beta)

def indifference_curve_3(x1):
    U = 3
    return (U / (x1 ** alpha)) ** (1 / beta)

x1_1 = np.linspace(0.1, 40, num = 100)
x1_2 = np.linspace(0.1, 40, num = 100)
x1_3 = np.linspace(0.1, 40, num = 100)

indifference_1_x2 = indifference_curve_1(x1_1)
indifference_2_x2 = indifference_curve_2(x1_2)
indifference_3_x2 = indifference_curve_3(x1_3) 



plt.plot(x1_1, indifference_1_x2, label = r"$U(x_1, x_2) = 5$")
plt.plot(x1_2, indifference_2_x2, label = r"$U(x_1, x_2) = 4$")
plt.plot(x1_3, indifference_3_x2, label = r"$U(x_1, x_2) = 3$")

plt.xlabel(r"$x_1$")
plt.ylabel(r"$x_2$")


plt.xticks([])
plt.yticks([])
plt.xlim(0, 25)
plt.ylim(0, 25)
plt.legend()

plt.show() 

# import numpy as np
# import matplotlib.pyplot as plt

# # Utility levels
# U_levels = [4, 8, 10]

# colors = ['tab:blue', 'tab:orange', 'tab:green']

# plt.figure(figsize=(6, 6))

# for U, c in zip(U_levels, colors):
#     x1_h = np.linspace(U, 24, 200)
#     x2_h = np.full_like(x1_h, 2 * U)

#     x2_v = np.linspace(2 * U, 24, 200)
#     x1_v = np.full_like(x2_v, U)

#     plt.plot(x1_h, x2_h, color=c, linewidth=2)
#     plt.plot(x1_v, x2_v, color=c, linewidth=2, label=rf"$U = {U}$")


# # Ray of expansion
# x1_ray = np.linspace(0, 12, 200)
# x2_ray = 2 * x1_ray
# plt.plot(x1_ray, x2_ray, linestyle='--', linewidth=1.5, label=r"$x_2 = 2x_1$")

# plt.xlabel(r"$x_1$")
# plt.ylabel(r"$x_2$")

# plt.xticks([])
# plt.yticks([])
# plt.xlim(0, 25)
# plt.ylim(0, 25)
# plt.legend()

# plt.show()
