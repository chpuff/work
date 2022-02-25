model lab03_2

  parameter Real a = 0.43;
  parameter Real b = 0.79;
  parameter Real c = 0.79;
  parameter Real h = 0.23;
  
  Real x(start = 44000, unit = "people");
  Real y(start = 33000, unit = "people");

equation

  der(x) = -a*x - b*y + sin(2*time)+1;
  der(y) = -c*x*y - h*y + cos(2*time);

end lab03_2;

