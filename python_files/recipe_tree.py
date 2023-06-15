from helper import RecipeFile
import os

class RecipeTree():
  def __init__(self, path):
    self._tree = {}
    if not os.path.exists(path + os.sep + 'recipes'):
        print("Can not find recipes folder")
        return
    else:
        root = os.walk(path + os.sep + 'recipes')
        for node in root:
            if node[1]:
                # These are directories
                for directory in node[1]:
                    if directory:
                        self.add_directory(directory)
            if node[2]:
                # These are files
                for file_name in node[2]:
                    # Find what directory we are in
                    folder = os.path.basename(node[0])
                    if folder == 'recipes':
                        self.add_file_to_dir(node[0], 'FLAT', file_name)
                    else:
                        self.add_file_to_dir(node[0], folder, file_name)

  @property
  def tree(self):
    return self._tree

  def __str__(self):
    string = "Recipes:\n"
    for folder in self.tree:
        if folder != 'FLAT':
            string += f'  {folder}\n'
            for node in self.tree[folder]:
                string += f'  ├── {node.file}\n'
    index = string.rfind('├')
    string = string[:index] + '└' + string[index + 1:]
    for folder in self.tree:
        if folder == 'FLAT':
            for node in self.tree[folder]:
                string = string + f'- {node.file}\n'

    return string

  def __repr__(self):
      # It is possible that this should be improved for pprints sake.
      return self.__str__

  def add_directory(self, folder):
      if folder:
          if folder not in self.tree:
              self._tree[folder] = []

  def add_file_to_dir(self, path, folder, file_name):
      if file_name.endswith('cook'):
          if folder not in self.tree:
              self._tree[folder] = [RecipeFile(file_name, path + os.sep + file_name)]
          else:
              if not self.tree[folder]:
                  self._tree[folder] = [RecipeFile(file_name, path + os.sep + file_name)]
              else:
                  self._tree[folder].append(RecipeFile(file_name, path + os.sep + file_name))
