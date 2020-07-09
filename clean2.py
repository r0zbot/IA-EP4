import sys

filenames = sys.argv[1:]

for f in filenames:
    with open(f, 'rb') as iso_file:
        text = iso_file.read()
        result = text.decode('iso-8859-1').encode('utf-8')
        with open(f + '_utf.csv', 'wb') as utf_file:
            utf_file.write(result)