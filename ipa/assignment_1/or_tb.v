module or_test;
reg a,b;
wire c;
or_gate or_test(a,b,c);
initial 
begin
    #000 a=0;b=0;
    #100 a=0;b=1;
    #100 a=1;b=0;
    #100 a=1;b=1;
end
initial
begin
    $monitor($time,"a=%b,b=%b,c=%b",a,b,c);
end
endmodule
