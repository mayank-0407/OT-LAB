clc 
clear all 
c=[2 5 0 0 0 0]; %% added 0 in last to avoid error in zjcj 
b=[24;21;9]; 
a=[1 4 1 0 0;3 1 0 1 0;1 1 0 0 1]; 
bv=[3 4 5]; % club a and b so that we dont have to perform operation on both 
A=[a b]; 
zj_cj=c(bv)*A-c; % display simplex table 
simplex_table=[A;zj_cj] %% combined a and zjcj to get table in one command 
var={'x1','x2','s1','s2','s3','sol'}; 
array2table(simplex_table,'VariableNames',var) 

RUN=true 
while(RUN) 
zc=zj_cj(1:end-1); % end gives last index of ele, we can also use length for this 
if any(zc<0) % any is used to check if any 1 is <0 then go in loop 
fprintf('The current BFS is not optimal') 
[enter_var,piv_col]=min(zc); 
pivot_col=A(:,piv_col); 
sol=A(:,end); 
if all(pivot_col<=0) 
error('Unbounded Solution'); 
else for i=1:size(A,1) 
if(pivot_col(i)>0) 
ratio(i)=sol(i)/pivot_col(i); 
else ratio(i)=inf; 
end 
end 
[leaving_var,pivot_row_index]=min(ratio); 
pivot_row=A(pivot_row_index,:); 
end 
bv(pivot_row_index)=piv_col; %% changing basic variables for next table 
pvt_element=A(pivot_row_index,piv_col) 
A(pivot_row_index,:)=A(pivot_row_index,:)/pvt_element 
for i=1:size(A,1) 
if i~=pivot_row_index 
A(i,:)=A(i,:)-A(i,piv_col)*A(pivot_row_index,:) % formula is new_value=old_value-corrpivotcolval*corrpivotrowval/pivotele 
end 
end 
zj_cj=c(bv)*A-c; 
next_table=[A;zj_cj]; 
array2table(simplex_table,'VariableNames',var) 
else 
RUN=false 
fprintf('The table is optimal') 
end 
end
