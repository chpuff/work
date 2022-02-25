model lab03_1

  parameter Real a = 0.55;
  parameter Real b = 0.8;
  parameter Real c = 0.8;
  parameter Real h = 0.35;
  
  Real x(start = 44000, unit = "people");
  Real y(start = 33000, unit = "people");

equation

  der(x) = -a*x - b*y + sin(time) + 1;
  der(y) = -c*x - h*y + cos(2 * time);

end lab03_1;

