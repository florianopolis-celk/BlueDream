from wifi import Cell

# Obter todas as células (redes Wi-Fi) disponíveis
cells = Cell.all('wlan0')

# Exibir informações sobre cada célula
for cell in cells:
    print(f"SSID: {cell.ssid}")
    print(f"Signal: {cell.signal}")
    print(f"Quality: {cell.quality}")
    print(f"Frequency: {cell.frequency}")
    print(f"Bit Rates: {cell.bitrates}")
    print(f"Encryption Type: {cell.encryption_type}")
    print("----------------------")
