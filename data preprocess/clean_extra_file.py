#encoding:utf-8
'''
there are some xml files don't match with any images.
this file is to remove those xml files.

need to modify outDir imgDir and annoDir.
'''

import os
import shutil
import glob
from PIL import Image

outDir=os.path.abspath('/home/sy/DataSet/cv-project/data/myanno')
imgDir=os.path.abspath('/home/sy/DataSet/cv-project/data/JPEGImages')
annoDir=os.path.abspath('/home/sy/DataSet/cv-project/data/Annotations')

#定义要处理的第一个文件夹变量
image1 = [] #image1指文件夹里的文件，包括文件后缀格式；
imgname1 = [] #imgname1指里面的文件名称，不包括文件后缀格式

#通过glob.glob来获取第一个文件夹下，所有'.jpg'文件
imageList1 = glob.glob(os.path.join(imgDir, '*.jpg'))

#遍历所有文件，获取文件名称（包括后缀）
for item in imageList1:
    image1.append(os.path.basename(item))

#遍历文件名称，去除后缀，只保留名称
for item in image1:
    (temp1, temp2) = os.path.splitext(item)
    imgname1.append(temp1)

#对于第二个文件夹路径，做同样的操作
anno2 = []#basename.xml
annoname2 = []#basename
annoList2 = glob.glob(os.path.join(annoDir, '*.xml'))#absname.xml

for item in annoList2:
    anno2.append(os.path.basename(item))

for item in anno2:
    (temp1, temp2) = os.path.splitext(item)
    annoname2.append(temp1)

#通过遍历，获取第一个文件夹下，文件名称（不包括后缀）与第二个文件夹相同的文件，并另存在outDir文件夹下。文件名称与第一个文件夹里的文件相同，后缀格式亦保持不变。

for item1 in imgname1:
    for item2 in annoname2:
        if item1 == item2:
            dir = annoList2[annoname2.index(item2)]
            
            name = os.path.basename(dir)
            shutil.copyfile(dir,os.path.join(outDir,name))
            #img.save(os.path.join(outDir, name))
            

'''
num=0
for item1 in imgname1:
    for item2 in annoname2:
        if item1 == item2:
            num=num+1
print(num)'''
