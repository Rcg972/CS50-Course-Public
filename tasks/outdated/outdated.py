def main():
    tahun, bulan, hari = ubah_bentuk_tanggal()
    print(f"{int(tahun):04}-{int(bulan):02}-{int(hari):02}")

def ubah_bentuk_tanggal():
    nama_bulan = [
        "January", "February", "March", "April", "May", "June",
        "July", "August", "September", "October", "November", "December"
    ]

    while True:
        date = input("Date: ").strip()
        try:
            if "," in date:
                date = date.replace(",", "")
                bulan, tanggal, tahun = date.split()
                if bulan in nama_bulan:
                    if int(tanggal) > 31:
                        continue
                    bulan_index = nama_bulan.index(bulan) + 1
                    return tahun, bulan_index, tanggal
                else:
                    continue
            elif "/" in date:
                bulan, tanggal, tahun = date.split("/")
                if not bulan.isdigit() or not tanggal.isdigit():
                    continue
                if int(bulan) > 12 or int(tanggal) > 31:
                    continue
                return tahun, bulan, tanggal
        except:
            continue


main()
