---
interact_link: content/notebooks/sdbeams/eq-demo-2.ipynb
kernel_name: python3
has_widgets: false
title: 'Equilibrium Demonstration (Notebook)'
prev_page:
  url: /text/sdbeams/free-body-diagrams.html
  title: 'Free Body Diagrams'
next_page:
  url: /notebooks/sdbeams/fbd-eg1-no-units.html
  title: 'Beam Reactions Example (Notebook)'
comment: "***PROGRAMMATICALLY GENERATED, DO NOT EDIT. SEE ORIGINAL FILES IN /content***"
---


#  2: Determinate Beams and Frames
## 2.4: Demonstration of Equilibrium for a Beam Structure

Consider the following beam structure.  Below, we will modify this structure to be statically determinate,
but for now just consider it as is show here:

![Beam Structure](../../images/sdbeams/eq/eq-demo-2-01.svg)



We will define some specific values for the parametewrs and draw a Free Body Diagram.  At the left end (point $a$)
there is complete fixity (against horizontal and vertical displacements, as well as against rotation),
so there are correspondingly three forces/moments, ($F_a$, $V_a$ and $M_a$).  At the right end
(point $c$) there is only a constraint against vertical displacement and so there is one 
vertical force, $V_c$, at that point.

![Beam FBD](../../images/sdbeams/eq/eq-demo-2-02.svg)



In the above FBD, there are 4 unknown forces shown, but we have only 3 equations of
equilibrium available on that FBD.  That means the structure as shown
is _statically indeterminate_.  That also means there are an infinite number of sets of forces that satisfy
the equations of equilibrium.  To demonstrate that, we will show 2 sets of them:

![EQ Soln 1](../../images/sdbeams/eq/eq-demo-2-03.svg)



The above forces are in equilibrium:



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
0       # sum Fx, +ive right

```
</div>

<div class="output_wrapper" markdown="1">
<div class="output_subarea" markdown="1">


{:.output_data_text}
```
0
```


</div>
</div>
</div>



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
+50 + 50 - 100     # sum Fy, +ive up

```
</div>

<div class="output_wrapper" markdown="1">
<div class="output_subarea" markdown="1">


{:.output_data_text}
```
0
```


</div>
</div>
</div>



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
+200 - 50*8 + 100*2     # sum Mc, +ive ccw

```
</div>

<div class="output_wrapper" markdown="1">
<div class="output_subarea" markdown="1">


{:.output_data_text}
```
0
```


</div>
</div>
</div>



But so is the following set of forces:

![EQ Soln 2](../../images/sdbeams/eq/eq-demo-2-04.svg)



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
0       # sum Fx, +ive right

```
</div>

<div class="output_wrapper" markdown="1">
<div class="output_subarea" markdown="1">


{:.output_data_text}
```
0
```


</div>
</div>
</div>



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
+40 + 60 - 100     # sum Fy, +ive up

```
</div>

<div class="output_wrapper" markdown="1">
<div class="output_subarea" markdown="1">


{:.output_data_text}
```
0
```


</div>
</div>
</div>



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
+120 - 40*8 + 100*2     # sum Mc, +ive ccw

```
</div>

<div class="output_wrapper" markdown="1">
<div class="output_subarea" markdown="1">


{:.output_data_text}
```
0
```


</div>
</div>
</div>



So which set of forces, if either, is 'correct'?  It depends.  You have to know more about this
beam than has been shown so far.



## A) If it is Statically Determinate



If there are additional conditions specified where an internal force in the beam is required to
be a specific value, then we have additional equations of equilibrium available to us.  These are equilibrium equations we can write on a *different* FBD that do not introduce additional unknowns.

For example, we might have a hinge in the beam
at point $d$, 4m from the right support.  

![FBD Right Side](../../images/sdbeams/eq/eq-demo-2-03c0.svg)



That hinge specifies that the
internal bending moment in the beam is known to be zero at that point, and allows us to form a FBD on one side of the pin.  We choose a side that allows us to write an equilibrium equation that contains only
one unknown; here the right side:

![FBD Right Side](../../images/sdbeams/eq/eq-demo-2-03c.svg)



Knowing the moment is 0 at point $d$, we can write an equilibrium equation $\sum M_d = 0$ that does not
involve either of the two new unknowns, $H_d$ nor $V_d$:

$$
\begin{align}
V_c\times 4 - 100\times (4-2) &=& 0\\
V_c &=& 50\\
\end{align}
$$

With a hinge at that location, here is the only correct set of forces (that satisfy all 4 equilibrium
equations):

![Soln 1](../../images/sdbeams/eq/eq-demo-2-03b.svg)



That was the first set shown to be in equilibrium, above.

On the other hand, if the hinge is 5m from the right support, here are the only forces that
satisfy all 4 equilibrium equations:

![Soln 2](../../images/sdbeams/eq/eq-demo-2-04b.svg)

And that was the second set shown to be in equilibrium, above.



## B) If it is Statically Indeterminate

On the other hand, there may be no conditions that allow for extra equilbrium equations.

If that is the case we must use knowledge of the elastic properties of the beam and this will
allow us to develope a *compatibility* equation to choose a set of forces such that the beam
deflections are correct.

For example, if there were no internal hinge, we could work out the vertical deflection at point
$c$ for each of the set of forces above.  It is quite likely that the resulting deflection would not be zero,
but we know it should be (the support constrains the vertical deflection to be zero).  In that case,
neither set of forces is correct.



We will use the method of 'consistent deformation' with displacements calculated by the
method of 'virtual work'.

> **Note:** the following is very briefly described.  It will be improved at sometime in the future.



![Beam Structure](../../images/sdbeams/eq/eq-demo-2-01.svg)



![Beam Structure](../../images/sdbeams/eq/eq-demo-2-05.svg)



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
from sympy import symbols, solve, integrate, init_printing
init_printing()

```
</div>

</div>



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
EI,L,P,d,x,Vc = symbols('EI L P d x V_c')

```
</div>

</div>



Expressions for bending moments in the released structure, $M$ (due to the real loads),
and $m$ (due to virtual loads), as functions of $x$, the distance from the right support.



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
M = -P*(x-d)
M

```
</div>

<div class="output_wrapper" markdown="1">
<div class="output_subarea" markdown="1">



$$- P \left(- d + x\right)$$


</div>
</div>
</div>



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
m = x
m

```
</div>

<div class="output_wrapper" markdown="1">
<div class="output_subarea" markdown="1">



$$x$$


</div>
</div>
</div>



'Delta' is the displacement in the released structure due to the real loads.  The +ive direction is
the direction of the unit virtual load.



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
Delta = integrate(m*M/EI,(x,d,L))
Delta

```
</div>

<div class="output_wrapper" markdown="1">
<div class="output_subarea" markdown="1">



$$- \frac{L^{3} P}{3 EI} + \frac{L^{2} P d}{2 EI} - \frac{P d^{3}}{6 EI}$$


</div>
</div>
</div>



'delta' is the displacement in the released structure due to a unit value of the redundant force (the
vertical reaction at $c$)



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
delta = integrate(m*m/EI,(x,0,L))
delta

```
</div>

<div class="output_wrapper" markdown="1">
<div class="output_subarea" markdown="1">



$$\frac{L^{3}}{3 EI}$$


</div>
</div>
</div>



Write a compatibility equation for displacement at point $c$ (that displacement is 0, so
this calculates the value of the reaction at $c$ that makes it so):



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
eqn = Delta + Vc*delta
soln = solve(eqn,Vc)[0]
soln

```
</div>

<div class="output_wrapper" markdown="1">
<div class="output_subarea" markdown="1">



$$P - \frac{3 P d}{2 L} + \frac{P d^{3}}{2 L^{3}}$$


</div>
</div>
</div>



Substitute numerical values for the parameters to get a numerical
value for the reaction at $c$:



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
rVc = soln.subs({L:8,d:2,P:100}).n()
rVc

```
</div>

<div class="output_wrapper" markdown="1">
<div class="output_subarea" markdown="1">



$$63.28125$$


</div>
</div>
</div>



Now write 3 equilbrium equations and solve them for the remaing 3 reactions:



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
Ha,Va,Ma = symbols('H_a V_a M_a')

```
</div>

</div>



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
eqns = [Ha,                      # sum Fx, +ive right
       Va + Vc - P,              # sum Fy, +ive up
       Ma + Vc*L - P*(L-d)]      # sum M about a, +ive ccw

```
</div>

</div>



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
solns = solve(eqns,[Ha,Va,Ma])
solns

```
</div>

<div class="output_wrapper" markdown="1">
<div class="output_subarea" markdown="1">



$$\left \{ H_{a} : 0, \quad M_{a} : L P - L V_{c} - P d, \quad V_{a} : P - V_{c}\right \}$$


</div>
</div>
</div>



And substitute the parameters to get numerical values:



<div markdown="1" class="cell code_cell">
<div class="input_area" markdown="1">
```python
{s:v.subs({L:8,d:2,P:100,Vc:rVc}) for s,v in solns.items()}

```
</div>

<div class="output_wrapper" markdown="1">
<div class="output_subarea" markdown="1">



$$\left \{ H_{a} : 0, \quad M_{a} : 93.75, \quad V_{a} : 36.71875\right \}$$


</div>
</div>
</div>



For a linearly elastic, prismatic, statically indeterminate beam, the reactions are:

![Beam Structure](../../images/sdbeams/eq/eq-demo-2-06.svg)



This shows a *third* set of forces that are in equilibrium for this beam, 
but only this set results
in the correct displacements (0 horizontal and vertical and 0 rotational at end
$a$ and 0 vertical at end $c$).

