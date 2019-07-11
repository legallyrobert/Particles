## Usage:
Particle creation depends on the `numpy` library for creating velocity and position vectors `v_i, p_i`, e.g. `v1_i = np.array([1,3])`

e.g.
````python
proton   = Particle(charge, mass, v1_i, p1_i)
electron = Particle(charge, mass, v2_i, p2_i)
````

Movements of the particles are simulated over `t` time, incremented over `s` steps in `t`. By default, `s=t*1000` for a relatively high resolution.

e.g.
````python
sim = Simulation(proton, electron, t, s=t*1000)
sim.simulate()
````
