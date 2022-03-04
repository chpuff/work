model lab04_2

  parameter Real two_gamma = 0.8;
  parameter Real sqr_omega = 3;
  parameter Real x_0 = 0.1;
  parameter Real y_0 = -1.1;
  
  Real x(start = x_0);
  Real y(start = y_0);
  
equation

  der(x) = y;
  der(y) = -two_gamma*y - sqr_omega*x;

end lab04_2;
