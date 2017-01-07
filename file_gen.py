# generates a post file
# @arg arg1 : name of post (may also include categories as an array)
# proc for creating post: write it all out first, check it over, gen file, paste, push
# default is markdown but may also want some html with css formatting
import sys
from datetime import datetime
if len(sys.argv) == 2:
    arg = sys.argv[1]
#    filename_arr = arg.replace('/', '%/').split(' ') # escape sequence for forbidden characters in url
    if '/' not in arg:
        filename_arr = arg.split(' ') # TODO: find a way to incorporate / characters in the filename
        now = datetime.now()
        index = '_posts/'
        file_format = '.markdown'
        timezone = '-0800'
        date = str(now.date())
        time = str(now.time())
        # filename: [year as first substring of date by " "]-[str1]-...-[strn].markdown
        # where stri are lowercase substrings of filename
        filename = '' + date # file name starts with date
        if len(filename_arr) > 0:
            for substr in filename_arr:
                filename += ('-' + substr.lower())
        f = open(index + filename + file_format, 'w')
        # write template content to the file
        f.write('---\n')
        f.write('layout: post\n')
        f.write('title:  \"' + arg + '\"\n')
        f.write('date:   ' + date + ' ' + time + ' ' + timezone +'\n')
        f.write('categories: \n')
        f.write('---\n')
    else:
        raise Exception( 'exception: do not include \'/\' in file name!' )
else:
    raise Exception( 'exception: could not generate file (please provide 1 string for args)' )
