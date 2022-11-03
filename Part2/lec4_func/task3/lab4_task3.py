import Constants as c
def full_mech_energy(mass, height, velocity):
  return mass * (velocity ** 2) / 2 + mass * c.g * height
m, h, v = map(float, input().split())
print(full_mech_energy(m, h, v))