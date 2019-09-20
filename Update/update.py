'''
github.com/razyar
Notice: ln: [19] (url = host) -> if you have your own update for 0x2. you have 2 choose:
    1- set your update name to up0x2.py
    2- set your fav name but you need change call.py file and change calling object to your update file name.
    3 <<< you can only change  in the update_url(). in update_github() it auto update from our github page.

Notice:
    " Before public the 0x2 change this file to your host. ex:
        change ln [19]: url = "https://razyar.github.io/up0x2.py"

'''

import os
import sys
import urllib2

def update_url(host):
    url = host
    file_name = url.split('/')[-1]
    u = urllib2.urlopen(url)
    f = open(file_name, 'wb')
    meta = u.info()
    file_size = int(meta.getheaders("Content-Length")[0])
    print "Downloading: %s Bytes: %s" % (file_name, file_size)
    file_size_dl = 0
    block_sz = 8192
    while True:
        buffer = u.read(block_sz)
        if not buffer:
            break
        file_size_dl += len(buffer)
        f.write(buffer)
        status = r"%10d  [%3.2f%%]" % (file_size_dl, file_size_dl * 100. / file_size)
        status = status + chr(8)*(len(status)+1)
        print status,

    f.close()



def update_github():
    try:
        os.system('git clone https://github.com/razyar/0x2')
        os.chdir('0x2')
        if os.path.exists("up0x2.py"):
            try:
                os.system('python up0x2.py')
                print 'Status: [Updated]'
            except Exception as UpError:
                print 'Error Func: [update_github: os.system("python up0x2.py")]'
        else:
            return 0

    except Exception as FunctionError:
        sys.exit(r"0")
