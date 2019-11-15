---
title: 'Method of Sections'
prev_page:
  url: /text/sdtrusses/method-of-joints.html
  title: 'Method of Joints'
next_page:
  url: /text/sdtrusses/worked-examples.html
  title: 'Worked Examples'
comment: "***PROGRAMMATICALLY GENERATED, DO NOT EDIT. SEE ORIGINAL FILES IN /content***"
---
# 3: Forces in Statically Determinate Trusses

## 3.4: Method of Sections

<div class="admonition note">
   This section by G. A. Hartley, damaged by N. M. Holtz.
</div>

### 3.4.1: Introduction

In the Method of Joints, we considered each joint in the structure in
turn and the forces acting at each point. We had available 2 equations
which could be used in this procedure.

Now we look at a method in which we isolate a portion of the truss by
making a cut through it. The purpose of the procedure is to calculate
only one, or perhaps a small number of bar forces in the interior of
the structure. Whereas the method of joints is a routine procedure for
calculating all bar forces in a truss, we may sometimes wish to
calculate one or two bar forces. This can be important, for example,
during stages of design of the structure when we are trying design
configurations. We find that with some trusses, particularly tied
trusses, we sometimes can't get the method of joints process started
because each external joint has 3 or more unknowns. The trick is to
start the process using the method of sections, and then to proceed by
method of joints.

We do the sectioning in a judicious way, and once more we will not
have many rules to guide us. The skill is developed through experience
and we will try to acquire some of this experience in the remainder of
this chapter.

In the method of sections process, we will usually find all three
equations of equilibrium (in a plane) useable since the forces systems
are normally general (i.e., neither concurrent nor parallel). The
strategy will be to try to generate in one step the equation in the
one unknown we are seeking. It may not always be possible to
accomplish this. It may require the calculation of another bar force
first, or we may have to solve simultaneous equations.

Before we look at an example this is the rule of play:

<div class="admonition note">
   **Procedure:** In applying sections, the cut must go right through
   the truss. It is preferable not to cut through joints, but rather
   the cut should pass through members. Care must be taken that each
   FBD of the isolated section has all approriate forces applied to
   it.
</div>

This is similar to taking sections in beams and frames where we are
trying to calculate internal shear and bending moment. We create, in
this way, a free body in isolation from the rest of the structure with
the exposed internal forces as unknowns in equilibrium equations.

### 3.4.2 Example S-1

![Figure](../../images/sdtrusses/equilibrium/sections/section-1-truss.svg)

Figure 3.4-1: Example S-1

The truss in Fig. 3.4-1 is a compound truss similar to the tied arch
trusses of Section 3.2. The "tie" in this case can be the tension
member A, or its symmetrical counterpart, or the members in the two
triangle unit at the top can be considered compression ties. We can
solve for the reactions at the simple supports, but will not be able
to proceed further until we have calculated a bar force using the
method of sections.


![Figure](../../images/sdtrusses/equilibrium/sections/section-1-fbd1.svg)

Figure 3.4-2: FBD of portion


The section cut is taken just to the left of the loaded joint at the
top and through member "A". In the FBD of the structure to the right
of the cut, we notice that there are four unknown member forces.
However, three of them pass through the top loaded joint, so we can
take moments about that joint to solve for one of the unknowns.  To do
that, we resolve the unknown force, $F_A$ into horizontal and vertical
components at the support joint:

$$
   \begin{split}
   &\sum M = 0~~~~~(\text{+CCW})\\
   &150\times2 - \frac{2}{\sqrt{5}}\times F_A \times 8 + \frac{1}{\sqrt{5}}\times F_A \times 2 = 0\\
   &F_A = 47.92 \text{kN}~~~~~(\therefore T)
   \end{split}
$$

Numerically we will not proceed further with Example S-1, but it
should be evident that the solution can now be completed using the
method of joints.

We have just seen method of sections used as a means of "kick
starting" the method of joints where there are no available joints
with only 2 unknowns at the outset. It can also be used when only a
limited number of bar forces are to be calculated, and this could have
a number of applications in structural engineering.

### 3.4.3 Example S-2

![Figure](../../images/sdtrusses/equilibrium/sections/cantilever-1.svg)

Figure 3.4-3: Cantilever Truss

Consider the example shown in Fig. 3.4-3.  Member 1 appears to be a
critical member, from the design perspective, as it has a relatively
high compression force from the given load case.


![Figure](../../images/sdtrusses/equilibrium/sections/cantilever-2.svg)

Figure 3.4-4: Modified Design

Consider the design modification in Fig. 3.4-4.  Member 2 has been
relocated to the other diagonal of the square panel it is within.


![Figure](../../images/sdtrusses/equilibrium/sections/cantilever-1-section1.svg)

Figure 3.4-5: Cut through member 1

This apparently does lead to an improvement in the force in member 1,
as we can verify by applying the method of sections to the first
design of Fig. 3.4-3, as shown in Fig. 3.4-5.  Here we see that there
the forces in member 1 and 2 together provide equilibrium for $\sum M$
about the upper joint.  If we drew a comparable section FBD for the
original design, we would see that only member 1 would resist the
moment, and thus the force in member 1 would be higher in that design.


![Figure](../../images/sdtrusses/equilibrium/sections/cantilever-1-section2.svg)

Figure 3.4-6: Cut through member 5

What about member 5, however?  By considering the section of
Fig. 3.4-6, of the original design, we see that the compressive force
in 5 is $\sqrt{2}$ times the force in member 1, and it is longer as
well.  Therefore, member 5 is actually the more critical member, and
the modified design does not help that at all.

This example demonstrates that the method of sections is more than a
numerical procedure.  Judicious use can help you can insight into the
behaviour of a structure, and can be used to qualitatively evaluate
different design configurations.


### 3.4.3 Example S-3

![Figure](../../images/sdtrusses/equilibrium/sections/S-3-1.svg)

Figure 3.4-7: K Truss

Continuing the discussion of the method of sections, consider the "K"
truss shown in Fig. 3.4-7.


![Figure](../../images/sdtrusses/equilibrium/sections/S-3-2.svg)

Figure 3.4-8: Section

The forces in the four members _i-j_, _k-j_, _k-m_, and _l-m_ can be
calculated by the method of sections as follows.  First, the force in
member _l-m_ can be found by taking moments about joint _i_ in the
sections shown in Figs. 3.4-8 and 3.4-9.


![Figure](../../images/sdtrusses/equilibrium/sections/S-3-3.svg)

Figure 3.4-9: FBD


![Figure](../../images/sdtrusses/equilibrium/sections/S-3-4.svg)

Figure 3.4-10: Section

The remaining three forces can be calculated by taking the section
shown in Figs. 3.4-10 and 3.4-11.


![Figure](../../images/sdtrusses/equilibrium/sections/S-3-5.svg)

Figure 3.4-11: FBD


### 3.4.4 Example S-4

As a final qualitative example, consider the truss of Fig. 3.4-12.

![Figure](../../images/sdtrusses/equilibrium/sections/S-4-1.svg)

Figure 3.4-12: Truss

As a general guideline we should try to avoid taking a section as
shown through a sloping member as the perpendicular distance from the
moment point to that member adds an unnecessary complication.


![Figure](../../images/sdtrusses/equilibrium/sections/S-4-2.svg)

Figure 3.4-13: FBD

The usual techniques is to resolve the unknown force in _A_ into
horizontal and vertical components, and compute moments using those
components.


![Figure](../../images/sdtrusses/equilibrium/sections/S-4-3.svg)

Figure 3.4-14: FBD

In this case we can also avoid having to deal with two components of
the force by taking the section up close to the joint at the right end
of the member. The moment about the lower joint in this section will
involve only the horizontal component of FA in the equilibrium
equation for solving FA.
