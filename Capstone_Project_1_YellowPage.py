#Selamat datang di Klinik Bina Sehat
#Klinik Bina Sehat merupakan Retail Klinik yang memiliki multiple branch di Indonesia
#Klinik Bina Sehat memiliki kerjasama dengan mitra Rumah Sakit yang tersebar diseluruh Indonesia
#Program ini merupakan Aplikasi Yellow Page yang dapat digunakan oleh Klinik Bina Sehat untuk membuat kontak, menampilkan semua kontak, mengedit kontak hingga menghapus kontak Rumah Sakit Mitra terdekat dengan lokasi klinik.

from colorama import Fore, Back, Style

# MAIN MENU
menu = [Fore.YELLOW + '1. Lihat Daftar Kontak Rumah Sakit Mitra',
        '2. Tambah Kontak RS Mitra Baru',
        '3. Edit Kontak',
        '4. Hapus Kontak',
        Fore.RED + '5. Keluar']

contacts = [{'Kode Area': 1, 'Kode Rumah Sakit': 'A', 'Nama Rumah Sakit': 'RS KSH', 'Lokasi': 'Semarang Barat',
             'Nomor Telp': '08123456789', 'Email': 'ksh@example.com'},
            {'Kode Area': 2, 'Kode Rumah Sakit': 'A', 'Nama Rumah Sakit': 'RS KSH', 'Lokasi': 'Pati',
             'Nomor Telp': '08123456789', 'Email': 'ksh@example.com'},
            {'Kode Area': 1, 'Kode Rumah Sakit': 'B', 'Nama Rumah Sakit': 'RS BSMC', 'Lokasi': 'Semarang Utara',
             'Nomor Telp': '08234567890', 'Email': 'bsmc@example.com'}]

# TAMPILAN UTAMA
def Lihat_Daftar_Kontak_Rumah_Sakit_Mitra():
    while True:
        print(Fore.GREEN + "\n+++++++ Daftar Kontak Rumah Sakit Mitra +++++++\n")
        print(Fore.MAGENTA + "Sub Menu:")
        print(Fore.CYAN + "1. Seluruh Rumah Sakit Mitra")
        print(Fore.CYAN + "2. Cari Rumah Sakit Mitra Tertentu")
        print(Fore.YELLOW + "3. Kembali ke Menu Utama")
        submenu_choice = input(Fore.WHITE +"Silakan pilih menu yang anda butuhkan [1-3]: ")
        if submenu_choice == '1':
            print(Fore.GREEN + "\n+++++++ Seluruh Rumah Sakit Mitra Klinik Bina Sehat +++++++\n")
            # Menampilkan Seluruh Rumah Sakit Mitra
            index = 1
            for kontak in contacts:
             print(f"{index}. Kode Area: {kontak['Kode Area']}, Kode Rumah Sakit: {kontak['Kode Rumah Sakit']}, Nama Rumah Sakit: {kontak['Nama Rumah Sakit']}, Lokasi: {kontak['Lokasi']}, Nomor Telp: {kontak['Nomor Telp']}, Email: {kontak['Email']}")
            index += 1
        elif submenu_choice == '2':
            Kode_Area = input("Silahkan masukkan kode Area anda: \n")
            Kode_Rumah_Sakit = input("Silahkan masukkan kode rumah sakit yang anda tuju: \n")
            found = False
            for kontak in contacts:
                if kontak['Kode Area'] == int(Kode_Area) and kontak['Kode Rumah Sakit'] == Kode_Rumah_Sakit:
                    print(Fore.CYAN + "\n+++++++ Data Kontak Rumah Sakit +++++++\n")
                    print(f"Kode Area: {kontak['Kode Area']}")
                    print(f"Kode Rumah Sakit: {kontak['Kode Rumah Sakit']}")
                    print(f"Nama Rumah Sakit: {kontak['Nama Rumah Sakit']}")
                    print(f"Lokasi: {kontak['Lokasi']}")
                    print(f"Nomor Telp: {kontak['Nomor Telp']}")
                    print(f"Email: {kontak['Email']}")
                    found = True
            if not found:
                print(Fore.RED + "Kode yang anda Input tidak Valid, Silahkan coba kembali atau kembali ke menu utama untuk menambahkan data yang anda inginkan\n")
        elif submenu_choice == '3':
            break
        else:
            print(Fore.RED + "Pilihan yang anda inginkan tidak valid. Silakan pilih kembali.\n")

# Create Data Function
def tambah_kontak_baru():
    while True:
        print(Fore.GREEN + "\n+++++++ Tambah Baru Kontak Rumah Sakit Mitra +++++++\n")
        print(Fore.MAGENTA + 'Sub Menu:')
        print(Fore.CYAN + "1. Input Manual")
        print(Fore.CYAN + "2. Kembali ke Menu Utama")
        submenu_choice = input(Fore.WHITE +"Silakan pilih menu yang anda butuhkan [1-2]: ")
        if submenu_choice == '1':
            # Input Manual Rumah Sakit Mitra
            print(Fore.GREEN + "\n+++++++ Silahkan Input Data Rumah Sakit Mitra yang Anda Inginkan +++++++\n")
            Kode_Area = int(input("Kode Area: "))
            Kode_Rumah_Sakit = input("Kode Rumah Sakit: ")
            Nama_Rumah_Sakit = input("Nama Rumah Sakit: ")
            Lokasi = input('Lokasi: ')

            # Nomor telepon harus 8-12 digit
            while True:
                Nomor_Telp = input("Nomor Telp: ")
                if 8 <= len(Nomor_Telp) <= 12 and Nomor_Telp.isdigit():
                    break
                else:
                    print(Fore.RED + "Nomor Telp harus terdiri dari 8-12 digit.\n")

            # Email harus mengandung '@' dan '.com'
            while True:
                Email = input("Email: ")
                if '@' in Email and '.com' in Email:
                    break
                else:
                    print(Fore.RED + "Email harus mengandung '@' dan '.com'.\n")


            # Cek apakah Kontak Rumah Sakit Mitra sudah ada sebelumnya
            data_exist = False
            for kontak in contacts:
                if kontak['Kode Area'] == Kode_Area and kontak['Kode Rumah Sakit'] == Kode_Rumah_Sakit:
                    data_exist = True
                    break

            if data_exist:
                # Duplikasi Kontak
                duplicate_choice = input(
                    "Kontak Rumah Sakit Mitra yang anda input sudah ada sebelumnya, apakah ingin menduplikasi kontak? [iya/tidak]: ")
                if duplicate_choice.lower() == 'iya':
                    # Jika 'iya', kembali ke submenu_choice
                    continue
                else:
                    # Jika 'tidak', kembali ke Input Manual
                    continue
            else:
                # Konfirmasi Data yang diinput sudah benar
                print("Apakah Kontak Rumah Sakit Mitra yang Anda akan simpan sudah Benar?")
                confirmation = input("Silahkan konfirmasi [Iya/Tidak]: ")
                if confirmation.lower() == 'iya':
                    # Selamat! Kontak Rumah Sakit Mitra yang baru telah berhasil ditambahkan!
                    contacts.append(
                        {'Kode Area': Kode_Area, 'Kode Rumah Sakit': Kode_Rumah_Sakit, 'Nama Rumah Sakit': Nama_Rumah_Sakit,
                         'Lokasi': Lokasi, 'Nomor Telp': Nomor_Telp, 'Email': Email})
                    print(Fore.GREEN + "Selamat! Kontak Rumah Sakit Mitra yang baru telah berhasil ditambahkan!\n")
                else:
                    # Jika 'Tidak', kembali ke submenu_choice
                    continue

        elif submenu_choice == '2':
            break
        else:
            print(Fore.RED + "Mohon maaf, permintaan yang anda inginkan tidak valid, silahkan kembali ke menu utama.\n")


# Edit Kontak
def edit_kontak():
    while True:
        print(Fore.MAGENTA + "\n+++++++ Edit Kontak Rumah Sakit Mitra +++++++\n")
        print(Fore.CYAN + "Submenu:")
        print(Fore.CYAN + "1. Edit kontak yang sudah terdaftar")
        print(Fore.YELLOW + "2. Kembali ke menu utama")
        submenu_choice = input(Fore.WHITE +"Silakan pilih submenu yang anda butuhkan [1-2]: ")
        if submenu_choice == '1':
            print(Fore.MAGENTA + "\n+++++++ Edit Kontak yang Sudah Terdaftar +++++++\n")
            kode_area = input("Masukkan Kode Area: ")
            kode_rumah_sakit = input("Masukkan Kode Rumah Sakit: ")
            found = False
            for kontak in contacts:
                if kontak['Kode Area'] == int(kode_area) and kontak['Kode Rumah Sakit'] == kode_rumah_sakit:
                    print("\nData Kontak Rumah Sakit yang ditemukan:")
                    print(f"Kode Area: {kontak['Kode Area']}")
                    print(f"Kode Rumah Sakit: {kontak['Kode Rumah Sakit']}")
                    print(f"Nama Rumah Sakit: {kontak['Nama Rumah Sakit']}")
                    print(f"Lokasi: {kontak['Lokasi']}")
                    print(f"Nomor Telp: {kontak['Nomor Telp']}")
                    print(f"Email: {kontak['Email']}")
                    found = True
                    update_choice = input("\nApakah anda benar ingin mengupdate Kontak ini? [iya/tidak]: ")
                    if update_choice.lower() == 'iya':
                        # Input data baru
                        Nama_Rumah_Sakit = input("Nama Rumah Sakit baru: ")
                        Lokasi = input('Lokasi baru: ')

                        # Nomor telepon harus 8-12 digit
                        while True:
                            Nomor_Telp = input("Nomor Telp baru: ")
                            if Nomor_Telp.isdigit() and 8 <= len(Nomor_Telp) <= 12:
                                break
                            else:
                                print(Fore.RED + "Nomor Telp harus terdiri dari 8-12 digit.\n")

                        # Email harus mengandung '@' dan '.com'
                        while True:
                            Email = input("Email baru: ")
                            if '@' in Email and '.com' in Email:
                                break
                            else:
                                print(Fore.RED + "Email harus mengandung '@' dan '.com'.\n")

                        # Konfirmasi Kesesuaian Data yang ingin di update
                        confirmation = input("Apakah data yang diupdate sudah sesuai? [iya/tidak]: ")
                        if confirmation.lower() == 'iya':
                            # Selamat! Kontak Berhasil di Update!
                            kontak.update(
                                {'Nama Rumah Sakit': Nama_Rumah_Sakit, 'Lokasi': Lokasi, 'Nomor Telp': Nomor_Telp,
                                 'Email': Email})
                            print(Fore.GREEN + "Selamat! Kontak Berhasil di Update!\n")
                            break
                        else:
                            print(Fore.RED + "Data tidak berhasil diupdate.\n")
                            break
                    else:
                        print(Fore.RED + "Data tidak berhasil diupdate.\n")
                        break
            if not found:
                print(Fore.RED + "Mohon maaf, Kontak tidak ditemukan.\n")
                continue
        elif submenu_choice == '2':
            break
        else:
            print(Fore.RED + "Mohon maaf, Pilihan yang anda inginkan tidak valid. Silakan pilih kembali ke menu utama.\n")

# Delete Kontak
def hapus_kontak():
    while True:
        print(Fore.MAGENTA + "\n+++++++ Hapus Kontak +++++++\n")
        print(Fore.MAGENTA + "Sub Menu:")
        print(Fore.CYAN + "1. Daftar Kontak Mitra RS yang terdaftar")
        print(Fore.YELLOW + "2. Kembali ke Menu Utama")
        submenu_choice = input(Fore.WHITE +"Silakan pilih submenu yang anda butuhkan [1-2]: ")
        if submenu_choice == '1':
            print(Fore.MAGENTA + "\n+++++++ Pilih Kontak yang Ingin Dihapus +++++++\n")
            if len(contacts) != 0:
                for index in range(len(contacts)):
                    print(f"{index + 1}. Nama Rumah Sakit: {contacts[index]['Nama Rumah Sakit']}")
                index = int(input("Pilih nomor kontak yang ingin dihapus: ")) - 1
                if 0 <= index < len(contacts):
                    # Tampilkan kontak yang dapat dihapus
                    selected_contact = contacts[index]
                    print("\nKontak yang akan dihapus:")
                    print(f"Nama Rumah Sakit: {selected_contact['Nama Rumah Sakit']}")
                    confirmation = input("\nApakah anda yakin akan menghapus kontak yang dipilih? [iya/tidak]: ")
                    if confirmation.lower() == 'iya':
                        # Menghapus kontak
                        del contacts[index]
                        print(Fore.GREEN + "Selamat! Kontak yang anda pilih berhasil dihapus!\n")
                    else:
                        print(Fore.RED + "Penghapusan kontak dibatalkan.\n")
                else:
                    print(Fore.RED + "Kontak yang anda pilih tidak valid.\n")
            else:
                print(Fore.RED + "Tidak ada kontak tersimpan.\n")
        elif submenu_choice == '2':
            break
        else:
            print(Fore.RED + "Mohon maaf, Pilihan yang anda inginkan tidak valid. Silakan pilih kembali ke menu utama.\n")



# Main Menu Function
def main_menu():
    while True:
        print(Fore.YELLOW + "\n+++++++ KLINIK BINA SEHAT +++++++\n")
        for item in menu:
            print(item)
        pilihan = input(Fore.WHITE + "Silakan pilih menu yang anda inginkan [1-5]: ")
        try:
            pilihan = int(pilihan)
            if pilihan == 1:
                Lihat_Daftar_Kontak_Rumah_Sakit_Mitra()
            elif pilihan == 2:
                tambah_kontak_baru()
            elif pilihan == 3:
                edit_kontak()
            elif pilihan == 4:
                hapus_kontak()
            elif pilihan == 5:
                print(Fore.GREEN + "\nTerima kasih! Sehat Selalu & Sampai jumpa.\n")
                break
            else:
                print(Fore.RED + "Pilihan tidak valid. Silakan pilih kembali ke menu utama.")
        except ValueError:
            print(Fore.RED + "Mohon maaf, kami belum dapat mengenali jawaban anda, silahkan kembali ke menu utama.")

# Start Program
if __name__ == "__main__":
    main_menu()

