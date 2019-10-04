%% Example 2, matrix methods, posted Sept 29, 2010
%% not discussed in class

coords = [  1  3  4    %% joint 1 is at x=3, y=4
            2  0  8
            3  6  8
            4  0  0
            5  6  0 ];

bars = [ 1  4  2       %% bar 1 goes from joint 4 to joint 2
         2  2  3
         3  3  5
         4  1  3
         5  2  1
         6  4  1
         7  1  5 ];

reacts = [ 8  4  1  0  %% reaction, 8, at joint 4, direction 1,0
           9  4  0  1  
          10  5  -cos(50*pi/180) cos(40*pi/180) ];

loads = [ 3  -21  0    %% joint 3, fx = -21
	     1   0  -42 ];

[Q,C,P] = sdtruss( coords, bars, reacts, loads )
