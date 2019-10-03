%% regular hexagon truss, complex truss, unstable

%%         i  x  y
coords = [ 1  1  0
	   2  0  1.7321
	   3  1  3.4641
	   4  3  3.4641
	   5  4  1.7321
	   6  3  0 ];

%%       k  i  j
bars = [ 1  1  2
	 2  2  3
	 3  3  4
	 4  4  5
	 5  5  6
	 6  6  1
	 7  1  4
	 8  2  5
	 9  3  6 ];

%%         k   i  lij mij
reacts = [ 10  1   0   1
           11  1   1   0
           12  6   0   1 ];

%%        i   fx  fy
loads = [ 5  100  0 ];

sdtruss( coords, bars, reacts, loads );

disp( "Now try it with joint 4 moved just a litle bit" );

coords(4,3) = 3.47;    %% was y=3.4641

sdtruss( coords, bars, reacts, loads );
