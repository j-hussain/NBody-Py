from Particle import *
import pygame as pg
from Constants import *

def render():

    pg.init()
    window = pg.display.set_mode((WIDTH, HEIGHT))

    particles = []
    keys = {
        pg.K_KP_MINUS: False,
        pg.K_KP_PLUS: False,
        pg.K_ESCAPE: False
    }

    for i in range(0, PARTICULATES):
        particles.append(Particle())

    zoom = 1.0

    while True:
        pg.display.flip()
        window.fill((0, 0, 0))
        window.lock()
        for particle in particles:
            if not particle._merged:
                # for the non-merged particles, draw a circle based on their radii
                # considering the zoom factor
                pg.draw.circle(window, (255, 255, 255),
                               (int(HWIDTH + zoom * HWIDTH * (particle._position[0] - HWIDTH) / HWIDTH),
                                int(HHEIGHT + zoom * HHEIGHT * (particle._position[1] - HHEIGHT) / HHEIGHT)),
                               int(particle._radius * zoom), 0)
        window.unlock()
        while True:
            # This block updates the state of whether a key has been pressed
            event = pg.event.poll()
            if event.type == pg.NOEVENT:
                break
            elif event.type in [pg.KEYDOWN, pg.KEYUP]:
                keys[event.key] = event.type == pg.KEYDOWN

        # Update the positions and speeds of the particles
        for p1 in particles:
            if p1._merged:
                continue
            p1._resetAcceleration()
            for p2 in particles:
                if p1 is p2 or p2._merged:
                    continue
                p1._updateAcceleration(p2)
            p1._updatePosition()

        # Conservation of total momentum; merge the particles that touch
        # using elastic collisions
        for p1 in particles:
            if p1._merged:
                continue
            for p2 in particles:
                if p1 is p2 or p2._merged:
                    continue
                if Particle._contact(p1, p2):
                    if p1._mass < p2._mass:
                        p1, p2 = p2, p1
                    p2._merged = True

                    p1._mass += p2._mass
                    p1._setRadius()
                    p1._newVelocity(p1, p2)

        if keys[pg.K_KP_PLUS]:
            zoom += 0.1
        if keys[pg.K_KP_MINUS]:
            zoom -= 0.1
        if keys[pg.K_ESCAPE]:
            break
        if event.type == pg.NOEVENT:
            pg.time.wait(10)