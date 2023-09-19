from listaDeTarefas import *

lista = ListaDeTarefas()

while 1:  	 
	lista.menu_principal()
	op = int(input("\nEscolha uma opção: "))
	if(op == 0):
		break
	elif(op == 1):
		id = lista.determinarProximoId()
		lista.inserirTarefa(id, input("Adicione uma descrição: "))
	elif(op == 2):
		lista.listarTarefas()
	elif(op == 3):
		id = int(input("Informe o ID: "))
		lista.removerTarefa(id)
	else:
		print("Opção inválida!")