---
title: 'Example - Frame 1'
prev_page:
  url: /text/sibeams/flexibility/examples/elastic-support.html
  title: 'Example - Elastic Supports'
next_page:
  url: /text/sibeams/flexibility/examples/frame2.html
  title: 'Example - Frame 2 (Alternate Redundant)'
comment: "***PROGRAMMATICALLY GENERATED, DO NOT EDIT. SEE ORIGINAL FILES IN /content***"
---
# 7: Statically Indeterminate Beams and Plane Frames

## 7.6: Example - Frame Example 1

Determine all of the reactions for the following frame:

![Figure 7.6-1: Frame Example 1](../../../../images/sibeams/flexibility/examples/frame1/frame1-1.svg)

### 1: Statical determinacy

The frame is 1 degree statically indeterminate.

### 2: Identify redundants

![Figure 7.6-2: Free body of real structure](../../../../images/sibeams/flexibility/examples/frame1/frame1-2.svg)

Choose the vertical reaction at *c* ($V_c$) as the redundant.

### 3: Analyze the primary structure

![Figure 7.6-3: Determinate structure with real loads](../../../../images/sibeams/flexibility/examples/frame1/frame1-3.svg)

### 4: Apply unit values of the redundants

![Figure 7.6-4: Determinate structure with unit redundants](../../../../images/sibeams/flexibility/examples/frame1/frame1-4.svg)

### 5: Compute Displacements in the primary structure

![Figure](../../../../images/sibeams/flexibility/examples/frame1/frame1-5.svg)

### 6: Compute flexibilty coefficients

![Figure](../../../../images/sibeams/flexibility/examples/frame1/frame1-6.svg)

### 7: Write compatibilty equations

The real vertical displacement at point *c* is zero, therefore:

$$
\begin{split}
0 &= \Delta_{10} + V_c f_{11}\\
  &= -\frac{24 P L^3}{E I_0} + V_c \times \frac{81 L^3}{2 E I_0}
\end{split}
$$

### 8: Solve for the redundant

$$V_c = \frac{16}{27} P$$

### 9: Other reactions by superposition

$$
\begin{split}
M_a &= M_{a0} + V_c m_{a1} \\
    &= 4PL +  \frac{16}{27} P \times -3L \\
	&= \frac{20}{9} P L\\
H_a &= H_{a0} + V_c h_{a1} \\
    &= P + \frac{16}{27} P \times 0 \\
	&= P\\
V_a &= V_{a0} + V_c v_{a1} \\
    &= 0 + \frac{16}{27} P \times -1 \\
	&= -\frac{16}{27} P
\end{split}
$$

### 10: Summary

![Figure 7.6-5: Summary of Frame Example 1](../../../../images/sibeams/flexibility/examples/frame1/frame1-7.svg)
