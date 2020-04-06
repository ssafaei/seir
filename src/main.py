import opencor as oc

# Open and run a 300-day simulation using the SEIR model.

simulation = oc.open_simulation(
    'https://models.physiomeproject.org/workspace/5d4/rawfile/b973009caf430b1636cfd1133a23bfd570a85691/COVIDSim.cellml')

simulation.data().set_ending_point(300)

simulation.reset() # In case another simulation had already been run.
simulation.run()

# Retrieve the results of the simulation.

results = simulation.results()

voi = results.voi()
states = results.states()
algebraic = results.algebraic()

S = states['main/S']
E = states['main/E']
P = states['main/P']
I_t = states['main/I_t']
I_u = states['main/I_u']
R_t = states['main/R_t']
R_u = states['main/R_u']

I = algebraic['main/I']
R = algebraic['main/R']
D = algebraic['main/D']
IFR = algebraic['main/IFR']

# Plot the results.

import matplotlib.pyplot as plt

plt.clf() # In case there is already a Matplotlib window.

plt.subplot(4, 1, 1)
plt.title('SEIR model')
plt.plot(voi.values(), S.values(), label=S.name())
plt.plot(voi.values(), E.values(), label=E.name())
plt.plot(voi.values(), P.values(), label=P.name())
plt.plot(voi.values(), I.values(), label=I.name())
plt.plot(voi.values(), R.values(), label=R.name())
plt.plot(voi.values(), D.values(), label=D.name())
plt.legend(loc='center left')

plt.subplot(4, 1, 2)
plt.plot(voi.values(), I.values(), label=I.name())
plt.plot(voi.values(), I_t.values(), label=I_t.name())
plt.plot(voi.values(), I_u.values(), label=I_u.name())
plt.legend(loc='center left')

plt.subplot(4, 1, 3)
plt.plot(voi.values(), R.values(), label=R.name())
plt.plot(voi.values(), R_t.values(), label=R_t.name())
plt.plot(voi.values(), R_u.values(), label=R_u.name())
plt.legend(loc='center left')

plt.subplot(4, 1, 4)
plt.plot(voi.values(), IFR.values(), label=IFR.name())
plt.legend(loc='center left')
plt.xlabel('time (day)')

plt.show()