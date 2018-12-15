import struct

def read_random_numbers():
    array_random_numbers = []
    with open ('randomnumbers.bin', 'rb') as file:
        while True:
            try:
                number = struct.unpack('i', file.read(4))[0]
                array_random_numbers.append(number)
            except:
                break
        return array_random_numbers


