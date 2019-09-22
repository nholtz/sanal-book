# 2: Forces in Statically Determinate Beams and Frames

## 2.8: Shear, Moment and Normal Force Diagrams

### 2.8.1: Relationship of Transverse Loads to Shears and Moments

![Figure](../../images/sdbeams/NVMdiagrams/lvm-relations.svg)

Fig. 2.8-1: Loads, Shears and Moments

Fig. 2.8-1 shows a beam with a varying distributed load, acting
upwards on the beam.  We are interested in developing a relationship
between the external loads and the internal forces.

The bottom portion of Fig. 2.8-1 shows a free body diagram of an
element of the beam of length $dx$.  All forces are shown in a
direction that is positive by the *beam sign convention*:

 - lateral loads are +ive acting in the upward (+ive *y*) direction.
 - shear forces are +ive if they tend to rotate the element clockwise.
 - bending moments are +ive if they cause compression in the *top* fibers of the beam.

We now write an equilibrium equation for the sum of forces in the vertical direction.

$$
   \sum F_y = 0~~~~~~~(+\uparrow)
$$

$$
   V - (V + dV) + w dx + (dw)(dx){1\over 2} = 0
$$

Neglecting the second-order term and rearranging, we get:

$$
   dV = w dx
$$

That can be interpreted two different ways.  

- As $dV = w dx$, it says that the change in shear between any two
    points is equal to the area under the distributed load diagram
    between those two points.

- As ${dV/dx} = w$, it says that the slope of the shear diagram at any
  point is equal to the intensity of the distributed load at that
  point.

Now, summing moments about point *o* on the right face, we have:

$$
   \sum M_o = 0~~~~~~(+{\mathrm{CCW}})
$$

$$
   -M + (M+dM) - V dx - w(dx){dx\over2} - (dw)(dx){1\over2}{dx\over3} = 0
$$

Neglecting the second- and third-order terms and rearranging gives us:

$$
   dM = V dx
$$

Again, that can be interpreted two different ways:

- As $dM = V dx$, it says that the change in moment between any two
  points is equal to the area under the shear diagram between those
  two points.

- As ${dM/dx} = V$, it says that the slope of the moment diagram at
  any point is equal to the intensity of the shear at that point.

<div class="admonition important"> 
   Because internal forces always
   occur in equal and opposite pairs, when we plot shear and moment
   diagrams we must associate a sign with a *pair* of forces.  Thus,
   beam sign convention.  </div>

<div class="admonition important"> 
   Because the original differential
   equation was developed assuming a distributed force, the resulting
   relationships work for the case of distributed loads.  </div>

<div class="admonition important"> 
   The relationships also work at
   locations of concentrated loads, recognizing that the load
   intensity is infinite, and the shear change across a concentrated
   force is equal to the value of the force.  </div>

<div class="admonition important"> 
   The relationships do not work
   directly for concentrated moments.  Shear does not change acroos a
   concentrated moment, and bending moment changes by the value of the
   applied moment.  </div>

### 2.8.2: Relationship of Longitudinal Loads to Normal Force

![Figure](../../images/sdbeams/NVMdiagrams/ln-relations.svg)

Figure 2.8-2: Longitudinal loads and normal forces.

All loads that action on beams and members in frames can be resolved
into two components, one perpendicular to the axis of the member and
one parallel to the axis.  The perpendicular components are the
transverse loads, and they affect shear forces and bending moments as
outlined above.  The parallel components are the longitudinal loads, $w_p$,
and they have direct effect only on the normal forces.  We also assume
that the beam depth has no significance and that all longitudinal
forces are coincident with the longitudinal axis.

By inspection from Fig. 2.8-2: we can derive the relationship:

- The change in normal force between two points along the axis of a
  beam is equal to the total longitudinal load between those two
  points.
