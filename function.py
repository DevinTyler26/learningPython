def convert(miles):
  km = 1.6*miles
  return km

def kilos(lbs):
  kilo = 2.2*lbs
  return kilo

def lbs(kilo):
  lbs = kilo/2.2
  return lbs

km = convert(60)
kg = kilos(45)
lbs = lbs(45)
print('Converting 60 MPH to KMH ', km)
print('Converting 45 LBS to KG ', kg)
print('Converting 45 KG to LBS', lbs)
