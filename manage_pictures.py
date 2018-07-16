import os
import sys
from mysite.settings import BASE_DIR

file_path = os.path.join(BASE_DIR, 'temp')
files = os.listdir(file_path)

for file in files:
