module or_gate(a,b,c);
input a,b;
output c;
reg c;

always@(a,b)
begin
    if(a==0 & b==0)
    c=0;
    else 
    c=1;
end
endmodule