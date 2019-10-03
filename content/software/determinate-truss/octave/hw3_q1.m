%% Solution of Question 1, HW 3, October 2011.

coords = [1 0 4
	  2 3 4
	  3 9 4
	  4 0 0
	  5 6 0
	  6 9 0 ]

bars = [ 1 1 2
	 2 2 3
	 3 1 4
	 4 2 4
	 5 1 6
	 6 3 5
	 7 3 6
	 8 4 5
	 9 5 6 ]

reacts = [ 10 4 1 0
	   11 4 0 1
	   12 6 0 1]

loads = [ 2 0 -100
	  5 0 -80 ]

sdtruss( coords, bars, reacts, loads )
