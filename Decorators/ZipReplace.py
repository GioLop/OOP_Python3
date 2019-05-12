import sys
import os
import shutil
import zipfile

class ZipReplace:
    def __init__(self, filename, search_string, replace_string):
        self.filename = filename
        self.search_string = search_string
        self.replace_string = replace_string
        self.temp_directory = "unzipped-{}".format(filename)
    
    def _full_filename(self, filename):
        return os.path.join(self.temp_directory, filename)
    
    def zip_find_replace(self):
        pass
    
    def unzip_files(self):
        os.mkdir(self.temp_directory)
        zip = zipfile.ZipFile(self.filename)

        try:
            zip.extractall(self.temp_directory)
        finally:
            zip.close()
    
    def find_replace(self):
        pass
    
    def zip_files(self):
        pass

if __name__ == "__main__":
    ZipReplace(*sys.argvs[1:4]).zip_find_replace()