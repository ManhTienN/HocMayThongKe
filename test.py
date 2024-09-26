import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from scipy import stats
dienTich = [31,42,26,34,23,27,40,46]
giaNha = [342,452,269,378,243,270,395,379]
def myfunc(x):
    return  0.122222222* x + 
mymodel = list(map(myfunc,dienTich))
plt.scatter(dienTich,giaNha, label= 'Đồ Thị Giá Nhà')
plt.title('Đồ Thị Phân Tán Giá nhà')
plt.xlabel("Diện Tích(m2)")
plt.ylabel("Giá nhà(triệu VND)")
plt.plot(dienTich, mymodel)
plt.legend()
plt.show()
gia = myfunc(30)
print(gia)