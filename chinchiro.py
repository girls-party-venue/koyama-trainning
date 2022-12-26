import random

cheating_flag = True
if cheating_flag:
  saikoro1 = random.randint(4,6)
  saikoro2 = random.randint(4,6)
  saikoro3 = random.randint(4,6)
else:
    saikoro1 = random.randint(1,6)
    saikoro2 = random.randint(1,6)
    saikoro3 = random.randint(1,6)

print(saikoro1, saikoro2, saikoro3)