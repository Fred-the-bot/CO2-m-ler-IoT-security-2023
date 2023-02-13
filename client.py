import random

prime=29
generator=3
client_key=15
server_key=19
client_full_key=server_key**client_key

print(client_full_key)

cryptographic=(client_full_key**generator+prime)/generator*prime
cryptographic=round(cryptographic)
print(cryptographic)


enc_sentence=[]
sentence=('hihi')
for i in range(len(sentence)):
    uni=ord(sentence[i])
    test=(uni+cryptographic)%255
    enc_sentence.append(test+15)

print(enc_sentence)
enc_sentence.append(random.randint(0,15))

for i in range(random.randint(10,55)):
    enc_sentence.append(random.randint(11,200))


print(enc_sentence)
# enc_sentence2=[]
# for i in range(len(enc_sentence)):
#     enc_sentence2.append(chr(enc_sentence[i]))
#
#
#
# print(enc_sentence2)
