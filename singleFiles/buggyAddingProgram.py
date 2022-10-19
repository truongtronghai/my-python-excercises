#! python

import webbrowser, sys, pyperclip
if len(sys.argv) > 1 :
    # get address from command line
    print(sys.argv)

pyperclip.copy('tom-kho-an-hoa-400g/')
webbrowser.open('https://liketobuy.vn/san-pham/' + pyperclip.paste())
