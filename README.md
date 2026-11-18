# Pagina-Web-de-Ordenamiento

Aplicación web interactiva desarrollada para la materia de Lenguaje de Programación II, diseñada para demostrar el funcionamiento práctico de algoritmos de ordenamiento avanzados, búsqueda eficiente y análisis de rendimiento (benchmark).

---

## Características Principales

* **Algoritmo Quicksort:** Ordenamiento eficiente de productos por ID, Nombre, Menor Precio y Mayor Precio (con soporte completo para caracteres especiales y acentos).
* **Búsqueda Binaria:** Localización optimizada de productos mediante ID utilizando precondición de ordenamiento previo.
* **Benchmark de Rendimiento:** Comparativa en tiempo real entre **Quicksort** y **Bubble Sort** procesando una muestra masiva de 1,000 elementos aleatorios en milisegundos (`ms`).

---

## Tecnologías Necesarias

* **Backend:** Python 3, Flask, JSON.
* **Frontend:** HTML5, CSS3 (Diseño responsivo y oscuro), JavaScript (Fetch API).
* **Infraestructura / Despliegue Híbrido:** 
  * **IPFS (Pinata):** Alojamiento descentralizado de archivos estáticos y datos.
  * **Vercel:** Redirección de rutas mediante `vercel.json`.

---

## Algoritmos Utilizados

- **Quicksort**: Es el algoritmo de ordenamiento utilizado como pivote central,con tres particiones (menores / iguales / mayores).
- **Búsqueda binaria**: O(log n). Requiere una lista organizada, por lo que se ordena por `id` antes de buscar.
- **Burbuja**: O(n²), usada para una comparación con el Quicksort.

 ---

 ## Pagina en Vercel

- (https://pagina-web-ordenamiento.vercel.app/)

 ---

 ## Licencia

MIT – ver [LICENSE](LICENSE).
