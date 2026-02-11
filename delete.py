import os

# 目標資料夾路徑（注意 r"" 避免跳脫問題）
target_folder = r"test"

# 掃描 test 底下的所有子資料夾
subfolders = [f.path for f in os.scandir(target_folder) if f.is_dir()]

for folder in subfolders:
    for item in os.scandir(folder):
        if item.is_file():
            os.remove(item.path)

print("✅ 已刪除 test 底下所有子資料夾內的檔案（資料夾保留）")