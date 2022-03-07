import math
tong_mau = 300
so_mau = 30
p = 0.06
muc_y_nghia = 0.05
f = so_mau / tong_mau
std = math.sqrt((p*(1 - p)) / tong_mau)
print(std)
z_score = (f - p) / std
print(z_score)
from scipy import stats
p_one_way_value = 1 - stats.norm.cdf(z_score)
p_value = p_one_way_value * 2
print(p_value)
## giá trị p_value xấp xỉ = 5% khác với mức ý nghĩa là 6%
## bác bỏ giã thuyết "Tỷ lệ người lớn ở Hà Nội đi làm việc bằng xe đạp là 6%"