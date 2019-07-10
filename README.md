# Particles
### A 2-body particle simulation

## Usage:
Particle creation depends on the `numpy` library for velocity and position vectors `v_i, p_i`, e.g. `v1_i = np.array([3,1,-2])`

````python
p1  = Particle(charge, mass, v1_i, p1_i)
p1  = Particle(charge, mass, v2_i, p2_i)
````

Movements of the particles are simulated over `t` time, incremented over `s` steps in `t`. By default, `s=1000` for 1000 iterations through `t`. For a "smoother" simulation, increase `s` with `t`.

````python
sim = Simulation(p1, p2, t[,s=1000])
````
