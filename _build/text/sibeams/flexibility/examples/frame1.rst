8: Statically Indeterminate Beams and Plane Frames
=====================================================

8.2: Examples
---------------

8.2.5: Frame Example 1
...........................

Determine all of the reactions for the following frame:

.. figure:: frame1-1.png
   :align: center

   Figure 8.2.5-1: Frame Example 1

1: Statical determinacy
,,,,,,,,,,,,,,,,,,,,,,,,,

The frame is 1 degree statically indeterminate.

2: Identify redundants
,,,,,,,,,,,,,,,,,,,,,,,,,,,

.. figure:: frame1-2.png
   :align: center

   Figure 8.2.5-2: Free body of real structure

Choose the vertical reaction at *c* (:math:`V_c`) as the redundant.

3: Analyze the primary structure
,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,

.. figure:: frame1-3.png
   :align: center

   Figure 8.2.5-3: Determinate structure with real loads

4: Apply unit values of the redundants
,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,

.. figure:: frame1-4.png
   :align: center

   Figure 8.2.5-4: Determinate structure with unit redundants

5: Compute Displacements in the primary structure
,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,

.. figure:: frame1-5.png
   :align: center

6: Compute flexibilty coefficients
,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,

.. figure:: frame1-6.png
   :align: center

7: Write compatibilty equations
,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,

The real vertical displacement at point *c* is zero, therefore:

.. math::
  
   \begin{split}
   0 &= \Delta_{10} + V_c f_{11}\\
     &= -\frac{24 P L^3}{E I_0} + V_c \times \frac{81 L^3}{2 E I_0}
   \end{split}

8: Solve for the redundant
,,,,,,,,,,,,,,,,,,,,,,,,,,,,,

.. math::

   V_c = \frac{16}{27} P

9: Other reactions by superposition
,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,

.. math::

   \begin{split}
   M_a &= M_{a0} + V_c m_{a1} = 4PL +  \frac{16}{27} P \times -3L = \frac{20}{9} P L\\
   H_a &= H_{a0} + V_c h_{a1} = P + \frac{16}{27} P \times 0 = P\\
   V_a &= V_{a0} + V_c v_{a1} = 0 + \frac{16}{27} P \times -1 = -\frac{16}{27} P
   \end{split}

10: Summary
,,,,,,,,,,,,,,,,

.. figure:: frame1-7.png
   :align: center

   Figure 8.2.5-5: Summary of Frame Example 1
