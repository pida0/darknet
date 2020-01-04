# coding=utf-8
import os
from os import listdir, getcwd
from os.path import join
if __name__ == '__main__':  # 只有在文件作为脚本文件直接执行时才执行下面代码
    source_folder='/home/sy/DataSet/cv-project/示例/示例/testimage/' #图片保存的路径
    dest='/home/sy/DataSet/cv-project/示例/示例/test.txt' #写有图片的名字的路径
    file_list=os.listdir(source_folder)#获取各图片的名称       
    test_file=open(dest,'a')    #追加写打开              
    count = 0              
    for file_obj in file_list:  
        count += 1                
        file_path=os.path.join(source_folder,file_obj) #路径拼接  指向 图片文件的路径
        # file_name,file_extend=os.path.splitext(file_path) #分离文件名与扩展名 file_name为去掉扩展名的图片名称 
        test_file.write(file_path+'\n')  #写入去掉扩展名的文件名名称
    test_file.close() #关闭文件


