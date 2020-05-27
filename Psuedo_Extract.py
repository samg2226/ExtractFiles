def zip():
    zip_archive = zipfile.ZipFile(filename, 'r')
    zip_archive.extractall(path=os.path.join(os.getcwd()) + '/extracted_zip')
    """move the file back into the other directory"""

def bzip():
    """unzip the file"""
    """move it bak the other original dir"""


def gzip():
    """extract gzip"""
    """move it back to the original dir"""



import magic
import zipfile
import os

def main():
    global filename
    """this is because the unzipping of files changes the name
       so you need to be able to mutate it all around the project"""

    filename = input('file name: ')
    """lets the user input the filename"""

    Current_ENC = magic.from_file(filename)

    while Current_ENC != 'ASCII text':

        Current_ENC = magic.from_file(filename)

        if Current_ENC[0:4] == 'gzip':
            gzip()

        elif Current_ENC == 'bzip':
            bzip()

        elif Current_ENC[0:3] == 'zip':
            zip()

    return 'success the file is in {}'.format(os.getcwd())




if __name__ == '__main__':
    main()

