import os

relativepath = 'relative_path.txt'  # 生成相对路径的txt
absolutepath = 'Absolute path.txt'  # 绝对路径的txt
fw_rel = open(relativepath, "w")
fw_abs = open(absolutepath, "w")

def get_all_file_name(dir):
    for root, dirs, files in os.walk(dir):
        dir
        # print("根目录", root)  # 当前目录路径
        # print("子目录", dirs)  # 当前路径下所有子目录
        # print("文件名", files)  # 当前路径下所有非目录子文件
        for file in files:
            #print("路径", root)
            #print("文件名", file)
            rel = root.replace(dir, "", 1)
            #print("相对路径", rel)
            #保存文件的相对路径
            save_rel = rel + file
            print("relativepath:",save_rel)
            fw_rel.write(save_rel+'\n')
            #保存文件的绝对路径
            save_abs = root + file
            print("absolutepath:",save_abs)
            fw_abs.write(save_abs+'\n')


if __name__ == '__main__':
    root_dir = os.getcwd()#输入当前文件路径
    get_all_file_name(root_dir)
    # dirpath = ""  # 指定根目录
    # read_directory(dirpath)
