import copy
from build123d import *
from ocp_vscode import show, show_object


def reference(obj, label, loc=None):
    new_obj = copy.copy(obj)
    if label is not None:
        new_obj.label = label
    if loc is None:
        return new_obj
    else:
        return new_obj.move(loc)


# %%

locs = HexLocations(6, 10, 10).local_locations

box = Solid.make_sphere(5)
box_references = [
    reference(box, label=f"Sphere_{i}", loc=loc) for i, loc in enumerate(locs)
]
assembly = Compound(children=box_references)

show(assembly)
# %%

box_references = [
    reference(box, label=f"Sphere_{i}", loc=loc) for i, loc in enumerate(locs)
]
assembly = Compound(children=box_references)

show(assembly)

# %%

s = Sphere(1)
b = Box(1, 2, 3)
b1 = Pos(X=3) * b
b2 = Pos(X=-3) * b

show(
    s,
    b1,
    b2,
    names=["s", "b1", "b2"],
    colors=["red", "green", "blue"],
    alphas=[0.8, 0.6, 0.4],
    timeit=False,
)

# %%

s = Sphere(1)
b = Box(1, 2, 3)
b1 = reference(b, label="b1", loc=Pos(X=3))
b2 = reference(b, label="b2", loc=Pos(X=-3))

show(
    s,
    b1,
    b2,
    colors=["red", "green", "blue"],
    alphas=[0.8, 0.6, 0.4],
    timeit=False,
)

# %%

b2 = b2 - Pos(X=-3) * Box(5, 0.2, 0.2)

show(
    s,
    b1,
    b2,
    names=["s", "b1", "b2"],
    colors=["red", "green", "blue"],
    alphas=[0.8, 0.6, 0.4],
    timeit=False,
)

# %%

show(Pos(X=1.5) * b, Pos(X=-1.5) * b, timeit=False)

# %%

b = Box(0.1, 0.1, 1)
c = Cylinder(1, 0.5)
p = Plane(c.faces().sort_by().last)
b = [p * loc * b for loc in PolarLocations(0.7, 12)]
c = Compound.make_compound(b + [c])

show(c, timeit=False)

# %%

show(*c.solids(), timeit=False)

# %%

b = Box(0.1, 0.1, 1)
c = Cylinder(1, 0.5)
p = Plane(c.faces().sort_by().last)
b = [reference(b, "pillar", p.to_location() * loc) for loc in PolarLocations(0.7, 12)]

show(*b)

# %%
b = Box(0.1, 0.1, 1)
c = Cylinder(1, 0.5)
p = Plane(c.faces().sort_by().last)
b = [copy.copy(b).move(p.to_location() * loc) for loc in PolarLocations(0.7, 12)]

show(*b, timeit=False)


# %%
c = Compound.make_compound(b + [c])
show(*c.solids(), timeit=False)

# %%
