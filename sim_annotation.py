import csv
from os import getcwd
import pandas as pd

sets=[('2007', 'train'), ('2007', 'val'), ('2007', 'test')]

classes = ["go","stop","warning"]

wd = getcwd()
wd = '/home/coldrain/data/'
sim = pd.read_csv(wd+'VOCdevkit/VOC2007/JPEGImages/annotation.csv')

def convert_annotation(year, image_id, list_file):
    for i in range(len(sim['Filename'])):
        # print(sim['Filename'][i].split('.')[0])
        if(sim['Filename'][i].split('.')[0] == image_id):
            cls = sim['label'][i]
            cls_id = classes.index(cls)
            b = (int(sim['Upper_left_corner_x'][i]), int(sim['Upper_left_corner_y'][i]), int(sim['Lower_right_corner_x'][i]), int(sim['Lower_right_corner_y'][i]))
            list_file.write(" " + ",".join([str(a) for a in b]) + ',' + str(cls_id))


for year, image_set in sets:
    image_ids = open(wd+'VOCdevkit/VOC%s/ImageSets/Main/%s.txt'%(year, image_set)).read().strip().split()
    list_file = open(wd+'%s_%s.txt'%(year, image_set), 'w')
    for image_id in image_ids:
        list_file.write('%sVOCdevkit/VOC%s/JPEGImages/%s.jpg'%(wd, year, image_id))
        convert_annotation(year, image_id, list_file)
        list_file.write('\n')
    list_file.close()

