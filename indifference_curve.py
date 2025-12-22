import numpy as np 
import matplotlib.pyplot as plt 


# Indifference curve

# U1 = sqrt(x1 * x2)
def indifference_curve_1(x1):
    return (20/x1) + 3

def indifference_curve_2(x1):
    return (45/x1**2)

x1 = np.linspace(1, 5, num = 100)
y = np.linspace(1, 5, num = 100)

indifference_1_x2 = indifference_curve_1(x1)
indifference_2_x2 = indifference_curve_2(x1)

A_x = 1.777
A_y = indifference_curve_1(1.777)

B_x = 1.5
B_y = indifference_curve_1(1.5)

C_x = 2.5
C_y = indifference_curve_2(2.5)

plt.plot(x1, indifference_1_x2, label = f"Indifference Curve #1")
plt.plot(x1, indifference_2_x2, label = f"Indifference Curve #2")

plt.xlabel(r"$x_1$")
plt.ylabel(r"$x_2$")

plt.plot(A_x, A_y, marker='o', ls='None', color='tab:green')
plt.plot(B_x, B_y, marker='o', ls='None', color='tab:red')
plt.plot(C_x, C_y, marker='o', ls='None', color='tab:purple')

plt.text(A_x, A_y, "  A", fontsize=12, ha='left', va='center', fontweight='bold')
plt.text(B_x, B_y, "  B", fontsize=12, ha='left', va='center', fontweight='bold')
plt.text(C_x, C_y, "  C", fontsize=12, ha='left', va='center', fontweight='bold')


plt.xticks([])
plt.yticks([])

plt.legend()

plt.show() 