clc
clear all
c=[2 10 4 5;6 12 8 11;3 9 5 7];

a=[12 25 20];
b=[25 10 15 5];
m=size(c,1);
n=size(c,2);
if sum(b)==sum(a)
fprintf('balanced')
else
fprintf('Not balanced')
if sum(a)<sum(b)
c(end+1,:)=zeros(1,n);
a(end+1)=sum(b)-sum(a);
m=m+1;
else
c(:,end+1)=zeros(1,m);
b(end+1)=sum(a)-sum(b);
n=n+1;
end
end
X=zeros(m,n);
orig_c=c;
for i=1:m
for j=1:n
cpq=min(min(c)); % you can also use min(c(:))
if cpq==inf
break
end
[p1,q1]=find(cpq==c);
p=p1(1);
q=q1(1);
X(p,q)=min(a(p),b(q));
if min(a(p),b(q))==a(p)
b(q)=b(q)-a(p);
a(p)=a(p)-X(p,q);
c(p,:)=inf;
else
a(p)=a(p)-b(q);
b(q)=b(q)-X(p,q);
c(:,q)=inf
end
end
end
SUM=0;
X
for i=1:m
for j=1:n
SUM=SUM+(X(i,j)*orig_c(i,j));
end
end
fprintf('the lcs : ')
SUM



% instead of selecting 1 1 from p q we can select like this
% xpq=min(a(p1),b(q1))
% [X1,ind]=max(xpq)
% p=p1(ind)
% q=q1(ind)
