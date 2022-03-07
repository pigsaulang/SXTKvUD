import math
tong_mau = 240
so_mau = 24
p = 0.06
muc_y_nghia = 0.05
f= so_mau / tong_mau
print(f)
std_dev = math.sqrt((p*(1 - p)) / tong_mau)
print(std_dev)
z_score = (f - p) / std_dev
from scipy import stats
p_one_way_value = 1 - stats.norm.cdf(z_score)
p_value = p_one_way_value * 2 
print(p_value)