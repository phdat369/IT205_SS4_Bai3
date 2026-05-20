quantity = int(input("Nhập số lượng hóa đơn trong ca: "))
max = 0
min = 100000000000
for i in range(1,quantity+1):
    price =int(input(f"Nhập giá trị hóa đơn thứ {i}: "))
    if price > max:
        max = price 
    if price < min:
        min = price  

print("--- KẾT QUẢ KIỂM TOÁN CA RIKKEI STORE ---")
print(f"Hóa đơn có giá trị cao nhất: {max} VND")
print(f"Hóa đơn có giá trị thấp nhất: {min} VND")