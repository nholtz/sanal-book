# 1: Fundamental Concepts
## 1.2: Equilibrium

Equilibrium is a fundamental concept in structural analysis.  Briefly,
it is the requirement that the resultant of each and every set of
forces that act on a structure, or on any part of the structure, be
zero.  This requirement is a mathematical tool that we can use to
setup and solve equations that will allow us to solve for unknown
forces.

### 1.2.1: Two Dimensional (2D) Equilibrium

In this course, we will deal almost exclusively with structures that
can be modeled as 2D, or *planar*, structures.  All forces, then are
assumed to lie in the plane of the structure.  In such a system, there
are three *independent* scalar equations of equilibrium that are
necessary and sufficient to establish equilibrium.

The particular equations used can vary from problem to problem, but
the idea that there are never more than three available on any one
force system is crucial.  Some special force systems have fewer than
three independent equations available.

.. figure:: couple-1.png
   :align: right

   Couple/Moment Equivalency

Before proceeding, we note the equivalency regarding a couple.  A
couple is a pair of equal, opposite and parallel forces, $F$,
separated by a non-zero distance, $d$.  A couple is equivalent
to a pure moment of magnitude $M = F \times d$; wherever one
appears in a force system, it can be replaced by the other with no
effect on the resulting system.

The three equations normally used for a general force system are the
sums of forces in two different directions (usually orthogonal
directions) and sum of the moments about some point in the plane,
often expressed as:

$$
\begin{eqnarray}
\sum F_x &=& 0\\
\sum F_y &=& 0\\
\sum M_o &=& 0\\
\end{eqnarray}
$$

These equations are commonly used because they are convenient and
there are few restrictions as to their applicability.

Other sets of equations are possible, for example moments about three
different points as long as they are not co-linear:

$$
\begin{eqnarray}
\sum M_a &=& 0 \\
\sum M_b &=& 0 \\
\sum M_c &=& 0 \\
\end{eqnarray} 
$$

as long as all points are different and point *c* is not on the line
through points *a* and *b*.

Even other equations are possible.  For example, for summing forces in
two different directions, the directions need not be orthogonal
(though they obviously cannot be parallel).  Or, you can use a force
and two moment equations, as long as a line through the two moment
points is not parallel to the force direction.


> :exclamation: In a general 2D force system, there are *never* more
> than three independent scalar equations available.

> :exclamation: In a general 2D force system, there is some choice as
> to which set of three equations you use.

### 1.2.2: Special Force Systems


In some force systems, there are even fewer than three equations available.

If forces are concurrent, :math:`\sum M_c = 0` happens automatically when point *c* is the point of concurrency, so only two equations remain.  You may still use a moment equation to solve for unknowns, but you can only use :math:`\sum M_o = 0` when point *o* is *not* the point of concurrency.

If forces are parallel, :math:`\sum F_y = 0`, where *y* is perpendicular to the forces, happens automatically no matter what the magnitude of the forces is, and so only two equations remain.
You could still use two force equations such as :math:`\sum F_x = 0` and :math:`\sum F_z = 0`, where direction *z* is neither parallel nor perpendicular to *x*.

.. IMPORTANT::
   In parallel and concurrent 2D force systems, only two scalar equations of equilibrium are available.

.. IMPORTANT::
   In parallel and concurrent 2D force systems, there is some choice as to which set of two equations you use.
   
