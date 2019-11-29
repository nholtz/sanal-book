# 8. Slope Deflection

## 8.1 Introduction  - Slope Deflection Equations

To use the method of slope-deflection, it is necessary
express the end moments of a beam segment as a function
of the end rotations, $\theta_a$ and $\theta_b$, and of the relative
lateral displacement (i.e., translation) of the ends, $\Delta_{ab}$, and of the applied loads.

![Figure](../../../../../images/sibeams/stiffness/slope-deflection/introduction/derivation-1.svg)

   Figure 8.1-1: End moments as functions of displacements and loads

In other words, referring to Fig. 8.1-1, we wish to be able to write something like:

$$
   \begin{split}
   M_{ab} &= f_1(\theta_a,\theta_b,\Delta_{ab},P,w(x),\dots)\\
   M_{ba} &= f_2(\theta_a,\theta_b,\Delta_{ab},P,w(x),\dots)\\
   \end{split}
$$

If we are able to do that, then we can treat joint displacements in beams and frames
as unknowns, write expressions for member end moments in terms of those unknowns, and then write
equilibrium equations involving the moments. This would allow us to solve for the unknown 
displacements, and then use those to calculate the member end moments.

### Use Superposition to Simplify the Derivation

![Figure](../../../../../images/sibeams/stiffness/slope-deflection/introduction/derivation-1sp.svg)

   Figure 8.1-2: Superposition of three simpler cases


As seen in Fig. 8.1-2,  we can make some headway by realizing that the 
most general case can be made up of the superposition of three simpler cases:

i. the beam segment with the applied loads and fixed ends - case i), plus
i. a segment undergoing only end rotations - case ii), plus
i. a segment undergoing only end translations - case iii).

We can then write the expressions for the end moments:

$$
   \begin{split}
   M_{ab} &= M^f_{ab} + M^r_{ab} + M^d_{ab}\\
   M_{ba} &= M^f_{ba} + M^r_{ba} + M^d_{ba}
   \end{split}
$$

### Superposition Case ii)

Consider case ii) first.  Using the method of virtual work, it is fairly straightforward to express
the inverse relationship -- the end rotations as functions of the end moments.
The relevant details are shown in Fig. 8.1-3.  

![Figure](../../../../../images/sibeams/stiffness/slope-deflection/introduction/derivation-3.svg)

   Figure 8.1-3:  Case ii) - end moments as functions of end rotations

In that figure, we show the bending moments corresponding to the applied end 
moments, $M^r_{ab}$ and $M^r_{ba}$
separately; this simplifies the resulting integration.

Using a virtual moment of 1 applied to end _a_, 
the rotation of end _a_ is determined thus:

$$
   \begin{split}
   \theta_a &= \int \frac{m_1 M_1}{E I} + \int \frac{m_1 M_2}{E I}\\
            &= \frac{1}{EI}\frac{L}{3}\times 1 \times M^r_{ab} +
               \frac{1}{EI}\frac{L}{6}\times 1 \times -M^r_{ba}\\
   \\
   \theta_a &= \frac{1}{EI}(\frac{L}{3} M^r_{ab} - \frac{L}{6}  M^r_{ba})
   \end{split}
$$

Similarly, the rotation of end _b_ is given as:

$$
   \begin{split}
   \theta_b &= \int \frac{m_2 M_1}{E I} + \int \frac{m_2 M_2}{E I}\\
            &= \frac{1}{EI}\frac{L}{6}\times -1 \times M^r_{ab} +
               \frac{1}{EI}\frac{L}{3}\times -1 \times -M^r_{ba}\\
   \\
   \theta_b &= \frac{1}{EI}(-\frac{L}{6} M^r_{ab} + \frac{L}{3}  M^r_{ba})
   \end{split}
$$

These two relationships can be expressed in matrix form:

$$
   \begin{split}
   \left\{
   \begin{array}{c}
   \theta_a\\
   \theta_b
   \end{array}
   \right\}
   =
   \frac{1}{6EI}
   \left[
   \begin{array}{cc}
   2L & -L\\
   -L & 2L
   \end{array}
   \right]
   \left\{
   \begin{array}{c}
   M^r_{ab}\\
   M^r_{ba}
   \end{array}
   \right\}
   \end{split}
$$

from which, by inverting the 2x2 matrix and pre-multiplying both sides by that inverse, we get:

$$
   \begin{split}
   \left\{
   \begin{array}{c}
   M^r_{ab}\\
   M^r_{ba}
   \end{array}
   \right\}
   =
   \frac{6EI}{1}
   \frac{1}{(2L)^2 - (L)^2}
   \left[
   \begin{array}{cc}
   2L & L\\
   L & 2L
   \end{array}
   \right]
   \left\{
   \begin{array}{c}
   \theta_a\\
   \theta_b
   \end{array}
   \right\}
   \end{split}
$$

or, simplifying:

$$
   \begin{split}
   \left\{
   \begin{array}{c}
   M^r_{ab}\\
   M^r_{ba}
   \end{array}
   \right\}
   =
   \frac{EI}{L}
   \left\{
   \begin{array}{c}
   4 \theta_a + 2 \theta_b\\
   2 \theta_a + 4 \theta_b
   \end{array}
   \right\}
   \end{split}
$$

The above expresses the end moments as a function of the end rotations.

### Superposition Case iii)

Now consider case iii), end translation only:

![Figure](../../../../../images/sibeams/stiffness/slope-deflection/introduction/derivation-2.svg)

   Figure 8.1-4: Case iii) - end moments as a function of end translation

As we see in Fig. 8.1-4, the beam segment with a translation and no
end rotation is equivalent to a segment with a rotation of $\Psi=-\Delta/L$ from
the _chord_.
This gives us:

$$
   \begin{split}
   \left\{
   \begin{array}{c}
   M^d_{ab}\\
   M^d_{ba}
   \end{array}
   \right\}
   =
   \frac{EI}{L}
   \left\{
   \begin{array}{c}
   4 \times -\Psi_{ab} + 2 \times -\Psi{ab}\\
   2 \times -\Psi_{ab} + 4 \times -\Psi{ab}
   \end{array}
   \right\}
   = 
   \frac{EI}{L}
   \left\{
   \begin{array}{c}
   -6\Psi_{ab}\\
   -6\Psi_{ab}
   \end{array}
   \right\}
   \end{split}
$$

### Summary

Case i) end moments are called '*fixed-end moments*' and they will be treated
separately, below.  For now, we will not develop these any further.

Using superposition of all three cases, we can now express the end moments
in terms of displacements and applied loads:

$$
   \begin{split}
   M_{ab} &= M^f_{ab} + M^r_{ab} + M^d_{ab}\\
       &= M^f_{ab} + \frac{EI}{L}(4\theta_a+2\theta_b) + \frac{EI}{L}(-6\Phi_{ab})\\
   M_{ab} &= \frac{EI}{L}(4\theta_a + 2\theta_b - 6\frac{\Delta_{ab}}{L}) + M^f_{ab}
   \end{split}
$$

$$
   \begin{split}
   M_{ba} &= M^f_{ba} + M^r_{ba} + M^d_{ba}\\
       &= M^f_{ba} + \frac{EI}{L}(2\theta_a+4\theta_b) + \frac{EI}{L}(-6\Phi_{ab})\\
   M_{ba} &= \frac{EI}{L}(2\theta_a + 4\theta_b - 6\frac{\Delta_{ab}}{L}) + M^f_{ba}
   \end{split}
$$

<div class="admonition important">
   The _slope-deflection_ equations express end moments as functions of 
   end displacements and applied loads.  They are summarized here:
</div>

$$
      \begin{split}
      M_{ab} &= \frac{EI}{L}(4\theta_a + 2\theta_b - 6\frac{\Delta_{ab}}{L}) + M^f_{ab}\\
      M_{ba} &= \frac{EI}{L}(2\theta_a + 4\theta_b - 6\frac{\Delta_{ab}}{L}) + M^f_{ba}\\
      \end{split}
$$

   where $M^f_{ab}$ and $M^f_{ba}$ are the _fixed-end moments_ due to
   the applied loads.
