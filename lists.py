def remove_elements(list_to_remove_elements):
    del nombres[0]
    del nombres[3]
    del nombres[3]
    return nombres

def add_elements(list_to_add_elements):
    apellidos.insert(0, 'Perez')
    apellidos.insert(7, 'Gomez')
    return apellidos 


def is_empty(list_to_check):
    if len(lista) == 0:
        return lista

def check_lists(list_to_compare1, list_to_compare2):
    if len(apodos)>2 and len(nombresh)>2:
        return apodos[2] == nombresh[2]
      

def list_of_lists(list_of_lists_to_modify):
    if len(familia[0]) > 2 and len(familia[1]) > 4: 
        return familia[0][:2] , familia[1][1:4] , familia[2][-2:]

nombres = ['Marina', 'Mora', 'Milagros', 'Mia', 'Maggie', 'Manuela']
apellidos = ['Fernandez', 'Fiore', 'Fiorentino', 'Ferrari']
lista = ['']
apodos = ['Rufi', 'Lola', 'Camilos', 'Ferno', 'Mataholic', 'Angel']
nombresh = ['Marcelo', 'Marcos', 'Camilo', 'Milo', 'Monse']
familia = [['Milagros','Santiago','Benicio','Dolores','Nahuel'], ['Matias','Sonia','Nina','Annie','Milagros','Santiago'], ['Tigra','Nicky','Tomi','Vainilla','Licha','Leon']]

