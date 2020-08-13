import zipfile
import os

zip_path = 'E:\\error_log.zip'
dir_path = 'E:\\automate\\error_log\\'

zip = zipfile.ZipFile(path, 'a')
for foldername, subfolders, filenames in os.walk(dir_path):
    for filename in filenames:
        zip.write(os.path.join(foldername, filename), compress_type=zipfile.ZIP_DEFLATED)
zip.close()
