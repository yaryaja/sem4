module and_gate(c,a,b);
input a,b;
output c;
reg c;


always@(a,b)
begin
    if(a==1 & b==1)
    c=1;
   
    else 
    c=0;
end
endmodule


