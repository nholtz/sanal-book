---
title: 'Matrix Methods'
prev_page:
  url: /text/sdtrusses/worked-examples.html
  title: 'Worked Examples'
next_page:
  url: /notebooks/sdtrusses/sdtruss.html
  title: 'Matrix Methods Implementation'
comment: "***PROGRAMMATICALLY GENERATED, DO NOT EDIT. SEE ORIGINAL FILES IN /content***"
---
# 3: Forces in Statically Determinate Trusses

## 3.6: Matrix Methods of Determinate Truss Analysis

### 3.6.1: Introduction

![Figure](../../images/sdtrusses/equilibrium/matrix/intro-truss.svg)

   Figure 3.6-1a: Three Bar Truss

This section introduces a more mechanical method of solvinf statically
determinat etrusses, and thus one that is more amenable to
computer-based solutions.  Many of the concepts introduced here will
be used in more advanced matrix methods later in your studies.

The method is based on the method of joints, and simply involves
writing all possible joint equilibrium equations and expressing the
resulting system in matrix form.

As an example, consider the simple three-bar truss shown in Fig. 3.6-1a. 


![Figure](../../images/sdtrusses/equilibrium/matrix/intro-fbds.svg)
   
Figure 3.6-1b: Joint FBDs

The free body diagrams of all three joints are shown in Fig. 3.6-1b.
We will write the two equilibrium equations at each joint as follows.

Joint a:

$$
   \begin{split}
   \sum F_x &= 0.8 T_{ab} + T_{ac} + H_a = 0\\
   \sum F_y &= 0.6 T_{ab} + V_a = 0
   \end{split}
$$

Joint b:

$$
   \begin{split}
   \sum F_x &= -0.8 T_{ab} + 60 = 0\\
            &~~~-0.8 T_{ab} = -60\\
   \sum F_y &= -0.6 T_{ab} - T_{bc} = 0\\
   \end{split}
$$


Joint c:

$$
   \begin{split}
   \sum F_x &= -T_{ac} = 0\\
   \sum F_y &= T_{bc} + V_c = 0
   \end{split}
$$


When doing this manually, we take pains to write the equations in the
correct order, with as few unknowns in each as possible, and solve as
we go.  But here, we simply assemble all six equilibrium equations into one matrix
expression:

$$
   \left[
   \begin{array}{ccccc}
   0.8 & 1 & 0 & 1 & 0 & 0\\
   0.6 & 0 & 0 & 0 & 1 & 0\\
   -0.8 & 0 & 0 & 0 & 0 & 0\\
   -0.6 & 0 & -1 & 0 & 0 & 0\\
   0 & -1  & 0 & 0 & 0 & 0\\
    0 & 0 & 1 & 0 & 0 & 1
   \end{array}
   \right]
   \left\{\begin{array}{c}T_{ab}\\T_{ac}\\T_{bc}\\H_a\\V_a\\V_c\end{array}\right\}
   =
   \left\{\begin{array}{c}0\\0\\-60\\0\\0\\0\end{array}\right\}
$$

or, in symbolic form:

$$
   \left[C\right] \left\{Q\right\} = \left\{P\right\}
$$

Solving, we have:

$$
   \left\{Q\right\} = \left[C\right]^{-1} \left\{P\right\} = 
   \left\{\begin{array}{r}75\\0\\-45\\-60\\-45\\45\end{array}\right\} =
   \left\{\begin{array}{c}T_{ab}\\T_{ac}\\T_{bc}\\H_a\\V_a\\V_c\end{array}\right\}  
$$

Fortunately, the creation of the matrices is easy to mechanize, as
shown in the following sections.

### 3.6.2: Development of General Method

![Figure](../../images/sdtrusses/equilibrium/matrix/member-1.svg)

Figure 3.6-2: Truss Portion

Fig. 3.6-2 part a) shows two joints in a truss, _i_ and _j_, and the
member _k_ that connects between them.  Also shown are other members
that frame into each joint, as well as the components of the loads, _P_, that are
applied to each joint.

To develop the equilibrium equations, we shall refer to part b) of
that figure which shows some dimensions, the forces corresponding to
member _k_, and the indices for the equilibrium equations to be developed:
_2i-1_ and _2i_ at joint _i_, and _2j-1_ and _2j_ at joint _j_.

We first define some of the geometric quantities:

$$
   \begin{split}
   \Delta_x &= x_j - x_i\\
   \Delta_y &= y_j - y_i\\
   L_k &= \sqrt{\Delta_x^2 + \Delta_y^2}\\
   l_{ij} &= \cos \theta_x = \Delta_x / L_k\\
   m_{ij} &= \cos \theta_y = \Delta_y / L_k
   \end{split}
$$

<div class="admonition important">
$l_{ij}$ and $m_{ij}$ are the <em>directional cosines</em> of the line from node $i$ to node $j$.
</div>

The equilibrium equation that corresponds to $\sum F_x=0$ at joint _i_
is equation number $2i-1$.  The equation itself, showing only the
contribution of member _k_ and the applied load, is:

$$
   \cdots + \cos\theta_x Q_k + \cdots + P_{ix} = 0
$$

or, rewriting to have only unknowns on the left and knowns on the
right:

$$
   \begin{split}
   &\cdots + l_{ij} Q_k + \cdots = -P_{ix}~~~~~~~~~~~~~~~~&(\sum F_x @ i)
   \end{split}
$$

Similarly, the other three equilibrium equations can be written directly:

$$
   \begin{split}
   &\cdots + m_{ij} Q_k + \cdots = -P_{iy}~~~~~~~~~~~~~~~~&(\sum F_y @ i)\\
   &\cdots - l_{ij} Q_k + \cdots = -P_{jx}~~~~~~~~~~~~~~~~&(\sum F_x @ j)\\
   &\cdots - m_{ij} Q_k + \cdots = -P_{jy}~~~~~~~~~~~~~~~~&(\sum F_y @ j)
   \end{split}
$$

We note that these four equations are the only ones in which the force
in member _k_ participates.  As there is one column in the **[C]**
matrix for each unknown, this gives us a way to easily and
mechanically construct the **[C]** matrix.  For each member, _k_, we
calculate the two directional cosine, and place them in 4 locations in
the column corresponding to member _k_, all other values in that
column being zero.  This is shown in Fig. 3.6-3.

![Figure](../../images/sdtrusses/equilibrium/matrix/member-2.svg)

Figure 3.6-3: Matrix Equations

In this figure, we show the four rows corresponding to the four
equilibrium equations developed above.  Column _k_ is the only column
that contains any data relevant to unknown _k_ (i.e., member _k_).  In
that column we show the four non-zero values derived from the geometry
of member _k_; all other entries in that column are zero.

To handle the unknowns corresponding to the reaction forces, we
observe that each of those impinges on only one joint and so will be
included in no more than two equilibrium equations.  We simply
determine the directional cosines of each reaction force vector, and
enter those in the column corresponding to that unknown, in the rows
appropriate for the joint on which it acts (rows _2i-1_ and _2i_ for
joint _i_).  This is easily seen in the example in the following
section.


### 3.6.3: Example M-1

![Figure](../../images/sdtrusses/equilibrium/matrix/example-m-1-truss.svg)

Figure 3.6-4: Example M-1

We are to solve the truss of Fig. 3.6-4 by the matrix method of
joints.  The figure shows the joints and unknowns numbered
sequentially starting from 1.  Joints are numbered thus: _1_ and
unknowns thus: **1**.


![Figure](../../images/sdtrusses/equilibrium/matrix/example-m-1-table.svg)

Figure 3.6-5: Example M-1 - Table of Member Data

Fig. 3.6-5 shows the tabular data used to compute the directional
cosines of all the unknowns.  Unknowns 1 through 7 are member forces,
and so the geometry calculations developed in the previous section are
used.

Unknowns 8, 9 and 10 are reaction forces.  Their directional cosines
are computed directly from the figure.  Each of these, of course,
touch only one joint.

The values for unknown 3 are highlighted so we can more easily observe
how the values are used to construction the **[C]** matrix.


![Figure](../../images/sdtrusses/equilibrium/matrix/example-m-1-matrix.svg)

Figure 3.6-6: Example M-1 - Matrix Equations **[C]{Q}={P}**

The resulting matrix equations are shown in Fig. 3.6-6.

Note column 3 of the **[C]** matrix.  The directional cosines from row
three of the table were placed there and are shown highlighted.  The
pair of directional cosines are placed directly in rows 1 and 2; those
are the rows corresponding to the _i_ joint of member 3 (joint 1).
The negatives of the directional cosines are placed in rows 7 and 8;
these are the rows corresponding to the equilibrium equations for the
_j_ joint of member 3 (joint 4).


Fig. 3.6-7, below, shows input prepared for Octave (i.e., Matlab) to perform the solution.

![Figure](../../images/sdtrusses/equilibrium/matrix/example-m-1-octave-in.svg)

Figure 3.6-7: Example M-1 - Input to Octave

Fig. 3.6-7, below, shows the results displayed by Octave.  In
particular, the member and reaction forces are shown.

![Figure](../../images/sdtrusses/equilibrium/matrix/example-m-1-octave-out.svg)

Figure 3.6-8: Example M-1 - Results from Octave


<div class="admonition important">
   You should now perform a statics check to verify the results.
</div>

![Figure](../../images/sdtrusses/equilibrium/matrix/example-m-1-summary.svg)

Figure 3.6-9: Example M-1 - Summary of Forces

The summary of the forces are shown in Fig. 3.6-9.

Note that in interpreting the results of Fig. 3.6-8, all development
was based on tension forces in members being positive.  Therefore,
negative values for these means the forces are compressive (members 4
and 7).  Negative values for the reactions simply means they act in a
direction opposite to that given by the directional cosines (reaction
9).


