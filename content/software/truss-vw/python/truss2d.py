import sys
import math

import numpy
import numpy.linalg
zeros = numpy.zeros
Float64 = numpy.float64
solve = numpy.linalg.solve
determinant = numpy.linalg.det

def norm( dx, dy ):
    """Return magnitude, direction cosines"""
    l = math.sqrt( dx*dx + dy*dy )
    return l, (dx/l, dy/l)

class Collection( object ):

    def __init__( self ):
        self.sequence = []
        self.index = {}

    def add( self, key, obj, attr='i' ):
        if key is not None and key in self.index:
            raise ValueError, "Multiply defined key: %s" % (key,)
        if attr:
            setattr( obj, attr, len(self.sequence) )
        self.sequence.append( obj )
        if key is not None:
            self.index[key] = obj
        return obj

    def __setitem__( self, key, obj ):
        self.add( key, obj )

    def __getitem__( self, key ):
        if type(key) is type(0):
            return self.sequence[key]
        return self.index[key]

    def __iter__( self ):
        return iter(self.sequence)

    def __len__( self ):
        return len(self.sequence)

    def list( self ):
        return self.sequence[:]

class Node( object ):

    def __init__( self, id, x, y ):
        self.id = str(id)
        self.x = x
        self.y = y
        self.i = None

class Element( object ):

    def __init__( self, idi, idj, area=None, nodes={} ):
        self.nodei = nodes[str(idi)]
        self.nodej = nodes[str(idj)]
        self.id = self.nodei.id + self.nodej.id
        self.area = area
        self.length, self.dc = norm( self.nodej.x - self.nodei.x, \
                                     self.nodej.y - self.nodei.y )
        self.i = None

class Reaction( object ):

    list = []

    def __init__( self, nid, dx, dy, nodes={} ):
        self.node = nodes[str(nid)]
        x,self.dc = norm( dx, dy )
        self.i = None
        

class Truss( object ):

    def __init__( self, nodes, elements, reactions, redundants=[] ):

        redundant_ids = [(str(a)+str(b)) for a,b in redundants]

        self.nodes = Collection()
        for data in nodes:
            node = Node(*data)
            self.nodes.add( node.id, node )

        self.elements = Collection()
        self.redundants = Collection()
        for data in elements:
            elem = Element( nodes=self.nodes, *data )
            if elem.id in redundant_ids:
                elem.redundant = True
                self.redundants.add( elem.id, elem )
            else:
                elem.redundant = False
                self.elements.add( elem.id, elem )

        self.reactions = Collection()
        for data in reactions:
            reac = Reaction( nodes=self.nodes, *data )
            self.reactions.add( None, reac )

    def all( self ):
        return self.elements.list() + self.redundants.list()

    def make_A( self ):

        m = len( self.elements )
        r = len( self.reactions )
        n = m + r
        j = len( self.nodes )
        if m+r < 2*j:
            raise ValueError, "Too few unknowns (r=%d, m=%d, j=%d)." % (r,m,j)
        if m+r > 2*j:
            raise ValueError, "Too many unknowns (r=%d, m=%d, j=%d)." % (r,m,j)

        A = zeros( (n,n), Float64 )
        for elem in self.elements:
            k = elem.i
            i = elem.nodei.i
            j = elem.nodej.i
            A[2*i,k] = elem.dc[0]
            A[2*i+1,k] = elem.dc[1]
            A[2*j,k] = -elem.dc[0]
            A[2*j+1,k] = -elem.dc[1]

        for reac in self.reactions:
            i = reac.node.i
            k = m + reac.i
            A[2*i,k] = reac.dc[0]
            A[2*i+1,k] = reac.dc[1]

        return A

    def solve_RT( self, A, loads, ri=0, rf=0.0 ):

        m = len(self.elements)
        n = m + len(self.reactions)
        P = zeros( (n,1), Float64 )

        for nid, p, dx, dy in loads:
            node = self.nodes[str(nid)]
            i = node.i
            x,dc = norm(dx,dy)
            P[2*i,0] += -p*dc[0]
            P[2*i+1,0] += -p*dc[1]

        try:
            F = solve(A,P)
        except:
            msg = "Matrix is singular, structure is unstable."
            print >>sys.stderr, '*' * (len(msg) + 4)
            print >>sys.stderr, '*', msg, '*'
            print >>sys.stderr, '*' * (len(msg) + 4)
            raise

        T = [F[e.i,0] for e in self.elements]
        R = [F[m+r.i,0] for r in self.reactions]

        if self.redundants:
            rT = [0.0] * len(self.redundants)
            rT[ri] = rf
            T = T + rT

        return R, T

    def print_RT( self, src, R, T ):

        msg = "Forces due to " + src

        print
        print "*" * (len(msg)+4)
        print "*", msg, "*"
        print "*" * (len(msg)+4)

        print
        print "Reactions:"
        print "=========="
        print
        print "Node      dx     dy      Force"
        print "----      --     --      -----"
        for i,reac in enumerate(self.reactions):
            print "%-5s %6g %6g %10.4g" % \
                  (reac.node.id,reac.dc[0],reac.dc[1],R[i])

        print
        print "Element Forces:"
        print "==============="
        print
        print "Elem      Force"
        print "----      -----"
        for i,e in enumerate(self.all()):
            print "%-4s %10.4g  %s" % \
                  (e.id,T[i],'(redundant)' if e.redundant else '')

    def print_D( self, src, T, vT, E, Area ):
        
        msg = "Delta corresp. to " + src

        print
        print "*" * (len(msg)+4)
        print "*", msg, "*"
        print "*" * (len(msg)+4)
        
        l = "E = %g GPa" % (E,)
        h = [ '           L     A            n            N         nNL/AE',
              'Member   [mm] [mm^2]                      [N]         [mm]',
              '----     ---- ------        -----        -----      -------',
              ]
        nw = len(h[0]) - len(l) - 1
        print
        print ' ' * nw, l
        ##print ' ' * nw, '.' * len(l)
        print
        for x in h: print x

        sumw = 0.0
        for i,e in enumerate(self.all()):
            f = vT[i]
            F = T[i]
            area = e.area or Area
            w = f*F*e.length/(E*area)
            sumw += w
            l = "%-4s %8.4g %6.0f %12.4f %12.0f %12.4f" % \
                (e.id, e.length, area, f, F*1000., w)
            print l

        ul = '-' * 12
        print ' ' * (len(l)-len(ul)-1), ul
        ul = "sum = %12.4g" % (sumw,)
        print ' ' * (len(l)-len(ul)-1), ul

        return sumw


def truss2d( nodes, elements, reactions, loads, 
             vloads=[], redundants=[], E=200.0, Area=1.,
             flexibility=False, redundant_force=0.0 ):

    nr = len(redundants)

    S = Truss( nodes, elements, reactions, redundants )
    A = S.make_A()
    R, T = S.solve_RT( A, loads, rf=redundant_force )

    S.print_RT( 'Real Loads', R, T )

    vforces = []
    for vload in vloads:
        vR, vT = S.solve_RT( A, [vload] )
        src = 'Virtual Joint Load %s' % (vload,)
        vforces.append( (src,[vload],vR,vT) )
        S.print_RT( src, vR, vT )

    for i,e in enumerate(S.redundants):
        node0 = e.nodei
        node1 = e.nodej
        rvloads = [ (node0.id, 1.0, node1.x-node0.x, node1.y-node0.y),
                    (node1.id, 1.0, node0.x-node1.x, node0.y-node1.y),
                    ]
        vR, vT = S.solve_RT( A, rvloads, ri=i, rf=1.0 )
        src = 'Virtual Redundant %s: %s' % (e.id,rvloads,)
        vforces.append( (src,rvloads,vR,vT) )
        S.print_RT( src, vR, vT )

    ans = []
    for src,vls,vR,vT in vforces:
        d = S.print_D( src, T, vT, E, Area )
        ans.append( d )

    if not flexibility:
        return ans

    l = 'Flexibility Coefficients: Virtual Forces'
    print
    print '*' * (len(l)+4)
    print '*', l, '*'
    print '*' * (len(l)+4)
    print

    n = len(vforces)
    for i in range(n):
        print "%5d. %s" % (i+1,vforces[i][0])
        
    for i in range(n):
        src1,vl1,vR,vT = vforces[i]
        for j in range(i,n):
            src2,vl2,rR,rT = vforces[j]
            src = "virtual # %d, due to unit value of # %d" % (i+1,j+1)
            d = S.print_D( src, rT, vT, E, Area )
            ans.append( d )

    return ans
        

################################################################

if __name__ == '__main__':

    nodes = [ ('a', 0.,    3000.),
              ('b', 4000., 3000.),
              ('c', 8000., 0.),
              ('d', 4000., 0.),
              ('e', 0.,    0.),
              ]

    elements = [ ('a', 'b', 1000.),
                 ('e', 'd', 4000.),
                 ('d', 'c', 2000.),
                 ('a', 'e', 2000.),
                 ('b', 'd', 2000.),
                 ('a', 'd', 1000.),
                 ('b', 'c', 1000.),
                 ]

    reactions = [ ('a', 1, 0),
                  ('e', 1, 0),
                  ('e', 0, 1),
                  ]

    loads = [ ('c', 100., 0, -1),
              ]

    vload = ('c', 1., 0, -1)

    truss2d( nodes, elements, reactions, loads, [vload] )
