#coding=utf-8
import sqlite3
import os

homedir = os.path.dirname(os.path.realpath(__file__))
# cx = sqlite3.connect(homedir+"/GeoDic.db", check_same_thread=False)
# cu = cx.cursor()

def create_table():
    cu.execute("create table catalog(word, Upper, Lower, rate)")

def insert_txt(url):
    fp = open(url)
    for lines in fp.readlines():
        lines = lines.strip().split('\t')
        cx.execute("insert into catalog values(?,?,?,?)", (lines[0].decode('utf-8'), lines[1].decode('utf-8'),
                                                           lines[2].decode('utf-8'), lines[3].decode('utf-8')))
    cx.commit()

def search(w):
    # try:
    #     w = w.decode('utf-8')
    # except:
    #     w = w.decode('gbk')
    # a = """select sent from catalog where word = '%s'"""%w
    # cu.execute(a)
    cx = sqlite3.connect(homedir+"/GeoDic.db", check_same_thread=False)
    cu = cx.cursor()

    cu.execute('select rate from catalog where word = ?',(w,))
    res = cu.fetchall()

    cx.close()
    if res:
        return res[0][0]
    else:
        return 0

if __name__ == '__main__':
    url = "./data/d-cap-pro.txt"
    create_table()
    insert_txt(url)
    print search('easter')
    cu.execute("create index word_index on catalog(word)")
