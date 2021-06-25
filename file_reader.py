# This will return the contents of a file
def read_file(file_name):

    file_contents = open(file_name, 'r')
    contents = file_contents.read()
    file_contents.close()

    return contents


if __name__ == '__main__':
    pass
