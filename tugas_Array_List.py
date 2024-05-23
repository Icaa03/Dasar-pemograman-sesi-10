import array as arr
print("NO 1")

# 1. Ilham memiliki sebuah list yang berisi angka-angka acak. Anda ingin menghapus semua angka yang memiliki nilai kurang dari 5 dan menggantinya dengan nilai 0, dan akan mengurutkan dari nilai yang terbesar ke yang terkecil. Bantu Ilham untuk menyelesaikan persoalan tersebut menggunakan array method.
# Input: [8, 3, 12, 4, 7, 2]
# Output: [12, 8, 7, 4, 0, 0]
arr = [8, 3, 12, 4, 7, 2]
output_arr = []
# menghapus semua angka yang memiliki nilai kurang dari 5 dan menggantinya dengan nilai 0
for i in arr:
    if i <= 5:
        output_arr.append(0)
    else:
        output_arr.append(i)
# mengurutkan dari nilai yang terbesar ke yang terkecil
output_arr.sort(reverse=True)
print(output_arr)  

print("NO 2")

# 2.Budi memiliki sebuah list yang berisi nilai-nilai angka. Dia ingin menghapus semua nilai yang merupakan bilangan ganjil dan mengurutkan sisa nilai tersebut dari terkecil ke terbesar. Bantu budi untuk menyelesaikan persoalan tersebut menggunakan array method.
# Input: [7, 4, 9, 2, 5, 1]
# Output: [2, 4]

arr = [7, 4, 9, 2, 5, 1]
output_arr = []
# menghapus semua nilai yang merupakan bilangan ganjil dan mengurutkan sisa nilai tersebut dari terkecil ke terbesar
for i in arr:
    if i % 2 == 0:
        output_arr.append(i)

output_arr.sort()
print(output_arr)

print("NO 3")

# 3.Rani memiliki sebuah list yang berisi buah-buahan. Dia ingin menghapus semua kata yang memiliki panjang kurang dari lima karakter dan mengurutkan sisa kata-kata tersebut secara alfabetis. Bantulah Rani untuk mencapai ini.
# Input: kata = ["apel", "jeruk", "mangga", "pisang", "anggur", "durian"]
# Output: ['anggur', 'durian', 'jeruk', 'mangga', 'pisang']

kata = ["apel", "jeruk", "mangga", "pisang", "anggur", "durian"]
output = []
# menghapus semua kata yang memiliki panjang kurang dari lima karakter dan mengurutkan sisa kata-kata tersebut secara alfabetis
for i in kata:
    if len(i) >= 5:
        output.append(i)

output.sort()
print(output)

print("NO 4")

# 4.Dewi memiliki dua list yang berisi nama-nama buah-buahan. Dia ingin menggabungkan kedua list tersebut dan menghapus semua buah yang memiliki nama yang sama. Setelah itu, dia ingin mengurutkan sisa buah-buahan secara alfabetis. Bantu Dewi
# Input: ["apel", "jeruk", "mangga"], ["apel", "anggur", "nanas"]
# Output: ['anggur', 'apel', 'jeruk', 'mangga', 'nanas']

list1 = ["apel", "jeruk", "mangga"]
list2 = ["apel", "anggur", "nanas"]
# menggabungkan kedua list tersebut dan menghapus semua buah yang memiliki nama yang sama, mengurutkan sisa buah-buahan secara alfabetis.
hasil = sorted(set(list1 + list2))
print(hasil)

print("NO 5")

# 5.Dina memiliki sebuah list yang berisi nilai-nilai angka. Dia ingin menghapus semua nilai yang kurang dari 10 dan lebih dari 100, dan mengurutkan sisa nilai tersebut dari terkecil ke terbesar. Implementasikan ini dengan menggunakan metode-metode yang tepat dari list.
# Input: [105, 20, 8, 150, 30, 5, 200]
# Output: [20, 30]
input_arr = [105, 20, 8, 150, 30, 5, 200]
output_arr = []
# menghapus semua nilai yang kurang dari 10 dan lebih dari 100
for i in input_arr:
    if 10 <= i <= 100:
        output_arr.append(i)

# mengurutkan sisa nilai tersebut dari terkecil ke terbesar
output_arr.sort()
print(output_arr)

print("NO 6")

# Buatlah aplikasi manajemen buku dengan menggunakan list dan dictionary, setiap buku terdiri dari (no_isbn, judul, pengarang, isihalaman, deskripsi, stok, booked). Lalu ada list mahasiswa (nama, nim, kontak, alamat) Lalu ada list peminjam (nim, no_isbn, tanggalpinjam, tanggal_kembali, status)

list_daftar_buku = []
list_daftar_mahasiswa = []
list_daftar_peminjaman = []

def addBuku (no_isbn, judul, pengarang, isiHalaman, deskripsi, stok, booked):
    buku = {
        "no_isbn": no_isbn,
        "judul": judul,
        "pengarang": pengarang,
        "isiHalaman": isiHalaman,
        "deskripsi": deskripsi,
        "stok": stok,
        "booked": booked
    }
    list_daftar_buku.append(buku)
    print("Buku telah ditambahkan ke dalam daftar")

# Daftar Buku yang Tersedia
def info_buku():
    if not list_daftar_buku:
        print("Tidak ada buku yang tersedia")
    else:
        for buku in list_daftar_buku:
            print(f"Judul: {buku['judul']}, No ISBN: {buku['no_isbn']}, Pengarang: {buku['pengarang']}, Isi Halaman: {buku['isiHalaman']}, Deskripsi: {buku['deskripsi']}, Stok: {buku['stok']}, Booked: {buku['booked']}")
 
def addMahasiswa(nama, nim, kontak, alamat):
    mahasiswa = {
        "nama": nama,
        "nim": nim,
        "kontak": kontak,
        "alamat": alamat
    }
    list_daftar_mahasiswa.append(mahasiswa)
    print("Mahasiswa telah ditambahkan ke dalam daftar")

def info_Mahasiswa():
    if not list_daftar_mahasiswa:
        print("Tidak ada mahasiswa yang terdaftar")
    else:
        for mahasiswa in list_daftar_mahasiswa:
            print(f"Nama: {mahasiswa['nama']}, NIM: {mahasiswa['nim']}, No HP: {mahasiswa['kontak']}, Alamat: {mahasiswa['alamat']}")

def addPeminjaman(nim, no_isbn, tanggal_pinjam, tanggal_kembali, status):
    peminjam = {
        "nim": nim,
        "no_isbn": no_isbn,
        "tanggal_pinjam": tanggal_pinjam,
        "tanggal_kembali": tanggal_kembali,
        "status": status
    }
    list_daftar_peminjaman.append(peminjam)
    print("Peminjaman telah ditambahkan ke dalam daftar")

def meminjamBuku(nim, no_isbn):
    mahasiswa = next((m for m in list_daftar_mahasiswa if m['nim'] == nim), None)
    buku = next((b for b in list_daftar_buku if b['no_isbn'] == no_isbn), None)
    
    if mahasiswa and buku:
        if buku['stok'] - buku['booked'] > 0:
            buku['booked'] += 1
            tanggalpinjam = datetime.now().strftime('%Y-%m-%d')
            tanggal_kembali = (datetime.now() + timedelta(days=14)).strftime('%Y-%m-%d')
            tambahPeminjam(nim, no_isbn, tanggalpinjam, tanggal_kembali, 'Dipinjam')
            print(f"Buku '{buku['judul']}' berhasil dipinjam oleh {mahasiswa['nama']}")
        else:
            print('mohon maaf stok buku sudah tidak mencukupi')
    else:
        print('mohon maaf mahasiswa atau buku tidak ditemukan')

def pengembalianBuku(nim, no_isbn):
    peminjaman = next((p for p in list_daftar_peminjaman if p['nim'] == nim and p['no_isbn'] == no_isbn and p['status'] == 'Dipinjam'), None)
    buku = next((b for b in list_daftar_buku if b['no_isbn'] == no_isbn), None)
    
    if peminjaman and buku:
        buku['booked'] -= 1
        peminjaman['status'] = 'Dikembalikan'
        peminjaman['tanggalkembali'] = datetime.now().strftime('%Y-%m-%d')
        print(f"Buku '{buku['judul']}' berhasil dikembalikan")
    else:
        print('mohon maaf untuk peminjaman buku tidak ditemukan')

def menu():
    while True:
        print("\n========== Manajemen Perpustakaan ==========")
        print("1. Add Buku")
        print("2. Info Buku")
        print("3. Add Mahasiswa")
        print("4. Info Mahasiswa")
        print("5. Peminjaman Buku")
        print("6. Pengembalian Buku")
        print("7. Keluar")
        
        pilihan = input("Pilih menu: ")
        if pilihan == '1':
            no_isbn = input("Masukkan ISBN buku: ")
            judul = input("Masukkan judul buku: ")
            pengarang = input("Masukkan pengarang buku: ")
            isiHalaman = int(input("Masukkan jumlah halaman buku: "))
            deskripsi = input("Masukkan deskripsi buku: ")
            stok = int(input("Masukkan stok buku: "))
            booked = 0  
            addBuku (no_isbn, judul, pengarang, isiHalaman, deskripsi, stok, booked)
        elif pilihan == '2':
            info_buku()
        elif pilihan == '3':
            nama = input("Masukkan nama mahasiswa: ")
            nim = input("Masukkan NIM mahasiswa: ")
            kontak = input("Masukkan kontak mahasiswa: ")
            alamat = input("Masukkan alamat mahasiswa: ")
            addMahasiswa(nama, nim, kontak, alamat)
        elif pilihan == '4':
            addMahasiswa()
        elif pilihan == '5':
            nim = input("Masukkan NIM mahasiswa: ")
            no_isbn = input("Masukkan ISBN buku: ")
            meminjamBuku(nim, no_isbn)
        elif pilihan == '6':
            nim = input("Masukkan NIM mahasiswa: ")
            no_isbn = input("Masukkan ISBN buku: ")
            pe(nim, no_isbn)
        elif pilihan == '7':
            print("Keluar dari program")
            break
        else:
            print("Pilihan tidak valid. Silakan coba lagi.") 
menu()
