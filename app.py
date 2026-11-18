from flask import Flask, jsonify, request, render_template
import json
import time
import random
import copy

app = Flask(__name__)

#(soporte de acentos)
def cargar_productos():
   with open ('productos.json', 'r', encoding='utf-8') as f:
            return json.load (f)

# Algoritmo Quicksort modular
def quicksort(items, clave, reverse=False):
  if len(items) <= 1: return items
  pivote = items[len(items) // 2][clave]
  izq = [x for x in items if (x[clave] > pivote if reverse else x[clave] < pivote)]
  centro = [x for x in items if x[clave] == pivote]
  der = [x for x in items if (x[clave] < pivote if reverse else x[clave] > pivote)]
  return quicksort(izq, clave, reverse) + centro + quicksort(der, clave, reverse)

  #3.BubbleSort
def bubble_sort(items, clave):
    arr = copy.deepcopy(items)
    n = len(arr)
    for i in range(n):
        hubo_cambio = False
        for j in range(0, n - i - 1):
            if arr[j][clave] > arr[j + 1][clave]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                hubo_cambio = True
        if not hubo_cambio:
            break
    return arr

    # Benchmark de 1.000 elementos (Quicksort vs Burbuja)
@app.route('/api/benchmark')
def ejecutar_benchmark():
    total = 1000
    muestra = [
        {'id': i, 'nombre': f'Item-{i}', 'precio': round(random.uniform(1.0, 999.0), 2)}
        for i in range(1, total + 1)
    ]
    random.shuffle(muestra)
    datos_quick, datos_burbuja = copy.deepcopy(muestra), copy.deepcopy(muestra)

    t0 = time.perf_counter()
    quicksort(datos_quick, 'precio', reverse=False)
    ms_quicksort = (time.perf_counter() - t0) * 1000
      
    t1 = time.perf_counter()
    bubble_sort(datos_burbuja, 'precio')
    ms_burbuja = (time.perf_counter() - t1) * 1000
     
    velocidad = round(ms_burbuja / ms_quicksort, 1) if ms_quicksort > 0 else 0
    return jsonify({
        'elementos': total,
        'quicksort_ms': round(ms_quicksort, 4),
        'burbuja_ms': round(ms_burbuja, 4),
        'comparativa': f'Quicksort fue {velocidad}x más rápido que BubbleSort'
    })

def busqueda_binaria(items, id_buscado):
    izquierda = 0
    derecha = len(items) - 1

    while izquierda <= derecha:
        medio = (izquierda + derecha) // 2
        
        if items[medio]['id'] == id_buscado:
            return items[medio]  # ¡Encontrado!
        elif items[medio]['id'] < id_buscado:
            izquierda = medio + 1
        else:
            derecha = medio - 1
            
    return None  # No encontrado

@app.route('/')
def index():
  return render_template('index.html')

@app.route('/api/productos')
def get_productos():
  productos = cargar_productos()
  sort_by = request.args.get('sort_by', 'precio')
  order = request.args.get('order', 'asc') == 'desc'
  ordenados = quicksort(productos, sort_by, reverse=order)
  return jsonify(ordenados)

@app.route('/api/productos/buscar')
def buscar_producto():
    productos = cargar_productos()
    
    id_buscado = request.args.get('id', type=int)
    if id_buscado is None:
        return jsonify({"error": "Debe proporcionar un ID válido"}), 400

    # PRECONDICIÓN: Ordenar primero por ID antes de la búsqueda binaria
    productos_ordenados = quicksort(productos, 'id', reverse=False)
    
    # Aplicar búsqueda binaria
    resultado = busqueda_binaria(productos_ordenados, id_buscado)
    
    if resultado:
        return jsonify(resultado)
    else:
        return jsonify({"error": "Producto no encontrado"}), 404

if __name__ == '__main__':
    app.run(debug=True)