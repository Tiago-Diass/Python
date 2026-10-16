nums = [2,5,8,11,7,9,13]

# Imprimir a lista
print(nums) # [2,5,8,11,7,9,13]

# Imprimir um elemento da lista
print(nums[2]) # 8

# Inserir um novo elemento no final da lista
nums.append(17) # [2,5,8,11,7,9,13,17]

# Inserir vários elementos no final da lista
nums.extend([12,16]) # [2,5,8,11,7,9,13,17,12,16]

# Inserir em posição específica
nums.insert(3,29) # [2,5,8,29,11,7,9,13,17,12,16]

# Remover o elemento no final da lista
nums.pop() # [2,5,8,29,11,7,9,13,17,12]

# Remover um elemento de uma posição especifíca da lista pelo índice
nums.pop(2) # [2,5,29,11,7,9,13,17,12]

# Remover um elemento de uma posição especifíca da lista pelo valor
nums.remove(17) # [2,5,29,11,7,9,13,12]

# Nº de elementos da lista
total = len(nums) # 8

# Para cada elemento da lista <= 10
for n in nums:
    if n <= 10:
        print(n, " ")

# Para percorrer por indice
for indice in range(len(nums)):
    if nums[indice] <= 10:
        print(nums[indice], end= " ")


nums2 = nums
nums.append(2)
print(nums, nums2)

nums3 = nums2.copy() # As listas são independentes
nums2.append(1000)
print(nums2, nums3)

# Ordenar
nums.sort