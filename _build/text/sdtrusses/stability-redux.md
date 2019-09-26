---
title: 'Stability and Matrix Methods'
prev_page:
  url: /text/sdtrusses/matrix-methods.html
  title: 'Matrix Methods'
next_page:
  url: 
  title: ''
comment: "***PROGRAMMATICALLY GENERATED, DO NOT EDIT. SEE ORIGINAL FILES IN /content***"
---
# 3: Forces in Statically Determinate Trusses

## 3.7: Stability and Matrix Methods


The matrix method is an effective way to determine the stability of
complex trusses.

When you setup the $\left[C\right]$ matrix, check its rank.  If its
rank is less than its size, then the truss is unstable.  Another way
of saying this is: if the determinant is zero, the truss is unstable.

<div class="admonition important">
   An unstable truss has a singular $\left[C\right]$ matrix (i.e., its rank is
   less than its size).  Of course, computing rank is subject to floating point truncation errors.
</div>

<div class="admonition note">
   More to come.
</div>
