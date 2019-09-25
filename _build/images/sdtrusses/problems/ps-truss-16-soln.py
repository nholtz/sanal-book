import sys
sys.path = ["../../../../software/determinate-truss/python"] + sys.path
from sdtruss import sdtruss

jc = [ ('a', 0, 0),
       ('b', 2, 2),
       ('c', 4, 4),
       ('d', 6, 2),
       ('e', 8, 0),
       ('f', 4, 2),
       ]

mi = [ ('a', 'b'),
       ('b', 'c'),
       ('c', 'd'),
       ('d', 'e'),
       ('a', 'f'),
       ('f', 'e'),
       ('b', 'f'),
       ('f', 'd'),
       ('c', 'f'),
       ]

rf = [ ('a', 1, 0),             # reaction force dirns
       ('a', 0, 1),
       ('e', 0, 1),
       ]

jl = [ ('c', 10, 1, 0),
       ('d', 20, 1, 0),
       ('f', 16, 0, -1),
       ]

sdtruss( jc, mi, rf, jl )
