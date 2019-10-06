import sys
#sys.path = ["../../../software/determinate-truss/python"] + sys.path
sys.path = ["../../../notebooks/sdtrusses"] + sys.path
from sdtruss import sdtruss

jc = [ ('a', 0, 2),
       ('b', 1, 2),
       ('c', 2, 2),
       ('d', 3, 2),
       ('e', 4, 2),
       ('f', 1, 1),
       ('g', 3, 1),
       ('h', 0, 0), 
       ('i', 2, 0),
       ('j', 4, 0),
       ]

mi = [ ('a', 'b'),
       ('b', 'c'),
       ('c', 'd'),
       ('d', 'e'),
       ('h', 'i'),
       ('i', 'j'),
       ('a', 'h'),
       ('a', 'f'),
       ('b', 'f'),
       ('c', 'f'),
       ('c', 'i'),
       ('c', 'g'),
       ('d', 'g'),
       ('e', 'g'),
       ('e', 'j'),
       ('g', 'j'),
       ('h', 'f'),
       ]

rf = [ ('h', 1, 0),             # reaction force dirns
       ('h', 0, 1),
       ('j', 0, 1),
       ]

jl = [ ('a', 1, 0, -1),
       ('b', 1, 0, -1),
       ('c', 1, 0, -1),
       ('d', 1, 0, -1),
       ('e', 1, 0, -1),
       ]

sdtruss( jc, mi, rf, jl )
