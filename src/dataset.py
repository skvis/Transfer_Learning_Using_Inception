import os
from zipfile import ZipFile


def download_dataset():
    link_list = ['https://storage.googleapis.com/laurencemoroney-blog.appspot.com/horse-or-human.zip',
                 'https://storage.googleapis.com/laurencemoroney-blog.appspot.com/validation-horse-or-human.zip']

    if not os.path.isdir('../input'):
        os.makedirs('../input')
        for item in link_list:
            os.system(f"wget --no-check-certificate {item} -O ../input/{item.split('/')[-1]}")
    else:
        for item in link_list:
            if not os.path.exists(f"../input/{item.split('/')[-1]}"):
                os.system(f"wget --no-check-certificate {item} -O ../input/{item.split('/')[-1]}")
            else:
                print('File already exits')


def unzip_dataset(data_path, zip_filename):
    zip_ref = ZipFile(data_path+zip_filename, 'r')
    zip_ref.extractall(data_path+zip_filename.split('.')[0])
    zip_ref.close()
    os.remove(data_path+zip_filename)

# def download_weight():


if __name__ == '__main__':
    download_dataset()
    unzip_dataset('../input/', 'horse-or-human.zip')
    unzip_dataset('../input/', 'validation-horse-or-human.zip')
    # download_weight()
