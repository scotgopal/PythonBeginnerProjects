import matplotlib.pyplot as plt
import numpy as np

t1 = np.arange(-360,360,1)

plt.plot(t1,np.cos(np.deg2rad(t1)),label="Line One-Cosine")
plt.plot(t1,np.sin(np.deg2rad(t1)), label="Line Two-Sine")
plt.title("Project 3")
plt.ylabel("f(x)")
plt.xlabel("x, degrees")
plt.xticks(np.linspace(-360,360, num=5 ,endpoint=True))
plt.legend()
plt.show()