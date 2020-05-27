def zip(filename):
    zip_archive = zipfile.ZipFile(filename, 'r')
    zip_archive.extractall(path=os.path.join(os.getcwd()) + '/extracted_zip')
    """move the file back into the other directory"""

def bzip(filename):
    """unzip the file"""
    """move it bak the other original dir"""


def gzip(filename):
    """extract gzip"""
    """move it back to the original dir"""



import magic
import zipfile
import os
def main(filename):

    Current_ENC = magic.from_file(filename)
    while(Current_ENC != 'ASCII text'):
        Current_ENC = magic.from_file(filename)
        if Current_ENC[0:4] == 'gzip':
            gzip(filename)
            """change the filename"""
        elif Current_ENC == 'bzip':
            bzip(filename)
            """change the filename"""
        elif Current_ENC[0:3] == 'zip':
            zip(filename)
            """change the filename"""

if __name__ == '__main__':
    main("""filename""")

    """create git tommorow"""