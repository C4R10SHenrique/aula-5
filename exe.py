#criando lista vazia
list_food = []

while True:
    print("\nMenu:")
    print("1. Adicionar comida")
    print("2. Remover comida")
    print("3. Modificar nome da comida")
    print("4. Ver lista")
    print("5. SAIR")


    option = input("Escolha uma opção:")

    if option == "1":
        food = input("Digite a comida que deseja inserir:")
        list_food.append(food)
    elif option == "2":
        delete_food = input("Digite a comida que deseja apagar:")
        if delete_food in list_food:
            list_food.remove(delete_food)
        else:
            print ("A comida não foi encontrada")
    elif option == "3":
        indice = int(input ("Digite o indice da comida que deseja modificar:'Indice inicia do 0'"))
        if 0 <= indice < len(list_food):
            new_food = input("Digite a nova comida que deseja inserir:")
            list_food[indice] = new_food
        else:
            print("Não foi encontrado o indice")
    elif option == "4":
        print("\n lista de comidas: ",list_food)
    elif option == "5":
        break

