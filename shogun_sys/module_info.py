# set this to your module directory, using forward slashes (/) not backward slashes (\):
export_dir = "C:/Users/Daniel/Desktop/Steam Folder/steamapps/common/MountBlade Warband/Modules/ShogunRP"

import os
import sys

if not os.path.isdir(export_dir) or not os.access(export_dir, os.W_OK):
  sys.exit("ERROR: unable to write to module export directory '" + export_dir + "'.")

def export_path(file_name):
  return os.path.join(export_dir, file_name)
