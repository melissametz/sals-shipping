weight = 41.5;

# Ground Shipping
if weight <= 2:
  cost = weight * 1.50 + 20.00;
  print("%1.2f " % cost);
elif weight <= 6:
  cost = weight * 3.00 + 20.00;
  print("%1.2f " % cost);
elif weight <=10:
  cost = weight * 4.00 + 20.00;
  print("%1.2f " % cost);
else:
  cost = weight * 4.75 + 20.00;
  print("Ground Shipping: $","%1.2f " % cost);

premium_cost = 125.00;
print("Ground Shipping Premium: $","%1.2f " % premium_cost);

# Drone Shipping
if weight <= 2:
  cost = weight*4.50 + 0.00;
  print("%1.2f " % cost);
elif weight <= 6:
  cost = weight * 9.00 + 0.00;
  print("%1.2f " % cost);
elif weight <= 10:
  cost = weight * 12.00 + 0.00;
  print("%1.2f " % cost);
else:
  cost = weight * 14.25 + 0.00;
  print("Drone Shipping: $","%1.2f " % cost);
  