while True:
    print("\n--- MENU MATRIKS ---")
    print("1. Penjumlahan")
    print("2. Pengurangan")
    print("3. Perkalian")
    print("0. Exit")

    pilihan = int(input("Pilih menu: "))

    if pilihan == 0:
        print("Program selesai.")
        break

    baris = int(input("Input jumlah baris: "))
    kolom = int(input("Input jumlah kolom: "))

    print("\nInput Matriks A:")
    A = []
    for i in range(baris):
        row = []
        for j in range(kolom):
            nilai = int(input(f"A[{i}][{j}] = "))
            row.append(nilai)
        A.append(row)

    print("\nInput Matriks B:")
    B = []
    for i in range(baris):
        row = []
        for j in range(kolom):
            nilai = int(input(f"B[{i}][{j}] = "))
            row.append(nilai)
        B.append(row)

    hasil = []
    for i in range(baris):
        row = []
        for j in range(kolom):
            if pilihan == 1:
                row.append(A[i][j] + B[i][j])
            elif pilihan == 2:
                row.append(A[i][j] - B[i][j])
            elif pilihan == 3:
                row.append(A[i][j] * B[i][j])
        hasil.append(row)

    print("\nHasil:")
    for row in hasil:
        for angka in row:
            print(angka, end="  ") # Biar angka ke samping
        print() 