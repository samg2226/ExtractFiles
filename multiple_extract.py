
def zip():
    global filename
    zip_archive = zipfile.ZipFile(filename, 'r')
    zip_archive.extractall(path=os.path.join(os.getcwd()) + '/extracted_zip')
    """this creates another directory and puts the file in that directory"""
    """move the file back into the other directory"""
    filename = filename[0:-4]
def bzip():
    global filename
    with bz2file.open(filename, 'rb') as infile:
        with open(filename[0:-4], 'wb') as outfile:
            for line in infile.readlines():
                outfile.write(line)
    outfile.close()
    filename = filename[0:-4]




"""move it back to the right dir"""

def gzip_func():
    global filename

    with gzip.open(filename, 'rb') as infile:
        with open(filename[0:-3], 'wb') as outfile:
            for line in infile:
                outfile.write(line)
    outfile.close()
    filename = filename[0:-3]


def tar():

    global filename

    org_list = os.listdir()
    tar = tarfile.open(filename)
    tar.extractall('extracted_tar')
    tar.close()
    """then have the other files search if this exist"""

def after_zip():
    for file in os.listdir():
        filename = file
        main()


def after_tar():
    for file in os.listdir():
        filename = file
        main()


import magic
import zipfile
import os
import bz2file
import gzip
import tarfile




def main():
    global filename
    """this is because the unzipping of files changes the name
       so you need to be able to mutate it all around the project"""



    Current_ENC = magic.from_file(filename)

    counter = 0
    tar_counter = 0
    while Current_ENC != 'ASCII text':

        Current_ENC = magic.from_file(filename)

        if Current_ENC[0:4] == 'gzip':
            gzip_func()

        elif Current_ENC[0:4] == 'bzip':
            bzip()

        elif Current_ENC[0:3] == 'Zip':
            if counter == 0:

                zip()
                os.chdir('extracted_zip')
                after_zip()
            elif counter == 1:
                zip()
                os.chdir('extracted_zip_2')
                after_zip()
            elif counter == 2:

                zip()
                os.chdir('extracted_zip_3')
                after_zip()

            counter = counter + 1

        elif Current_ENC[0:9] == 'POSIX tar':
            if tar_counter == 0:
                tar()
                os.chdir('extracted_tar')
                after_tar()
            elif tar_counter == 1:
                tar()
                os.chdir('extracted_tar_2')
                after_tar()
            elif tar_counter == 2:
                tar()
                os.chdir('extracted_tar_3')
                after_tar()





if __name__ == '__main__':
    global filename
    filename = input('file name: ')
    """lets the user input the filename"""
    main()
    print('success')




