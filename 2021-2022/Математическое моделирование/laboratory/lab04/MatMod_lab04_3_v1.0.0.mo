model lab04_3

  parameter Real two_gamma = 3.3;
  parameter Real sqr_omega = 0.1;
  parameter Real x_0 = 0.1;
  parameter Real y_0 = -1.1;
  
  Real x(start = x_0);
  Real y(start = y_0);
  
equation

  der(x) = y;
  der(y) = -two_gamma*y - sqr_omega*x + 0.1*sin(3*time);

end lab04_3;
