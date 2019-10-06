from collections import namedtuple, OrderedDict
import numpy
import numpy.linalg
import math

##N O T   F I N I S H E D (needs comments)

def sdtruss( jc, mi, rf, jl, print_flag=True ):

    assert len(mi)+len(rf) == 2*len(jc)
    N = 2*len(jc)

    joints = OrderedDict()
    Joint = namedtuple('Joint','id n x y')

    for n,(jid,x,y) in enumerate(jc):
        joints[jid] = Joint(jid,n,x,y)

    unk = OrderedDict()
    C = numpy.zeros( (N,N), numpy.float64 )
    for k,(jid_i,jid_j) in enumerate(mi):
        mid = str(jid_i)+'-'+str(jid_j)
        unk[k] = mid
        ji = joints[jid_i]
        jj = joints[jid_j]
        dx = jj.x - ji.x
        dy = jj.y - ji.y
        L = math.sqrt( dx*dx + dy*dy)
        lij = dx/L
        mij = dy/L
        C[ji.n*2,k] = lij
        C[ji.n*2+1,k] = mij
        C[jj.n*2,k] = -lij
        C[jj.n*2+1,k] = -mij

    for jid,dx,dy in rf:
        k = len(unk)
        rid = 'R'+str(jid)+str(dx)+str(dy)
        unk[k] = rid
        L = math.sqrt( dx*dx + dy*dy)
        lij = dx/L
        mij = dy/L
        ji = joints[jid]
        C[ji.n*2,k] = lij
        C[ji.n*2+1,k] = mij

    P = numpy.zeros( (N,1), numpy.float64 )
    for jid,p,dx,dy in jl:
        L = math.sqrt( dx*dx + dy*dy)
        lij = dx/L
        mij = dy/L
        ji = joints[jid]
        P[ji.n*2,0] = -lij*p
        P[ji.n*2+1,0] = -mij*p

    Q = numpy.linalg.solve(C,P)

    if print_flag:
        print 'Unk.       Force'
        print '------ ---------'
        for k in range(N):
            print '%-6s %9.4g' % (unk[k], Q[k,0])
        

    return Q,unk
    
if __name__ == '__main__':

    print 'Solution of Question 2, HW 2, October 2019.'

    jc = [ ('a', 0, 4),           # joint coordinates (j,x,y)
           ('b', 3, 4),
           ('c', 9, 4),
           ('d', 0, 0),
           ('e', 6, 0),
           ('f', 9, 0),
           ]

    mi = [ ('a','b'),               # member incidences (i,j)
           ('b','c'),
           ('a','d'),
           ('b','d'),
           ('a','f'),
           ('c','e'),
           ('c','f'),
           ('d','e'),
           ('e','f'),
           ]

    rf = [ ('f',1,0),             # reaction forces (j,dcx,dcy)
           ('f',0,1),
           ('d',0,1),
           ]

    jl = [ ('b',80,0,-1),        # joint loads (j,p,dcx,dcy),
           ('e',100,0,-1),
           ]

    sdtruss( jc, mi, rf, jl )
