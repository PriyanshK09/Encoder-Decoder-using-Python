# Encoder and Decoder using Python (Classes and OOPS)

class Encoder:
    def __init__(self):
        self
        
    def encode(self, message):
        encoded = ""
        for i in message:
            encoded += chr(ord(i) + 1)
        return encoded
    
class Decoder:
    def __init__(self):
        self
        
    def decode(self, message):
        decoded = ""
        for i in message:
            decoded += chr(ord(i) - 1)
        return decoded  
    
class EncoderDecoder:
    def __init__(self):
        self
        
    def encode(self, message):
        encoded = ""
        for i in message:
            encoded += chr(ord(i) + 1)
        return encoded
    
    def decode(self, message):
        decoded = ""
        for i in message:
            decoded += chr(ord(i) - 1)
        return decoded
    
def main():
    print("Encoder and Decoder using Python (Classes and OOPS)")
    print("1. Encoder")
    print("2. Decoder")
    print("3. Encoder and Decoder")
    choice = int(input("Enter your choice: "))
    if choice == 1:
        encoder = Encoder()
        message = input("Enter the message to be encoded: ")
        print("Encoded message: ", encoder.encode(message))
        
    elif choice == 2:
        decoder = Decoder()
        message = input("Enter the message to be decoded: ")
        print("Decoded message: ", decoder.decode(message))
        
    elif choice == 3:
        encoderDecoder = EncoderDecoder()
        message = input("Enter the message to be encoded and decoded: ")
        print("Encoded message: ", encoderDecoder.encode(message))
        print("Decoded message: ", encoderDecoder.decode(message))
        
    else:
        print("Invalid choice")
        
if __name__ == "__main__":
    main()
