## PRECISO ESTRUTURAR A ÁRVORE;

## tamanho da árvore -> 2^altura - 1;

def	perguntas(p):
	if p == -1: 
		print("A casa está ABAIXO DO PREÇO!")
	if p == 0: 
		print("A casa tem o PREÇO NA MÉDIA!")
	if p == 1: 
		print("A casa está ACIMA DO PREÇO!")
	if p == 2: 
		print("sqrft_living > 1800?") ## <=1.5
	if p == 3:
		print("sqrft_basement <= 310?") ## <= 0.5
	if p == 4:
		print("View <= 0.5")
	if p == 5:
		print("sqrft_living <= 2690?") ## <= 0.5
	if p == 6:
		print("Bathroom <= 2.625?")
	if p == 7:
		print("Bathroom <= 2.125?")
	if p == 8:
		print("sqrft_basement > 910?") ## <= 1.5
	if p == 9:
		print("sqrft above <= 1590?") ## <= 0.5
	if p == 10:
		print("Condition <= 3.5?")
	if p == 11:
		print("sqrft_basement <= 310 ou >= 940 ?") ## <= 1
	if p == 12:
		print("Bedroom <= 3.5?")
	if p == 13:
		print("sqrft_above <= 1590 ou >= 2340?") ## <= 1
	if p == 14:
		print("Bedroom <= 2.5?")
	if p == 15:
		print("sqrft_lot está entre 67269 e 21370?") ## <= 0.5
	if p == 16:
		print("Floors <= 1.25?")

	return


def arvore_nula(altura):
	tree = [1]

	for i in range(((2**altura) -1) + 10):
		tree.append(0)
	
	return tree

def arvore_33(v):
	v[1] = 2 
	v[2] = 3 
	v[3] = 10 
	v[4] = 4 
	v[5] = 8
	v[6] = 15
	v[7] = 16
	v[8] = 5
	v[9] = 1
	v[10] = -1
	v[11] = 9
	v[12] = 1
	v[13] = 12
	v[14] = 11
	v[15] = 0
	v[16] = 7
	v[17] = 6
	v[22] = 7
	v[23] = -1
	v[26] = 11
	v[27] = 0
	v[28] = 1
	v[29] = 0
	v[32] = -1
	v[33] = 0
	v[34] = -1
	v[35] = 0
	v[44] = 0
	v[45] = 12
	v[52] = 13
	v[53] = 0
	v[90] = -1
	v[91] = 0
	v[104] = 14 
	v[105] = 0
	v[208] = 0
	v[209] = 1

	return v

def consulta(no, tree):
	no = int(no)
	if tree[no] == -1 or tree[no] == 0 or tree[no] == 1:
		return tree[no]

	perguntas(int(tree[no]))	

	esquerdo = 2*no	
	direito = 2*no + 1

	op = input()

	if op == "s":
		return consulta(esquerdo, tree)
	if op == "n":
		return consulta(direito, tree)
	if op == "x":
		return op



def cabecalho():
	print("###########################################")
	print("##         CHATBOT - PRECO CASAS         ##")
	print("##    Programacao Estruturada QS 2020    ##")
	print("###########################################")
	print("###########################################")
	print("#### GRUPO 33   ###########################")
	print("###########################################")
	print("#### ABNER A.   ###########################")
	print("#### MICHEL M.  ###########################")
	print("#### RODRIGO M. ###########################")
	print("###########################################")
	print("## Responda as perguntas com:            ##")
	print("## s -> sim                              ##")
	print("## n -> não                              ##")
	print("## x -> para o programa                  ##")
	print("###########################################")
	print()
	print()
	
	return

def main():
	cabecalho()	

	arvore = arvore_nula(8)
	
	arvore = arvore_33(arvore)

	op = 's'  

	while op != 'x':
		op = consulta(1, arvore);
		if op != 'x':
			perguntas(int(op))	
		print("*******************************************")
		
	
	print("*******************************************")
	print("Fim do programa")

if __name__ == "__main__":
	main()
		