import os
import shutil
import random

# 源文件夹和目标文件夹的路径
source_folder = '/root/autodl-fs/sun_temp/datasets/dataset_cls/civitai_imgs'
destination_folder = '/root/autodl-fs/sun_temp/datasets/dataset_cls/civitai_imgs_20000'

# 获取源文件夹中所有文件的列表
all_files = os.listdir(source_folder)

# 如果源文件夹中的文件少于20000个，你可以选择所有文件
if len(all_files) <= 20000:
    selected_files = all_files
else:
    # 使用集合来跟踪已选择的文件，确保不重复选择
    selected_files = set()

    # 随机选择20000个不重复的文件
    while len(selected_files) < 20000:
        file_name = random.choice(all_files)
        selected_files.add(file_name)

# 确保目标文件夹存在，如果不存在则创建它
if not os.path.exists(destination_folder):
    os.makedirs(destination_folder)

# 复制选中的文件到目标文件夹
for file_name in selected_files:
    source_file_path = os.path.join(source_folder, file_name)
    destination_file_path = os.path.join(destination_folder, file_name)
    shutil.copy(source_file_path, destination_file_path)

print(f'已从{source_folder}复制{len(selected_files)}个文件到{destination_folder}')
