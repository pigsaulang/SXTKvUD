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
print("THỰC HÀNH 16")
print(p_value)

## Kiểm tra p-value với mức ý nghĩa là 0.05, như định nghĩa ở trên. P_value < muc_y_nghia=0.05 (P_value ≈ . 1)
## Từ đó có thể suy ra p-value của hai đuôi (0.04) nhỏ hơn mức ý nghĩa thống kê là 0.05.
## Vậy, bác bỏ giả thuyết không và chấp nhận giả thuyết nghịch.
## Kết luận: chứng cứ rằng "Tỷ lệ người dân ở Hà Nội đi làm bằng xe
## đạp khác với 6%“.ác bỏ giã thuyết "Tỷ lệ người lớn ở Hà Nội đi làm việc bằng xe đạp là 6%" 