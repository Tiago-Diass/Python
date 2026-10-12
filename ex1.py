from random import randint

nums = []
nums_maiores_media = []
nums_pares = 0
nums_impares = 0
nums_maior_media = 0

for _ in range(30):
    y = randint(1,100)
    nums.append(y)
    print(y)

print(f"O maior numero: {max(nums)}")
print(f"O menor numero: {min(nums)}")
media = round(sum(nums)/len(nums),2)
print(f"A media: {media}")



for a in range(len(nums)):
    if nums[a] > media:
        nums_maior_media += 1
        nums_maiores_media.append(nums[a])
    
    if a % 2 == 0:
        nums_pares += 1
    else:
        nums_impares += 1

print(f"Numeros pares: {nums_pares}")
print(f"Numeros impares: {nums_impares}")
print(f"Numeros maiores que a media: {nums_maior_media}")
print(f"Lista dos superiores que a media: ")

for indice in range(len(nums_maiores_media)):
    print(nums_maiores_media[indice], end = " ")