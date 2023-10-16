import os
from PIL import Image

# 指定要检测的文件夹路径
folder_path = "/root/autodl-fs/sun_temp/datasets/dataset_cls/aesthetics_60000"

# 获取文件夹中的所有文件
file_list = os.listdir(folder_path)

# 定义支持的图片文件格式扩展名
valid_extensions = (".jpg", ".jpeg", ".png")

# 遍历文件夹中的文件，删除非支持格式的文件
for filename in file_list:
    file_extension = os.path.splitext(filename)[1].lower()
    if file_extension not in valid_extensions:
        file_to_remove = os.path.join(folder_path, filename)
        os.remove(file_to_remove)
        print(f"已删除非支持格式的文件: {file_to_remove}")

# 再次获取更新后的文件列表
updated_file_list = os.listdir(folder_path)

# 遍历文件夹中的文件
for filename in updated_file_list:
    # 构建完整的文件路径
    file_path = os.path.join(folder_path, filename)
    
    try:
        # 尝试打开图像文件
        with Image.open(file_path) as img:
            img.verify()  # 尝试验证图像文件的完整性
    except (IOError, SyntaxError) as e:
        # 如果图像文件损坏，捕获异常并删除它
        os.remove(file_path)
        print(f"已删除损坏的文件: {file_path}")
    except Exception as e:
        print(f"处理文件时出错: {file_path} - {e}")

print("删除非支持格式的文件、损坏的文件完成")
