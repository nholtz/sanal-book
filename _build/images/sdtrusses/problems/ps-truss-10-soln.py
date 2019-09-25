import sys
sys.path = ["../../../../software/determinate-truss/python"] + sys.path
from sdtruss import sdtruss

jc = [ ('a', 0, 1),
       ('b', 1, 1),
       ('c', 2, 1),
       ('d', 3, 1),
       ('e', 0, 0),
       ('f', 1, 0),
       ('g', 2, 0),
       ('h', 3, 0),
       ]

mi = [ ('a', 'b'),
       ('b', 'c'),
       ('c', 'd'),
       ('e', 'f'),
       ('f', 'g'),
       ('g', 'h'),
       ('b', 'e'),
       ('b', 'f'),
       ('b', 'h'),
       ('c', 'g'),
       ('d', 'h'),
       ('g', 'd'),
       ]

rf = [ ('a', 1, 0),             # reaction force dirns
       ('a', 0, 1),
       ('e', 1, 0),
       ('e', 0, 1),
       ]

jl = [ ('f', 1, 0, -1),
       ('g', 1, 0, -1),
       ('h', 1, 0, -1),
       ]

sdtruss( jc, mi, rf, jl )
