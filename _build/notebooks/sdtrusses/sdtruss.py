#!/usr/bin/env python
# coding: utf-8

# # Statitically Determinate 2D Trusses

# In[1]:


import numpy as np
from numpy.linalg import solve, matrix_rank
from math import sqrt, atan2, degrees


# In[2]:


class SDTError(Exception):
    pass


# In[3]:


Joints = dict()
class Joint:
    
    def __init__(self,jid,x,y):
        if jid in Joints:
            raise SDTError("Joint '{}' is defined more than once.".format(jid))
        for oj in Joints.values():
            if oj.x == x and oj.y == y:
                raise SDTError("Joint '{}' has the same coordinates as '{}'.".format(jid,oj.jid))
        self.jid = jid
        self.n = len(Joints)
        self.x = x
        self.y = y
        Joints[self.jid] = self


# In[4]:


Unknowns = dict()
JointPairs = dict()

class Member:
    
    def __init__(self,jid_i,jid_j):
        if jid_i == jid_j:
            raise SDTError("Member '{}' has both joints the same: '{}'.".format(mid,jid_i))
        for jid in [jid_i,jid_j]:
            if jid not in Joints:
                raise SDTError("Joint '{}' for member '{}' is not defined.".format(jid,mid))
        mid = jid_i + jid_j
        if mid in Unknowns:
            raise SDTError("Member '{}' is defined more than once.".format(mid))
        jpair = (jid_i,jid_j)
        if jpair in JointPairs:
            raise SDTError("Joints '{}' and '{}' are also connected by member '{}'.".format(jid_i,jid_j,JointPairs[jpair].mid))
        ji = Joints[jid_i]
        jj = Joints[jid_j]
        dx = jj.x - ji.x
        dy = jj.y - ji.y
        L = sqrt(dx*dx + dy*dy)
        if L == 0.:
            raise SDTError("Length of member '{}' is zero.".format(mid))
        l = dx/L
        m = dy/L
        self.uid = mid
        self.n = len(Unknowns)
        self.ji = ji
        self.jj = jj
        self.L = L
        self.l = l
        self.m = m
        Unknowns[self.uid] = self
        JointPairs[jpair] = self


# In[5]:


class Reaction:
    
    def __init__(self,jid,dx,dy):
        if jid not in Joints:
            raise SDTError("Joint '{}' is not defined for reaction.".format(jid))
        L = sqrt(dx*dx + dy*dy)
        if L == 0.:
            raise SDTError("dx,dy invalid for joint reaction @ '{}': '{},{}'.".format(jid,dx,dy))
        rid = 'R' + jid
        if dx != 0 and dy == 0:
            rid += 'x'
        elif dy != 0 and dx == 0:
            rid += 'y'
        else:
            a = degrees(atan2(dy,dx))
            if a < 0.:
                a += 360.
            rid += '{:.0f}'.format(a)
        if rid in Unknowns:
            raise SDTError("Reaction '{}' already defined at joint '{}'.".format(rid,jid))
        self.jid = jid
        self.uid = rid
        self.n = len(Unknowns)
        self.ji = Joints[self.jid]
        self.jj = None
        self.l = dx/L
        self.m = dy/L
        Unknowns[self.uid] = self


# In[16]:


def sdtruss( jc, mi, rf, jl, print_flag=True ):
    
    global Joints, Unknowns, JointPairs
    Joints = dict()
    Unknowns = dict()
    JointPairs = dict()
    connected = set()

    assert len(mi)+len(rf) == 2*len(jc)
    N = 2*len(jc)
    
    for jid,x,y in jc:
        Joint(jid,x,y)
    for ijid,jjid in mi:
        Member(ijid,jjid)
        connected.add(ijid)
        connected.add(jjid)
    for jid in Joints:
        if jid not in connected:
            raise SDTError("Joint '{}' is not connected to any member.".format(jid))
    for jid,dx,dy in rf:
        Reaction(jid,dx,dy)
        
    C = np.zeros((N,N),np.float64)
    for unk in Unknowns.values():
        k = unk.n
        ji = unk.ji
        jj = unk.jj
        C[ji.n*2,k] = unk.l
        C[ji.n*2+1,k] = unk.m
        if jj:
            C[jj.n*2,k] = -unk.l
            C[jj.n*2+1,k] = -unk.m
            
    P = np.zeros((N,1),np.float64)
    for jid,p,dx,dy in jl:
        if jid not in Joints:
            raise SDTError("Joint '{}' not defined in load input.".format(jid))
        L = sqrt(dx*dx + dy*dy)
        if L == 0.:
            raise SDTError("Improper dx,dy for load on joint '{}': {},{}".format(jid,dx,dy))
        l = dx/L
        m = dy/L
        j = Joints[jid]
        P[j.n*2,0] = -l*p
        P[j.n*2+1,0] = -m*p
    
    if matrix_rank(C) < N:
        raise SDTError("'C' matrix is rank-deficient, truss is probably unstable.")
    Q = solve(C,P)
    
    if not print_flag:
        return Q,C,P
    
    print('uid   iid   jid        force')
    print('---   ---   ---        -----')
    for unk in Unknowns.values():
        uid = unk.uid
        iid = unk.ji.jid
        jid = unk.jj.jid if unk.jj else ''       
        t = Q[unk.n,0]
        if jid:
            s = 'T' if t >= 0 else 'C'
            print("{:5s} {:5s} {:5s} {:10.4g} {}".format(uid,iid,jid,abs(t),s))
        else:
            print("{:5s} {:5s} {:5s} {:10.4g} {}".format(uid,iid,jid,t,''))


# ![Figure](2019-hw2-q2.svg)

# In[17]:

if __name__ == '__main__':
    
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


# In[ ]:




