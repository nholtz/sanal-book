%% sdtruss - statically determinate 2-D truss analysis, method of joints
%%
%%  sdtruss( joints, members, reactions, loads ):
%%
%% Input arrays:
%%
%% joints(3,nj) - joint coordinates (1 row per joint):
%%                 col 1: joint # (1 - nj)
%%                 col 2: x coordinate
%%                 col 3: y coordinate
%%
%% members(3,nm) - member connectivity (1 row per member):
%%              col 1: member (i.e. unknown) #, k
%%              col 2: joint # at start of member, i
%%              col 3: joint # at end of member, j
%%
%% reactions(4,nr) - reaction components (1 row per component)
%%              col 1: reaction (i.e. unknown) #, k
%%              col 2: joint #, i
%%              col 3: lij - cos(theta x) - directional cosine, x-axis
%%              col 4: mij - cos(theta y) - directional cosine, y-axis
%%
%% loads(3,nl) - applied loads (1 row per loaded joint)
%%              col 1: joint #, i
%%              col 2: x-component of load, +-ive rightward
%%              col 3: y-component of load, +-ive upward
%%
%%  by:  N.M. Holtz, October 12, 2011
%%       nholtz@cee.carleton.ca

function [Q,C,P] = sdtruss( joints, members, reactions, loads )

  x(joints(:,1)) = joints(:,2); %% extract coordinates into our own x, y, arrays
  y(joints(:,1)) = joints(:,3);

  nm = size(members,1);         %% number of members
  nr = size(reactions,1);       %% number of reaction components
  N = nm+nr;                    %% number of unknowns
  nj = size(x,2);               %% number of joints

  if N > 2*nj
    error( "Truss is statically indeterminate. (# unknowns > # eqns)." );
  endif
  if N < 2*nj
    error( "Truss is unstable.  (# unknowns < # eqns)." );
  endif
    
  C = zeros( N, N );            %% initialize C to all 0's
  
  for m = 1:nm                  %% for each bar in the truss 
      k = members(m,1);         %% member number
      i = members(m,2);         %% joint number at start
      j = members(m,3);         %% joint number at end
      dx = x(j)-x(i);           %% projection on x-axis 
      dy = y(j)-y(i);           %% projection on y-axis
      L = sqrt( dx*dx + dy*dy ); %% length of member
      dc = [dx;dy]/L;		%% directional cosines, as a column vector
      C(2*i+[-1;0],k) = dc;     %% assign directional cosines into C matrix
      C(2*j+[-1;0],k) = -dc;
  endfor

  for m = 1:nr                  %% for each reaction component
      k = reactions(m,1);       %% reaction number
      i = reactions(m,2);       %% joint number
      d = reactions(m,3:4)';	%% relative components of reactions
      C(2*i+[-1;0],k) = d/norm(d); %% assign directional cosines into C
  endfor

  P = zeros(2*nj,1);            %% right hand side (-ives of loads)

  for m = 1:size(loads,1)       %% for each loaded joint
      i = loads(m,1);           %% joint #
      P(2*i+[-1;0],1) += -loads(m,2:3)';  
  endfor

  if rank(C) < N
    warning( "Equations are rank deficient.  Truss is unstable." );
    return
  endif

  Q = C\P;                      %% solve for the forces

  printf( "\n" );
  printf( "  k    force(k)\n" );
  printf( "---    --------\n" );
  for i = 1:N
    printf( "%3d  %10.4g\n", i, Q(i) );
  endfor
