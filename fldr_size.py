import os
def get_tree_size(path):
    """Return total size of files in given path and subdirs."""
    total = 0
    for entry in os.scandir(path):
        if entry.is_dir(follow_symlinks=False):
            total += get_tree_size(entry.path)
        else:
            total += entry.stat(follow_symlinks=False).st_size
    return total


list_of_fldrs = [
    r"c:\sciezka\jakis\cos"
]



for item in list_of_fldrs:
    line = item.split("\\")
    list_of_func = [ line[ len(line)-1].upper() ]
    #print(list_of_func)
    #print('{0:4}=> {1} {2}'.format(list_of_func[0], get_tree_size(item)/1048576,' MB'))
    print('{0:4}=> {1:06.5f} {2}'.format(list_of_func[0], get_tree_size(item)/1048576,' MB'))


#https://www.python.org/dev/peps/pep-0471/
#TODO 1 - zaokraglic wyniki rozmiaru folderow, print("%.2f" % a)
#TODO 2 - umieścić ilosc plikow przy kazdej funkcji
