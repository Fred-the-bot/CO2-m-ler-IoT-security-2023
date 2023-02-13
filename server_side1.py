import requests
import math
prime=29
generator=3
server_key=13
to_client=generator**server_key%29
server_full_key=math.pow(26,13)%29
print(server_full_key)
client_key=15
cryptographic=(server_full_key**generator+prime)/generator*prime
cryptographic=round(cryptographic)
#cryptographic=math.floor((math.pow(server_full_key,server_key)+server_key)/prime)
print(cryptographic)

sentence=[121, 122, 121, 122, 11, 171, 53, 148, 166, 15, 156, 190, 125, 56, 141, 90, 34, 133, 60, 85, 16, 148, 73, 92, 14, 141, 99, 106, 158, 137, 200, 142, 138, 179, 16, 94, 125, 91, 192, 193, 26, 177]

dec_sentence=[]
decrypt_sentence=[]
for i in range(len(sentence)):

    if sentence[i] <= 15:
        print("finished")
        break
    character = (sentence[i]-15)
    test = (character - cryptographic) % 255
    dec_sentence.append(test)
    decrypt_sentence.append(chr(dec_sentence[i]))

print(dec_sentence)
print(decrypt_sentence)




#test= 'https://api.thingspeak.com/update?api_key=81WRL4OZQE9YSVXX&field1='
#test=test+'60'



#test2=requests.get(test)
#print(test)
#print(test2)


