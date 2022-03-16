model lab06

  parameter Real N = 10850;
  parameter Real I_0 = 209;
  parameter Real R_0 = 42;
  parameter Real a = 0.3;
  parameter Real b = 0.8;
  
  Real I(start = I_0);
  Real R(start = R_0);
  Real S(start = N - I_0 - R_0);

equation

  der(R) = b*I;
  
  // случай 1 - I(0)<=I^*
  //der(S) = 0;
  //der(I) = -b*I;
  
  // случай 2 - I(0)>I^*
  der(S) = -a*S;
  der(I) = a*S - b*I;

end lab06;
