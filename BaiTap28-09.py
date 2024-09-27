import pandas as pd
import numpy as np 
import re

# Đọc dữ liệu
data = pd.read_csv("Bengaluru_House_Data.csv")
df = pd.DataFrame(data)

# Điền giá trị null
df['society'] = df['society'].fillna('Null')
df['bath'] = df['bath'].fillna(0)
df['balcony'] = df['balcony'].fillna(0)

# Xóa giá trị trùng lặp
df1 = df.drop_duplicates()
def convert_to_float(value):
    if isinstance(value, str) and value.replace('.', '', 1).isdigit():  # Kiểm tra nếu chỉ chứa số
        return float(value)  # Chuyển đổi sang float
    return value  # Giữ nguyên nếu không phải số
# Định nghĩa hàm kiểm tra float
def is_float(x):
    try:
        float(x)
    except:
        return False
    return True
def convert_sq_meter_to_sqft(x):
    if isinstance(x, str):
        # Chỉ chuyển đổi khi có từ khóa 'meter'
        number_part = ''.join(filter(str.isdigit, x))
        if number_part:
            return float(number_part) * 10.7639
    return x  

# Định nghĩa hàm chuyển đổi
def convert_sqft_to_num(x):
    if isinstance(x, str):
        tokens = x.split('-')
        if len(tokens) == 2:
            return (float(tokens[0]) + float(tokens[1])) / 2
        try:
            return float(x)
        except ValueError:
            return x
    return x
df1['total_sqft'] = df1['total_sqft'].apply(convert_to_float)

df2 = df1.copy()
df2['total_sqft'] = df2['total_sqft'].apply(convert_sqft_to_num)

# Sao chép DataFrame
df3 = df2.copy()
df3['total_sqft'] = df3['total_sqft'].apply(convert_sq_meter_to_sqft)

# Lọc các hàng có giá trị không null
df2 = df2[df2.total_sqft.notnull()]

# In kích thước của các DataFrame
print(df1[~df1['total_sqft'].apply(is_float)].shape)
print(df.shape)
print(df1.head(10))
print(df2.head(10))
print(df3.head(10))
df3.to_csv('check.csv', index=False)

