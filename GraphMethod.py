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
title('Question 1') 
xlabel('x1'); 
ylabel('x2'); 
legend('x1+x2=10','x1+x2=6','x1-2x2=1') 
%phase 3 
% line 1 points 
c1=find(x1==0); 
c2=find(x21==0); 
line1=[x1([c1 c2]);x21([c1 c2])] 
%line 2 points 
c3=find(x1==0); 
c4=find(x22==0); 
line2=[x1([c3 c4]);x22([c3 c4])]' 
%line 3 points 
c5=find(x1==0); 
c6=find(x23==0); 
line3=[x1([c5 c6]);x23([c5 c6])]' 
%take transpose to combine these vectors 
newLine=[line1;line2;line3]; 
corPts=unique(line,'rows') 
%ad loop i=1 and j=i+1 
a1=a(1:2,:); 
b1=b(1:2); 
x=inv(a1)*b
