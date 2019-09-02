---
interact_link: content/fundamentals/eq-demo-2.ipynb
kernel_name: python3
has_widgets: false
title: 'Equilibrium Example'
prev_page:
  url: /fundamentals/free-body-diagrams.html
  title: 'Free Body Diagrams'
next_page:
  url: /fundamentals/fbd-eg1.html
  title: 'FBD Example 1'
comment: "***PROGRAMMATICALLY GENERATED, DO NOT EDIT. SEE ORIGINAL FILES IN /content***"
---
# Demonstration of Equilibrium for a Beam Structure
The following beam structure may not be completely shown, though it is complete enough to
discuss the principles of equilibrium.

![Beam Structure](images/eq/eq-demo-2-01.svg)



We will define some specific values and draw the Free Body Diagram.  At the left end (point $a$)
there is complete fixity (against horizontal and vertical displacements, as well as against rotation),
so there are correspondingly three forces, ($F_a$, $V_a$ and $M_a$).  At the right end
(point $c$) there is only a constraint against vertical displacement and so there is one 
vertical force, $V_c$, at that point.

![Beam FBD](images/eq/eq-demo-2-02.svg)



Considerinng the above FBD, there are 4 unknown forces shown, but we have only 3 equations of
equilibrium available.  That means there are an infinite number of sets of forces that satisfy
equilibrium.  To demonstrate that, we will show 2 of them:

![EQ Soln 1](images/eq/eq-demo-2-03.svg)



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

![EQ Soln 2](images/eq/eq-demo-2-04.svg)



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



## a) It Is Statically Determinate



If there are additional conditions specified where an internal force in the beam is required to
be a specific value, then we have additional equiations of equilibrium available to us.  These are equilibrium equations we can write on a *different* FBD that do not introduce additional unknowns.

For example, we might have a hinge in the beam
at point $d$, 4m from the right support.  That specifies that the
internal bending moment in the beam is zero at that support, and allows us to form a FBD on one side of the pin.  We choose a side that allows us to write an equilibrium equation that contains only
one unknown; here the right side:

![FBD Right Side](images/eq/eq-demo-2-03c.svg)



Knowing the moment is 0 at point $d$, we can write an equilibrium equation $\sum M_d = 0$ that does not
reference either of the two new unknowns, $H_d$ nor $V_d$:

$$
\begin{align}
V_c\times 4 - 100\times (4-2) &=& 0\\
V_c &=& 50\\
\end{align}
$$

With a hinge at that location, here is the only correct set of forces (that satisfy all 4 equilibrium
equations):

![Soln 1](images/eq/eq-demo-2-03b.svg)



On the other hand, if the hinge is 5m from the right support, here are the only forces that
satisfy all 4 quilibrium equations:

![Soln 2](images/eq/eq-demo-2-04b.svg)



## b) It Is Statically Indeterminate

On the other hand, there may be no conditions that allow for extra equilbrium equations.

If that is the case we must use knowledge of the elastic properties of the beam and this will
allow us to develope a *compatibility* equation to choose a set of forces such that the beam
deflections are correct.

For example, if there were no internal hinge, we could work out the vertical deflection at point
$c$ for each of the set of forces above.  It is quite likely that the resulting deflection would not be zero,
but we know it should be (the support constrains the vertical deflection to be zero).  In that case,
neither set of forces is correct.

