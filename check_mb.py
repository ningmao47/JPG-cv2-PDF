import os
import csv

target_folder = r"test"

def get_folder_size(folder_path):
    total_size = 0
    for root, dirs, files in os.walk(folder_path):
        for file in files:
            file_path = os.path.join(root, file)
            if os.path.exists(file_path):
                total_size += os.path.getsize(file_path)
    return total_size

folder_sizes = []

# 計算每個子資料夾大小
for item in os.scandir(target_folder):
    if item.is_dir():
        size_bytes = get_folder_size(item.path)
        size_mb = size_bytes / (1024 * 1024)
        folder_sizes.append((item.name, size_mb))

# 由大到小排序
folder_sizes.sort(key=lambda x: x[1], reverse=True)

# 只取前 200 個
top_200 = folder_sizes[:200]

# CSV 輸出路徑
csv_path = os.path.join(target_folder, "folder_size_top200.csv")

with open(csv_path, mode="w", newline="", encoding="utf-8-sig") as f:
    writer = csv.writer(f)
    writer.writerow(["排名", "資料夾名稱", "大小 (MB)"])
    for idx, (name, size) in enumerate(top_200, start=1):
        writer.writerow([idx, name, f"{size:.2f}"])

print("✅ 已完成：只匯出前 200 個最大資料夾")
print(f"📄 CSV 檔案位置：{csv_path}")