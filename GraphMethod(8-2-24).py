clc 
clear all 
% phase 1 
a=[1 2;1 1;1 -2]; 
b=[10;6;1]; 
a=[1 2;1 1;1 -2]; 
%phase 2 
x1=0:max(b); 
x21=(b(1)-a(1,1)*x1)/a(1,2); 
x22=(b(2)-a(2,1)*x1)/a(2,2); 
x23=(b(3)-a(3,1)*x1)/a(3,2); 
x21=max(0,x21); 
x22=max(0,x22); 
x23=max(0,x23); 
plot(x1,x21,'r',x1,x22,'b',x1,x23,'k'); 
% we can use hold if we want to write 3 plots
title('Question 1') 
xlabel('x1'); 
ylabel('x2'); 
legend('x1+x2=10','x1+x2=6','x1-2x2=1') 
%phase 3 
% line 1 points 
c1=find(x1==0); 
c2=find(x21==0); 
line1=[x1([c1 c2]);x21([c1 c2])]' 
%line 2 points 
c3=find(x1==0); 
c4=find(x22==0); 
line2=[x1([c3 c4]);x22([c3 c4])]'
%line 3 points 
c5=find(x1==0); 
c6=find(x23==0); 
line3=[x1([c5 c6]);x23([c5 c6])]' 
%take transpose to combine these vectors and ' is for transpose
newLine=[line1;line2;line3]; 
corPts=unique(newLine,'rows') 
%ad loop i=1 and j=i+1
sol=[0;0]
for i=1:size(a,1)  % this size is the size of row
    for j=i+1:size(a,1)
        a1=a([i j],:); 
        b1=b([i j]); 
        x=inv(a1)*b1
        sol=[sol,x]
    end
end
pt=sol'
% phase 5 all points
allpt=[corPts;pt]
points=unique(allpt,'rows')

% phase 6 feasible region
for i=1:size(a,1)
const1(i) = a(1,1)*points(i,1)+a(1,2)*points(i,2) -b(1)
const2(i) = a(2,1)*points(i,1)+a(2,2)*points(i,2)-b(2)
const3(i) = a(3,1)*points(i,1)+a(3,3)*points(i,2)-b(3)
end

s1=find(const1>0);
s2=find(const2>0);
s3=find(const3>0);
s=unique([s1,s2,s3]);
points(s,:)=[]

% phase7
z=points*c';
[obj,idxx]=max(z)
x1=points(idxx,1)
x2=points(idxx,2)
