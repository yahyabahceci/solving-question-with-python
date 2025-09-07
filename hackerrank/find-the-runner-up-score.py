n = int(input())
a = input()

liste = a.split()
liste = [int(x) for x in liste]

liste = sorted(set(liste))

print(liste[-2])