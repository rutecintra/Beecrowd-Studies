# https://www.beecrowd.com.br/judge/pt/problems/view/1038

lanches = []
for i in range(5):
	lanches = lanches + [[0]*3]

lanches[0][0] = int(1)
lanches[0][1] = str('Cachorro Quente')
lanches[0][2] = float(4)

lanches[1][0] = int(2)
lanches[1][1] = str('X-Salada')
lanches[1][2] = float(4.5)

lanches[2][0] = int(3)
lanches[2][1] = str('X-Bacon')
lanches[2][2] = float(5)

lanches[3][0] = int(4)
lanches[3][1] = str('Torrada simples')
lanches[3][2] = float(2)

lanches[4][0] = int(5)
lanches[4][1] = str('Refrigerante')
lanches[4][2] = float(1.5)

l1,l2 = map(int,input().strip().split(" "))
total = float(0)

for linha in range(5):
	if lanches[linha][0] == l1:
		total = lanches[linha][2] * l2

print("Total: R$ %.2f" % (total))