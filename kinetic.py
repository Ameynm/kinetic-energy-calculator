def Kinetic_Energy(mass, velocity):
    ke = (0.5*(mass)*(velocity**2))
    return print("kinetic energy is " + str(ke))

mass = int(input("enter mass Kg:"))
velocity = int(input("enter velovity m/s:"))
Kinetic_Energy(mass,velocity)
