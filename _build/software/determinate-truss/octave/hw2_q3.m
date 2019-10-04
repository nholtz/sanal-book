%% Solution of Question 3, HW2, October 2011.

coords = [1 0 0
          2 1 0
          3 2 0
          4 3 -1
          5 2 -1
	  6 1 -1];

bars = [1 1 2
        2 2 3
        3 3 4
        4 5 4
        5 6 5
        6 1 6
        7 2 6
        8 3 6
	9 3 5];

reacts = [10 1 1 0
          11 1 0 1
	  12 4 -1 3];

loads = [6 0 -80
	 5 0 -100];

sdtruss( coords, bars, reacts, loads );
