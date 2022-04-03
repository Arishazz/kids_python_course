print("Message Encoder and Decoder")
print("To decode a message set valueshift to the difference of the original valueshift and 26")
message = input("Enter the message here:") # get users msg
valueshift = int(input("How much would you like to shift it by?:")) # ask what to shift it by
message = message.upper()           
output = ""                         
for letter in message:              
    if letter.isupper():           
        value = ord(letter) + valueshift    
        letter = chr(value)         
        if not letter.isupper():    
            value -= 26            
            letter = chr(value)     
    output += letter               
print("Encoded/Decoded message:", output)   

