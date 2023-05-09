import smbus

# Define the I2C bus number to use (for Raspberry Pi 3B+ use 1, for older versions use 0)
bus_num = 1

# Create a new smbus object
bus = smbus.SMBus(bus_num)

# Define the range of I2C addresses to scan (0x03 to 0x77 are valid addresses for I2C devices)
min_addr = 0x03
max_addr = 0x77

# Scan for I2C devices
for addr in range(min_addr, max_addr+1):
    try:
        bus.read_byte(addr)
        print("Device found at address: 0x{:02x}".format(addr))
    except:
        pass
