from pymongo import MongoClient

conexao = MongoClient("localhost", 27017)
db = conexao["ListaDeTarefas"]
colecao = db.get_collection("tarefas")

class ListaDeTarefas:    
    def determinarProximoId(self):
        response = colecao.find()
        listResponse = list(response)
        if(len(listResponse) == 0):
            return 1
        else:
            listaIds = []
            j = 0

            for i in listResponse:
                listaIds.append(listResponse[j]["codigo"])
                j+=1

            proximoId = max(listaIds, key=int)
            proximoId += 1
            return proximoId       
        
    def inserirTarefa(self, id, descricao):              
        tarefa = {"codigo":id, "descricao":descricao}
        colecao.insert_one(tarefa)    

    def listarTarefas(self):
        j = 0
        response = colecao.find()
        listResponse = list(response)
        print("ID ------------ DESCRIÇÃO")
        print()
        for i in listResponse:
           print(listResponse[j]["codigo"],"            ",listResponse[j]["descricao"])
           j += 1        
        print()

    def excluirTarefa(self, id):
        colecao.delete_one({"codigo":id})
