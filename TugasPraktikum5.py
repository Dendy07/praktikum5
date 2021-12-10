# -- encoding: utf-8 --
import os,sys
P = print
Oc = os,system
while True:
    P('')
    P('')
    C = input("(L)ihat, (T)ambah, (U)bah, (H)apus, (C)ari, (K)eluar: ")
    if c.lower() == 'k':
        break
    elif c.lower() == 'l':
        i = open('database.txt','r').read().splitlines()
        P("Daftar Nilai")
        P("==========================================================")
        P("| No |   NIM   |    NAMA     | TUGAS | UTS | UAS | AKHIR |")
        P("==========================================================")
        for l in i:
            if l == '':
                pass
            else:
                li = l.replace('No : ','').replace('NIM : ','').replace('Nama : ','').replace('Tugas : ','').replace('UTS : ','').replace('UAS : ','').replace('Akhir : ','')
                no,ni,na,tu,uts,uas,akhir = li.strip().split('|')
                P((' | ')+(no).ljust(17)+('| ')+(ni).ljust(17)+('| ')+(na[:15]).ljust(17,'.')+('| ')+(tu).ljust(6)+('| ')+(uts).ljust(6)+('| ')+(uas).ljust(6)+('| ')+(akhir).ljust(6)+('|'))
        P("==========================================================")