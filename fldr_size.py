import os

def get_tree_size(path):
    """Return total size of files in given path and subdirs."""
    total = 0
    files = 0
    for entry in os.scandir(path):
        if entry.is_dir(follow_symlinks=False):
            total += get_tree_size(entry.path)
            files += 1
        else:
            total += entry.stat(follow_symlinks=False).st_size
    return total


list_of_fldrs = [
    r"c:\intel"
    # r"z:\03_Work\05_GroundTruth\FS",
    # r"z:\03_Work\05_GroundTruth\LA",
    # r"z:\03_Work\05_GroundTruth\LbD",
    # r"z:\03_Work\05_GroundTruth\LD",
    # r"z:\03_Work\05_GroundTruth\ObsD",
    # r"z:\03_Work\05_GroundTruth\PED",
    # r"z:\03_Work\05_GroundTruth\ped3",
    # r"z:\03_Work\05_GroundTruth\ppp",
    # r"z:\03_Work\05_GroundTruth\sl",
    # r"z:\03_Work\05_GroundTruth\tld",
    # r"z:\03_Work\05_GroundTruth\tsr",
    # r"z:\03_Work\05_GroundTruth\ucr",
    # r"z:\03_Work\05_GroundTruth\ved",
    # r"z:\03_Work\05_GroundTruth\ved3",
    # r"z:\03_Work\05_GroundTruth\vlb",
    # r"z:\03_Work\05_GroundTruth\vlm",
    # r"z:\03_Work\05_GroundTruth\vlr"
]



for item in list_of_fldrs:
    line = item.split("\\")
    list_of_func = [ line[ len(line)-1].upper() ]
    #print(list_of_func)
    print('{0:4}=> {1} {2}'.format(list_of_func[0], get_tree_size(item)/1048576,' MB' ))


#https://www.python.org/dev/peps/pep-0471/