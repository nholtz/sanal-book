---
title: 'Introduction'
prev_page:
  url: /text/sdtrusses/index.html
  title: 'Forces in Statically Determinate Trusses'
next_page:
  url: /text/sdtrusses/determinacy-and-stability.html
  title: 'Determinacy and Stability'
comment: "***PROGRAMMATICALLY GENERATED, DO NOT EDIT. SEE ORIGINAL FILES IN /content***"
---
# 3: Forces in Statically Determinate Trusses

## 3.1: Introduction

The mathematical model of a truss makes the following assumptions and simplifications:

* All members are straight and connected at each of their two ends
  using small, frictionless pins.  The pins are incapable of
  transmitting any moment to the members.
* All external forces are applied to the structure through the pins at
  the joints.
* If self weight of the members is to be included, the weight of a
  member can be applied equally to the pin at either end.

![Figure](../../images/sdtrusses/intro/bar-forces.svg)

Figure 3.1.1: Forces imparted by pins on members

With these assumptions, equilibrium will require that every member is
subjected to two forces -- one at each end transmitted by the pin.
The forces must be equal and opposite at the ends, directed along the
axis joining the pins, and will subject the member to either a pure
tensile or pure compressive force.  There will no shears or bending
moments in the members.

All this leads to the ability to use a very special analysis technique
to determine the internal forces in trusses.

### 3.1.1 Real World Trusses

Real world trusses are not built like the assumptions in the model.
However, if care is taken in detailing a real structure to approximate
some of these conditions, internal shears and bending moments in the
truss members may indeed by very small - almost negligible.  Under
these conditions, the truss assumptions may be used and a truss
analysis may be performed.

<div class="admonition important">
It is the responsibility of the design engineer to know when the truss
assumptions and simplifications are valid, and when they are not.
</div>
