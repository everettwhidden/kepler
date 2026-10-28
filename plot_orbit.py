from physics import simulate, energy, angular_momentum
import matplotlib.pyplot as plt
import numpy as np

r0 = np.array([1.471e11, 0.0])
v0 = np.array([0.0, 30290.0])
dt = 3600
n_steps = 8766

rs, vs = simulate(r0, v0, dt, n_steps)

plt.plot(rs[:,0], rs[:,1])
plt.plot(0, 0, 'yo')
plt.axis("equal")
plt.xlabel("x (m)")
plt.ylabel("y (m)")
plt.title("Earth Orbit")
plt.show()
