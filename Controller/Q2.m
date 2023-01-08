%% ME850A_Monojit_Layek(21105049)
%% Answer_2.b
n=[1, -1, 12, 2];
d=[1, -1, 1, -7, 22];
g=tf(n,d)
step(g);
syms EPS
Routh_Array = routh(d,EPS)
disp('Answer: as the sign changes in the 1st column of routh array i.e OLTF is unstable');