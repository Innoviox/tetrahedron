import trimesh

fill = None
faces = []
fills = []
vertices = []
colors = {'Red': [255, 0, 0, 255],
          'Blue': [0, 0, 255, 255],
          'Green': [0, 255, 0, 255],
          'Yellow': [255, 255, 0, 255]}

for i in open("tetra.txt"):
    if i.startswith("#"):
        _, fill, *_ = i.split()
    if i.startswith("v"):
        _, a, b, c = i.split()
        vertices.append([-int(a), -int(b), -int(c)])
    elif i.startswith("f"):
        _, a, b, c = i.split()
        faces.append((int(a), int(b), int(c)))
        fills.append(fill)

mesh = trimesh.Trimesh(vertices=vertices, faces=faces)
for face in mesh.faces:
    mesh.visual.face_colors[face] = trimesh.visual.random_color()
    
mesh.show()
