import asyncio
import time
import random
import multiprocessing

#Funcion asincrona para verificar el inventario
async def check_inventory(item):
    print(f"Verificando inventario para {item}...")
    await asyncio.sleep(random.randint(3,6))
    print(f"Inventario verificado para {item}")
    #Simular disponibilidad del producto
    return random.choice([True, False])

#Funciona asincrona para procesar el pago
async def process_payment(order_id):
    print(f"Procesando pago para la orden {order_id}...")
    #Simular el tiempo de espera que tiene el servicio de pago
    await asyncio.sleep(random.randint(3,6))
    print(f"Pago procesado para la orden {order_id}")
    return True

#Funcion intensiva en CPU para calcular el costo del pedido total
def calculate_total(items):
    print(f"Calculando el costo total para {len(items)} articulos...")
    time.sleep(5)
    total = sum(item['price'] for item in items)
    print(f"Costo total calculado: {total}")
    return total

async def process_order(order_id, items):
    print(f"Iniciando el procesamiento de la orden {order_id}...")
    #Verificar inventario para cada articulo
    inventory_checks = [check_inventory(item['name']) for item in items]
    inventory_results = await asyncio.gather(*inventory_checks)

    if not all(inventory_results):
        print(f"Orden {order_id} cancelada: Producto no disponible")

    with multiprocessing.Pool() as pool:
        total = pool.apply(calculate_total, (items,))

    #Procesador el pago asincronicamente
    payment_result = await process_payment(order_id)

    if payment_result:
        print(f"Orden {order_id} completada con exito. Total {total}")
    
    else:
        print(f"Error al procesar la orden {order_id}")

async def main():
    orders = [
        {'order_id': 1, 'items': [{'name': 'Laptop', 'price': 1000}, {'name': 'Mouse', 'price': 50}]},
        {'order_id': 2, 'items': [{'name': 'Teclado', 'price': 80}, {'name': 'Monitor', 'price': 300}]},
        {'order_id': 3, 'items': [{'name': 'Smartphone', 'price': 700}, {'name': 'Funda', 'price': 20}]}
    ]

    #Procesar multiples ordenes concurrentemente
    tasks = [process_order(order['order_id'], order['items']) for order in orders ]
    await asyncio.gather(*tasks)

#Creamos el evenloop 
if __name__ == '__main__':
    asyncio.run(main())

