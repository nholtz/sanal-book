import sys
sys.path = ["../../../../software/determinate-truss/python"] + sys.path
from sdtruss import sdtruss

jc = [ ('a', 0, 0),
       ('b', 4, 2),
       ('c', 8, 4),
       ('d', 12, 2),
       ('e', 16, 0),
       ('f', 12, 0),
       ('g', 8, 0),
       ('h', 4, 0),
       ]

mi = [ ('a', 'b',),
       ('b', 'c',),
       ('c', 'd',), 
       ('d', 'e',),
       ('a', 'h',),
       ('h', 'g',),
       ('g', 'f',),
       ('f', 'e',),
       ('b', 'h',),
       ('b', 'g',),
       ('c', 'g',),
       ('g', 'd',),
       ('d', 'f',),
       ]

rf = [ ('a', 1, 0),             # reaction force dirns
       ('a', 0, 1),
       ('e', 0, 1),
       ]

jl = [ ('a', 20.0, 2, -4),      # joint loads (j, p, dx, dy)
       ('b', 40.0, 2, -4),
       ('c', 20.0, 2, -4),
       ]

sdtruss( jc, mi, rf, jl )
