import os

def add_gitkeep(directory):
    # 检查每个文件夹，确定它是否为空
    for dirpath, dirnames, filenames in os.walk(directory):
        # 如果文件夹为空（没有子文件夹和文件）
        if not dirnames and not filenames:
            gitkeep_path = os.path.join(dirpath, '.gitkeep')
            # 创建一个空的 .gitkeep 文件
            open(gitkeep_path, 'a').close()
            print(f'Created {gitkeep_path}')

# 获取脚本当前所在的目录
current_directory = os.path.dirname(os.path.realpath(__file__))
add_gitkeep(current_directory)
