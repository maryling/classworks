import os
import re

tree = os.walk('.') #ходим по текущей папке, выводит generator - схлопнутый массив
#for d in tree:
#    print(d)

#for root, dirs, files in tree:
#    files = [f for f in files if len(f) > 7]
#    print(root, len(files))
    
#Задача 1
def delete_everything(path):
    for root, dirs, files in os.walk(path, topdown = False):
        for f in files:
            os.remove(os.path.join(root, f))
        for d in dirs:
            os.rmdir(os.path.join(root, d))
    return "Done!"
    
print(delete_everything("2539"))

#Задача 2 (недоделано)
def paint_tree(path):
    for root, dirs, files in os.walk(path):
        depth_root = root.count('\\')
        depth_dir = [f for f in files]
        #print(depth_root, dirs)
        print('{:>2}'.format())
    
print(paint_tree("ФИКЛ"))
