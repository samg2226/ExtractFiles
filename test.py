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

    tar = tarfile.open(filename)
    tar.extractall()
    tar.close()
    """then have the other files search if this exist"""


def after_zip():
    org_dir = os.getcwd()
    extracted_zip_listdir = os.listdir()
    counter = 0
    for file in extracted_zip_listdir:
        if counter >= 1:
            os.chdir(org_dir)
        test_dir = os.path.isdir(file)
        if test_dir == True:
            os.chdir(file)
            filename = file
            main()
        filename = file
        main()
        counter=+1


import magic
import zipfile
import os
import bz2file
import gzip
import tarfile
import numpy

def main():
    global filename
    """this is because the unzipping of files changes the name
       so you need to be able to mutate it all around the project"""

    Current_ENC = magic.from_file(filename)

    counter = 0

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
            old_files = os.listdir()
            tar()
            new_files = os.listdir()
            name_to_newdir = numpy.setdiff1d(new_files, old_files)
            name_to_newdir = str(name_to_newdir)
            os.chdir(name_to_newdir[2:-2])
            for files in os.listdir():
                filename = files
                main()
    """we need to go back in and change the directory back to what it was currently"""




if __name__ == '__main__':
    global filename
    filename = input('file name: ')
    """lets the user input the filename"""
    main()
    print('success')


