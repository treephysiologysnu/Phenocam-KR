import os, glob
from django.shortcuts import render
from mysite.settings import BASE_DIR

def get_folder_list(path, files):
    result = []
    for file in files:
        if os.path.isdir(os.path.join(path, file)):
            result.append(file)
    return result

def read_sites_path():
    path = os.path.join(BASE_DIR, 'data')
    files = os.listdir(path)
    return get_folder_list(path, files)

def read():
    result = dict()
    site_list = read_sites_path()
    for site in site_list:
        path = os.path.join(BASE_DIR, 'data', site)
        year_list = get_folder_list(path, os.listdir(path))
        max_year = max(year_list)
        path = os.path.join(path, max_year)
        max_month = max(os.listdir(path))
        path = os.path.join(path, max_month)
        file_list = os.listdir(path)
        file_list.sort()
        result[site] = os.path.join('data', site, max_year, max_month, file_list.pop())
    print(result)
    return result

def index(request):
    site_list = read()
    context = {
        'site_list' : site_list,
    }
    return render(request, 'gallery/index.html', context)