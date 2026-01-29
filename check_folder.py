import os
import sys
import glob

# 列出C盘根目录所有文件夹
print("C盘根目录文件夹:")
for item in os.listdir("C:\\"):
    if os.path.isdir(os.path.join("C:\\", item)):
        print(f"  {item}")

# 尝试找到那个中文文件夹
print("\n尝试读取中文文件夹内容:")
try:
    # 使用原始字符串和编码处理
    chinese_folders = [f for f in os.listdir("C:\\") 
                      if os.path.isdir(os.path.join("C:\\", f)) and len(f) > 5]
    
    for folder in chinese_folders:
        print(f"\n检查文件夹: {folder}")
        try:
            folder_path = os.path.join("C:\\", folder)
            items = os.listdir(folder_path)
            for item in items[:10]:  # 只显示前10个
                item_path = os.path.join(folder_path, item)
                size = os.path.getsize(item_path) if os.path.isfile(item_path) else 0
                print(f"  {item} (Size: {size} bytes)")
        except Exception as e:
            print(f"  无法读取: {e}")
except Exception as e:
    print(f"错误: {e}")