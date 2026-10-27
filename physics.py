import numpy as np


#constants
G = 6.67430e-11
M = 1.989e30 

# r is np.array
def acceleration(r):
    d = np.linalg.norm(r)
    a = -(G*M*r)/d**3
    return a

# r and v is np.array
def step(r, v, dt):
    new_v = v + acceleration(r)*dt
    new_r = r + new_v*dt
    return new_r, new_v

# creates array pos and vel over time 
def simulate(r0, v0, dt, n_steps):

    rs = np.zeros((n_steps + 1, 2))
    vs = np.zeros((n_steps + 1, 2))
    rs[0] = r0
    vs[0] = v0

    r, v = r0, v0

    for i in range(n_steps):
        r, v = step(r, v, dt)
        rs[i+1] = r
        vs[i+1] = v
    
    return rs, vs

# returns total energy (ke + pe)
def energy(r, v):
    d = np.linalg.norm(r)
    ke = (v**2)/2
    pe = -G*M/d
    return ke + pe

def angular_momentum(r, v):
    return r[0]*v[1] - v[0]*r[1] #cross product of r and v (both vectors)
