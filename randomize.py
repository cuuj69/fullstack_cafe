import random
num_list = [x for x in range(1,25)]
set_a = []
set_b = []
set_c = []

for i in range(1,29):
    dist_num = random.shuffle(num_list)
  
    

set_a = num_list[:8]
set_b = num_list[8:16]
set_c = num_list[16:]

print(f'set_a: \t{set_a}\nset_b: \t{set_b}\nset_c: \t{set_c}')
