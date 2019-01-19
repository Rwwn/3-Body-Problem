from visual import *

#Initial conditions

G = 6.674*10**-11 #Gravitational constant
dt = 10 #Time increments in seconds. Lower gives better accuracy, but a slower simulation
m1 = 2000 #Mass of typical artificial satellite in kg (negligible compared to the others)
m2 = 5.972*10**24 #Mass of the Earth in kg
m3 = 7.348*10**22 #Mass of the Moon in kg
p1 = vector(1.923*10**8, -3.329*10**8, 0) #Satellite displacement from Earth in m
p2 = vector(0, 0, 0) #Take the Earth as the stationary reference point
p3 = vector(3.84*10**8, 0, 0) #Moon displacement from Earth in m
v1 = vector(900, 500, 0) #Satellite orbital velocity in m/s
v2 = vector(0, 0, 0) #Earth taken as stationary
v3 = vector(0, 1022, 0) #Moon's velocity relative to Earth in m/s

#Creating the visualisation

r1 = 1000000 #Satellite radius set very large so it is visible in the animation, has no effect on the physics
r2 = 6371000 #Earth radius in m
r3 = 1737000 #Moon radius in m
scene.width = 1000
scene.height = 1000
scene.title = 'Earth, Moon, Satellite system'
P1 = sphere(pos = p1, radius = r1, color = color.red) #Satellite
P2 = sphere(pos = p2, radius = r2, color = color.green) #Earth
P3 = sphere(pos = p3, radius = r3, color = color.blue) #Moon
P1.trail = curve(color = color.orange)
P2.trail = curve(color = color.green)
P3.trail = curve(color = color.cyan)

#Now for the physics

def gravity(p, p_m, m): #Newton's law of gravitation for two bodies
    r = p - p_m
    a = (-G*m/(mag(r)**2)) * norm(r)
    return a

n=0 #n counts the iterations. Making it higher just makes the simulation last longer.
while n < 1000000: #Could be replaced by 'while True' to simulate indefinitely
    n = n + 1

    a1 = gravity(P1.pos, P2.pos, m2) + gravity(P1.pos, P3.pos, m3) #Combining acceleration due to both other bodies
    a2 = gravity(P2.pos, P1.pos, m1) + gravity(P2.pos, P3.pos, m3)
    a3 = gravity(P3.pos, P2.pos, m2) + gravity(P3.pos, P1.pos, m1)
    
    v1 = v1 + a1*dt #Euler's method; calculating velocity and position in for each time increment
    v2 = v2 + a2*dt
    v3 = v3 + a3*dt
    
    dp1 = v1*dt
    dp2 = v2*dt
    dp3 = v3*dt
    
    P1.pos = P1.pos + dp1 #Updates positions of bodies
    P1.trail.append(pos=P1.pos) #And saves the position for displaying the trail
    P2.pos = P2.pos + dp2
    P2.trail.append(pos=P2.pos)
    P3.pos = P3.pos + dp3
    P3.trail.append(pos=P3.pos)
    scene.center = P2.pos 
