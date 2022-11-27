import CFGclass
machine=CFGclass.CFGmsk("save.txt")
while True:
    print("Menu Program:\n1.Cek kebenaran string\n2.keluar")
    pilihan=input()
    if pilihan=="1":
        print("masukan string yang ingin di cek")
        try:
            machine.checkstring(input())
        except:
            print("terjadi suatu kesalahan")
    else:
        exit()

