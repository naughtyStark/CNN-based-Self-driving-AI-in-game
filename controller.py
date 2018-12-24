import pyvjoy

j = pyvjoy.VJoyDevice(1)

def controller(steer,throttle):
    if steer >= 0:
        j.data.wAxisX = 22000 + 110*int(steer)
    elif steer < 0:
        j.data.wAxisX = 22000 + 220*int(steer)

    j.data.wAxisY = 16384 + int(163.84*throttle)
    j.update()
