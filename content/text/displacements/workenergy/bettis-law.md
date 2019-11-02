# 6. Elastic Displacements

## 6.3 Bettis Law and Virtual Work

### Principle of Superposition

![Figure](../../../images/displacements/workenergy/bending-1.svg)

The above figure shows, in sub-figure a), a beam subject to two concentrated forces, 
$P_1$ and $P_2$.  At each of those locations is also shown the corresponding
vertical displacements, $\Delta_1$ and $\Delta_2$.

Shown below in sub-figures b) and c) is the same beam with the loads
acting individually, rather than together as in a).

The principle of superposition says that any structural effect in 
a) can be determined by summing the same effect from b) and c).
More specifically:

$$
\begin{align}
\Delta_1 = \delta_{11} + \delta_{12}\\
\Delta_2 = \delta_{21} + \delta_{22}\\
\end{align}
$$

where:

$\delta_{ij}$ is the displacement at location $i$ due to the force at location $j$.

![Figure](../../../images/displacements/workenergy/bending-2.svg)

The above figure shows the same three beams, but this time with the
bending moment diagram for each.  And again, the principle of superposition
says, that for any point along the span, the bending moment at that point in beam a)
is the sum of the bending moments at the same point in b) and c).

In beam b) the bending moment diagram is labelled as $M_1$ as it is results
from the force applied at location 1.  Beam b)'s bending moment diagram
is labelled as $M_2$ as it results from the force at location 2.

### External Work and Strain Energy

__Step a)__

In the above beam, first imagine the force at location 1 increasing from 0 to
$P_1$ while $P_2$ is held at 0.  This would correspond to beam b) in the above figures.

We can then compute external work and strain energy for that system:

$$
\begin{align}
U_{e1} &= \frac12 P_1\delta_{11}\\
U_{i1} &= \int_0^L \frac{M_1^2}{2 E I} dx\\
\\
\text{and}\\
\\
U_{e1} &= U_{i1}\\
\end{align}
$$

__Step b)__

Now imagine the force $P_1$ held to 0 and the force at location 2
increasing from 0 to $P_2$.

Now the work and energy terms are:

$$
\begin{align}
U_{e2} &= \frac12 P_2\delta_{22}\\
U_{i2} &= \int_0^L \frac{M_2^2}{2 E I} dx\\
\\
\text{and}\\
\\
U_{e2} &= U_{i2}\\
\end{align}
$$

__Step c)__

Finally imagine the force at location 1 increasing from 0 to $P_1$, then being held constant
at that value while the force at location 2 is increased from 0 to $P_2$.  The final state will be 
beam a) in the above figures.

The total external work will involve the work done by force 1 as it increases and moves through
the displacement at 1, plus the work done by the constant force $P_1$ as it moves through
the displacement at location 1 caused by increasing force $P_2$, plus the work done by $P_2$
as it increases and moves through the displacement it causes at location 2.

In other words:

$$
U_e = \frac12 P_1\delta_{11} + P_1\delta_{12} + \frac12 P_2 \delta_{22}
$$

and the strain energy calculations are similar:

$$
U_i = \int_0^L \frac{M_1^2}{2 E I} dx + \int_0^L \frac{M_1 M_2}{E I} dx + 
      \int_0^L \frac{M_2^2}{2 E I} dx
$$

The three terms above are:
1. strain energy due to increasing moments caused by force 1 acting through increasing
   curvatures caused by force 1.
1. strain energy due to constant moments caused by force 1 acting through increasing
   curvatures caused by force 2.
1. strain energy due to increasing moments caused by force 2 acting through increasing
   curvatures caused by force 2.
   
and, of course

$$
U_e = U_i
$$
 
 so:
 
![Figure](../../../images/displacements/workenergy/bending-3.svg)

and we are left with

$$
 P_1\delta_{12} =  \int_0^L \frac{M_1 M_2}{E I} dx
$$

This is a remarkable result.  It essentially says:

<div class="admonition important">
The external work done by load 1 acting through the
displacements caused by load 2 is equal to
the strain energy of the moments of load 1 
acting through the curvatures caused by load 1.
</div>
