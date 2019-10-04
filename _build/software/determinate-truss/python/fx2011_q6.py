# question 6, final exam, Dec 2011

jc = [('a',0,0),
      ('b',0,3),
      ('c',4,3),
      ('d',8,3),
      ('e',4,0),
      ]

mi = [('a','b'),
      ('a','c'),
      ('a','e'),
      ('b','e'),
      ('c','d'),
      ('c','e'),
      ('d','e'),
      ]

rf = [('a',1,0),
      ('a',0,1),
      ('e',0,1),
      ]

jlR = [('d',60,0,-1),
       ]

jlU = [('b',1,1,0),
       ('c',1,-1,0),
       ]

from sdtruss import sdtruss

sdtruss( jc, mi, rf, jlR )
sdtruss( jc, mi, rf, jlU )
