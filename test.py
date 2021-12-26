userAdmin = "admin"
passAdmin = "admin"

users = {
    1: {"Nama User": "user1", "Password": "user1", "Status": "Penyewa"},
    2: {"Nama User": "user2", "Password": "user2", "Status": "Penyewa"},
    3: {"Nama User": "user3", "Password": "user3", "Status": "Penyewa"},
    4: {"Nama User": "ajeng", "Password": "test", "Status": "Penyewa"},
    5: {"Nama User": "pembeli1", "Password": "pembeli1", "Status": "Pembeli"},
    6: {"Nama User": "pembeli2", "Password": "pembeli2", "Status": "Pembeli"},
}

kendaraan = {
    1: {"Nama Kendaraan": "mobil1", "Status": "Pernah disewa", "Penyewa": "-", "Kondisi": "Bekas"},
    2: {"Nama Kendaraan": "mobil2", "Status": "Tidak pernah disewa", "Penyewa": "-", "Kondisi": "Baru"},
    3: {"Nama Kendaraan": "mobil3", "Status": "Pernah disewa", "Penyewa": "-", "Kondisi": "Bekas"},
    4: {"Nama Kendaraan": "mobil4", "Status": "Tidak pernah disewa", "Penyewa": "-", "Kondisi": "Baru"},
    5: {"Nama Kendaraan": "mobil5", "Status": "Pernah disewa", "Penyewa": "-", "Kondisi": "Bekas"},
}

riwayatbeli = {
    "pembeli2": [
        ["mobil6", "Bekas"], ["mobil7", "Baru"]
    ]
}


def masukadmin():
    print("\nHello, Admin!! \n")
    counts = 0
    while counts == 0:
        print("\n====MENU====")
        pilih = input("1. Input Kendaraan \n 2. Hapus Kendaraan \n 3. List Kendaraan  \n 4. Logout \n Input : ")
        pilih = int(pilih)
        if pilih == 1:
            inputkendaraan()
        elif pilih == 2:
            deletekendaraan()
        elif pilih == 3:
            showkendaraan()
        elif pilih == 4:
            counts += 1
            login()
        else:
            print("Input salah.")
            print(type(pilih))
    return


def masukuser(user):
    print("\nHello, " + user + " !!")
    print("---Penyewa---")
    counts = 0
    while counts == 0:
        print("\n====MENU====")
        pilih = input("1. Sewa Kendaraan \n 2. Kembalikan Kendaraan \n 3. List Kendaraan  \n 4. Logout \n Input : ")
        pilih = int(pilih)
        if pilih == 1:
            sewakendaraan(user)
        elif pilih == 2:
            kembalikendaraan(user)
        elif pilih == 3:
            showkendaraan()
        elif pilih == 4:
            counts += 1
            login()
        else:
            print("Input salah.")
            print(type(pilih))
    return


def masukpembeli(user):
    print("\nHello, " + user + " !!\n")
    print("---Pembeli---")
    counts = 0
    while counts == 0:
        print("\n====MENU====")
        pilih = input("1. Sewa Kendaraan \n 2. Beli Kendaraan \n 3. Kembalikan Kendaraan "
                      "\n 4. List Kendaraan \n 5. Riwayat Pembelian \n 6. Logout \n Input : ")
        pilih = int(pilih)
        if pilih == 1:
            sewakendaraan(user)
        elif pilih == 2:
            belikendaraan(user)
        elif pilih == 3:
            kembalikendaraan(user)
        elif pilih == 4:
            showkendaraan()
        elif pilih == 5:
            riwayat(user)
        elif pilih == 6:
            counts += 1
            login()
        else:
            print("Input salah.")
            print(type(pilih))
    return


def belikendaraan(user):
    showkendaraan()
    beli = input("Masukkan no kendaraan yang ingin dibeli : ")
    beli = int(beli)

    if kendaraan[beli]["Penyewa"] == "-":
        kendaraanbeli = [kendaraan[beli]["Nama Kendaraan"], kendaraan[beli]["Kondisi"]]
        del kendaraan[beli]
        riwayatbeli[user].append(kendaraanbeli)
        print("Kendaraan telah berhasil anda beli.")
        riwayat(user)
    elif kendaraan[beli]["Status"] == "Sedang disewa":
        print("Kendaraan sedang disewa oleh", kendaraan[beli]["Penyewa"], ". Belum dapat dibeli")


def riwayat(user):
    if user in riwayatbeli:
        print("\n===RIWAYAT PEMBELIAN===")
        print(riwayatbeli[user])
        print("=======================")
    else:
        print("Anda belum membeli kendaraan.")


def showkendaraan():
    print("\n ===== LIST KENDARAAN ===== ")
    for no, nama in kendaraan.items():
        print("No : ", no)
        for key in nama:
            print(key + " : ", nama[key])
        print(" ---------- ")
    print("===============================\n")


def sewakendaraan(user):
    showkendaraan()
    sewa = input("Masukkan no kendaraan yang ingin disewa : ")
    sewa = int(sewa)

    if kendaraan[sewa]["Penyewa"] == user:
        print("Kendaraan telah anda sewa.")
    elif kendaraan[sewa]["Status"] == "Sedang disewa":
        print("Kendaraan sedang disewa oleh", kendaraan[sewa]["Penyewa"])
    else:
        kendaraan[sewa]["Status"] = "Sedang disewa"
        kendaraan[sewa]["Penyewa"] = user
        print("Kendaraan berhasil disewa.")


def kembalikendaraan(user):
    showkendaraan()
    kembali = input("Masukkan no kendaraan yang ingin dikembalikan : ")
    kembali = int(kembali)
    if kendaraan[kembali]["Penyewa"] == user:
        kembali = int(kembali)
        kendaraan[kembali]["Status"] = "Pernah disewa"
        kendaraan[kembali]["Penyewa"] = "-"
        kendaraan[kembali]["Kondisi"] = "Bekas"
        print("Kendaraan telah dikembalikan")
    else:
        print("Hanya '" + kendaraan[kembali]["Penyewa"] + "' yang dapat mengembalikan kendaraan ini.")


def inputkendaraan():
    i = len(kendaraan)

    while True:
        i += 1
        masukandata = input("Memasukkan data baru? [Y/N]")
        if masukandata == "Y" or masukandata == "y":
            kendaraanbaru = input(str("Masukkan Data Kendaraan: "))
            # kondisikendaraan = input(str("Masukkan Kondisi Kendaraan (Baru/Bekas) : "))
            kondisikendaraan = "Baru"

            # jika fitur tidak mengizinkan data yang sama
            # for cekkendaraan in kendaraan:
            #     if kendaraanbaru in kendaraan[cekkendaraan]["Nama Kendaraan"]:
            #         print("Kendaraan sudah ada di daftar\n")
            #         break
            # else:
            new_kendaraan = {i: {"Nama Kendaraan": kendaraanbaru, "Status": "Tidak pernah disewa",
                                 "Penyewa": "-", "Kondisi": kondisikendaraan}}
            kendaraan.update(new_kendaraan)
        else:
            break
    print(kendaraan)

    showkendaraan()


def deletekendaraan():
    showkendaraan()

    hapus = input("Masukkan no kendaraan yang ingin dihapus : ")
    hapus = int(hapus)
    del kendaraan[hapus]

    print("Data telah dihapus")
    showkendaraan()


def login():
    print("\n======PEMINJAMAN dan PEMBELIAN KENDARAAN=======")
    count = 0
    while count == 0:
        akun = input("Masukkan username : ")
        password = input("Masukkan password : ")

        if akun != "" and password != "":
            password = str(password)
            akun = str(akun)
            penyewa = "Penyewa"
            pembeli = "Pembeli"

            if akun == userAdmin and password == passAdmin:
                masukadmin()
                break
            #
            # for sortir in users:
            #     if akun in users[sortir]["Nama User"] and password in users[sortir]["Password"] \
            #             and users[sortir]["Status"] == "Penyewa":
            #         masukuser(akun)
            #         break
            #     elif akun in users[sortir]["Nama User"] and password in users[sortir]["Password"] \
            #             and users[sortir]["Status"] == "Pembeli":
            #         masukpembeli(akun)
            #         break
            #     elif akun in users[sortir]["Nama User"] or password in users[sortir]["Password"]:
            #         print("Username/Password salah!\n")
            #         login()
            #

            for sortir in users:
                if akun in users[sortir]["Nama User"] and password == users[sortir]["Password"]:
                    if penyewa in users[sortir]["Status"]:
                        masukuser(akun)
                    elif pembeli in users[sortir]["Status"]:
                        masukpembeli(akun)
                    break
                elif akun in users[sortir]["Nama User"] or password == users[sortir]["Password"]:
                    print("Username/Password salah!\n")
                    login()

        else:
            print("____Data tidak boleh kosong!\n")


login()