from compas.geometry import Box, Translation
from compas.geometry import dot_vectors
from compas.datastructures import Mesh

box = Box.from_width_height_depth(1, 1, 1)
cage = Mesh.from_shape(box)
cage.update_default_edge_attributes({'crease': 0})

top = sorted(cage.faces(), key=lambda face: dot_vectors(cage.face_normal(face), [0, 0, 1]))[-1]
bottom = sorted(cage.faces(), key=lambda face: dot_vectors(cage.face_normal(face), [0, 0, -1]))[-1]

c0 = cage.copy()
c1 = c0.transformed(Translation.from_vector([1.5, 0, 0]))
c2 = c1.transformed(Translation.from_vector([1.5, 0, 0]))
c3 = c2.transformed(Translation.from_vector([1.5, 0, 0]))
c4 = c3.transformed(Translation.from_vector([1.5, 0, 0]))
c5 = c4.transformed(Translation.from_vector([1.5, 0, 0]))

c1.edges_attribute('crease', 1, keys=list(cage.face_halfedges(top)))
c1.edges_attribute('crease', 1, keys=list(cage.face_halfedges(bottom)))

c2.edges_attribute('crease', 2, keys=list(cage.face_halfedges(top)))
c2.edges_attribute('crease', 2, keys=list(cage.face_halfedges(bottom)))

c3.edges_attribute('crease', 3, keys=list(cage.face_halfedges(top)))
c3.edges_attribute('crease', 3, keys=list(cage.face_halfedges(bottom)))

c4.edges_attribute('crease', 4, keys=list(cage.face_halfedges(top)))
c4.edges_attribute('crease', 4, keys=list(cage.face_halfedges(bottom)))

c5.edges_attribute('crease', 5, keys=list(cage.face_halfedges(top)))
c5.edges_attribute('crease', 5, keys=list(cage.face_halfedges(bottom)))

s0 = c0.subdivide(k=5)
s1 = c1.subdivide(k=5)
s2 = c2.subdivide(k=5)
s3 = c3.subdivide(k=5)
s4 = c4.subdivide(k=5)
s5 = c5.subdivide(k=5)