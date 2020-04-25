prem = 1

def ship_ground(weight, prem):
  if prem = 0:
    cost = weight *4 + 20
  elif:
    cost = weight *4 + 20 +20
  return cost

def ship_drone(weight, drone):
  if drone = 0:
    cost = weight *4 + 20
  elif:
    cost = weight *4 + 10
  return cost

def ship(weight) :
  if ship_ground(weight) > ship_drone(weight):
    print('The drone shipping is the cheapest.')
  else:
    print('ground shiping is the best')
