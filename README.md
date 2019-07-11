## Usage:
Particle creation depends on the `numpy` library for creating velocity and position vectors `v_i, p_i`, e.g. `v1_i = np.array([1,3,])`

e.g.
````python
proton   = Particle(charge, mass, v1_i, p1_i)
electron = Particle(charge, mass, v2_i, p2_i)
````

Movements of the particles are simulated over `t` time, incremented over `s` steps in `t`. By default, `s=1000` for 1000 iterations through `t`. For a "smoother" simulation, increase `s` with `t`.

e.g.
````python
sim = Simulation(proton, electron, t, s=1000)
sim.simulate()
````
