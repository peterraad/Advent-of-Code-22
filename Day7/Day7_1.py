
# def search_directory(tree):
#     for object in tree:
#         # if object is folder
#         if object is folder:
#             folder_ownership_list.append(folder_name)
#             search_directory(object)
#         else:
#             for folder in folder_ownership_list:
#                 folder.file_size += object.file_size    

class Folder:
    level: int
    name: str

    def __init__(self, level, name) -> None:
        self.level = level
        self.name = name

# class File:
#     level: int
#     size: int
#     folder_ownership_list: list


class Ownership:
    folder_owner: str
    size: int
    child_of_folders: list

    def __init__(self, folder_name, size, child_of_folders) -> None:
        self.folder_name = folder_name
        self.size = size
        self.child_of_folders = child_of_folders

    def add_size(self, file_size):
        self.size += file_size


current_folder_list = []
file_list = []
folder_ownership_dict = {}


with open("test_fs.txt") as rpsFile:
    lines = []
    current_level = 0
    
    for line in rpsFile:
        line = line.rstrip()
        # check if command
        # detect file ownership
        
        if line[0] == '$':
            # is command
            if line[2:4] == 'cd':
                # cd command
                if line[5:7] == '..':
                    # go up one level
                    current_level -= 1
                    current_folder_list.pop()
                else: 
                    # went into new folder
                    current_level += 1
                    current_folder_list.append(Folder(level=current_level, name=line[5:len(line)]))
                    # folder_ownership_list.append(Ownership(line[0:len(line)], ))
        else:

            if line[0:3] != 'dir':
                for parent_folder in current_folder_list:
                    file_size = int(''.join(filter(str.isdigit, line)))

                    if parent_folder.name in folder_ownership_dict:
                        folder_ownership_dict[parent_folder.name].add_size(file_size)
                    else:
                        folder_ownership_dict[parent_folder.name] = Ownership(folder_name=parent_folder.name, size=file_size,
                                                                              child_of_folders=current_folder_list[:-1])
            # else:
            #     for folder in current_folder_list:
            #         folder_ownership_list.append(Ownership(folder.name, ))

tally_folders = 0
for folder_owner in folder_ownership_dict:
    if len(folder_ownership_dict[folder_owner].child_of_folders) != 0:
        print(folder_ownership_dict[folder_owner].child_of_folders)
        for parent_folder in folder_ownership_dict[folder_owner].child_of_folders:
            folder_ownership_dict[parent_folder.name].add_size(folder_ownership_dict[folder_owner].size)

for folder_owner in folder_ownership_dict:
    print(
        f"folder {folder_ownership_dict[folder_owner].folder_name} has a total of {folder_ownership_dict[folder_owner].size}")
    if folder_ownership_dict[folder_owner].size < 100000:
        tally_folders += 1

print(tally_folders)
