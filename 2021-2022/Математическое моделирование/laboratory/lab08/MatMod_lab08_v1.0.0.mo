model lab08

  parameter Real p_cr = 43; // критическая стоимость продукта
  parameter Real tau_1 = 27; // длительность производственного цикла фирмы 1
  parameter Real tau_2 = 20; // длительность производственного цикла фирмы 2
  parameter Real p_1 = 12; // себестоимость продукта фирмы 1
  parameter Real p_2 = 9.7; // себестоимость продукта фирмы 2
  parameter Real N = 87; // число потребителей производимого продукта
  parameter Real q = 1; // максимальная потребность одного человека в продукте в единицу времени
  
  parameter Real b = p_cr/(tau_1*tau_1*p_1*p_1*tau_2*tau_2*p_2*p_2*N*q);
  parameter Real c_1 = (p_cr - p_1)/(tau_1*p_1);
  parameter Real c_2 = (p_cr - p_2)/(tau_2*p_2);
  parameter Real a_1 = p_cr/(tau_1*tau_1*p_1*p_1*N*q);
  parameter Real a_2 = p_cr/(tau_2*tau_2*p_2*p_2*N*q);
  
  Real M_1(start = 7.2); // оборотные средства фирмы 1
  Real M_2(start = 8.2); // оборотные средства фирмы 2
  Real theta; // безразмерное время 

equation

  time = c_1*theta;
  //1 случай
  //der(M_1) = M_1 - b/c_1*M_1*M_2 - a_1/c_1*M_1*M_1;
  //der(M_2) = c_2/c_1*M_2 - b/c_1*M_1*M_2 - a_2/c_1*M_2*M_2;
  //2 случай
  der(M_1) = M_1 - (b/c_1 + 0.00014)*M_1*M_2 - a_1/c_1*M_1*M_1;
  der(M_2) = c_2/c_1*M_2 - b/c_1*M_1*M_2 - a_2/c_1*M_2*M_2;

end lab08;
