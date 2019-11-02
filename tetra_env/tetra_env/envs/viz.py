import pygame
from numpy import array
from math import cos, sin
from itertools import combinations
from rubix import Tetra, Color, Dir

######################
#                    #
#    math section    #
#                    #
######################

X, Y, Z = 0, 1, 2


def rotation_matrix(α, β, γ):
    """
    rotation matrix of α, β, γ radians around x, y, z axes (respectively)
    """
    sα, cα = sin(α), cos(α)
    sβ, cβ = sin(β), cos(β)
    sγ, cγ = sin(γ), cos(γ)
    return (
        (cβ*cγ, -cβ*sγ, sβ),
        (cα*sγ + sα*sβ*cγ, cα*cγ - sγ*sα*sβ, -cβ*sα),
        (sγ*sα - cα*sβ*cγ, cα*sγ*sβ + sα*cγ, cα*cβ)
    )


class Physical:
    def __init__(self, vertices, faces, tetra):
        """
        a 3D object that can rotate around the three axes
        :param vertices: a tuple of points (each has 3 coordinates)
        :param edges: a tuple of pairs (each pair is a set containing 2 vertices' indexes)
        """
        self.__vertices = array(vertices)
        self.__faces = tuple(faces)
        self.__rotation = [0, 0, 0]  # radians around each axis
        self.shift = array([0, 0, 0])
        self.tetra = tetra

    def rotate(self, axis, θ):
        self.__rotation[axis] += θ

    @property
    def faces(self):
        location = self.__vertices.dot(rotation_matrix(*self.__rotation))  # an index->location mapping
        location = list(map(self.shift.__add__, location))
        for side in self.__faces:
            yield ((location[v1], location[v2], location[v3], f1, f2) for v1, v2, v3, f1, f2 in side)

    def get_color(self, face, side):
        return self.tetra.pieces[face][side].name.title()

######################
#                    #
#    gui section     #
#                    #
######################


BLACK, RED = (0, 0, 0), (255, 128, 128)
colors = {'Red': (255, 0, 0),
          'Green': (0, 255, 0),
          'Blue': (0, 0, 255),
          'Yellow': (255, 255, 0)
          }

class Paint:
    def __init__(self, shape, keys_handler):
        self.__shape = shape
        self.__keys_handler = keys_handler
        self.__size = 450, 450
        self.__clock = pygame.time.Clock()
        self.__screen = pygame.display.set_mode(self.__size)
        self.__mainloop()

        self.dragging = False

    def __fit(self, vec):
        """
        ignore the z-element (creating a very cheap projection), and scale x, y to the coordinates of the screen
        """
        # notice that len(self.__size) is 2, hence zip(vec, self.__size) ignores the vector's last coordinate
        return [round(70 * coordinate + frame / 2) for coordinate, frame in zip(vec, self.__size)]

    def __handle_events(self):
        if not hasattr(self, "dragging"): self.dragging = False
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit()
##            elif event.type == pygame.MOUSEBUTTONDOWN:
##                self.dragging = True
##            elif event.type == pygame.MOUSEBUTTONUP:
##                self.dragging = False
##            elif event.type == pygame.MOUSEMOTION and self.dragging:
##                mouse_x, mouse_y = event.pos
##                self.__shape.shift[0] += mouse_x / 200
##                self.__shape.shift[1] += mouse_y / 200
##                
        self.__keys_handler(pygame.key.get_pressed())

    def __draw_shape(self, thickness=4):
        sides = list(map(list, self.__shape.faces))
        sides = sorted(sides, key=lambda i: self.get_center(i)[2])
        # x = sorted(x, key=lambda i: i[-1][2])
        for side in sides:
            for points in side:
                *points, f1, f2 = points
                color = colors[self.__shape.get_color(f1, f2)]
                # pygame.draw.line(self.__screen, RED, self.__fit(start), self.__fit(end), thickness)
                pygame.draw.polygon(self.__screen, color, list(map(self.__fit, points)))
                for start, end in combinations(points, 2):
                    pygame.draw.line(self.__screen, BLACK, self.__fit(start), self.__fit(end), thickness)

    def get_center(self, side):
        a, b, c = 0, 0, 0
        for j in side:
            for i in j[:-2]:
                a += i[0]
                b += i[1]
                c += i[2]
        return (a / len(side), b / len(side), c / len(side))

    def __mainloop(self):
        while True:
            self.__handle_events()
            self.__screen.fill(BLACK)
            self.__draw_shape()
            pygame.display.flip()
            self.__clock.tick(40)


######################
#                    #
#     main start     #
#                    #
######################


from pygame import K_q, K_w, K_a, K_s, K_z, K_x

vertices = []
faces = []
fill = None
for i in open("tetra.txt"):
    if i.startswith("#"):
        _, fill, *_ = i.split()
        faces.append([])
    if i.startswith("v"):
        _, a, b, c = i.split()
        vertices.append([-int(a), -int(b), -int(c)])
    elif i.startswith("f"):
        _, a, b, c, d, e = i.split()
        faces[-1].append([int(a), int(b), int(c), int(d), int(e)])

def render(tetra):
    cube = Physical(
        vertices=vertices,
        faces=faces,
        tetra=tetra
    )

    counter_clockwise = 0.05  # radians
    clockwise = -counter_clockwise

    params = {
        K_q: (X, clockwise),
        K_w: (X, counter_clockwise),
        K_a: (Y, clockwise),
        K_s: (Y, counter_clockwise),
        K_z: (Z, clockwise),
        K_x: (Z, counter_clockwise),
    }

    def keys_handler(keys):
        for key in params:
            if keys[key]:
                cube.rotate(*params[key])

    pygame.init()
    pygame.display.set_caption('Control -   q,w : X    a,s : Y    z,x : Z')
    Paint(cube, keys_handler)

