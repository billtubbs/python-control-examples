
% H-infinity example from MATLAB
load hinfsynExData P

assert(isequal(size(P), [5 4]))

if ~exist('data', 'dir')
  mkdir('data')
end

writematrix(P.A,'data/A.csv')
writematrix(P.B,'data/B.csv')
writematrix(P.C,'data/C.csv')
writematrix(P.D,'data/D.csv')

ncont = 1; 
nmeas = 2; 
[K1,CL,gamma] = hinfsyn(P,nmeas,ncont);

writematrix(K1.A,'data/K1_A.csv')
writematrix(K1.B,'data/K1_B.csv')
writematrix(K1.C,'data/K1_C.csv')
writematrix(K1.D,'data/K1_D.csv')
