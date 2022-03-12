model lab05
  
   parameter Real a = -0.38;
   parameter Real b = -0.037;
   parameter Real c = -0.36;
   parameter Real d = -0.035;
   
   // Real x(start = 4);
   // Real y(start = 14);
   
   Real x(start = c/d);
   Real y(start = a/b);
   
equation

  der(x) = a*x - b*x*y;
  der(y) = -c*y + d*x*y;

end lab05;

