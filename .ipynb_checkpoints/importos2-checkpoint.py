import cv2
import os

# 数据集文件夹路径
dataset_folder = '/root/autodl-fs/sun_temp/datasets/dataset_cls/civitai_imgs/'

# 存储问题文件的列表
invalid_files = []

# 遍历数据集文件夹
for root, dirs, files in os.walk(dataset_folder):
    for file in files:
        file_path = os.path.join(root, file)
        try:
            # 尝试使用OpenCV打开图像文件
            img = cv2.imread(file_path)
            if img is None or img.size == 0:
                print(f"Invalid image: {file_path}")
                invalid_files.append(file_path)
                # 可以选择删除无效文件
                os.remove(file_path)
        except Exception as e:
            print(f"Error opening image: {file_path}")
            invalid_files.append(file_path)
            os.remove(file_path)

# 输出无效文件的数量
print(f"Number of invalid files: {len(invalid_files)}")

# 如果需要，你可以在这里处理无效文件，例如删除它们或进行其他修复操作
