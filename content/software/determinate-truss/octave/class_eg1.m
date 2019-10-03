%% Example truss from CIVE3203 class, September 26, 2010.

jcoords = [ 1  0    0
            2  4.5  3   %% joint 2 is at x=4.5, y=3
            3  9.0  0
            4  6.0  0
            5  3.0  0 ];

bars = [ 1  1  2
         2  5  2        %% bar 2 goes from joint 5 to joint 2
         3  4  2 
         4  2  3
         5  1  5
         6  5  4
         7  4  3 ];

reacts = [  8  1  1  0   %% reaction, 8, at joint 1 has direction 1,0
            9  1  0  1
           10  3  0  1 ];

loads = [ 2  100    0    %% load at joint 2 of 100 in x-direction
          4    0  -50 ];

sdtruss( jcoords, bars, reacts, loads );
