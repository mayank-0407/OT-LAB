%% steepest descent method solve mimn only
clc
clear all
%objective function
syms x1 x2
f= x1-x2+2*x1^2+2*x1*x2+x2^2; % function with @ you can put points but with sysms you cant put points
fx=inline(f); % f is not a function and inline converts this f handle to function
fobj=@(X) fx(X(1),X(2)) % we wil have to define self function to use vectors in func fx
% find gradient of f
grad=gradient(f);
G=inline(grad);
gx=@(X) G(X(1),X(2)); % to put points
% find hessian matrix
H=hessian(f);
X0=[0;0]
maxiter=6

tol=10^-3 % for optimal stopping condition as it is close to 0
iter=0;
while norm(gx(X0))>tol && iter<maxiter
S=-gx(X0)% search direction si
lambda=(S'*S)/(S'*H*S)% step length lambda i
Xnew= X0 +S*lambda %new pt x(i+1)
X0=Xnew
iter=iter+1
end
