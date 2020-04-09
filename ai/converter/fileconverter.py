import zlib
import hashlib


def get_filename_without_ending(file_path):
    """
    Returns the filename without extension
    :param file_path:
    :return:
    """

    # if filename has file_path parts
    if '/' in file_path:
        filename = file_path.rsplit('/')[-1]
    else:
        filename = file_path

    return filename.rsplit('.', 1)[0]


def crc(filename):
    prev = 0
    for line in open(filename, "rb"):
        prev = zlib.crc32(line, prev)
    return "%X" % (prev & 0xFFFFFFFF)


def md5_checksum(file_path):
    """
    Returns the md5 checksum of the file from the given file_path
    :param file_path:
    :return:
    """
    fh = open(file_path, 'rb')
    m = hashlib.md5()
    while True:
        data = fh.read(8192)
        if not data:
            break
        m.update(data)
    return m.hexdigest()
