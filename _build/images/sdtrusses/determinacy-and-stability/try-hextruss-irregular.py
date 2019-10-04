import sys
sys.path = ["../../../software/determinate-truss/python"] + sys.path
from sdtruss import sdtruss

jc = [ ('a', 0, 0),
       ('b', 0, 4),
       ('c', 3, 8),
       ('d', 7, 8),
       ('e', 10, 4),
       ('f', 10, 0),
       ]

mi = [ ('a', 'b',),
       ('b', 'c',),
       ('c', 'd',), 
       ('d', 'e',),
       ('e', 'f',),
       ('f', 'a',),
       ('b', 'e',),
       ('c', 'f',),
       ('a', 'd',),
       ]

rf = [ ('a', 1, 0),             # reaction force dirns
       ('a', 0, 1),
       ('f', 0, 1),
       ]

jl = [ ('c', 100.0, 1, 0),      # joint loads (j, p, dx, dy)
       ]

sdtruss( jc, mi, rf, jl )
