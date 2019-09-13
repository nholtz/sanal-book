# 2: Forces in Statically Determinate Beams and Plane Frames

## 2.6: Reactions in Beams - Examples

### Example 2.6-1:

Figure 2.3-1 shows a structural model of a beam with three supports
and an internal hinge.

![Figure](../../images/sdbeams/eg-beams/br-example-1-0.svg)

Fig. 2.3-1: Beam Example 1

In order to analyze it, it must be both stable and statically
determinate.  We can tell by inspection that it is stable
(because it is not possible to find a mechanism, chiefly
because member _b-c-d-e_ is constrained to remain straight and 
without displacement). Counting
the unknowns and equations, we have _m=3_, _r=4_, _j=4_, and _c=1_, so
_3m+r=13_, and _3j+c=13_.  These are equal, so the structure is
statically determinate as well.  We can now proceed to draw the free
body diagram of Fig. 2.3-2.

![Figure](../../images/sdbeams/eg-beams/br-example-1-1.svg)

Fig. 2.3-2: Free Body Diagram of Complete Structure

We see there are 4 unknowns, but only 3 equations of equilibrium, so
we cannot solve for all unknowns on this FBD.  We can solve for one of
them, as the resulting equation for $\sum F_x$ has only one unknown:

$$
   \begin{split}
   \sum F_x &= 0~~~~{\text{+}}\rightarrow\\
   H_c + 0 &= 0\\
   H_c &= 0
   \end{split}
$$

However, that is all we can do.  We have three unknowns remaining, but
only two equations.

<div class="admonition important">
   You may be able to "tell by inspection" that $H_c=0$, but that does
   not help you very much.  You use an equation of equilibrium to
   determine that, and you now have only two remaining.
</div>

Obviously, we must draw a different free body diagram.  The structure
has a release condition, the internal hinge, so we can break the
structure there and draw an FBD of the right portion, as shown in by
**FBD-2** in Fig. 2.3-3.

![Figure](../../images/sdbeams/eg-beams/br-example-1-2.svg)

Fig. 2.3-3: Free Body Diagram of Right Portion

Unfortunately, we can't solve for much here, either.  $H_c$ is known
to be 0 from **FBD-1**, leaving us with 4 unknowns, but only three
equations.  We could solve for $H_b=0$, but that is all.  We have to
look at the other portion of the structure, **FBD-3** as shown in
Fig. 2.3-4.

![Figure](../../images/sdbeams/eg-beams/br-example-1-3.svg)

Fig. 2.3-4: Free Body Diagram of Left Portion

Notice, that we had already chosen directions for $H_b$ and $V_b$ on
the previous FBD; we now _must_ now show those same internal forces
acting equally and oppositely on the new FBD.  Internal forces
_always_ occur in equal and opposite pairs.

<div class="admonition important">
   When you draw two FBDs that share a contact point, all forces at
   the contact must be shown to be of equal magnitude and opposite
   direction on each of the FBDs.  That is best done by using the same
   symbols, and showing the arrows in opposite directions.
</div>

Using **FBD-3**, we can solve for all three of the unknown forces
acting on it:

$$
   \begin{split}
   \sum F_x &= 0~~~~~\text+ \rightarrow\\
   &= -H_b + 0\\
   H_b &= 0\\
   \\
   \sum M_b &=0~~~~~\text{+CCW}\\
   &= -V_a\times6 + 20\times6\times{6\over2}\\
   V_a &= 60~~~~~(\therefore \uparrow)\\
   \\
   \sum F_y &= 0~~~~~\text+\uparrow\\
   &= V_a - 20\times6 - V_b\\
   &= 60 - 120 - V_b = 0\\
   V_b &= -60~~~~~(\therefore\uparrow)
   \end{split}
$$

We notice that $V_b$ acts upwards on _b_, not downwards as we had
assumed (thats about the only significance of the minus sign in the
value computed for $V_b$ -- it just tells us we drew the wrong
direction on the FBD).

<div class="admonition important">
   Negative answers from solving equilibrium equations tell you that
   you had the unknown forces shown in the wrong direction on the FBD.
</div>

Knowing $V_a$ (and $H_a$), we can now return to **FBD-2**, there are
now only three unknowns and we can solve them all:

$$
   \begin{split}
   \sum M_c &= 0~~~~~\text{+CCW}\\
   &= -V_b\times4 + 20\times6\times(4-{6\over2}) + V_d\times6 - 50\times8\\
   &=-(-60)\times4 + 120 + 6V_d - 400\\
   6V_d &= 40\\
   V_d &= 6.67~~~~~(\therefore\uparrow)\\
   \end{split}
$$

Note that we very carefully first wrote equation using the direction
of the forces as shown on **FBD-1**, then substituted in the correct
numerical values, including sign.  This reduces the likelihood of
getting the signs wrong.

<div class="admonition important">
   Minimize the number of steps you 'do in your head'.  Write
   equilibrium equations with signs derived from the direction of
   forces shown on the FBD, then substitue numerical values for the
   knowns, with correct signs.
</div>

We can use a second moment equation to get the other vertical reaction:

$$
   \begin{split}
   \sum M_d &= 0~~~~~\text{+CCW}\\
   &= -V_b\times10 + 20\times6\times(10-3) - V_c\times6 - 50\times2\\
   &= -(-60)\times10 + 840 - 6 V_c - 100\\
   V_c &= 223.33~~~~~(\therefore\uparrow)
   \end{split}
$$

To complete this portion, we redraw the FBD of the whole structure,
showing all forces in their proper directions, and rounding numerical
values to 3 significant digits (with the largest value setting the
number of decimal points).  This is seen in Fig. 2.3-5.

![Figure](../../images/sdbeams/eg-beams/br-example-1-4.svg)

Fig. 2.3-5: Result Free Body Diagram

**Summary**

All of the diagrams above are repeated on a single drawing here
for ease of reading:

![Figure](../../images/sdbeams/eg-beams/br-example-1-5.svg)

Fig. 2.3-6: Summary Free Body Diagrams




### Example 2.3-2:

Figure 2.3-6 shows Example 2:

![Figure](../../images/sdbeams/eg-beams/br-example-2-0.svg)

Fig. 2.3-6: Beam Example 2

We can quickly tell that it is stable and statically determinate, and
that we can solve for the reaction at b if we draw a free body diagram
of portion _a-b-c-d_, as shown in Fig. 2.3-7:

![Figure](../../images/sdbeams/eg-beams/br-example-2-1.svg)

Fig. 2.3-7: Free Body of Left Portion

Note that there is a 40kN load applied at point _d_.  For simplicity
we did not show it on FBD-1, above.  However, that means if we draw a
free body of portion _d-e_, we _must_ show the 40kN load acting on
that one.  In cases like this, where a concentrated load is applied to
the same point at which we cut, we should think of the cut being just
to one side of the load, and it doesn't matter which side, as long as
we are consistent.  If we show the load on one FBD of a pair sharing
the common point, we must _not_ show it on the other.


<div class="admonition important">
   Concentrated forces applied to points at which we 'cut' the
   structure must be shown on only one of the two possible free body
   diagrams.
</div>

$$
   \begin{split}
   \sum M_d &= 0~~~~~\text{+CCW}\\
   &= 100\times8 + 150 - V_b\times6\\
   V_b  &= 158.33~~~~~(\therefore\uparrow)\\
   \\
   \sum F_y &= 0~~~~~\text+\uparrow\\
   &= -100 + V_b + V_d\\
   &= -100 + 158.33 + V_d\\
   V_d &= -58.33~~~~~(\therefore\downarrow)
   \end{split}
$$

If we now draw a free body diagram of just portion _d-e_, at point _d_
we would now show a force of 58.33 acting upward (the reaction from
_a-b-c-d_) plus a force of 40kN acting upward (because we didn't show
it on the left FBD).  However, instead will will show the whole
structure, as in Fig. 2.3-8:

![Figure](../../images/sdbeams/eg-beams/br-example-2-2.svg)

Fig. 2.3-8: Free Body of Complete Strcture

$$
   \begin{split}
   \sum F_x &= 0~~~~~\text+\rightarrow\\
   &= H_e\\
   H_e &= 0\\
   \\
   \sum F_y &= 0~~~~~\text+\uparrow\\
   &= -100 + 158.33 + 40 -{ {15+25} \over2}\times8 + V_e\\
   V_e &= 61.67~~~~~(\therefore\uparrow)\\
   \\
   \sum M_e &= 0~~~~~\text{+CCW}\\
   &= 100\times16 - 158.33\times14 + 150 - 40\times8 + (15\times8\times{8\over2}) + ((25-15)\times{8\over2}\times{8\over3}) - M_e\\
   M_e &= -200 \text{kN-m}~~~~~(\therefore \text{CCW})
   \end{split}
$$

And finally, we show the summary free body diagram:

![Figure](../../images/sdbeams/eg-beams/br-example-2-3.svg)

Fig. 2.3-9: Results Free Body Diagram

**Summary**

And all of the above diagrams repeated on one figure here
for ease of reading:

![Figure](../../images/sdbeams/eg-beams/br-example-2-4.svg)

Fig. 2.3-9: Summary Free Body Diagrams

