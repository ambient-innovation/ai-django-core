import zlib
import hashlib


def get_filename_without_ending(filepath):
    """
    Returns the filename without extension
    :param filename:
    :return:
    """

    # if filename has filepath parts
    if '/' in filepath:
        filename = filepath.rsplit('/')[-1]
    else:
        filename = filepath

    return filename.rsplit('.', 1)[0]


def crc(fileName):
    prev = 0
    for eachLine in open(fileName,"rb"):
        prev = zlib.crc32(eachLine, prev)
    return "%X"%(prev & 0xFFFFFFFF)


def md5_checksum(filePath):
    """
    Returns the md5 checksum of the file from the given filepath
    :param filePath:
    :return:
    """
    fh = open(filePath, 'rb')
    m = hashlib.md5()
    while True:
        data = fh.read(8192)
        if not data:
            break
        m.update(data)
    return m.hexdigest()
