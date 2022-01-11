def velocity_calculator(a):
    def get_velocity(u, t):
        v = u+a*t
        print(v)
    return get_velocity

velocity_earth = velocity_calculator(9.8)
velocity_moon = velocity_calculator(1.625)

velocity_earth(0, 2)
velocity_moon(0, 2)