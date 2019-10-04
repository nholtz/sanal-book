%% Solution of Question 2, PA 2, September 30, 2010 -- CIVE 3203

coords = [  1   0   0
            2   3   5
            3   9   5
            4  12   0
            5   6   3 ];

bars = [ 1  1  2
         2  1  5
         3  5  3
         4  3  4
         5  5  4
         6  1  4
         7  2  5 ];

reacts = [ 8  1  1  0
           9  1  0  1
          10  4  0  1 ];

loads = [ 3  20   0
          5   0  -30 ];

sdtruss( coords, bars, reacts, loads );
