from os import listdir
import sys, getopt
import pdf2image # https://pypi.org/project/pdf2image/ (pip install pdf2image)


# Download poppler
# https://github.com/oschwartz10612/poppler-windows/releases/download/v20.09.0/Release-20.09.0.zip
# unzip poppler to ./poppler-20.09.0


def convert(p):
    l = listdir(p)
    for file in l:
        file = p + '\\' + file
        pages = pdf2image.convert_from_path(
            file, 500, 
            poppler_path=r"poppler-20.09.0\bin")
        n = 0
        for page in pages:
            new_file = file.lower().replace('.pdf', '.jpg').replace(' ', '_')
            if n:
                new_file = new_file.replace('.jpg', '_%s.jpg' % n)
            page.save(new_file, 'JPEG')
            n += 1


def main(argv):
    p = None
    try:
        opts, args = getopt.getopt(argv, "p:", ["path=", ])
    except getopt.GetoptError:
        print('python pdf2jpg.py -p <path>')
        sys.exit(2)
    for opt, arg in opts:
        if opt in ("-h", "--help", '-?'):
            print('python pdf2jpg.py -p <path>')
            sys.exit()
        elif opt in ("-p", "--path"):
            p = arg
    if p:
        convert(p)
        print()
    else:
        print('Example:')
        print('python pdf2jpg.py -p <path>')


if __name__ == "__main__":
    main(sys.argv[1:])
