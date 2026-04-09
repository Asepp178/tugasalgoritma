mahasiswa = {
    "10121001": "Asep",
    "10121002": "Budi",
    "10121003": "Cecep"
}

data_nilai = [
    {"NIM": "10121001", "MK1": 95, "MK2": 75, "MK3": 90, "MK4": 80},
    {"NIM": "10121002", "MK1": 85, "MK2": 78, "MK3": 80, "MK4": 65},
    {"NIM": "10121003", "MK1": 57, "MK2": 88, "MK3": 67, "MK4": 69}
]

nilai_rata = {}
for data in data_nilai:
    nim = data["NIM"]
    total_nilai = data["MK1"] + data["MK2"] + data["MK3"] + data["MK4"]
    nilai_rata[nim] = total_nilai / 4

nim_terpintar = max(nilai_rata, key=nilai_rata.get)
nama_terpintar = mahasiswa[nim_terpintar]
nilai_tertinggi = nilai_rata[nim_terpintar]


mata_kuliah = ["MK1", "MK2", "MK3", "MK4"]
nilai_rata = {}
jumlah_mhs = len(data_nilai)

for mk in mata_kuliah:
    total_nilai_mk = sum(data[mk] for data in data_nilai)
    nilai_rata[mk] = total_nilai_mk / jumlah_mhs

mk_terkecil = min(nilai_rata, key=nilai_rata.get)
nilai_mk_terkecil = nilai_rata[mk_terkecil]

print(f"Mahasiswa Terpintar : {nama_terpintar} (Nilai :{nilai_tertinggi:.2f})")
print(f"Mata Kuliah Nilai Terkecil : {mk_terkecil} (Nilai : {nilai_mk_terkecil:.2f})")