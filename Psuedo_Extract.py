def zip():
    zip_archive = zipfile.ZipFile(filename, 'r')
    zip_archive.extractall(path=os.path.join(os.getcwd()) + '/extracted_zip')

    """this creates another directory and puts the file in that directory"""
    """move the file back into the other directory"""

def bzip():
    """check for extracted_zip_2 later"""

    if 'extracted_zip' in os.listdir():
        os.chdir('extracted_zip')
        line_list = []
        file = bz2file.open(filename, 'r')
        for line in file.readlines():
            line = str(line)
            line = line.replace('b', '')
            line = line[1:-3]
            line_list.append(line)
        filename = filename[0:-4]
        f = open(filename, 'w')
        new_file = '\n'.join(line_list)
        f.write(new_file)
        f.close()


    else:
        line_list = []
        file = bz2file.open(filename, 'r')
        for line in file.readlines():
            line = str(line)
            line = line.replace('b', '')
            line = line[1:-3]
            line_list.append(line)
        filename = filename[0:-4]
        f = open(filename, 'w')
        new_file = '\n'.join(line_list)
        f.write(new_file)
        f.close()



"""move it back to the right dir"""

def gzip():
    """have python check if there is a directory named extracted_zip and if there is then go
       into that directory and then run the code below, MAYBE DO THIS TWICE BECAUSE THERE COULD BE
       ZIP FILES IN THE EXTRACTED_ZIP DIRECTORY"""
    if 'extracted_zip' in os.listdir():
        os.chdir('extracted_zip')
        line_list = []
        import gzip
        f = gzip.open(filename, 'rb')
        for line in f.readlines():
            line = str(line)
            line = line.replace('b', '')
            line = line[1:-3]
            line_list.append(line)
        filename = filename[0:-3]
        f = open(filename, 'w')
        new_file = '\n'.join(line_list)
        f.write(new_file)
        f.close()
    else:
        line_list = []
        import gzip
        f = gzip.open(filename, 'rb')
        for line in f.readlines():
            line = str(line)
            line = line.replace('b', '')
            line = line[1:-3]
            line_list.append(line)
        filename = filename[0:-3]
        f = open(filename, 'w')
        new_file = '\n'.join(line_list)
        f.write(new_file)
        f.close()

def tar():
    global filename
    if 'extracted_zip' in os.listdir():
        os.chdir('extracted_zip')
        org_list = os.listdir()
        import tarfile
        tar = tarfile.open(filename)
        tar.extractall()
        tar.close()
        """then have the other files search if this exist"""
        new_list = os.listdir()

        for i in new_list:
            if i not in org_list:
                filename = i

    else:

        org_list = os.listdir()
        import tarfile
        tar = tarfile.open(filename)
        tar.extractall()
        tar.close()
        """then have the other files search if this exist"""
        new_list = os.listdir()

        for i in new_list:
            if i not in org_list:
                filename = i





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

        elif Current_ENC[0:9] == 'POSIX tar':
            tar()






if __name__ == '__main__':
    global filename
    main()
    print('success the filename is: {}'.format(filename))
