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
##Ta có p-value gần bằng 0.01. Nó có ý nghĩa là giả sử 6% người lớn ở Hà Nội đi làm bằng xe đạp, khả năng ta lấy được một mẫu ngẫu nhiên có 10% người Hà Nội đi làm bằng xe đạp là 1%.
##Kiểm tra p-value với mức ý nghĩa là 0.05, như định nghĩa ở trên. P_value < muc_y_nghia=0.05 (P_value ≈ . 1)
##Từ đó có thể suy ra p-value của hai đuôi (0.01) nhỏ hơn mức ý nghĩa thống kê là 0.05.
##Vậy, bác bỏ giả thuyết không và chấp nhận giả thuyết nghịch.
##Kết luận: chứng cứ rằng "Tỷ lệ người dân ở Hà Nội đi làm bằng xe
##đạp khác với 6%“