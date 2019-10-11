import sys
sys.path[:1] = ["../../../../../software/truss-vw/python"]
from truss2d import truss2d

# solution for Problem 3

nodes = [ ('a',4000,0),
          ('b',0,0),
          ('c',0,3000),
          ('d',4000,6000,),
          ('e',8000,3000),
          ('f',8000,0),
          ]

bars = [ ('a','b',2000),
         ('a','c',2000),
         ('a','d',2000),
         ('a','e',2000),
         ('a','f',2000),
         ('b','c',2000),
         ('c','d',2000),
         ('d','e',2000),
         ('e','f',2000),
         ]

reactions = [ ('b',0,1),
              ('f',0,1),
              ('f',1,0),
              ]

loads = [ ('e', 48., 1, 0),
          ]

vloads = [ ('a',1, 0,-1) ]

truss2d( nodes, bars, reactions, loads, vloads )
