---
title: 'Frame Reactions, Part 2'
prev_page:
  url: /text/sdbeams/frame-reactions-1.html
  title: 'Frame Reactions, Part 1'
next_page:
  url: /text/sdbeams/frame-reaction-problems.html
  title: 'Problems - Frame Reactions'
comment: "***PROGRAMMATICALLY GENERATED, DO NOT EDIT. SEE ORIGINAL FILES IN /content***"
---
# 2: Forces in Statically Determinate Beams and Plane Frames

## 2.7: External Reactions in Frames (Part 2)

<div class="admonition note">
   This section by G.A. Hartley.
</div>

### 2.7.4: Reactions in Statically Determinate Frames

We will
now look at examples of statically determinate flexural type
structures and the calculation of reactions. This is preparation for
the next chapter in which we will calculate and plot internal forces
throughout these structures.  Generally we will have to solve for
reactions first before applying the method of sections and solving for
internal forces so that this is a skill we must acquire before going
on to Chapt. 3. Later we will consider statically indeterminate
frames. One basic skill required in the analysis of statically
indeterminate structures is the ability to analyze statically
determinate ones - the process in fact breaks down into a series of
such analyses.

In these, we may often find in the beginning that the calculation of
reactions is a challenge. We may sometimes have to try to resist a
tendency to see the answer (the wrong one) too quickly. There is also
a tendency for it too look easy when the answer is in front of us. So
try all of the problems at the end of the this chapter, or if time
does not permit, at least sketch the FBD's and satisy yourself that
you do know how to do the numbers when required.

The general procedure is already well established from earlier
courses. We either sketch or try to imagine free body diagrams of the
structure or parts of it. The strategy will be to establish equations
to solve for reactions, preferably uncoupled equations having only one
unknown.

**Example 2.7.4-1   Solve for Reactions in a Beam**


![Figure](../../images/sdbeams/frames2/B13.svg)

Figure 2.7.4-16: Example 2.7.4-1

An FBD of the whole beam in Fig.2.7.4-16 or an FBD of the structure to the
left of the hinge, will make it obvious that we want to take moments
(about the hinge) of forces to the left.



![Figure](../../images/sdbeams/frames2/B14.svg)

Figure 2.7.4-17: Example 2.7.4-1

The forces $V_p$ and $H_p$ in Fig. 2.7.4-17 represent the reaction of the
structure to the right of the hinge on the FBD shown. There are no
moments at the hinge. We can sum moments and set these equal to zero
about either the roller or the hinge.

$$
   \begin{split}
   &\sum M_p = 0\\
   &-12 \times 6 \times (4 + 3) + V_r \times 4 = 0.\\
   &V_r = 126.~~~~~\text{(directed as shown)}
   \end{split}
$$

The sign convention for summing moment vectors in the moment
equilibrium equation is clockwise positive. In our later discussions
of internal forces we might stop here and begin plotting the bending
moment and shear forces directly since these are available throughout
by taking FBD's of the structure with cuts isolating left hand
portions. From the solution of $\sum F_x = 0.$, and $\sum F_y = 0.$

$$
   \begin{split}
    &V_p = -54.~~~~~\text{(acting opposite direction shown above)}\\
    &H_p = 0.
   \end{split}
$$

To complete this problem in reaction solving, and as an exercise,
FBD's of both sections are shown. The reader should now spend some
time looking at the complete solution to determine whether the numbers
look correct. Check the total applied load; check to see if forces
balance in both directions; and check to see if the applied reaction
moment is counterbalanced by applied loads. Never assume that, even
for simple problems, the job is done when the numbers have been
computed.

![Figure](../../images/sdbeams/frames2/B15.svg)

Figure 2.7.4-18: Example 2.7.4-1

The next example is one variation of a type of statically determinate
frame that we will see more of in this text. This is called a simply
supported frame. 

**Example 2.7.4-2:   Solve for Reactions in Simply Supported Frame**

We will solve for the 3 base reaction forces in the given frame in Fig. 2.7.4-19.

![Figure](../../images/sdbeams/frames2/B16.svg)

Figure 2.7.4-19: Example 2.7.4-2

The procedure is fairly obvious here since this structure is supported
by pin and roller combination. There is only one FBD to be considered
and it is shown in Fig. 2.7.4-20 and indicates the general approach.



![Figure](../../images/sdbeams/frames2/B17.svg)

Figure 2.7.4-20: Example 2.7.4-2

There are 2 unknowns at the pin, and one at the roller. This suggests
taking moments about the pin. So we will establish the routine that
generally when we have a pin and roller combination, we take moments
about the pin. The reader will note that the horizontal reaction is
available by inspection and has the value given on the free body
diagram, therefore moments could be taken about the right hand
reaction. We will save that equation for the calculation of $V_l$ and use
the simple $\sum F_y$ equation as a check.

$$
   \begin{split}
   &\sum M_l = 0\\
   &  40 \times 2.5 + 25 \times 5^2/2 - V_r \times 5 = 0.\\
   & Vr = 82.5~\mathrm{kN}\\
   &\sum M_r = 0\\
   &  40 \times 2.5 + V_l \times 5 - 25 * 5^2/2 = 0.\\
   & V_l = 42.5~\text{kN}~~~~~\text{ (as shown)}\\
   \\
   &\mathrm{check} \sum F_y:  25 * 5 = 125 = 82.5 + 42.5~~~~~\text{O.K.}\\
   \end{split}
$$

In the second equation for $\sum M_r$ we have combined the two 40 kN forces
as a single couple, taking into account the couple's direction (CW).

**2.7.4-2: Three-Hinged Frames**

The next example is another generic type of statically determinate
frame. This is a *three hinged frame*, and once again we can adopt
routine procedures for the calculation of reactions.

With experience at solving these problems, we start making educated
guesses about the directions of unknown forces on free body
diagrams. In other words putting these forces on the FBD exactly the
way we know they go. Mathematics will always take care of the signs if
directions are taken incorrectly. When the signs change from those
originally assumed in the FBD, it slows us down by requiring
additional FBD's to show the correct orientation of forces. It also
creates confusion, since we will have in our notes the same forces
going in different directions. An experienced analyst will not feel
comfortable with forces on FBD's whose direction clearly indicates
that equilibrium is not satisfied.


**Example 2.7.4-3   Solve for Reactions in Three-Hinged Frame**

![Figure](../../images/sdbeams/frames2/B18.svg)

Figure 2.7.4-21: Example 2.7.4-3

There are four base reactions in Fig. 2.7.4-21, indicating that we must
take advantage of the zero moment condition at the internal
hinge. Before we do this, however, we note from the FBD in Fig. 2.7.4-22
that the pinned supports at the base align horizontally. This may not
always be the case, but we will come across this arrangement often
enough for this type of structure that we should watch for it. This
provides the condition that the horizontal reactions are in-line and
do not provide a contribution to moments about either reaction.

![Figure](../../images/sdbeams/frames2/B19.svg)

Figure 2.7.4-22: Example 2.7.4-3

The first step in calculating the reactions, therefore, will be to
take moments about either the left or right support and calculate the
vertical reaction at the other support. Following this we could
calculate the other vertical reaction.

Taking moments about the left support:

$$
   \begin{split}
   &\sum M_l = 0\\
   &  10 \times 8.5 - V_r \times 10 = 0.\\
   & V_r = + 8.5~~~~~\text{(plus indicates directed as shown)}
   \end{split}
$$

Now we take moments about the interior hinge. It may be easier to
sketch an FBD of the partial structure to the left (or the right) of
the interior hinge. After some experience this step can be
avoided. Inspection of the previous FBD indicates that Hr is not in
the direction shown. We can see this in two ways from the FBD in
Fig. 2.7.4-23.

![Figure](../../images/sdbeams/frames2/B20.svg)

Figure 2.7.4-23: Example 2.7.4-3

First the member is a two-force member, having a pin at each end and
no loads between the joints. The directions of components $H_r$ and $V_r$ at
the base, if correct, creates a transverse shear, which is not
possible. Therefore $H_r$ must be opposite the direction shown. The
second way to see this is to imagine moments about the upper
hinge. Both forces give rise to the same direction of moment about the
top pin which again is not possible for equilibrium.

The complete solution of this three-hinged arch is given below,
showing the true directions of all external and internal reactions.



![Figure](../../images/sdbeams/frames2/B21.svg)

Figure 2.7.4-24: Example 2.7.4-3

Once the forces in the right hand strut have been calculated we
transfer these with equal and opposite directions to the point on the
other section in accordance with Newton's Third Law of
action/reaction. From this second FBD we can obtain the two remaining
lower left reactions using equilibrium equations.  An appropriate way
to do these calculations is to apply $\sum F_x$ and $\sum F_y$ and then apply a
moment equation to confirm the results. As an exercise it is
recommended that once again you pause and try some moment calculations
about any of the 3 exterior member edges in the second FBD, or take
some time to reflect on whether the forces seem to be creating moment
equilibrium in the Fig. 2.7.4-24.

**2.7.4-3:  Propped Cantilever Frames**

In this last example, the ability to look at the computed results as
presented in the final FBD and determine by inspection whether they
make sense is indispensible. The presentation of results for reactions
on FBD's is desirable for 4 reasons. If these are quiz problems being
marked, the marker knows exactly what was computed, including
directions. Secondly, when we look at diagrams like this, equilibrium
errors tend to reveal themselves. Thirdly, Newton's Third Law of
action/reaction must be adhered to and the internal forces at hinges
for example clearly shows this. Finally, if the objective of the
exercise is moment and shear diagrams, a diagram such as this is an
excellent place to start and makes the plotting of these diagrams
easier, and having the load/reaction FBD on the same page as the
bending moment and shear diagrams shows clearly the mathematical
relationships between them.

A final problem in this chapter will introduce a third generic
statically determinate frame, the *propped cantilever with internal
articulation*.


**Example 2.7.4-4:   Solve for Reactions in a Propped Cantilever Frame**

![Figure](../../images/sdbeams/frames2/B22.svg)

Figure 2.7.4-25: Example 2.7.4-4


The condition of zero moment at the internal hinge described earlier
in Example 2.7.4-3 is again the key to starting our calculations in this
problem. We can do this immediately because the roller in Fig. 2.7.4-25
has a single vertical reaction. In a manner similar to Ex. 2.7.4-1 we can
start the analysis with the simple supported portion of the structure.



![Figure](../../images/sdbeams/frames2/B23.svg)

Figure 2.7.4-26: Example 2.7.4-4

We first calculate the vertical reactions in the simply supported
portion and then, sketching both FBD's as shown in Fig. 2.7.4-26, we take
care, as we did in the previous problem, to adhere to Newton's Third
Law of action/reaction. The computations are not complete in this case
until, as example, the student has confirmed the direction of the base
moment in the left hand FBD and the reversal of direction in the shear
at the pin between the right and left segments of the structure.

**2.7.4-5: Summary and Advice**

Once again the student is strongly encouraged to prepare neat sketches
such as the one shown above. Then look at it carefully in order to get
an intuitive feel for the subject which goes beyond the crunching of
numbers.

Some of the exercise problems at the end of this chapter are
variations of the example problems. Watch for these variations. The
mastery of these calculations will be important throughout the course,
and especially important in the next chapter, and a later chapter
dealing with indeterminate structures. Before proceeding the student
should feel confident that the material presented to this point is
understood.
