---
interact_link: content/notebooks/sdtrusses/hextruss-irregular.ipynb
kernel_name: python3
has_widgets: false
title: 'Stability and Matrix Methods'
prev_page:
  url: /text/sdtrusses/matrix-methods.html
  title: 'Matrix Methods'
next_page:
  url: /text/sdtrusses/suggested-problems.html
  title: 'Suggested Problems'
comment: "***PROGRAMMATICALLY GENERATED, DO NOT EDIT. SEE ORIGINAL FILES IN /content***"
---


# Truss Stabilty Investigation by the Matrix Method of Analysis

The following truss is unstable.  Instead of determining that by finding a mechanism or by
use of the zero-load test, this section will setup a full matrix analysis.



![Figure](hextruss-irregular.svg)



Import some utilities from a library for statically determinate 2D truss analysis.



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
from sdtruss import sdtruss, SDTError

```
</div>

</div>



## Joint Coordinates
This section specifies the _x-y_ coordinates of each joint.  Each line of input specifies
the id of the joint and its _x_ and _y_ coordinates:



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
jc = [ ('a', 0, 0),
       ('b', 0, 4),
       ('c', 2, 8),
       ('d', 6, 8),
       ('e', 8, 4),
       ('f', 8, 0),
       ]

```
</div>

</div>



## Member Incidences
This section defines each member in the truss by specifying the ids of the joints
at either end of each member.  Each member is connected to exactly two joints.



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
mi = [ ('a', 'b',),   # there is a member from joint a to joint b, etc.
       ('b', 'c',),
       ('c', 'd',), 
       ('d', 'e',),
       ('e', 'f',),
       ('f', 'a',),
       ('b', 'e',),
       ('c', 'f',),
       ('a', 'd',),
       ]

```
</div>

</div>



## Reactions
This section specifies the reaction components.  Each line specifies one independent reaction
by naming the joint on which it impinges and the direction of the reaction.  Directions are given
as relative direction components.  For example, a direction component of '0,1' means a vertical
reaction (in the $y$-direction).  A direction component of '3,4' would specify an angle of 53.13 degrees to the $x$-axis ($\tan^{-1}{4\over3}$ - relative components of 3 in $x$ and 4
in $y$).



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
rf = [ ('a', 1, 0),             # reaction force dirns - horizontal at a
       ('a', 0, 1),             # vertical at a
       ('f', 0, 1),
       ]

```
</div>

</div>



## Joint Loads
Joint loads arfe specified by naming the joint, providing the magnitude, and direction components
in which it acts.



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
jl = [ ('c', 1, 1, 0),      # joint loads (j, p, dx, dy) - this is a unit load at c, in x-direction
       ]

```
</div>

</div>



## Analysis
Now we analyze by providing the above data to the library function.



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
try:
    sdtruss( jc, mi, rf, jl )
except SDTError as err:
    print('**** Error: {0}'.format(err))

```
</div>

<div class="output_wrapper" markdown="1">
<div class="output_subarea" markdown="1">
{:.output_stream}
```
**** Error: 'C' matrix is rank-deficient, truss is probably unstable.
```
</div>
</div>
</div>



We see above the the rank-check of the matrix failed.  The rank of the coefficient matrix was less than
the number of columns and thus no solution was possible.



## Change the Geometry
Here we see a very small change made to the geometry, by moving joint _c_ up 1mm.



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
jc = [ ('a', 0, 0),
       ('b', 0, 4),
       ('c', 2, 8.001),
       ('d', 6, 8),
       ('e', 8, 4),
       ('f', 8, 0),
       ]

```
</div>

</div>



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
try:
    sdtruss( jc, mi, rf, jl )
except SDTError as err:
    print('**** Error: {0}'.format(err))

```
</div>

<div class="output_wrapper" markdown="1">
<div class="output_subarea" markdown="1">
{:.output_stream}
```
uid   iid   jid        force
---   ---   ---        -----
ab    a     b           1779 T
bc    b     c           1988 T
cd    c     d           2222 T
de    d     e           1988 T
ef    e     f           1778 T
fa    f     a           1334 T
be    b     e          889.1 C
cf    c     f           2224 C
ad    a     d           2222 C
Rax   a                   -1 
Ray   a                   -1 
Rfy   f                    1 
```
</div>
</div>
</div>



Mathematically, the truss is no longer unstable, but notice the very large member forces (compared
to the small applied load).  Forces were amplified by about a factor of 2000.  This demonstrates
that trusses that are unstable or nearly so will have very high member forces, leading to large distortions and geometry changes.  This is very undesireable in a civil engineering structure.

