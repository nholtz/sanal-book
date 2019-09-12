---
title: 'Free Body Diagrams'
prev_page:
  url: /text/sdbeams/determinacy-and-stability-problems.html
  title: 'Problems - Determinacy and Stability'
next_page:
  url: /notebooks/sdbeams/eq-demo-2.html
  title: 'Equilibrium Demonstration'
comment: "***PROGRAMMATICALLY GENERATED, DO NOT EDIT. SEE ORIGINAL FILES IN /content***"
---
# 2: Determinate Beams and Frames

## 2.3: Free Body Diagrams


The construction of a proper free body diagram (FBD) is an essential
first step in a structural analysis.  A free body diagram is a sketch
of the outline of a structure, roughly to scale and isolated from its
surroundings.  It shows key features of the geometry, all applied
forces (loads), and all relevant reactive forces at the points of
contact between the portion shown and its surroundings.

To determine the character of the reactive forces (i.e. their types
and directions), you determine the displacement contraints, and show
the force corresponding to each.

![Beam Model and FBD](../../images/sdbeams/fbd/drawing-1.svg)

   Fig 3-1: Beam model and FBD of complete structure

Fig. 3-1 shows the structural model of a beam in the top portion and a
free body diagram of the entire beam in the bottom portion.  Note that
the figure shows a beam that is completely fixed at the left end, has
a roller support 2m from the right end, and an internal hinge at point
_b_, 6m to the left of the roller support.  Two applied loads, a
uniformly distributed load of 28kN/m over the entire beam and a
concentrated load of 65kN are shown.

At two locations, _a_ and _d_, the beam is in contact with its
surroundings; the surroundings are not shown.  At these locations,
then, we must determine the displacement constraints, and show the
corresponding forces.

At point _a_, the symbol on the model shows that that point is
constrained against rotation, against vertical displacement and
against horizontal displacement.  Therefore, at point _a_ on the FBD
we show a moment corresponding to the rotational constraint, a
vertical force corresponding to the vertical displacement constraint,
and a horizontal force corresponding to the horizontal displacement
constraint.  These are unknown forces, and so we label them with
convenient symbols: $M_a$, $V_a$, and $H_a$,
respectively.

At point _d_, there is only the constraint against vertical
displacement, and so we show only a vertical force, $V_d$.

The location of the internal hinge is not particularly relevant on
this FBD, so it is not shown.

<div class="admonition important">
   Free body diagrams should <em>not</em> show uniformly distributed loads
   replaced by their statically equivalent concentrated loads.  That
   does not make things simpler, but it does increase chances for
   confusion and error later when you draw shear force and bending
   moment diagrams.
</div>

<div class="admonition important">
   After a little experience, you can tell by 'inspection' that the
   horizontal force at <em>a</em>, $H_a$, is 0.  However, you use an
   equation of equilibrium to know that, and it is important not to
   fool yourself into thinking you have fewer unknowns than you do.
   All forces that <em>could</em> develop under other loading conditions
   should be shown, even if you can trivially determine they are zero
   under the given loading condition.
</div>

![FBD of portion b-c-d](../../images/sdbeams/fbd/drawing-2.svg)

Fig 3-2: Beam - FBD of portion b-c-d

We will see later that it is often necessary to draw a FBD of a
portion of the structure, particularly when we can 'break', or 'cut',
the structure at an internal release condition such as the hinge at
_b_.

Fig. 3-2 shows a FBD of portion _b-c-d_ of one portion of the
structure.  Of course, we show only those applied loads that act on
the portion of the structure that we show.  The 65kN concentrated
force is as before, but the length of the distributed load has been
reduced to 8m to match the length of the portion.

At point _b_, there are relative displacement constraints that require
that both the vertical and horizontal displacements of the beam on
either side of the hinge must each be equal.  Therefore we must show
forces corresponding to that portion of the beam that is in contact
but not shown.  These are internal forces.

There is no constraint against relative rotation of the beam to either
side of the hinge -- after all, that is what a hinge allows -- and so
we do not show an internal moment at _b_.

<div class="admonition important">
  Recognizing points in a structure at which internal forces are known 
  to be zero is crucial to
  analyzing many complex structures.
</div>

![FBD of portion a-b](../../images/sdbeams/fbd/drawing-3.svg)

Fig 3-3: Beam - FBD of portion a-b

Occasionally it is important to also draw the FBD of adjacent portions
of a structure.  Fig. 3-3 shows one such FBD for the portion _a-b_
which is immediately adjacent to the FBD portion shown in Fig. 3-2.
It is _vital_ to realize that the forces shown at _b_ are _internal_
forces and that internal forces always occur in equal and opposite
pairs.  A single FBD of a structure cut at a point only shows one of
the forces at each pair.  The other FBD must then show the other forces
of the pair.

Once you have established the assumed direction of forces on one FBD,
you _must_ show those forces as equal and opposite on the adjacent
FBD.  You establish equality by using the same label, and you
establish 'oppositeness' by showning the forces in the opposite
direction.

The FBD of Fig. 1-3 shows the forces at _b_, $H_b$ and $V_b$ being
equal and opposite to those shown in Fig. 3-2.

<div class="admonition important">
   Unknown internal forces shown on one FBD of a portion of a
   structure must be shown as equal and opposite at the same point on
   the adjacent FBD.
</div>

### References

* [Wikipedia](http://en.wikipedia.org/wiki/Free_body_diagram)
* [Architectonics](http://web.mit.edu/4.441/1_lectures/1_lecture14/1_lecture14.html)
