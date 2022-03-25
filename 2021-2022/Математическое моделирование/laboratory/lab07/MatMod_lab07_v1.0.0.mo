model lab07

  parameter Real N = 945;
  parameter Real n_0 = 13;
    
  Real n1(start = n_0);
  Real n2(start = n_0);
  Real n3(start = n_0);

equation

  // 1 случай
  der(n1) = (0.51 + 0.000099*n1)*(N - n1);
  
  // 2 случай
  der(n2) = (0.000019 + 0.99*n2)*(N - n2);
  
  // 3 случай
  der(n3) = (0.99*time + 0.3*cos(4*time)*n3)*(N - n3);

end lab07;
