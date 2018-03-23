vk = input("Сумма вклада: ")
s = input("Процентная ставка в год: ")
vkm = input("Срок вклада в месяц: ")
vk = int(vk)
vkm = int(vkm)
s = int(s)
s1 = s/12
s1 = float(s1)

print("Ваш ежемесячный доход от депозита: ", vk * s1 / 100)

