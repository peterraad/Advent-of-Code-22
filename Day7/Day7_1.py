
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
    folder_name: str
    size: int
    parent_folders: list

    def __init__(self, folder_name, size, parent_folders) -> None:
        self.folder_name = folder_name
        self.size = size
        self.parent_folders = parent_folders

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
                    current_folder_list.append(line[5:len(line)])
                    # folder_ownership_list.append(Ownership(line[0:len(line)], ))
        else:

            if line[0:3] != 'dir':
                for parent_folder in current_folder_list:
                    file_size = int(''.join(filter(str.isdigit, line)))

                    if parent_folder in folder_ownership_dict:
                        folder_ownership_dict[parent_folder].add_size(file_size)
                    else:
                        folder_ownership_dict[parent_folder] = Ownership(folder_name=parent_folder, size=file_size,
                                                                              parent_folders=current_folder_list)
            # else:
            #     for folder in current_folder_list:
            #         folder_ownership_list.append(Ownership(folder.name, ))

# for folder_owner in reversed(folder_ownership_dict):
#     if len(folder_ownership_dict[folder_owner].parent_folders) != 0:
#         current_folder_key = folder_ownership_dict[folder_owner].folder_name
#         print(f"Current folder we are in: {folder_ownership_dict[folder_owner].folder_name}")
#         parent_folder_to_be_added_key = folder_ownership_dict[folder_owner].parent_folders[-1].name
#         print(parent_folder_to_be_added_key)
#         print(f"adding {folder_ownership_dict[current_folder_key].size} from {folder_ownership_dict[current_folder_key].folder_name} to {folder_ownership_dict[parent_folder_to_be_added_key].folder_name}")
#         folder_ownership_dict[parent_folder_to_be_added_key].add_size(folder_ownership_dict[current_folder_key].size)
        # for parent_folder in folder_ownership_dict[folder_owner].parent_folders:
        #     print(parent_folder.name)
        #     folder_ownership_dict[parent_folder.name].add_size(folder_ownership_dict[folder_owner].size)
        #     print(f"adding {folder_ownership_dict[folder_owner].size} to {folder_ownership_dict[parent_folder.name].size}")

tally_folders = 0
target_directories = []

for folder_owner in folder_ownership_dict:
    print(
        f"folder {folder_ownership_dict[folder_owner].folder_name} has a total of {folder_ownership_dict[folder_owner].size}")
    if folder_ownership_dict[folder_owner].size <= 100000:
        target_directories.append(folder_ownership_dict[folder_owner])

print(len(target_directories))
for folder in target_directories:
    tally_folders += folder.size
print(tally_folders)
