import os 

MY_FILES = ['index.html', 'style.css', 'app.js']


html_args = [
            '<!DOCTYPE html>\n',
            '<html>\n<head>\n <link rel="stylesheet" href="style.css">\n </head>\n',
            '<body>\n <script src="app.js"></script>\n </body>\n</html>'
             ]

HTML_BOILERPLATE = f'{html_args[0]} {html_args[1]} {html_args[2]}'


# function to create files
def create_files(files):
    for file in files:
        content = open( file, 'w')
        content.close()

#function to check if there are files already
# True == 1 and False == 0
def check_files():
    current_dir_files = os.listdir()
    for file in current_dir_files:
        if file == 'index.html' or file == 'style.css' or file == 'app.js':
            return 1
    return 0
