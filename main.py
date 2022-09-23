print("="*40)

def menu():
  print("""
  1. Makanan
  2. Minuman""")
  nomor = int(input("Pilih menu :"))
  if nomor == 1:
    global totalmakan
    global porsi
    global makan
    print("""
    1. Ayam Geprek - 15000
    2. Ayam Goreng - 15000
    3. Mie Ayam - 15000
    4. Nasi Goreng 15000
    5. Ayam Bakar - 19000
    """)
    pilih = int(input("Pilih makanan :"))
    porsi = int(int(input("Pilih porsi :")))
    if pilih == 1:
      totalmakan = porsi*15000
      print(porsi, "Ayam Geprek = Rp.", totalmakan)
      makan = ("Ayam Geprek")
    elif pilih == 2:
      totalmakan = porsi*15000
      print(porsi, "Ayam Goreng Rp.", totalmakan)
      makan = ("Ayam Goreng")
    elif pilih == 3:
      totalmakan = porsi*15000
      print(porsi, "Mie Ayam Rp.", totalmakan)
      makan = ("Mie Ayam")
    elif pilih == 4:
      totalmakan = porsi*15000
      print(porsi, "Nasi Goreng Rp.", totalmakan)
      makan = ("Nasi Goreng")
    elif pilih == 5:
      totalmakan = porsi*19000
      print(porsi, "Ayam Bakar Rp.", totalmakan)
      makan = ("Ayam Bakar")
    else:
      makanan()
    lanjutBeli = input("lanjut beli minuman?(y/n)")
    if lanjutBeli == 'y':
      menu()
  def minuman():
      if nomor == 2:
        global totalminum
        global gelas
        global minum
        print("""
        1. Es Teh - 4000
        2. Es Serut - 8000
        3. Es Jeruk - 7000
        4. Es Dawet - 7000
        5. Es Cincau 8000
        """)
        tunjuk = int(input("Pilih minuman :"))
        gelas = int(input("Berapa gelas? :"))
        if tunjuk == 1:
          totalminum = gelas*4000
          print(gelas, "Es Teh = Rp.", totalminum)
          makan = ("Es Teh")
        elif tunjuk == 2:
          totalminum = gelas*8000
          print(gelas, "Es Serut = Rp.", totalminum)
          makan = ("Es Serut")
        elif tunjuk == 3:
          totalminum = gelas*7000
          print(gelas, "Es Jeruk = Rp.", totalminum)
          makan = ("Es Jeruk")
        elif tunjuk == 4:
          totalminum = gelas*7000
          print(gelas, "Es Dawet = Rp.", totalminum)
          makan = ("Es Dawet")
        elif tunjuk == 5:
          totalminum = gelas*8000
          print(gelas, "Es Cincau = Rp.", totalminum)
          makan = ("Es Cincau")
        else:
          minuman()

      elif lanjutBeli == 'y':
        totalsemua = totalmakan+totalminum
        print("Subtotal :", totalsemua)
  minuman()
menu()
