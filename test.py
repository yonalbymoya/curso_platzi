'''new_product = {

    'name ' : 'Wireless Charger',
    'price' : '75',
    'quantity' : 100,
    'brand' : 'ChargerMaster',
    'category' : 'Accesories',
    'entry_date' : '2024-10-27'

}

with open('products.csv', mode='a', newline = '') as file:
    #file.write('\n)
    csv.write = csv.DictReader(file, fieldnames= new_product.keys())
    csv.writer.writerow(new_product)'''

'''with open(file_path, mode='r') as file:
    csv_reader = csv.DictReader(file)
    #Obtener los nombres de las columnas existentes
    fieldnames = csv_reader.fieldnames + ['total_value']

    with open(updated_file_path, mode='w', newline='') as updated_file:
        csv_writer = csv.DictWriter(updated_file, fieldnames=fieldnames)
        csv_writer.writeheader()

        for row in csv_reader:
            row['total_value'] = float(row['price'] ) * int(row['quantity'])
            csv_writer.writerow(row)'''

'''def json_a_csv(json1, csv1):
    with open(json1, mode='r', encoding='utf-8') as json_file:
        list_dates = json.load(json_file)

    headers = list_dates[0].keys()

    with open(csv1, mode='w', newline='', encoding='utf-8') as csv_file:
        csv_writer = csv.DictWriter(csv_file, fieldnames=headers)
        csv_writer.writeheader()
        csv_writer.writerows(list_dates)

json_a_csv(json2, csv2)


def csv_to_json(csv1, json1):
    with open(csv1, mode='r', encoding='utf-8') as csv_file:
        csv_reader = csv.DictReader(csv_file)
        list_dates = list(csv_reader)

    with open(json1, mode='w', encoding='utf-8') as json_file:
        json.dump(list_dates, json_file, indent=4)
        '''

'''import statistics
import csv

monthly_sales = {}
with open('monthly_sales.csv',mode='r') as file:
    reader = csv.DictReader(file)
    for row in reader:
        month = row['month']
        sales = int(row['sales'])
        monthly_sales[month] = sales

sales = list(monthly_sales.values())
print(sales)

mean_sales = statistics.mean(sales)
print(f"La media es: {mean_sales}")

mean_sales = statistics.median(sales)
print(f"La mediana es: {mean_sales}")

mean_sales = statistics.mode(sales)
print(f"La moda es: {mean_sales}")

mean_sales = statistics.mean(sales)
print(f"La media es: {mean_sales}")

mean_sales = statistics.stdev(sales)
print(f"La desviacion es: {mean_sales}")

mean_sales = statistics.variance(sales)
print(f"La varianza es: {mean_sales}")

max_sales = max(sales)
min_sales = min(sales)

range_sales = max_sales - min_sales
print(f'Rango de ventas: {range_sales}')'''

'''import os

cwd = os.getcwd()
txt_files = [f for f in os.listdir('.') if f.endswith('.txt')]
os.rename('wordlist.txt', 'wordlist1.txt')
print("archivo renombrado")
txt_files = [f for f in os.listdir('.') if f.endswith('.txt')]
print(f"nuevo nombre {txt_files}")'''

'''lista = [
    {"nombre": "Maria La del Barrio",
     "edad": 30,
     "sueldo": 30000
     },
    {"nombre": "Luis Miguel",
     "edad": 25,
     "sueldo": 25000
     },
    {"nombre": "Ana Bolena",
     "edad": 20,
     "sueldo": 20000
     },
     {"nombre": "Pepe Grillo",
     "edad": 20,
     "sueldo": 50000
     }
]

def lista_empleados(lista_empleado: list, sueldo_empleado: float) -> list:
    #return (emp['nombre'] for emp in lista_empleado if emp['sueldo'] > sueldo_empleado)
    resultados = []
    for k in range(len(lista_empleado)):
        if lista_empleado[k]['sueldo'] > sueldo_empleado:
            resultados.append(lista_empleado[k]['nombre'])
        print(resultados)
        return resultados
    
    
lista_empleados(lista, 28000)'''

#Decorador que comprueba si un empleado tiene un rol especifico
def check_access(required_role):
    print('dentro de check')
    def decorator(func):
        print('dentro de decorador')
        def wrapper(employee):
            print('dentro de wrapper')
            #Si el rol del empleado coincide con el rol requerido
            if employee.get('role') == required_role:
                return func(employee)
            else:
                print(f'ACCESO DENEGADO. Solo {required_role} pueden realizar esta accion')
        return wrapper
    return decorator

def log_action(func):
    def wrapper(employee):
        print(f'Registrando accion para el empleado {employee['name']}')
        return func(employee)
    return wrapper


@check_access('admin')
@log_action
def delete_employee(employeed):
    print(f'El empleado {employeed['name']} ha sido eliminado')

admin1 = {'name': 'Yonalby', 'role': 'admin'}

delete_employee(admin1)







