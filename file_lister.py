# this is used to produce the list of directories and STL files they contain as a tree.
# it will self prune, so directories that don't contain any STL files will get cut.
import os

def scan_directory(root, path):
    tree = []
    for entry in os.scandir(path):
        if entry.is_dir():
            dir = {
                'type': 'folder',
                'name': entry.name,
                'children': scan_directory(root, entry.path)
            }
            if __dir_has_stl_file(dir):
                tree.append(dir)
        elif entry.is_file() and entry.name.lower().endswith('.stl'):
            tree.append({
                'type': 'file',
                'name': entry.name,
                'path': os.path.relpath(entry.path, root).replace('\\', '/')
            })
        
    return tree
    
def __dir_has_stl_file(dir_node):
    for node in dir_node['children']:
        print(node)
        if 'children' in node: # is a dir, so scan it
            if (__dir_has_stl_file(node)):
                return True
        else:
            return True
    return False
