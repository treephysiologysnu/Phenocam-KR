import csv
import os
from django.shortcuts import render
from mysite.settings import BASE_DIR

'''
File Format in metadata files
site_name, Mt. Chilbo(01)
lat, 37.265542
long, 126.940473
location, Suwon, Gyeonggi-do
start_date, 2018-05-18
species, Kousa Dogwood
camera, Raspberry Pi Camera V2
'''


def read_metadata(site_name):
    result = dict()
    meta_path = os.path.join(BASE_DIR, 'data', site_name, 'metadata')
    f = open(meta_path, 'r', encoding='utf-8')
    reader = csv.reader(f)
    for line in reader:
        result[line[0]] = line[1]
    f.close()
    return result

def index(request, site_name):
    context = read_metadata(site_name)
    return render(request, 'sites/index.html', context)