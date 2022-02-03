
def bilgi (isim, saglik, ac):
    birinci_saglik = ""
    for i in range(int(saglik[0]/2)):
        birinci_saglik = birinci_saglik +"|"
    ikinci_saglik = ""
    for i in range(int(saglik[0]/2)):
        ikinci_saglık = ikinci_saglik + "|"
    first = "HP[{}]:{}".format(saglik[0], birinci_saglik)
    second = "HP[{}]:{}".format(saglik[1], ikinci_saglik)
    if ac == 0:
        print('\n{:60s} {:60s}'.format(isim[0], isim[1]))
        print('{:60s} {:60s}'.format(birinci, ikinci))
    else:
        print('\n{:60s} {:60s}'.format(isim[1], isim[0]))
        print('{:60s} {:60s}'.format(ikinci, birinci))