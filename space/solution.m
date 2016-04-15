c=[200 100 50 25];
A=[1,-1,0,0;400,400,150,50];
b=[0;1000];

lb=[0;0;0;0];
ub=[1;1;6;4];
ctype=["L";"U"];
vtype=["I";"I";"I";"I"];

sense=-1;
[xopt,zmx]=glpk(c,A,b,lb,ub,ctype,vtype,sense)
