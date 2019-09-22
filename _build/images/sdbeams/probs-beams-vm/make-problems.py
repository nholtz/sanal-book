# generate a bunch of reaction problems + solutions

numberOfProblems = [(5,3),(5,5),(5,7),(5,9)] # [(n,level),...]
section = '2-6'
configChoices = [
    (20, 'P:R'),       # Pin and Roller support, possible cantilevers
    (50, 'C.P:R'),
    (50, 'C.P:R.C'),
    (100, 'P:R.H:R'),     # Pin Roller Hinge Roller
    (100, 'C.P:R.H:R'),     # Pin Roller Hinge Roller
    (100, 'C.P:R.H:R.C'),     # Pin Roller Hinge Roller
    (50,  'P:R.H:R.H:R'),
    (50,  'C.P:R.H:R.H:R'),
    (50,  'C.P:R.H:R.H:R.C'),
    (50,  'P:R.H:H.R:R'),
    (50,  'C.P:R.H:H.R:R'),
    (50,  'C.P:R.H:H.R:R.C'),
    (25,  'F:C'),
    (100,  'F:H:R'),
    (100,  'F:H:R.C'),
    (30,  'F:H:R.H:R'),
    (30,  'F:H:R.H:R.C'),
    (30,  'F:H:H.R:R'),
    (30,  'F:H:H.R:R.C'),
    #(10,  'F:H:H:F'),     # technically statically indeterminate
    ]
dloadChoices = [(20,'U'),(5,'D')]
cloadChoices = [(20,'P'),(5,'M')]

################

dbname = 'P-%s.sqlite3' % (section,)
filenames = 'P-%(section)s-%(bno)s-%(type)s.%(ext)s'

################################################################

import sys
import os
from os.path import expanduser
sys.path[:0] = [expanduser(s) for s in ['~/work/Programs/python/beam-generator/v2' ]]

import StringIO
import base64

import beamlib
import gen2 as gen
import beamlib_svg

def main():

    for N,Level in numberOfProblems:
        for i in range(N):
            beam = gen.gen_beam( level=Level, choices=configChoices, 
                                 dloads=dloadChoices, cloads=cloadChoices )
            n = beamlib.bsave(beam,dbname=dbname,idpfx=section)
            bno = '%04d' % (n,)
            prob = beamlib_svg.render( beam, visibleSolutions=False, visibleFBD=False, showVM=False,
                                       inkscape=True, showLevel=True, media='screen' )
            beam.solve()
            soln = beamlib_svg.render( beam, visibleSolutions=True, visibleFBD=True, showVM=True,
                                       inkscape=True, showLevel=True, media='screen' )
            for body,type in [(prob,'prob'),(soln,'soln')]:
                svgname = filenames % dict( globals(), bno=bno, type=type, ext='svg' )
                print svgname

                f = file( svgname, 'w' )
                f.write( body )
                f.close()

                os.system( 'svg2png %s' % (svgname,) )

main()
