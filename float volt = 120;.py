  float volt = 120;
  float amp = 20;
  int pf = 100;
  float theta = acos(pf / 100);
  float vars = volt * amp * sin(theta);
  float Cap = vars / (2 * 3.14 * volt * volt);
    print(Cap);
