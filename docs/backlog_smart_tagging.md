**BACKLOG DE EJECUCIÓN**

**Smart Tagging con IA**

desglose de fases en tareas ejecutables

*Cuaderno de trabajo del plan v1.2. Cada fase se abre en tareas
concretas, y cada tarea declara el concepto de ciencia de datos que se
practica al resolverla y la condición que la cierra. Incluye la revisión
de la estructura de repositorio propuesta.*

| **Campo**          | **Detalle**                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
|--------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Documento          | Backlog de ejecución — **versión 1.2**                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
| Documento maestro  | Plan de proyecto v1.2 (Plan_Smart_Tagging_Ecommerce.docx). Este backlog no lo reemplaza: lo ejecuta.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
| Fecha              | 12 de septiembre de 2026                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| Total de tareas    | **111 tareas** en 11 fases: 92 en el alcance comprometido (F0–F6, F8 y F10) y 19 en extensiones (F7 y F9)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| Orden de ejecución | F0 → F1 → F2 → F3 → F4 → F5 → F6 → **F8** → F7 → F9 → F10                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| Cambios v1.1       | Revisión de consistencia interna. **Defectos corregidos:** split de calibración ahora se congela en F2 (lo exigía F5.2 y no existía); F5.6 se reduce al mecanismo porque en F5 no hay correcciones que incorporar; la congelación del protocolo de recomendación se mueve al inicio de F8; el endpoint de búsqueda pasa de F7 a F9 (dependía de un contrato posterior); la demo del MVP deja de prometer búsqueda por texto; el .gitignore deja de bloquear sus propios entregables. **Tareas nuevas:** F0.11–F0.13, F1.4, F1.6, F2.4, F2.7, F2.10, F7.4, F7.7. **Reencuadres:** L1 como adaptación local y no reproducción; línea textual como sonda de fuga; acuerdo con estadístico corregido por azar en F7 igual que en F6. **Nuevo:** backlog.yaml con validación del grafo de dependencias. |
| Cambios v1.2       | Tras cerrar F0.1 y leer el texto literal de las reglas de H&M aparecieron **dos restricciones que el plan no contemplaba**, ambas en la sección 8 de las reglas: la obligación de compartir en Kaggle el código que se publique (8.B) y el requisito de que las dependencias y los pesos usen licencia permisiva OSI no copyleft (8.C). Se reflejan en **F0.3** (archivo LICENSE y atribución a Fashionpedia), **F4.9 y F4.10** (la licencia pasa a ser criterio de selección de modelo) y **F10.6** (enlace al repositorio en el foro de la competencia). Además se documenta el **orden real de ejecución de F0** —F0.6 va primero— sin renumerar los identificadores, y se parte la verificación de F0.3 en dos momentos.                                                                       |
| Propósito          | Ejecutar con consciencia: una tarea a la vez, entendiendo qué concepto se practica y por qué está antes o después de las demás.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |

**Cómo usar este documento**

El objetivo declarado del proyecto no es terminar rápido: es **entender
cada paso mientras se ejecuta**. Este documento está construido para
eso, y conviene usarlo de una forma concreta.

1.  **Una tarea a la vez, en orden.** Las dependencias están pensadas.
    Saltarse una tarea suele funcionar hasta que aparece un resultado
    que no se puede explicar, y entonces cuesta más rehacer que haber
    esperado.

2.  **Leer la columna de concepto antes de escribir código.** Es la
    columna que convierte la tarea en aprendizaje. Si el concepto no
    está claro, ahí está la señal de qué estudiar antes de abrir el
    editor.

3.  **Cerrar con la condición de terminado, no con la sensación de
    terminado.** La columna "terminado cuando" es deliberadamente
    verificable. Si no se puede comprobar, la tarea sigue abierta.

4.  **Escribir la conclusión de cada tarea en una línea.** Al cerrar una
    tarea, anotar en el cuaderno o en el commit qué se aprendió o qué
    sorprendió. Es lo que después se convierte en el informe técnico sin
    tener que reconstruirlo de memoria.

**Convenciones**

| **Marca**                 | **Significado**                                                                                                                          |
|---------------------------|------------------------------------------------------------------------------------------------------------------------------------------|
| **\[nube\]**              | La tarea necesita GPU: se ejecuta en el entorno de nube gratuita, dentro de la plataforma donde residen los datos (sección 12 del plan). |
| **\[local\]**             | La tarea corre en el equipo propio, sobre CPU o gráficos integrados. Es la mayoría del proyecto.                                         |
| **\[mixta\]**             | Parte en nube, parte en local. La tarea indica el reparto.                                                                               |
| **\[MVP\]** / **\[EXT\]** | Fase del alcance comprometido o extensión condicionada, según la frontera de la sección 13.2 del plan.                                   |
| código                    | Nombre de archivo, campo, módulo o comando concreto.                                                                                     |

**Orden de ejecución y por qué F8 va antes que F7**

MVP COMPROMETIDO

F0 ─▶ F1 ─▶ F2 ─▶ F3 ─▶ F4 ─▶ F5 ─▶ F6 ─▶ F8 ──┐

encuadre taxo datos base modelo calib humano negocio │

│

EXTENSIONES │

F7 (búsqueda) ─▶ F9 (producto y MLOps) ◀─────────────────────┘

│

▼

F10 cierre y publicación

El plan cierra el MVP en F0–F6 más F8, y deja F7 y F9 como primera
extensión. La consecuencia práctica para este backlog es que **F8 se
ejecuta inmediatamente después de F6**, aunque su número sea mayor: es
la fase que sostiene la pregunta de valor de negocio y la que diferencia
el proyecto de un ejercicio de visión por computador. F7 llega después.

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<tbody>
<tr class="odd">
<td><p><strong>Una advertencia sobre F4</strong></p>
<p>F4 es la fase donde este tipo de proyecto se estanca, porque siempre
hay otro modelo que probar y cada intento parece que va a mover la
cifra. F4 tiene diez tareas y <strong>cierra al terminarlas</strong>. Un
enfoque adicional es una decisión que se toma con F8 ya cerrado, nunca
en medio de F4.</p></td>
</tr>
</tbody>
</table>

**El backlog también vive en el repositorio**

Con más de cien tareas, un documento de Word sirve para entender el
razonamiento pero no para trabajar. Las dependencias entre tareas y los
artefactos que cada una produce son **datos**, no prosa, y como datos
pueden validarse. Por eso el backlog se duplica en docs/backlog.yaml,
con una entrada por tarea:

\- id: F2.12

fase: F2

bloque: MVP

modo: local

titulo: Congelar los cuatro splits con agrupamiento por producto

depends_on: \[F2.7, F2.11\]

outputs:

\- data/processed/splits/\*.parquet

\- docs/decisions/criterio_splits.md

dod: \>

Cuatro splits persistidos con hash. Ninguna variante de un mismo

producto aparece en dos splits distintos (test automático).

La razón no es el orden por el orden. Un backlog.yaml permite escribir
un test que verifique tres cosas que a mano se pasan por alto: que el
grafo de dependencias no tenga ciclos, que todo artefacto declarado como
entrada tenga alguna tarea que lo produzca, y que **ninguna tarea
dependa de una fase posterior a la suya**.

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<tbody>
<tr class="odd">
<td><p><strong>Ese test habría encontrado por sí solo tres de los
defectos de la versión anterior</strong></p>
<p>La versión 1.0 de este backlog tenía tres inconsistencias de
dependencia que un humano leyendo la tabla no detectó: F5.2 exigía un
conjunto de calibración que F2.9 no creaba; F5.6 pedía correcciones
humanas que en F5 aún no existían; y la condición de cierre de F7.7
referenciaba un contrato OpenAPI que nace en F9.2. Las tres son
violaciones del grafo, y las tres las habría marcado una validación
automática en segundos.</p>
<p>Es el mismo principio que el resto del proyecto aplica a la taxonomía
y a la matriz de procedencia: <strong>lo que puede ser dato validado no
debe quedarse en prosa confiada.</strong> La tarea F0.11 construye este
archivo y su test.</p></td>
</tr>
</tbody>
</table>

**F0 · Encuadre, licencias y entorno \[MVP\]**

Trece tareas. Ninguna involucra modelos, y todas condicionan el resto
del proyecto. Es la fase que se salta con más frecuencia y la que más
caro cuesta saltarse: aquí se decide qué se podrá publicar y si el
proyecto será reproducible.

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<tbody>
<tr class="odd">
<td><p><strong>Orden de ejecución dentro de F0, y por qué los
identificadores no se renumeran</strong></p>
<p><strong>F0.6 —inicializar el repositorio— es la primera acción física
de la fase</strong>, aunque lleve el número seis. F0.3 escribe el
.gitignore y el README, que son archivos dentro de un repositorio que
todavía no existe si se sigue el orden numérico. El orden real es:
<strong>F0.6 → F0.3 → F0.1 → F0.2 → F0.4 → F0.5 → F0.7 → …</strong></p>
<p>Los identificadores <strong>no se renumeran</strong> aunque el orden
no coincida con ellos. Desde el momento en que un identificador aparece
en un mensaje de commit, en docs/licencias.md o en el backlog.yaml, deja
de ser una etiqueta interna y pasa a ser una <strong>interfaz</strong>:
renumerarla rompe todas las referencias que ya existen. El orden se
documenta; los nombres se respetan.</p></td>
</tr>
</tbody>
</table>

| **ID** | **Tarea — qué hacer**                                                                                                                                                                                                                                                                                                                                                                                                                                                                               | **Concepto que se practica**                                                                                                                                                                                                                                                                                                                                                                                                                                                        | **Terminado cuando**                                                                                                                                                                                                                                                                                                                             |
|--------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| F0.1   | **\[local\]** Abrir la página oficial de reglas de H&M, aceptar la competencia y localizar la cláusula de datos. Copiar su **texto literal** a docs/licencias.md, con URL y fecha de consulta.                                                                                                                                                                                                                                                                                                      | La diferencia entre permiso de **uso** y permiso de **redistribución**: son dos permisos independientes y el segundo no se deriva del primero. Por qué un resumen de una cláusula no sustituye a la cláusula.                                                                                                                                                                                                                                                                       | docs/licencias.md contiene la cláusula textual, no parafraseada, con URL y fecha. Si difiere de lo asumido en el plan v1.2, las secciones 6.2, 7.3, 7.4 y 14 quedan anotadas para corregir.                                                                                                                                                      |
| F0.2   | **\[local\]** Registrar los términos de Fashionpedia por componente: anotaciones y ontología (CC BY 4.0), software del dataset (BSD 2-Clause) e imágenes (propiedad de terceros: Flickr, Unsplash, Burst by Shopify, Freestocks, Kaboompics, Pexels).                                                                                                                                                                                                                                               | Licencias compuestas: un mismo dataset puede tener tres licencias distintas sobre tres componentes distintos, con obligaciones distintas. Qué implica una cláusula de atribución en la práctica.                                                                                                                                                                                                                                                                                    | Tabla componente → licencia → obligación concreta en docs/licencias.md. La atribución CC BY 4.0 está redactada y lista para el README.                                                                                                                                                                                                           |
| F0.3   | **\[local\]** Trasladar la tabla 7.4 del plan (contrato de publicación) al README y **traducirla a \`.gitignore\` con patrones acotados por ruta**, no con globs globales de extensión: data/\* con excepción explícita de data/README.md, nunca data/ a secas. Añadir al README la **atribución CC BY 4.0 a Fashionpedia** y crear el archivo **\`LICENSE\`** con una licencia permisiva aprobada por la OSI (MIT o Apache-2.0). Ignorar también referencias/, donde vive la literatura académica. | Controles preventivos frente a correctivos, y **semántica real de \`.gitignore\`**: Git no desciende a un directorio excluido, así que una negación dentro de él no funciona. Un control mal escrito da falsa sensación de protección y además bloquea los propios entregables. El LICENSE responde a la sección 8.B de las reglas de H&M, que da por licenciado bajo OSI permisiva todo código de la competencia que se comparta; hacerlo explícito es mejor que dejarlo deducido. | **Verificación parcial aquí:** los patrones están escritos y revisados, el LICENSE existe y la atribución está en el README. **Verificación completa en F2.1**, con los datos ya descargados: git status no muestra ningún archivo de datos **y sí muestra** data/README.md, las figuras de reports/figures/ y las imágenes del catálogo propio. |
| F0.4   | **\[local\]** Instalar nbstripout como hook de pre-commit, para que los notebooks se comiten **sin salidas**.                                                                                                                                                                                                                                                                                                                                                                                       | Las salidas de un notebook incrustan imágenes en base64 dentro del .ipynb. Un notebook con imágenes de producto en sus salidas es, al comitearse, una redistribución de datos restringidos dentro del repositorio.                                                                                                                                                                                                                                                                  | Un notebook con una imagen renderizada en su salida se comitea limpio: git show del .ipynb no contiene bloques base64.                                                                                                                                                                                                                           |
| F0.5   | **\[local\]** Decidir y documentar si se publicarán los pesos del modelo ajustado sobre H&M, con la cláusula literal de F0.1 a la vista.                                                                                                                                                                                                                                                                                                                                                            | Derivados de datos restringidos: un modelo entrenado no es el dato, pero tampoco es independiente de él. Cómo se documenta una decisión tomada bajo incertidumbre legal.                                                                                                                                                                                                                                                                                                            | Decisión escrita con su justificación en docs/licencias.md. Por defecto: no se publican hasta que la lectura de la cláusula lo respalde.                                                                                                                                                                                                         |
| F0.6   | **\[local\]** Inicializar el repositorio con pyproject.toml, entorno virtual, *src-layout*, pre-commit con linter y formateador, y primer commit. Instalar el paquete en modo editable.                                                                                                                                                                                                                                                                                                             | Por qué un proyecto se estructura como **paquete instalable** y no como carpeta de scripts: el *src-layout* impide importar por accidente desde el directorio de trabajo, lo que obliga a que el código funcione de verdad instalado.                                                                                                                                                                                                                                               | pip install -e . funciona; import smart_tagging funciona desde cualquier directorio; pre-commit run --all-files pasa en limpio.                                                                                                                                                                                                                  |
| F0.7   | **\[local\]** Configurar DVC y MLflow con backend de archivos. Registrar un run de prueba con un parámetro y una métrica ficticios. Fijar el manejo de semillas en src/smart_tagging/seeds.py.                                                                                                                                                                                                                                                                                                      | Versionar datos no es versionar código: son dos historias distintas que deben poder cruzarse. Qué identifica un experimento de forma única — código, datos, configuración y semilla, no solo el código.                                                                                                                                                                                                                                                                             | Un run visible en la interfaz de MLflow; dvc status limpio; una función de semillas que fija Python, NumPy y el framework de deep learning en una sola llamada.                                                                                                                                                                                  |
| F0.8   | **\[nube\]** Abrir el notebook de la plataforma que aloja los datos. Verificar GPU disponible, memoria y versión del framework. Medir el tiempo de un paso hacia adelante de un codificador pequeño sobre un lote fijo.                                                                                                                                                                                                                                                                             | **Caracterizar el entorno antes de diseñar el experimento.** Sin una medición de referencia de throughput no se puede estimar cuánto tardará extraer embeddings de N imágenes, y el plan entero depende de esa estimación.                                                                                                                                                                                                                                                          | 00_setup_y_licencias.ipynb imprime GPU, memoria disponible y throughput medido en imágenes por segundo, con el tamaño de lote usado.                                                                                                                                                                                                             |
| F0.9   | **\[local\]** Exportar un codificador pequeño a ONNX, ejecutarlo con OpenVINO en gráficos integrados y en CPU, y comparar latencia contra el framework original.                                                                                                                                                                                                                                                                                                                                    | Runtimes de inferencia frente a frameworks de entrenamiento: por qué un modelo exportado y optimizado corre varias veces más rápido sin cambiar de arquitectura. Primer contacto con cuantización y su costo en precisión.                                                                                                                                                                                                                                                          | Tabla de latencia (framework original / ONNX-CPU / OpenVINO-iGPU) para el mismo modelo y lote, guardada en reports/metrics/.                                                                                                                                                                                                                     |
| F0.10  | **\[local\]** Definir el contrato de datos de salida en configs/output_schema.json: atributo, valor, confianza, nivel de evidencia, versión de taxonomía y versión de modelo.                                                                                                                                                                                                                                                                                                                       | El producto es el **contrato de datos**, no el modelo — la lección del benchmark de mercado. Versionar la salida desde el principio evita que cada consumidor del sistema invente su propio formato.                                                                                                                                                                                                                                                                                | Esquema validable con jsonschema y un ejemplo de respuesta que lo satisface, con un test que lo verifica.                                                                                                                                                                                                                                        |
| F0.11  | **\[local\]** Cerrar la columna de reproducibilidad y seguridad: generar el archivo de bloqueo de dependencias (uv.lock o equivalente), montar CI que ejecute tests y linter, configurar un **remoto DVC privado con acceso verificado**, añadir .env.example y un hook de detección de secretos. Escribir docs/backlog.yaml con el test que valida su grafo.                                                                                                                                       | La diferencia entre declarar rangos de dependencias y fijar versiones exactas. Y una advertencia de licencia: **un remoto DVC mal configurado es redistribución.** Empujar el caché a un bucket público o a una carpeta compartida entrega los datos igual que comitear el CSV.                                                                                                                                                                                                     | El lock existe; CI pasa en verde; el remoto DVC es privado **y su privacidad está verificada, no supuesta**; el test del grafo del backlog detecta ciclos, artefactos huérfanos y dependencias hacia fases posteriores.                                                                                                                          |
| F0.12  | **\[local\]** Crear el manifiesto de adquisición de datos en docs/manifiesto_datos.md: por cada descarga, fuente, URL, fecha de acceso, versión del dataset, hash de los archivos y ubicación local.                                                                                                                                                                                                                                                                                                | Linaje de datos frente a versionado de contenido. **DVC registra el hash de lo que hay en tu disco; no registra de dónde vino ni cuándo.** Para un dataset licenciado esa es exactamente la información que hace falta, porque sin fecha de acceso no se puede demostrar qué versión de los términos se aceptó.                                                                                                                                                                     | Manifiesto completo para cada fuente descargada, con hash verificable contra los archivos locales.                                                                                                                                                                                                                                               |
| F0.13  | **\[local\]** Crear tests/fixtures/ con datos sintéticos públicos que imiten la estructura de H&M y de Fashionpedia: unas decenas de registros y un puñado de imágenes generadas.                                                                                                                                                                                                                                                                                                                   | Por qué los tests no deben depender de los datos reales: sin fixtures, **CI no puede probar nada que toque datos**, que es casi todo el pipeline. Y al ser sintéticos son publicables, así que un tercero puede ejecutar la suite sin obtener H&M.                                                                                                                                                                                                                                  | La suite completa corre con pytest sin acceso a data/. Los fixtures están comiteados y el CI de F0.11 los usa.                                                                                                                                                                                                                                   |

**F1 · Taxonomía y ontología \[MVP\]**

Diez tareas. Es la capa cero de la arquitectura y bloquea todo lo demás:
sin taxonomía cerrada no se sabe qué se está prediciendo ni contra qué
se mide.

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<tbody>
<tr class="odd">
<td><p><strong>Sobre el orden respecto al EDA</strong></p>
<p>El plan pide taxonomía antes de datos, y aquí conviene precisar por
qué eso no es contradictorio con explorar primero. La taxonomía necesita
el <strong>inventario de esquema</strong> —qué campos existen, de qué
tipo, con qué valores admitidos—, que es barato de obtener. El EDA
completo necesita la taxonomía, porque las distribuciones se analizan
<strong>agrupadas por atributo de la taxonomía</strong>. Así que el
orden real es: inventario de esquema (F1.1) → taxonomía (F1.2–F1.10) →
EDA de distribuciones (F2).</p></td>
</tr>
</tbody>
</table>

| **ID** | **Tarea — qué hacer**                                                                                                                                                                                                                                                | **Concepto que se practica**                                                                                                                                                                                                                                                                                                                                                                                               | **Terminado cuando**                                                                                                                                                                           |
|--------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| F1.1   | **\[local\]** Inventariar el esquema de articles.csv: cada columna, su tipo, su cardinalidad y sus valores distintos. Identificar si existe un **identificador de producto padre** compartido entre variantes de color — es la clave que F2.7 necesita.              | La diferencia entre inventario de esquema y análisis exploratorio. Cardinalidad como primera señal de si un campo es categórico controlado, texto libre o identificador.                                                                                                                                                                                                                                                   | Tabla de columnas con tipo, número de valores distintos y muestra de valores. Está respondido si existe o no un identificador de producto padre.                                               |
| F1.2   | **\[local\]** Inventariar la ontología de Fashionpedia: 27 categorías principales, 19 partes de prenda, 294 atributos finos en 9 super-categorías. Cargar el JSON de anotaciones y recorrer su estructura jerárquica.                                                | Cómo se estructura una ontología construida por expertos: categorías, partes, atributos y jerarquía de super-categorías. Formato COCO extendido y qué añade el campo de atributos.                                                                                                                                                                                                                                         | Estructura recorrida y documentada, con el conteo verificado contra la fuente y no asumido.                                                                                                    |
| F1.3   | **\[local\]** Construir el mapeo **a nivel de atributo** Fashionpedia ↔ H&M. Marcar correspondencias exactas, parciales y ausentes en cada dirección.                                                                                                                | Reconciliación de vocabularios: dos taxonomías del mismo dominio casi nunca se corresponden una a una. Las correspondencias parciales son las interesantes y las que hay que documentar con criterio explícito.                                                                                                                                                                                                            | configs/mapping_fashionpedia_hm.yaml con una fila por atributo, el tipo de correspondencia y una nota de criterio en las parciales.                                                            |
| F1.4   | **\[local\]** Construir el mapeo **a nivel de valores**, que es donde está el trabajo real: equivalencias entre valores concretos, sinónimos, correspondencias parciales y valores sin equivalente en la otra taxonomía.                                             | **El mapeo de valores es lo que define qué cuenta como acierto.** Si una fuente dice "off-white" y la otra "White", ¿la predicción es correcta? Esa decisión tiene que congelarse antes de evaluar, o la métrica se vuelve negociable después de conocerla — el mismo principio de preinscripción de F3.9, aplicado a la taxonomía.                                                                                        | Tabla de valores con su equivalencia y el criterio aplicado. Los valores no mapeables están listados de forma explícita, no omitidos en silencio.                                              |
| F1.5   | **\[local\]** Asignar el nivel de evidencia A, B o C a cada atributo, según la sección 7.6 del plan. Ningún atributo queda sin nivel.                                                                                                                                | Que la métrica admisible depende del tipo de ground truth disponible. Por qué "no tiene etiqueta" es una propiedad que se declara y no un atributo que se omite del esquema.                                                                                                                                                                                                                                               | Todo atributo tiene nivel asignado y el conteo por nivel está documentado, con las métricas admisibles de cada nivel escritas al lado.                                                         |
| F1.6   | **\[local\]** Añadir las **reglas ontológicas**: aplicabilidad (qué atributos aplican a qué categorías), exclusión mutua entre valores, y combinaciones inválidas. Por ejemplo, largo de manga no aplica a pantalón; "sin tirantes" y "manga larga" no coexisten.    | Las reglas rinden dos veces. Son **precisión gratis**: un post-procesamiento que suprime predicciones inaplicables o contradictorias mejora la precisión a costo cero de modelo. Y son **validación sin etiquetas**: la tasa de predicciones contradictorias es una señal de calidad que no requiere ground truth, y por tanto es utilizable en el monitoreo de producción de F9.5, donde por definición no hay etiquetas. | Reglas expresadas en configs/taxonomy.yaml de forma evaluable por código, con tests. El post-procesamiento que las aplica está implementado y su efecto en precisión está medido por separado. |
| F1.7   | **\[local\]** Escribir configs/taxonomy.yaml: por atributo, definición operativa, vocabulario controlado, cardinalidad, nivel de evidencia, campo fuente de verdad y reglas de aplicabilidad.                                                                        | Vocabulario controlado frente a texto libre. Por qué la definición **operativa** —redactada para que dos personas apliquen el mismo criterio— es la parte difícil y la que decide la calidad del ground truth.                                                                                                                                                                                                             | El archivo cubre el 100% de los atributos y cada uno tiene definición redactada, no solo nombre.                                                                                               |
| F1.8   | **\[local\]** Implementar src/smart_tagging/taxonomy/: carga, validación, consulta por nivel de evidencia, resolución de versión y evaluación de las reglas ontológicas.                                                                                             | La taxonomía como **artefacto de primera clase** y no como constante enterrada en el código. Cargar configuración validada frente a leer un YAML y confiar en él.                                                                                                                                                                                                                                                          | El módulo carga el YAML, falla con error claro ante un atributo mal definido, y expone tanto la consulta por nivel como la verificación de consistencia ontológica.                            |
| F1.9   | **\[local\]** Escribir los tests de la taxonomía: que todo atributo tenga nivel, que los vocabularios no tengan duplicados ni valores vacíos, que el mapeo no referencie atributos ni valores inexistentes, y que las reglas ontológicas no se contradigan entre sí. | Tests sobre datos de configuración, no solo sobre funciones. Un test que valida el esquema detecta el error el día que alguien edita el YAML, no tres semanas después en una métrica rara.                                                                                                                                                                                                                                 | pytest pasa, y falla de forma legible ante un atributo sin nivel, un vocabulario con duplicados o una regla ontológica inconsistente.                                                          |
| F1.10  | **\[local\]** Fijar el versionado semántico de la taxonomía y su política de deprecación: un atributo no se elimina, se marca obsoleto. Registrar la versión inicial y el registro de cambios.                                                                       | Concept drift en la taxonomía, no solo en los datos: el referente académico midió un Jaccard de 0,41 entre los tópicos de dos años consecutivos. En moda la temporada es la deriva, y una taxonomía sin versión hace que cada cambio rompa la comparabilidad histórica.                                                                                                                                                    | configs/taxonomy.yaml tiene campo de versión; docs/taxonomy_changelog.md existe con la entrada inicial; la política de deprecación está escrita.                                               |

**F2 · Datos, EDA y splits congelados \[MVP\]**

Catorce tareas. Al final de esta fase los datos quedan inmovilizados:
los splits no vuelven a cambiar, y cualquier resultado posterior es
comparable con cualquier otro.

| **ID** | **Tarea — qué hacer**                                                                                                                                                                                                                                                                                  | **Concepto que se practica**                                                                                                                                                                                                                                                                                                                                      | **Terminado cuando**                                                                                                                                                                                                         |
|--------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| F2.1   | **\[nube\]** Acceder a los datos en el entorno donde residen y verificar integridad: archivos presentes, tamaños, conteo de filas real de cada CSV y número de imágenes. Registrar todo en el manifiesto de F0.12.                                                                                     | Verificar antes de confiar. Los conteos de filas del plan están marcados como no verificados: esta es la tarea que los cierra con el dato de la fuente.                                                                                                                                                                                                           | Conteos reales registrados en el manifiesto y en el diccionario de datos, contrastados con lo que el plan asumía.                                                                                                            |
| F2.2   | **\[mixta\]** Capa bronze: convertir los CSV a Parquet con tipos explícitos, sin ninguna transformación de negocio. Registrar el hash de cada archivo resultante en DVC.                                                                                                                               | Arquitectura por capas (bronze/silver/gold) y por qué la capa cruda no se toca nunca. Parquet frente a CSV: tipado, compresión y lectura por columnas — la diferencia que hace viable trabajar con 16 GB de memoria.                                                                                                                                              | Parquet generado con esquema explícito; hashes versionados en DVC; la conversión es reproducible con un comando.                                                                                                             |
| F2.3   | **\[local\]** Perfilar articles.csv: nulos por columna, duplicados, valores fuera del vocabulario de la taxonomía, inconsistencias entre campos correlacionados.                                                                                                                                       | Perfilado de calidad como paso explícito. Detectar valores fuera de vocabulario es lo que conecta el EDA con la taxonomía de F1 en lugar de dejarlos como dos ejercicios separados.                                                                                                                                                                               | Informe de calidad por columna, con la lista de valores fuera de vocabulario y una decisión por cada uno.                                                                                                                    |
| F2.4   | **\[local\]** Convertir el perfilado en una **puerta del pipeline**: esquema esperado, tipos, rangos, nulos admitidos y vocabularios válidos, expresados como contrato ejecutable que detiene la ejecución si no se cumple.                                                                            | La diferencia entre un perfilado que informa y un contrato que bloquea. **Un perfilado que solo informa se ignora**; una puerta que falla impide que el pipeline produzca un resultado silenciosamente equivocado sobre datos corruptos.                                                                                                                          | El pipeline falla con mensaje claro ante un archivo que viola el contrato. Hay un test que lo comprueba corrompiendo a propósito un fixture de F0.13.                                                                        |
| F2.5   | **\[local\]** Analizar la distribución de frecuencia de cada atributo. Cuantificar el desbalance: atributos muy frecuentes, cola larga y soporte mínimo por atributo.                                                                                                                                  | Desbalance de clases en un problema multi-etiqueta. Por qué esta distribución decide la elección de F1 macro, micro o ponderado, y por qué el referente académico usó el ponderado explícitamente.                                                                                                                                                                | Gráfica de distribución y tabla de soporte por atributo. **Umbral de soporte mínimo propuesto y justificado**, con la lista de atributos que quedarían excluidos del entrenamiento supervisado.                              |
| F2.6   | **\[local\]** Perfilar las imágenes sobre una muestra: resolución, relación de aspecto, uniformidad del fondo, presencia de modelo. Comparar con una muestra de Fashionpedia.                                                                                                                          | **Cuantificar el domain shift antes de sufrirlo.** Es la medición que respalda —o refuta— el riesgo declarado en la sección 7.5 del plan, en lugar de dejarlo como una preocupación abstracta.                                                                                                                                                                    | Comparación documentada entre ambos dominios, con una conclusión sobre la magnitud esperada del problema.                                                                                                                    |
| F2.7   | **\[local\]** Detectar imágenes idénticas y casi idénticas **antes** de congelar splits: hash perceptual o similitud de embeddings sobre un umbral, más el agrupamiento por identificador de producto padre si F1.1 confirmó que existe.                                                               | **Fuga visual, el error que más silenciosamente infla las métricas en catálogo de moda.** La misma prenda aparece en varias combinaciones de color con fotos casi idénticas, y un mismo artículo tiene varias tomas. Una variante en entrenamiento y otra en prueba hace que el modelo memorice en lugar de generalizar, y nada en la métrica delata el problema. | Grupos de variantes identificados y cuantificados. El informe dice qué fracción del catálogo pertenece a un grupo con más de un miembro — que es la magnitud del riesgo evitado.                                             |
| F2.8   | **\[local\]** Consultar transactions_train.csv con DuckDB sobre Parquet: volumen por fecha, estacionalidad, distribución de compras por cliente y por artículo, canal de venta. Sin cargar el histórico en memoria.                                                                                    | Consultar en lugar de cargar: SQL analítico sobre archivos columnares. Es la técnica que hace posible el experimento de recomendación con memoria limitada, y la que evita el primer bloqueo de la máquina.                                                                                                                                                       | Consultas ejecutadas sin agotar la memoria; agregados guardados; medición del tiempo de consulta frente a lo que costaría cargar todo.                                                                                       |
| F2.9   | **\[local\]** Medir la deriva de **vocabulario** entre periodos: qué atributos aparecen y desaparecen de una temporada a la siguiente, con un índice de solapamiento entre conjuntos.                                                                                                                  | Concept drift medido en los propios datos. El referente académico usó el coeficiente de Jaccard entre conjuntos de tópicos; aquí el equivalente es el solapamiento del vocabulario de atributos entre temporadas.                                                                                                                                                 | Serie de solapamiento entre periodos consecutivos, documentada.                                                                                                                                                              |
| F2.10  | **\[local\]** Medir la deriva de **distribución**, no solo de vocabulario: cambio en la frecuencia relativa de cada atributo entre periodos, con una distancia distribucional (índice de estabilidad poblacional, divergencia de Jensen-Shannon o Wasserstein para ordinales).                         | **El vocabulario puede ser idéntico entre temporadas y la distribución haber cambiado por completo**: todos los colores siguen presentes, pero el negro pasa del 5% al 30%. El solapamiento de conjuntos no ve eso. Es además la misma métrica que el bucle rápido de monitoreo usará en F9.5, aplicada aquí al histórico.                                        | Distancia distribucional calculada entre periodos consecutivos, con una conclusión sobre si la partición temporal del experimento de recomendación enfrentará deriva y de qué tipo — de vocabulario, de frecuencia, o ambas. |
| F2.11  | **\[local\]** Definir y ejecutar el muestreo estratificado del subconjunto de trabajo: representación controlada por categoría de producto y por frecuencia de atributo. Documentar el criterio.                                                                                                       | Muestreo estratificado frente a aleatorio, y por qué con cola larga el aleatorio deja atributos sin ejemplos. **Un subconjunto bien muestreado y declarado es metodología; uno improvisado es un sesgo no medido.**                                                                                                                                               | Criterio escrito, subconjunto generado y versionado, y comparación de distribuciones entre el subconjunto y el catálogo completo.                                                                                            |
| F2.12  | **\[local\]** Congelar **cuatro** splits para la tarea de tagging —entrenamiento, validación, **calibración** y prueba— y la partición **temporal** para transacciones. El split se hace **por grupo de producto**, usando los grupos de F2.7, no por imagen. Guardar identificadores y hashes en DVC. | Por qué hacen falta cuatro y no tres: la calibración post-hoc de F5.2 exige un conjunto propio, distinto del de entrenamiento y del de prueba, o la calibración se sobreajusta y el ECE reportado es ficticio. Y por qué el split es por grupo: si una variante de color cae en entrenamiento y otra en prueba, se está midiendo memorización.                    | Cuatro splits persistidos con hash, más la partición temporal. **Un test verifica que ningún grupo de producto de F2.7 aparece en dos splits distintos.** A partir de aquí no cambian.                                       |
| F2.13  | **\[local\]** Implementar la matriz de procedencia de la sección 7.7 **como código** en src/smart_tagging/data/provenance.py: dada un atributo objetivo, devuelve los campos bloqueados y falla si alguno aparece entre las entradas.                                                                  | Control de fuga de información ejecutable en lugar de documentado. Cubre los dos canales: texto → objetivo y **campo → campo** entre columnas correlacionadas, que es el que se pasa por alto.                                                                                                                                                                    | La función existe, tiene tests, y el pipeline de features la invoca de forma que sea imposible construir un conjunto de entrada con un campo bloqueado.                                                                      |
| F2.14  | **\[local\]** Encadenar todo en el pipeline reproducible (dvc.yaml o Makefile): de bronze a gold con un solo comando, con dependencias declaradas y la puerta de validación de F2.4 activa.                                                                                                            | Reproducibilidad como propiedad verificable y no como aspiración. Un pipeline con dependencias declaradas solo re-ejecuta lo que cambió, que es lo que hace soportable iterar con cómputo limitado.                                                                                                                                                               | Corre de punta a punta desde cero con un comando; modificar un paso intermedio re-ejecuta solo lo que depende de él.                                                                                                         |

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<tbody>
<tr class="odd">
<td><p><strong>El orden interno de F2 no es negociable en dos
puntos</strong></p>
<p><strong>F2.7 antes de F2.12:</strong> los grupos de variantes tienen
que existir antes de partir, porque el split se hace por grupo. Detectar
la fuga visual después de congelar obliga a rehacer todo lo que dependa
de los splits.</p>
<p><strong>F2.4 antes del resto del pipeline:</strong> la puerta de
validación se instala antes de que haya resultados que defender. Una
puerta añadida al final se ajusta, sin querer, a los datos que ya
pasaron.</p></td>
</tr>
</tbody>
</table>

**F3 · Línea base \[MVP\]**

Nueve tareas. La fase más subestimada del proyecto: produce el número
contra el cual se compara todo lo demás. Sin ella, cualquier resultado
de F4 es una cifra sin referencia.

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<tbody>
<tr class="odd">
<td><p><strong>El orden dentro de esta fase importa: el evaluador se
escribe antes que los modelos</strong></p>
<p>F3.2 construye el marco de evaluación <strong>antes</strong> de
entrenar el primer modelo real. Hacerlo al revés —modelo primero,
métricas después— produce dos problemas: se termina midiendo lo que el
modelo ya hace bien, y cada modelo se evalúa con un código ligeramente
distinto, lo que hace incomparables los resultados sin que se
note.</p></td>
</tr>
</tbody>
</table>

| **ID** | **Tarea — qué hacer**                                                                                                                                                                                                                                                                          | **Concepto que se practica**                                                                                                                                                                                                                                                                                                                                                                                                            | **Terminado cuando**                                                                                                                                                                                               |
|--------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| F3.1   | **\[local\]** Línea base trivial: predecir siempre los atributos más frecuentes del catálogo, ignorando la imagen por completo.                                                                                                                                                                | El piso del problema. Con distribuciones muy desbalanceadas esta línea base es engañosamente buena en *accuracy*, y sirve precisamente para **detectar métricas mal elegidas** antes de confiar en ellas.                                                                                                                                                                                                                               | La cifra está calculada y documentada. Si una métrica hace que esta línea base parezca buena, esa métrica queda descartada para el proyecto.                                                                       |
| F3.2   | **\[local\]** Implementar src/smart_tagging/evaluation/: precision, recall, F1 (macro, micro, ponderado), mAP, Hamming loss, subset accuracy y tasa de cobertura. Todo **por atributo y por nivel de evidencia**, con salida en formato fijo.                                                  | Cómo se calculan las métricas multi-etiqueta y en qué difieren macro, micro y ponderado. Por qué en el nivel C solo se puede reportar precisión: **sin etiquetas el denominador del recall no existe**, así que un F1 de nivel C sería una cifra inventada.                                                                                                                                                                             | El módulo tiene tests con casos construidos a mano cuyo resultado se conoce. Intentar calcular recall sobre atributos de nivel C **falla con un error explícito**, no devuelve un número.                          |
| F3.3   | **\[nube\]** Extraer características de la última capa totalmente conectada de una CNN profunda (VGG-19 con transfer learning) para todo el subconjunto. Persistir el caché con nombre que codifique modelo, versión, split y hash del dataset.                                                | Transfer learning y extracción de características frente a entrenamiento desde cero. **El esquema de nombres del caché es parte del diseño**: un caché mal nombrado se reutiliza silenciosamente con el modelo equivocado, y ese error no produce un fallo, produce un resultado falso.                                                                                                                                                 | Caché persistido y verificable; el nombre identifica sin ambigüedad qué lo produjo; recargarlo y recalcular una muestra da el mismo vector.                                                                        |
| F3.4   | **\[local\]** Implementar KNN multi-etiqueta ponderado por inversa de distancia sobre el caché. **Nombrarlo y documentarlo como "adaptación local del método de literatura", no como reproducción.**                                                                                           | Por qué no es una reproducción: el método original opera sobre un espacio multietiqueta grande y ruidoso de tags parseados; aquí las etiquetas son campos categóricos limpios de vocabulario controlado. **Difiere la forma de la tarea, no solo los datos.** Y también: por qué se descarta un clasificador por etiqueta, que exige un modelo por atributo y todos activos en inferencia.                                              | La adaptación corre sobre el caché sin recalcular features y es determinista con semilla fija. El informe la llama adaptación, y **en ningún lugar se compara su cifra contra la publicada** en el paper original. |
| F3.5   | **\[local\]** Barrer K (1, 3, 5, 7) y trazar la curva precisión-recall resultante. Observar y explicar la tendencia.                                                                                                                                                                           | El compromiso precisión-recall hecho visible: en la publicación de referencia la precisión sube y el recall baja al aumentar K, hasta precisión 0,819 con recall 0,210. **Entender por qué** es lo que convierte el umbral en una decisión de producto y no en un hiperparámetro más. Este patrón cualitativo sí transfiere entre dominios; el número no.                                                                               | Curva trazada y la tendencia explicada por escrito en una o dos frases propias. Queda claro cuál es el cuello de botella del problema.                                                                             |
| F3.6   | **\[local\]** Ejecutar la **sonda de fuga**: TF-IDF sobre los campos de texto que la matriz de procedencia **bloquea** (típicamente description), prediciendo atributos de nivel A. Correrla una vez, etiquetarla como sonda y **nunca reportarla como resultado**.                            | Reencuadre respecto a la versión anterior de este backlog. Si para los atributos de nivel A la descripción está bloqueada, una "línea base textual" no puede competir como resultado. Pero correrla deliberadamente sobre los campos bloqueados **cuantifica la fuga**: si TF-IDF alcanza F1 0,95 prediciendo la categoría desde la descripción, eso demuestra por qué el campo está bloqueado, con un número en lugar de un argumento. | Sonda ejecutada y su cifra registrada en reports/metrics/ bajo un nombre que la identifica como sonda de fuga. Queda escrito qué fracción del desempeño aparente del texto era fuga.                               |
| F3.7   | **\[local\]** Línea base textual legítima **solo si existen campos de texto permitidos** para algún atributo objetivo. Si la matriz de procedencia no deja ninguno para nivel A, la conclusión es que esta línea base no existe para esos atributos, y se declara como tal.                    | Que una tarea puede cerrarse con "no aplica" y eso es un resultado, no un fallo de ejecución. La matriz de procedencia es una restricción de diseño, y aceptar sus consecuencias es parte de respetarla.                                                                                                                                                                                                                                | O hay una línea base textual entrenada sobre campos permitidos, o está escrito por qué no existe para los atributos de nivel A. Las dos salidas cierran la tarea.                                                  |
| F3.8   | **\[local\]** Implementar bootstrap sobre el conjunto de evaluación para obtener intervalos de confianza de cada métrica.                                                                                                                                                                      | Que una diferencia entre modelos no significa nada sin su varianza. El bootstrap como forma no paramétrica de estimar el error de un estimador cuando no se conoce su distribución.                                                                                                                                                                                                                                                     | Cada métrica de la tabla de línea base se reporta con intervalo de confianza, no como valor puntual.                                                                                                               |
| F3.9   | **\[local\]** Calibrar los umbrales objetivo con la línea base en mano, escribirlos en configs/success_criteria.yaml y **congelarlos con marca de tiempo en un commit**, antes de entrenar el modelo final. El anclaje es la adaptación local de F3.4, no una cifra publicada en otro dominio. | **Preinscripción.** La diferencia entre calibrar y racionalizar no está en cuándo se calcula el umbral, sino en el orden respecto a haber visto el resultado. Un criterio fijado después del resultado no es un criterio.                                                                                                                                                                                                               | Archivo congelado y comiteado con fecha. El commit es anterior al primer entrenamiento de F4. Toda revisión posterior se documenta junto a la cifra anterior.                                                      |

**F4 · Modelo de tagging \[MVP\]**

Diez tareas. **La fase cierra al terminarlas.** Un enfoque adicional se
decide con F8 cerrado, no aquí.

| **ID** | **Tarea — qué hacer**                                                                                                                                                                                                                                  | **Concepto que se practica**                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              | **Terminado cuando**                                                                                                                                                                                            |
|--------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| F4.1   | **\[nube\]** Extraer embeddings de imagen con un codificador contrastivo imagen-texto (familia CLIP/SigLIP) para todo el subconjunto. Persistir con el mismo esquema de nombres de F3.3.                                                               | Modelos contrastivos multimodales: cómo se entrena un espacio compartido entre imagen y texto, y por qué eso habilita clasificación sin entrenamiento. Diferencia frente a las features de una CNN de clasificación.                                                                                                                                                                                                                                                                                                      | Caché persistido y validado. Medición del tiempo total de extracción contra la estimación hecha en F0.8.                                                                                                        |
| F4.2   | **\[local\]** Clasificación zero-shot: construir plantillas de prompt por atributo, codificar las etiquetas como texto y clasificar por similitud coseno contra el embedding de la imagen.                                                             | Clasificación zero-shot por similitud en espacio compartido. Por qué el vocabulario de la taxonomía se convierte directamente en el clasificador, sin datos de entrenamiento.                                                                                                                                                                                                                                                                                                                                             | Zero-shot evaluado sobre los mismos splits, con métricas por atributo y por nivel de evidencia.                                                                                                                 |
| F4.3   | **\[local\]** Iterar las plantillas de prompt: comparar al menos tres formulaciones por atributo y medir el efecto en F1, **ajustando en validación**.                                                                                                 | **El prompt es un hiperparámetro**, no una decisión estética, y su efecto puede superar el de cambiar de modelo. También: por qué ajustar prompts mirando el conjunto de prueba invalida la prueba.                                                                                                                                                                                                                                                                                                                       | Comparación documentada, con la elección final justificada por su desempeño en validación y no en prueba.                                                                                                       |
| F4.4   | **\[local\]** Sondeo lineal: entrenar una capa lineal multi-etiqueta sobre los embeddings congelados, en CPU.                                                                                                                                          | Sondeo lineal como diagnóstico de calidad de la representación: si un clasificador lineal separa bien, la información ya está en el embedding. **Es el mejor retorno por unidad de cómputo de todo el proyecto** — minutos en CPU sobre features ya calculadas.                                                                                                                                                                                                                                                           | Entrenado y evaluado; comparado con zero-shot; tiempo de entrenamiento registrado.                                                                                                                              |
| F4.5   | **\[local\]** Cabeza MLP multi-etiqueta con tratamiento explícito del desbalance: pérdida ponderada por soporte del atributo, y comparación contra la versión sin ponderar.                                                                            | Tratamiento del desbalance en multi-etiqueta y su efecto diferencial sobre F1 macro frente a ponderado. Por qué la ponderación mejora la cola larga a costa de las clases frecuentes.                                                                                                                                                                                                                                                                                                                                     | Ambas variantes evaluadas. El efecto sobre macro y sobre ponderado está medido por separado y explicado.                                                                                                        |
| F4.6   | **\[nube\]** Ajuste fino con adaptadores de bajo rango (LoRA) sobre el codificador de imagen, con acumulación de gradiente y checkpointing frecuente por expiración de sesión.                                                                         | Ajuste fino eficiente en parámetros: por qué entrenar matrices de bajo rango alcanza casi el desempeño del ajuste completo con una fracción de la memoria. Acumulación de gradiente como sustituto de un lote grande.                                                                                                                                                                                                                                                                                                     | Entrenamiento completado con checkpoints recuperables; evaluado sobre los mismos splits; costo en horas de GPU registrado.                                                                                      |
| F4.7   | **\[local\]** Evaluar cada enfoque por las **tres pistas de entrada**: imagen sola, texto solo y multimodal, con la matriz de procedencia activa en todas. Aplicar el post-procesamiento de reglas ontológicas de F1.6 y medir su efecto por separado. | Aislamiento de la contribución de cada modalidad. La pista imagen-sola es el titular honesto porque corresponde al caso de negocio real. Y las reglas ontológicas son precisión gratis: conviene saber cuánta aportan.                                                                                                                                                                                                                                                                                                    | Tabla de tres pistas × enfoques, con y sin post-procesamiento ontológico. La conclusión sobre la contribución real de la visión está escrita.                                                                   |
| F4.8   | **\[local\]** Análisis de errores: matriz de confusión por atributo, atributos con peor F1, inspección de los casos peor clasificados y búsqueda de patrones (oclusión, fondo, prendas múltiples).                                                     | Análisis de errores como fuente de hipótesis y no como trámite. Es donde se descubre si el modelo falla por el modelo, por el dato o por la definición del atributo en la taxonomía — tres causas con tres soluciones distintas.                                                                                                                                                                                                                                                                                          | Al menos tres patrones de error identificados, cada uno con su causa atribuida y su acción propuesta.                                                                                                           |
| F4.9   | **\[local\]** Consolidar la tabla comparativa: todos los enfoques sobre los mismos splits, con F1 por nivel de evidencia, intervalos de confianza, **segundos por imagen, horas de GPU consumidas y licencia de cada modelo preentrenado**.            | Que el desempeño sin su costo es información incompleta. Un modelo que gana dos puntos de F1 a cuarenta veces el costo de inferencia no es el ganador en un catálogo de cientos de miles de SKU. Y **la licencia es un criterio de selección, no un trámite posterior**: la sección 8.C de las reglas de H&M exige licencias permisivas OSI no copyleft, y varios modelos de visión-lenguaje se distribuyen con licencias no comerciales o propias que no lo son. Descubrirlo después de elegir obliga a repetir la fase. | Tabla única con desempeño, costo y licencia. La elección del modelo está justificada considerando las tres dimensiones, y **ningún modelo con licencia copyleft o de no uso comercial entró a la comparación**. |
| F4.10  | **\[local\]** Registrar el modelo elegido en MLflow con su versión de taxonomía, hash de splits, configuración, métricas **y licencia de origen**. Verificar contra los umbrales congelados en F3.9.                                                   | Registro de modelos y trazabilidad: qué información hace que un modelo sea reproducible —y auditable— seis meses después. Comparación contra un criterio fijado de antemano en lugar de contra la expectativa del momento.                                                                                                                                                                                                                                                                                                | Modelo registrado y recuperable, con su licencia anotada; comparación explícita contra los umbrales congelados, con el veredicto escrito (se cumple o no, y en qué atributos).                                  |

**F5 · Calibración y revisión humana \[MVP\]**

Siete tareas. Convierte un clasificador en un sistema operable: decide
qué se acepta automáticamente y qué va a revisión.

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<tbody>
<tr class="odd">
<td><p><strong>Corrección respecto a la versión anterior: en F5 todavía
no hay correcciones humanas</strong></p>
<p>La versión 1.0 pedía en F5.6 incorporar correcciones humanas al
entrenamiento, pero en F5 no existe ninguna: la cola de revisión se
acaba de construir y F6 no ha ocurrido. F5.6 se reduce ahora a
<strong>construir y probar el mecanismo</strong> con correcciones
sintéticas; la ejecución real del ciclo se hace en F9.8, alimentada por
la cola.</p>
<p><strong>Y una advertencia que no puede perderse:</strong> el conjunto
adjudicado de F6 <strong>nunca</strong> entra al entrenamiento. Es el
patrón oro contra el que se mide el acuerdo humano-máquina y la
incompletitud de la metadata; entrenar sobre él infla ambas mediciones y
destruye el único ground truth de calidad superior que el proyecto
produce. La fuente legítima de correcciones es la cola de F5.5, no la
muestra de F6.</p></td>
</tr>
</tbody>
</table>

| **ID** | **Tarea — qué hacer**                                                                                                                                                                                                                                                                                       | **Concepto que se practica**                                                                                                                                                                                                                                                                                                                                  | **Terminado cuando**                                                                                                                                                                          |
|--------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| F5.1   | **\[local\]** Trazar curvas de fiabilidad y calcular el error de calibración esperado (ECE) del modelo elegido, por atributo.                                                                                                                                                                               | Calibración frente a discriminación: un modelo puede ordenar bien y estar mal calibrado. Sin calibración, una confianza de 0,8 no significa 80% de acierto, y cualquier umbral construido sobre ella es arbitrario.                                                                                                                                           | Curvas trazadas y ECE calculado por atributo. Los atributos peor calibrados están identificados.                                                                                              |
| F5.2   | **\[local\]** Aplicar calibración sobre el **split de calibración congelado en F2.12**, distinto del de entrenamiento y del de prueba. Comparar el ECE antes y después, reportado sobre prueba.                                                                                                             | Métodos de calibración post-hoc y por qué requieren un conjunto propio. Con un split de calibración reducido —lo habitual al partir en cuatro un subconjunto con cola larga— **la regresión isotónica sobreajusta**, porque es hambrienta de datos; el escalado de Platt pasa de alternativa a opción por defecto. La decisión del split determina el método. | ECE reducido de forma medible, reportado sobre prueba y no sobre calibración. La elección del método está justificada por el tamaño real del split.                                           |
| F5.3   | **\[local\]** Optimizar el umbral de aceptación **por atributo**, no global. Documentar el valor elegido y su criterio para cada uno.                                                                                                                                                                       | Por qué el umbral es una decisión de producto por atributo: el costo de un falso positivo no es igual en todos. Equivocar el color es visible para el cliente; equivocar la ocasión de uso, casi no. El referente académico optimizó un umbral de 0,48 para maximizar F1.                                                                                     | Un umbral por atributo con su justificación. El criterio de optimización está declarado y es el mismo para todos.                                                                             |
| F5.4   | **\[local\]** Trazar la curva cobertura-precisión: qué porcentaje del catálogo queda auto-etiquetado a cada nivel de precisión exigido, **solo para niveles A y B**.                                                                                                                                        | El compromiso central del producto: cuánta cobertura se sacrifica por cuánta confiabilidad. En nivel C no hay cobertura medible, solo precisión sobre muestra — de ahí la restricción.                                                                                                                                                                        | Curva trazada y punto de operación elegido marcado sobre ella, con la tasa de revisión manual que implica.                                                                                    |
| F5.5   | **\[local\]** Implementar la cola de revisión: las predicciones bajo umbral se encolan ordenadas por valor de información (cercanía al umbral, atributos de cola larga, baja concordancia entre pistas, violaciones de reglas ontológicas).                                                                 | Aprendizaje activo aplicado: no todas las revisiones humanas valen lo mismo, y priorizar los casos informativos hace que el mismo esfuerzo humano mejore más el modelo. Las violaciones ontológicas de F1.6 son un criterio de priorización que no necesita etiquetas.                                                                                        | La cola existe, está ordenada por un criterio explícito, y se puede exportar al formato de la herramienta de anotación.                                                                       |
| F5.6   | **\[local\]** Implementar **el mecanismo** de realimentación y probarlo con correcciones sintéticas: ingesta de correcciones, marcado de procedencia (corregido por humano / metadata original / adjudicado-retenido) y re-entrenamiento ejecutable. **No se ejecuta con datos reales aquí** — eso es F9.8. | Construir el mecanismo antes de tener los datos, y probarlo con datos sintéticos, es lo que permite que F5 cierre sin depender de una fase posterior. El marcado de procedencia es lo que hace posible, más tarde, medir si las correcciones ayudaron — y lo que impide que el conjunto retenido de F6 entre por descuido.                                    | Mecanismo implementado con tests sobre fixtures de F0.13. **Existe una marca de "retenido" y un test que verifica que un registro marcado así no puede entrar al conjunto de entrenamiento.** |
| F5.7   | **\[local\]** Medir la tasa de revisión manual resultante y traducirla a costo operativo: horas humanas por 1.000 SKU en régimen.                                                                                                                                                                           | El costo operativo de un sistema con intervención humana. Es la cifra que convierte la curva cobertura-precisión en un argumento económico comparable con el costo del etiquetado manual completo.                                                                                                                                                            | Tasa de revisión y horas por 1.000 SKU calculadas, comparadas contra la referencia de ≈3 minutos por producto del etiquetado manual.                                                          |

**F6 · Evaluación humana \[MVP\]**

Diez tareas. Es lo que separa un proyecto de visión por computador de un
proyecto de ciencia de datos aplicada, y la fase que más credibilidad
aporta por unidad de esfuerzo.

| **ID** | **Tarea — qué hacer**                                                                                                                                                                                                 | **Concepto que se practica**                                                                                                                                                                                                                                                                   | **Terminado cuando**                                                                                                                                                                 |
|--------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| F6.1   | **\[local\]** Redactar la guía de anotación: definición operativa de cada atributo, valores admitidos, casos límite resueltos, y ejemplos positivos y negativos por atributo.                                         | La guía es el instrumento de medición. Un desacuerdo entre anotadores puede venir del criterio de las personas o de la ambigüedad de la guía, y solo una guía explícita permite distinguirlos.                                                                                                 | docs/guia_anotacion.md versionada junto a la taxonomía, con al menos un caso límite resuelto por atributo fino.                                                                      |
| F6.2   | **\[local\]** Ejecutar un piloto sobre una muestra pequeña con todos los anotadores. Medir el acuerdo del piloto.                                                                                                     | Pilotaje del instrumento antes de gastar el esfuerzo principal. El acuerdo del piloto es un diagnóstico de la guía, no del modelo.                                                                                                                                                             | Piloto ejecutado y acuerdo calculado. Las ambigüedades detectadas están listadas.                                                                                                    |
| F6.3   | **\[local\]** Corregir la guía con lo aprendido en el piloto y registrar los cambios. No reutilizar las anotaciones del piloto en la muestra definitiva.                                                              | Por qué las anotaciones hechas con una versión anterior de la guía no son comparables con las posteriores. Versionado del instrumento de medición.                                                                                                                                             | Guía en versión 2 con registro de cambios; las anotaciones del piloto quedan marcadas como no utilizables para la métrica final.                                                     |
| F6.4   | **\[local\]** Diseñar el muestreo **estratificado por frecuencia de atributo y por dificultad estimada** (por ejemplo, baja confianza del modelo como proxy de dificultad).                                           | Por qué una muestra aleatoria no sirve aquí: contendría casi ningún ejemplo de la cola larga, que es exactamente donde el acuerdo por atributo importa más y donde quedaría incalculable.                                                                                                      | Criterio de estratificación escrito y muestra generada, con el conteo por estrato verificado.                                                                                        |
| F6.5   | **\[local\]** Dimensionar la muestra a partir de la precisión deseada del estimador de acuerdo, asegurando instancias suficientes por atributo.                                                                       | Cálculo de tamaño de muestra en función del error admisible del estimador, en lugar de elegir un número redondo. Por qué el acuerdo por atributo necesita su propio mínimo de instancias.                                                                                                      | Tamaño justificado con el cálculo escrito. **Queda fijado: no se amplía después aunque los resultados resulten interesantes.**                                                       |
| F6.6   | **\[local\]** Montar la anotación en la herramienta (Label Studio o equivalente) y ejecutarla con evaluadores independientes. **Criterio de moda requerido para los atributos finos.**                                | Diseño de una tarea de anotación: independencia entre anotadores, orden aleatorizado, y por qué un evaluador sin criterio de dominio produce ruido en lugar de desacuerdo informativo.                                                                                                         | Anotación completada por todos los evaluadores, de forma independiente y sin ver las predicciones del modelo.                                                                        |
| F6.7   | **\[local\]** Adjudicar los desacuerdos en una ronda documentada, registrando el criterio de resolución. **Marcar el conjunto resultante como retenido** con la marca implementada en F5.6.                           | Adjudicación como forma de construir un ground truth superior al de partida. Y la razón de la marca: este conjunto es el patrón oro de dos mediciones, así que entrenar sobre él las invalidaría. La tentación es real porque es el conjunto de mejor calidad del proyecto.                    | Conjunto adjudicado disponible y **marcado como retenido**; el test de F5.6 confirma que no puede entrar al entrenamiento; el criterio de resolución está registrado por desacuerdo. |
| F6.8   | **\[local\]** Calcular el acuerdo **con estadístico corregido por azar** (alfa de Krippendorff o kappa de Fleiss), por atributo y agregado, con intervalos. Reportar el porcentaje simple solo como cifra secundaria. | **Aquí copiar al referente académico sería un error.** Ellos usaron porcentaje simple y lo justificaron por tener 799 etiquetas posibles, donde el azar es despreciable. En moda, con ocho o diez valores por atributo, el acuerdo por azar es alto y el porcentaje simple infla el resultado. | Acuerdo humano-humano y humano-máquina calculados con estadístico corregido, por atributo, con intervalos. Ambas cifras se reportan siempre juntas.                                  |
| F6.9   | **\[local\]** Comparar el conjunto adjudicado contra la metadata original de H&M para **cuantificar su incompletitud**: atributos correctos que la metadata omite.                                                    | El hallazgo del referente académico convertido en medición propia: ellos observaron que los anotadores humanos anclaban en tres etiquetas (μ 3,54) mientras el modelo usaba 2–5 (μ 4,10), señal de un ground truth incompleto que castiga predicciones correctas.                              | Porcentaje de incompletitud medido en el propio dominio, con la implicación explícita sobre cuánto subestiman las métricas de nivel A del proyecto.                                  |
| F6.10  | **\[local\]** Verificar el criterio de éxito: que el acuerdo humano-máquina caiga dentro del intervalo de confianza del acuerdo humano-humano medido.                                                                 | Criterio relativo al techo de la tarea en lugar de absoluto. Un techo humano bajo hace fácil cumplir una brecha fija por la razón equivocada — de ahí que el criterio sea el intervalo y no los 10,4 puntos de otro dominio.                                                                   | Veredicto escrito contra el criterio congelado en F3.9, con las dos cifras y sus intervalos al lado.                                                                                 |

**F8 · Valor de negocio en recomendación \[MVP\]**

Trece tareas. **Se ejecuta aquí, inmediatamente después de F6**, aunque
su número sea mayor que el de F7: es la fase que sostiene la pregunta de
valor y la que diferencia el proyecto.

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<tbody>
<tr class="odd">
<td><p><strong>Recordatorio del diseño: H3 tiene dos mitades y la
segunda es la importante</strong></p>
<p>En H&amp;M la metadata está completa, así que un atributo predicho
desde la imagen es <strong>redundante</strong> con una columna que ya
existe. H3a (metadata completa) probablemente dé un efecto pequeño — no
porque el Smart Tagging no sirva, sino porque este dataset no tiene el
problema que resuelve. H3b enmascara metadata para simular producto de
proveedor sin ficha, y es ahí donde el sistema puede mostrar su
valor.</p></td>
</tr>
</tbody>
</table>

| **ID** | **Tarea — qué hacer**                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             | **Concepto que se practica**                                                                                                                                                                                                                                                                                                                                                                                                                                             | **Terminado cuando**                                                                                                                                                                                          |
|--------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| F8.1   | **\[local\]** **Congelar el protocolo completo antes de entrenar nada**, en un solo documento comiteado con fecha: definición de cold-start (cuántas interacciones y medidas a qué fecha), catálogo elegible en el periodo de evaluación, tratamiento de las compras ya observadas (se excluyen o no de las recomendaciones), estrategia de generación de candidatos, y el mecanismo de enmascaramiento de H3b — fracción, criterio de selección de artículos y campos suprimidos — **más la población sobre la que se evalúa MAP@12 en el régimen enmascarado**. | Cada una de estas decisiones mueve MAP@12 de forma material, y todas son negociables después de ver el resultado si no se fijan antes. Excluir o no lo ya comprado cambia la cifra; el corte de cold-start determina el segmento que sostiene H3a; y evaluar sobre todos los clientes o solo sobre los afectados por el enmascaramiento son dos números distintos. **Es una sola congelación porque dos congelaciones separadas invitan a hacer una y olvidar la otra.** | Documento en docs/decisions/protocolo_recomendacion.md, comiteado **antes de F8.2** y antes de cualquier construcción de features. Cada decisión tiene su valor y su justificación.                           |
| F8.2   | **\[local\]** Construir la matriz de interacciones cliente × artículo con DuckDB sobre Parquet, en formato disperso, sin cargar el histórico completo en memoria.                                                                                                                                                                                                                                                                                                                                                                                                 | Representación dispersa de interacciones implícitas. Por qué una matriz de interacciones nunca se materializa densa: el producto de dimensiones excede cualquier memoria razonable.                                                                                                                                                                                                                                                                                      | Matriz construida en formato disperso; uso de memoria medido; el proceso es repetible sin bloquear la máquina.                                                                                                |
| F8.3   | **\[local\]** Aplicar la partición **temporal** de F2.12 y escribir una verificación anti-fuga: comprobar programáticamente que ninguna feature del conjunto de entrenamiento se calcula con datos posteriores al corte.                                                                                                                                                                                                                                                                                                                                          | Fuga temporal, el error que más infla métricas de recomendación. La verificación automática existe porque la inspección visual de un pipeline de features no detecta este error de forma fiable.                                                                                                                                                                                                                                                                         | La verificación es un test que falla si se introduce a propósito una feature calculada con datos futuros.                                                                                                     |
| F8.4   | **\[local\]** Implementar MAP@12 y validarla contra casos construidos a mano con resultado conocido. Añadir Recall@12 y NDCG@12.                                                                                                                                                                                                                                                                                                                                                                                                                                  | Métricas de ranking: qué penaliza exactamente MAP y en qué difiere de Recall y de NDCG. Por qué la posición importa y cómo la promedia MAP. Es la métrica oficial del dataset, lo que hace el resultado contextualizable.                                                                                                                                                                                                                                                | Implementación con tests de casos conocidos. Un caso trivial (todas las recomendaciones correctas, en orden) da exactamente 1,0.                                                                              |
| F8.5   | **\[local\]** Línea base de popularidad reciente, segmentada (por ejemplo, por canal de venta o por grupo de edad).                                                                                                                                                                                                                                                                                                                                                                                                                                               | Por qué la popularidad reciente es sorprendentemente competitiva en retail con fuerte estacionalidad. Ignorarla lleva a sobrestimar el modelo propio, y es la comparación que un revisor pedirá primero.                                                                                                                                                                                                                                                                 | Evaluada con MAP@12 sobre la partición temporal. La cifra está registrada como referencia mínima.                                                                                                             |
| F8.6   | **\[local\]** Modelo de co-visitación ítem-ítem: co-ocurrencia de artículos en el historial de un mismo cliente.                                                                                                                                                                                                                                                                                                                                                                                                                                                  | Filtrado colaborativo sin factores latentes. Es rápido, robusto e interpretable, y suele ser una línea base más dura de lo que se espera.                                                                                                                                                                                                                                                                                                                                | Evaluado sobre los mismos splits; el tiempo de construcción registrado.                                                                                                                                       |
| F8.7   | **\[local\]** Factorización matricial para retroalimentación implícita (ALS y BPR) con la librería implicit, en CPU. **Este es el Modelo A — línea base.**                                                                                                                                                                                                                                                                                                                                                                                                        | Retroalimentación implícita frente a explícita: no hay calificaciones, solo compras, y la ausencia de compra no es una calificación negativa. Cómo ALS trata esa asimetría con pesos de confianza.                                                                                                                                                                                                                                                                       | Modelo A entrenado y evaluado; hiperparámetros ajustados en validación; tiempo de entrenamiento en CPU registrado.                                                                                            |
| F8.8   | **\[local\]** Arquitectura de dos etapas: generación de candidatos según la estrategia congelada en F8.1, y reordenamiento con gradient boosting (LightGBM) sobre features de cliente y artículo.                                                                                                                                                                                                                                                                                                                                                                 | Recuperación y reordenamiento, la arquitectura estándar en recomendación a escala. Por qué se separan: recuperar es barato y aproximado, reordenar es caro y preciso, y aplicarlo a todo el catálogo sería inviable.                                                                                                                                                                                                                                                     | Pipeline de dos etapas funcionando; tasa de acierto de la generación de candidatos medida por separado del reordenamiento.                                                                                    |
| F8.9   | **\[local\]** Construir las features de contenido: atributos generados por IA (con su confianza) y embeddings de imagen agregados por cliente e ítem. **Este es el Modelo B — enriquecido.**                                                                                                                                                                                                                                                                                                                                                                      | Ingeniería de features de contenido en recomendación. Cómo se agrega un embedding por cliente (promedio del historial, o ponderado por recencia) y por qué la elección de agregación importa más de lo que parece. Nota de orden: se construye **después** de F8.1, para que saber qué artículos van enmascarados no influya en el diseño de las features.                                                                                                               | Modelo B entrenado con las mismas particiones e hiperparámetros de búsqueda que el A, para que la comparación aísle el efecto de las features.                                                                |
| F8.10  | **\[local\]** Ablación **acumulativa**: solo colaborativo → + metadata original → + atributos IA → + embeddings → + ambos.                                                                                                                                                                                                                                                                                                                                                                                                                                        | Contribución incremental dada la configuración anterior. Responde: ¿vale la pena añadir esto sobre lo que ya tengo?                                                                                                                                                                                                                                                                                                                                                      | Cinco configuraciones evaluadas con la misma métrica y partición; tabla con la diferencia respecto al paso previo.                                                                                            |
| F8.11  | **\[local\]** Ablación **leave-one-out** desde el modelo completo: completo menos atributos IA, completo menos embeddings, completo menos metadata original.                                                                                                                                                                                                                                                                                                                                                                                                      | Contribución marginal dados **todos** los demás grupos de features. Es la pregunta correcta cuando las features son parcialmente redundantes entre sí, y la que la ablación acumulativa no puede responder porque confunde el efecto con el orden de entrada.                                                                                                                                                                                                            | Tres configuraciones evaluadas; la comparación entre ambas direcciones de ablación está interpretada por escrito.                                                                                             |
| F8.12  | **\[local\]** Ejecutar el régimen de metadata incompleta **según el mecanismo ya congelado en F8.1**, en tres configuraciones: metadata completa (referencia), enmascarada sin sustituto, y enmascarada con atributos IA como sustituto.                                                                                                                                                                                                                                                                                                                          | **Es la prueba de la hipótesis de negocio.** Si los atributos de IA recuperan parte del desempeño perdido, eso es evidencia directa de la propuesta de valor — evidencia que el régimen de metadata completa no puede producir por construcción.                                                                                                                                                                                                                         | Tres configuraciones evaluadas sobre la población declarada en F8.1; la fracción de desempeño recuperada está cuantificada con intervalo de confianza; el informe declara el enmascaramiento como simulación. |
| F8.13  | **\[local\]** Bootstrap sobre clientes para los intervalos; desagregación por cuantil de frecuencia de interacción de cliente y de artículo; desempeño en artículos nuevos según la definición de cold-start de F8.1. Redactar el informe del experimento.                                                                                                                                                                                                                                                                                                        | Por qué el bootstrap se hace **sobre clientes** y no sobre interacciones: la unidad de observación independiente es el cliente, y remuestrear interacciones subestima la varianza. Análisis de segmento para no esconder un efecto real detrás de un promedio.                                                                                                                                                                                                           | Informe con las diferencias A frente a B en ambos regímenes, con intervalos, desagregado por segmento, y el veredicto sobre H3a y H3b escrito por separado.                                                   |

**F7 · Búsqueda semántica \[EXT — primera extensión\]**

Ocho tareas. Se aborda con el MVP cerrado. Su costo real no está en el
índice vectorial sino en el protocolo de juicios de relevancia, que es
tiempo de persona y no de cómputo — y esa es precisamente la razón por
la que queda fuera del alcance comprometido.

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<tbody>
<tr class="odd">
<td><p><strong>Cambio respecto a la versión anterior</strong></p>
<p>El endpoint de búsqueda se movió de aquí a <strong>F9.4</strong>: su
condición de cierre referenciaba el contrato OpenAPI que nace en F9.2,
de modo que F7 dependía de una fase posterior. Y el protocolo de juicios
se equipara al de F6: si el protocolo importa para anotar atributos,
importa igual para juzgar relevancia. <strong>F7 cierra ahora con un
veredicto de medición, no con un servicio</strong> — una fase que
termina en una cifra es más fácil de dar por terminada que una que
termina en una API.</p></td>
</tr>
</tbody>
</table>

| **ID** | **Tarea — qué hacer**                                                                                                                                                                                                            | **Concepto que se practica**                                                                                                                                                                                                                                                                   | **Terminado cuando**                                                                                                                                             |
|--------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| F7.1   | **\[local\]** Construir el índice vectorial exacto sobre los embeddings cacheados y medir la latencia de búsqueda por fuerza bruta.                                                                                              | Similitud coseno sobre vectores normalizados y por qué la normalización convierte el producto punto en coseno. El exacto es la referencia de calidad contra la que se mide el aproximado.                                                                                                      | Índice exacto funcionando; latencia p50 y p95 medidas; los resultados sirven como verdad de recall para F7.2.                                                    |
| F7.2   | **\[local\]** Construir el índice aproximado (HNSW o IVF-PQ) y trazar la curva recall-latencia frente al exacto, barriendo los parámetros del índice.                                                                            | Búsqueda aproximada de vecinos cercanos: qué se sacrifica y cuánto se gana. El recall del índice es una métrica del índice, distinta del recall de la tarea — confundirlas es un error frecuente.                                                                                              | Curva recall-latencia trazada; el punto de operación elegido está justificado con la latencia objetivo de 300 ms p95.                                            |
| F7.3   | **\[local\]** Diseñar el conjunto de consultas en dos familias: atributos sueltos y lenguaje natural compuesto. **Redactadas como las teclearía un comprador, incluyendo términos que no existen en el vocabulario controlado.** | Cómo el diseño de las consultas determina el resultado: si todas usan palabras que ya están en los filtros de metadata, se mide el mejor caso del baseline y se oculta la ventaja real del sistema semántico.                                                                                  | Conjunto de consultas escrito, con la proporción de términos fuera de vocabulario declarada.                                                                     |
| F7.4   | **\[local\]** Redactar la **guía de relevancia** —escala, criterio por grado, casos límite resueltos— y correr un piloto con los evaluadores para ajustarla antes de la ronda definitiva.                                        | Tarea nueva. Un juicio de relevancia es tan dependiente del instrumento como una anotación de atributo: sin guía, dos personas juzgan cosas distintas y el desacuerdo no informa nada. Es el mismo razonamiento de F6.1 aplicado a recuperación.                                               | docs/guia_relevancia.md versionada; piloto ejecutado y guía corregida antes de juzgar el pool definitivo.                                                        |
| F7.5   | **\[local\]** Ejecutar ambos sistemas (semántico y filtros de metadata), unir los top-K en un pool común y **barajarlo eliminando toda marca de procedencia**.                                                                   | *Pooling* como técnica estándar de evaluación en recuperación de información. El barajado es el control que hace posible el juicio ciego.                                                                                                                                                      | Pool generado y barajado; verificado que no queda ninguna señal de qué sistema produjo cada resultado.                                                           |
| F7.6   | **\[local\]** Obtener los juicios de relevancia sobre el pool barajado con **dos o más evaluadores independientes**, y adjudicar los desacuerdos en una ronda documentada.                                                       | **Rompe la circularidad y además mide su propio instrumento.** Si la relevancia se define con reglas de metadata, el buscador por filtros compite contra su propia definición y puede acercarse al 100% por construcción. Y un solo evaluador no permite saber si su criterio es reproducible. | Juicios completados por todos los evaluadores de forma independiente; conjunto adjudicado disponible con el criterio de resolución registrado.                   |
| F7.7   | **\[local\]** Calcular el **acuerdo entre jueces** con estadístico corregido por azar, y reportarlo junto a las métricas de recuperación.                                                                                        | Tarea nueva, por la misma razón que F6.8: con una escala corta de relevancia el acuerdo por azar es alto y el porcentaje simple infla. Y sin acuerdo entre jueces no se sabe si una diferencia de NDCG entre sistemas es mayor o menor que el ruido del propio juicio humano.                  | Acuerdo calculado con intervalo. Está escrito si la diferencia observada entre sistemas supera el ruido del instrumento.                                         |
| F7.8   | **\[local\]** Calcular Precision@K, Recall@K, NDCG@K y MRR de ambos sistemas sobre los juicios adjudicados, desagregado por familia de consulta.                                                                                 | Métricas de recuperación con relevancia graduada: por qué NDCG admite grados de relevancia mientras precisión y recall los binarizan.                                                                                                                                                          | Comparación completa; la conclusión indica en qué familia de consulta gana cada sistema y por cuánto, con intervalos. **La fase cierra aquí, con el veredicto.** |

**F9 · Producto, servicio y MLOps \[EXT — primera extensión\]**

Once tareas. Convierte los resultados en un sistema que alguien podría
operar, y produce las cifras de costo que sostienen el argumento
económico.

| **ID** | **Tarea — qué hacer**                                                                                                                                                                                                                                                                                                             | **Concepto que se practica**                                                                                                                                                                                                                                                                                                 | **Terminado cuando**                                                                                                                                                                                |
|--------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| F9.1   | **\[local\]** Exportar el modelo elegido a ONNX y optimizarlo con OpenVINO. Verificar equivalencia numérica contra el original sobre un lote de prueba.                                                                                                                                                                           | Por qué un modelo exportado hay que **verificar** y no solo convertir: las diferencias de precisión numérica y de implementación de operadores pueden cambiar predicciones de forma silenciosa.                                                                                                                              | Modelo exportado; diferencia máxima de salidas contra el original medida y dentro de una tolerancia declarada.                                                                                      |
| F9.2   | **\[local\]** Implementar la API con FastAPI según el contrato de F0.10: atributos, confianza, nivel de evidencia, versión de taxonomía y versión de modelo en cada respuesta.                                                                                                                                                    | Diseño de API para inferencia: modos lote y unitario, validación de entrada, y por qué la respuesta lleva las versiones — sin ellas es imposible reconstruir después qué produjo una predicción concreta.                                                                                                                    | API respondiendo; contrato OpenAPI generado; la respuesta valida contra configs/output_schema.json.                                                                                                 |
| F9.3   | **\[local\]** Medir latencia (p50, p95) y throughput del servicio en el hardware propio, en lote y en unitario, con el modelo optimizado.                                                                                                                                                                                         | Caracterización de desempeño de un servicio frente a desempeño de un modelo: el segundo ignora serialización, preprocesamiento y espera. Es la diferencia entre la cifra del notebook y la cifra real.                                                                                                                       | Latencias y throughput registrados. **Cifra de segundos por imagen en una máquina sin GPU dedicada** — que es un argumento de producto en sí mismo.                                                 |
| F9.4   | **\[local\]** Exponer el endpoint de búsqueda (texto → productos e imagen → productos) sobre el índice elegido, integrado al contrato OpenAPI de F9.2. **Condicionada: solo si F7 está cerrada**; en caso contrario se expone únicamente similitud imagen → imagen, etiquetada como no evaluada.                                  | Tarea movida desde F7. Servir un índice vectorial: ciclo de vida del índice, cuándo se reconstruye y cómo se mantiene sincronizado con el catálogo. Y una distinción útil: **el índice es barato, la evaluación es cara** — se puede servir búsqueda sin haberla medido, siempre que se diga.                                | Endpoint funcionando con latencia dentro del objetivo y documentado en el contrato. Si F7 no está cerrada, la respuesta y la documentación declaran que la calidad no está evaluada.                |
| F9.5   | **\[local\]** Implementar las señales de deriva **sin etiquetas** del bucle rápido: distancia entre distribuciones de embeddings de entrada, desplazamiento de la distribución de predicciones y de confianza, volumen y composición de la cola, tasa fuera de taxonomía y **tasa de violaciones de reglas ontológicas** de F1.6. | **En producción no hay etiquetas, así que el F1 no es observable.** Estas señales no miden desempeño: detectan que algo cambió. La tasa de contradicciones ontológicas es especialmente valiosa porque es una señal de calidad que no necesita ground truth. Se reutiliza la distancia distribucional implementada en F2.10. | Señales calculadas sobre ventana móvil contra una distribución de referencia; umbrales de alerta declarados.                                                                                        |
| F9.6   | **\[local\]** Definir el protocolo de auditoría muestral del bucle lento: cadencia, tamaño de muestra e intervalo de confianza objetivo. **La muestra se extrae de la población completa, nunca de la cola de revisión.**                                                                                                         | Por qué la cola está sesgada por construcción hacia los casos difíciles: estimar F1 con ella subestima el desempeño y dispara reentrenamientos innecesarios. Son dos muestras con dos propósitos distintos.                                                                                                                  | Protocolo escrito con cadencia y tamaño justificados; el muestreo implementado extrae de la población y un test lo verifica.                                                                        |
| F9.7   | **\[local\]** Construir el dashboard: señales de deriva, histórico de F1 auditado con intervalos, tasa de revisión manual y throughput.                                                                                                                                                                                           | Observabilidad de un sistema de aprendizaje automático: qué se muestra en un panel y qué se deja en los logs. Mostrar el F1 auditado con su intervalo evita reaccionar ante ruido.                                                                                                                                           | Dashboard funcionando con datos reales del proyecto; el F1 aparece con intervalo y con la fecha de su auditoría.                                                                                    |
| F9.8   | **\[local\]** **Ejecutar** el ciclo de realimentación construido en F5.6: incorporar las correcciones reales de la cola de revisión, re-entrenar y medir si el desempeño mejoró. **Sin tocar el conjunto retenido de F6.7.**                                                                                                      | Tarea movida desde F5.6, donde no podía ejecutarse porque aún no existían correcciones. Sistemas que mejoran con el uso, y cómo se comprueba que efectivamente mejoraron: el marcado de procedencia de F5.6 permite atribuir la mejora a las correcciones y no al azar del reentrenamiento.                                  | Re-entrenamiento ejecutado con correcciones reales de la cola; efecto medido contra el modelo anterior con intervalo. **El test de retención confirma que ningún registro adjudicado de F6 entró.** |
| F9.9   | **\[local\]** Contenerizar el servicio con Docker y documentar el arranque desde cero.                                                                                                                                                                                                                                            | Reproducibilidad del entorno de ejecución, distinta de la reproducibilidad del experimento. Por qué el contenedor es lo que hace que "funciona en mi máquina" deje de ser una afirmación.                                                                                                                                    | El contenedor se construye y arranca desde un clon limpio siguiendo solo el README.                                                                                                                 |
| F9.10  | **\[local\]** Calcular el costo por 1.000 SKU: cómputo real más revisión humana residual, contra el costo del etiquetado manual equivalente.                                                                                                                                                                                      | Construcción de un caso económico con supuestos explícitos. La referencia de industria es ≈3 minutos por producto y ≈50 horas por 1.000; el cálculo propio debe ser comparable y declarar sus supuestos.                                                                                                                     | Cálculo con cada supuesto listado y su fuente. Las cifras propias y las de industria están claramente separadas.                                                                                    |
| F9.11  | **\[local\]** Redactar el documento de producto y monetización: módulos, unidades de cobro, integraciones y límites del sistema.                                                                                                                                                                                                  | Cómo se empaqueta un modelo como producto: suites y módulos adicionales, unidad de cobro alineada con la unidad de costo del cliente, y por qué la integración con el sistema de registro del cliente es la barrera real de adopción.                                                                                        | Documento escrito con los supuestos separados de los hechos verificados, y sin cifras de precio inventadas para el referente de mercado.                                                            |

**F10 · Cierre, comunicación y publicación \[MVP\]**

Seis tareas. Se ejecuta sobre el alcance que efectivamente se cerró, no
sobre el planeado: un alcance recortado y declarado es un proyecto
terminado; un alcance completo a medias no lo es.

| **ID** | **Tarea — qué hacer**                                                                                                                                                                                                                                                                                            | **Concepto que se practica**                                                                                                                                                                                                                                                                                                                                                                                                                                     | **Terminado cuando**                                                                                                                                                                                                  |
|--------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| F10.1  | **\[local\]** Redactar el informe técnico: metodología, resultados de cada experimento, análisis de errores, limitaciones y lo que quedó fuera.                                                                                                                                                                  | Comunicación técnica honesta: reportar el resultado nulo con la misma claridad que el positivo, y declarar las limitaciones antes de que las encuentre el lector. Es lo que distingue un informe de un folleto.                                                                                                                                                                                                                                                  | Un lector técnico puede replicar el resultado leyendo solo el informe y el repositorio.                                                                                                                               |
| F10.2  | **\[local\]** Escribir la *model card*: datos de entrenamiento y procedencia, desempeño por atributo y por nivel de evidencia, condiciones de degradación, sesgos conocidos y no medidos, usos no soportados.                                                                                                    | Documentación de modelo como práctica de responsabilidad. Declarar los sesgos **no medidos** es tan importante como reportar los medidos: afirmar equidad no medida es una afirmación sin respaldo.                                                                                                                                                                                                                                                              | *Model card* completa, incluida la sección de sesgos no medidos y la frontera explícita de que el sistema describe prendas y no personas.                                                                             |
| F10.3  | **\[local\]** Construir la demo con **catálogo propio**. Alcance del MVP: subir imagen → atributos con confianza y nivel de evidencia, más la vista de la cola de revisión de F5.5, más similitud imagen → imagen **etiquetada como no evaluada**. La **búsqueda por texto se incluye solo si F7 está cerrada**. | Corregido respecto a la versión anterior, que prometía búsqueda por texto siendo F7 una extensión. Y una distinción que amplía lo mostrable: el índice de similitud visual necesita solo los embeddings de F4.1, no el protocolo de juicios de F7. Se puede mostrar; hay que decir que no está medido, porque la pregunta "¿qué tan buena es?" llega sola.                                                                                                       | Demo funcionando sin una sola imagen de H&M ni archivo de imagen de Fashionpedia. Cada capacidad mostrada declara si su calidad fue evaluada o no. La procedencia de cada imagen del catálogo propio está registrada. |
| F10.4  | **\[local\]** Escribir el resumen ejecutivo de una página: qué se demostró, con qué evidencia, **qué no se demostró** y qué costaría llevarlo a producción. Citando solo métricas de nivel A.                                                                                                                    | Traducción de resultados técnicos a lenguaje de decisión. No convertir una mejora en MAP@12 en una afirmación sobre ventas, y no mezclar niveles de evidencia en el titular.                                                                                                                                                                                                                                                                                     | Una página. Un lector de negocio entiende el valor y los límites sin leer el informe técnico.                                                                                                                         |
| F10.5  | **\[local\]** Auditoría de publicación contra el contrato de F0.3, **archivo por archivo**: datos, embeddings, splits, pesos, salidas de notebooks y figuras de los informes. Recorrer también el histórico de Git.                                                                                              | Verificación frente a confianza. Las figuras generadas y las salidas de notebooks pueden contener imágenes de producto: son vectores de redistribución tan reales como un CSV, y el .gitignore no los cubre.                                                                                                                                                                                                                                                     | Checklist firmado. git log recorrido en busca de archivos de datos comiteados por error en cualquier punto del histórico, no solo en el estado actual.                                                                |
| F10.6  | **\[local\]** Publicar el repositorio con README, data/README.md con las instrucciones de obtención, atribución CC BY 4.0 a Fashionpedia, LICENSE permisiva OSI y la cláusula de H&M citada. **Publicar además un enlace al repositorio en el foro de la competencia en Kaggle, o un notebook que apunte a él.** | Reproducibilidad **por instrucción** cuando la reproducibilidad por datos está prohibida: el README debe permitir que un tercero reconstruya el proyecto obteniendo los datos por su cuenta, y los fixtures de F0.13 le permiten al menos correr los tests sin obtenerlos. El enlace en Kaggle cumple la sección 8.B, que obliga a compartir en la competencia el código que se comparte públicamente; la lectura es ambigua pero el costo de cumplirla es nulo. | Un tercero con acceso a los datasets puede reproducir el proyecto siguiendo solo el README. La atribución, el LICENSE y la cláusula están visibles. El enlace está publicado en Kaggle.                               |

**Tablero de seguimiento**

Conteo por fase, para marcar avance. El alcance comprometido suma **92
tareas** (F0–F6, F8 y el cierre F10); las extensiones F7 y F9 suman 19.
Total: 111.

| **Fase**                           | **Bloque** | **Tareas** | **Entregable principal**                                                                      | **Avance** |
|------------------------------------|------------|------------|-----------------------------------------------------------------------------------------------|------------|
| F0 · Encuadre, licencias y entorno | MVP        | 13         | Licencias literales, contrato de publicación, manifiesto de datos, repositorio, CI y fixtures | ☐          |
| F1 · Taxonomía y ontología         | MVP        | 10         | taxonomy.yaml con niveles, mapeo de valores y reglas ontológicas                              | ☐          |
| F2 · Datos, EDA y splits           | MVP        | 14         | Pipeline con puerta de validación y cuatro splits congelados por grupo                        | ☐          |
| F3 · Línea base                    | MVP        | 9          | Tabla de línea base, sonda de fuga y umbrales congelados                                      | ☐          |
| F4 · Modelo de tagging             | MVP        | 10         | Modelo registrado y tabla comparativa con costo                                               | ☐          |
| F5 · Calibración y revisión humana | MVP        | 7          | Umbrales por atributo, cola de revisión y mecanismo de realimentación                         | ☐          |
| F6 · Evaluación humana             | MVP        | 10         | Acuerdo corregido por azar e incompletitud medida                                             | ☐          |
| F8 · Valor de negocio              | MVP        | 13         | Protocolo congelado y veredicto sobre H3a y H3b con intervalos                                | ☐          |
| F7 · Búsqueda semántica            | EXT        | 8          | Comparación sobre juicios adjudicados con acuerdo entre jueces                                | ☐          |
| F9 · Producto y MLOps              | EXT        | 11         | Servicio, monitoreo sin etiquetas, realimentación ejecutada y costo por 1.000 SKU             | ☐          |
| F10 · Cierre y publicación         | MVP        | 6          | Informe, model card, demo y repositorio público                                               | ☐          |

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<tbody>
<tr class="odd">
<td><p><strong>Los seis puntos de no retorno</strong></p>
<p>Tareas que, una vez cerradas, no deberían reabrirse — y que por eso
merecen más cuidado que el resto:</p>
<p><strong>F1.4</strong> (mapeo de valores): define qué cuenta como
acierto. Cambiarlo después hace negociable la métrica.</p>
<p><strong>F2.7 antes de F2.12</strong> (grupos de variantes antes de
partir): si se detecta la fuga visual después de congelar, hay que
rehacer todo lo que dependa de los splits.</p>
<p><strong>F2.12</strong> (congelar los cuatro splits): reabrirlo
invalida toda comparación posterior.</p>
<p><strong>F3.9</strong> (congelar umbrales): reabrirlo después de ver
un resultado convierte el criterio en racionalización.</p>
<p><strong>F6.5</strong> (dimensionar la muestra de anotación):
ampliarla a mitad del ejercicio sesga el estimador de acuerdo.</p>
<p><strong>F8.1</strong> (congelar el protocolo de recomendación,
enmascaramiento incluido): definirlo después de ver el resultado
convierte la simulación en un ajuste a conveniencia.</p></td>
</tr>
</tbody>
</table>

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<tbody>
<tr class="odd">
<td><p><strong>Y una regla que no es una tarea</strong></p>
<p>El conjunto adjudicado de <strong>F6.7 nunca entra al
entrenamiento.</strong> Es el patrón oro del acuerdo humano-máquina y de
la medición de incompletitud de la metadata; entrenar sobre él infla
ambas y destruye el único ground truth de calidad superior que el
proyecto produce. La tentación es real porque es precisamente el
conjunto mejor etiquetado que existirá. El control está implementado en
F5.6 como marca de retención con test, y se verifica de nuevo en
F9.8.</p></td>
</tr>
</tbody>
</table>

**Revisión de la estructura de repositorio propuesta**

Veredicto breve antes del detalle: **la estructura propuesta está por
encima de lo habitual en proyectos de portafolio y las decisiones de
fondo son correctas.** No es una carpeta de notebooks con un
requirements.txt, que es lo que suele encontrarse; es un paquete
instalable con configuración externalizada, datos fuera de Git y tests.
Lo que falta no son correcciones de rumbo sino piezas que completan la
columna vertebral de reproducibilidad, más un control específico que la
licencia de este proyecto vuelve obligatorio.

**Lo que está bien decidido, y por qué**

| **Decisión**                                      | **Por qué es correcta**                                                                                                                                                                                                                                                                                                                                                                                 |
|---------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| src/smart_tagging/ en lugar de paquete en la raíz | Es el *src-layout*, y su ventaja no es estética: impide importar el paquete accidentalmente desde el directorio de trabajo. Eso fuerza a que el código funcione **instalado**, que es la única forma de saber que el pyproject.toml está bien y que no hay dependencias implícitas del directorio actual. Mucha gente descubre que su paquete estaba roto el día que intenta usarlo desde otra carpeta. |
| Separación notebooks/ y src/                      | Es la disciplina más importante del repositorio. Los notebooks narran y exploran; el código vive en src/ y los notebooks lo importan. Sin esta separación, la lógica queda atrapada en celdas, no se puede testear y no se puede reutilizar entre notebooks.                                                                                                                                            |
| taxonomy.yaml dentro de configs/                  | Coincide exactamente con la decisión de arquitectura del plan: la taxonomía es la capa cero y un artefacto versionado **independiente del código**. Si viviera incrustada en Python, cada cambio de temporada exigiría un cambio de código y se perdería la comparabilidad histórica.                                                                                                                   |
| configs/experiments/                              | Externalizar la configuración de experimentos es lo que permite reproducir una corrida sin editar código, y lo que hace que el registro de MLflow sea interpretable meses después.                                                                                                                                                                                                                      |
| data/ excluido de Git                             | En este proyecto no es una buena práctica, es un **requisito de licencia**. La cláusula de H&M prohíbe redistribuir los datos, y un repositorio público con un CSV dentro es redistribución.                                                                                                                                                                                                            |
| tests/ existe                                     | Es lo que más distingue este esqueleto del promedio. La mayoría de proyectos de portafolio no tienen tests, y su ausencia es lo primero que nota un revisor técnico. Le falta una pieza para ser completo: tests/fixtures/ con datos sintéticos públicos (tarea F0.13), sin los cuales **CI no puede probar nada que toque datos**, que es casi todo el pipeline.                                       |
| pyproject.toml                                    | Estándar actual de empaquetado, con metadatos, dependencias y configuración de herramientas en un solo archivo.                                                                                                                                                                                                                                                                                         |

**Lo que falta, en orden de importancia**

**1. El control que la licencia vuelve obligatorio: limpiar las salidas
de los notebooks**

Esta es la observación más importante de la revisión, y es específica de
este proyecto. Un archivo .ipynb guarda **las salidas de las celdas
dentro del propio archivo**, y una imagen renderizada se almacena como
base64 incrustado. Por lo tanto:

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<tbody>
<tr class="odd">
<td><p><strong>La trampa</strong></p>
<p>Un notebook que muestra una cuadrícula de imágenes de producto de
H&amp;M y se comitea <strong>lleva esas imágenes dentro del
`.ipynb`</strong>. El .gitignore no lo cubre, porque el .ipynb no es un
archivo de datos: es código que hay que versionar. El resultado es un
repositorio público que redistribuye datos restringidos sin que nadie lo
note, y que además queda en el histórico de Git aunque después se
borre.</p>
<p>La misma trampa aplica a reports/: una figura PNG generada que
contenga recortes de producto es un vector de redistribución tan real
como un CSV.</p></td>
</tr>
</tbody>
</table>

La solución es un hook de nbstripout en pre-commit (tarea F0.4) más la
auditoría del histórico en F10.5. Es barato de instalar y no tiene
sustituto: la disciplina manual de "limpiar antes de comitear" falla la
primera vez que se comitea con prisa.

**1b. Y el \`.gitignore\` no puede escribirse con globs globales de
extensión**

Corolario del punto anterior, y un error fácil de cometer al traducir el
contrato de publicación a reglas: ignorar \*.png y \*.jpg de forma
global **bloquea los propios entregables** — las figuras publicables de
reports/figures/, las imágenes del catálogo propio de la demo y
cualquier imagen de docs/.

Hay además una trampa de semántica de Git que conviene conocer antes de
escribir la primera regla: **Git no desciende a un directorio
excluido**, así que una negación dentro de él nunca se evalúa. Esto
significa que data/ a secas hace imposible versionar data/README.md, que
es justamente el archivo que sustituye a no poder redistribuir los
datos:

\# INCORRECTO — la negación nunca se evalúa

data/

!data/README.md \# inútil: Git no entró al directorio

\# CORRECTO — se excluyen los hijos, no el directorio

data/\*

!data/README.md

!data/.gitkeep

artifacts/\*

!artifacts/.gitkeep

\# Patrones de datos acotados por ruta, no globales

data/\*\*/\*.csv

data/\*\*/\*.parquet

artifacts/\*\*/\*.npy

models/\*\*/\*.pt

\# reports/figures/, docs/ y los activos de la demo NO se ignoran

**2. La columna de reproducibilidad está incompleta**

El plan exige que el pipeline corra de punta a punta con un comando. En
la estructura propuesta **no hay un lugar donde eso viva**. Faltan tres
piezas:

- dvc.yaml y params.yaml (o un Makefile) — la definición del pipeline
  con dependencias declaradas. Sin esto, "reproducible" es una
  intención. Con esto, modificar un paso intermedio re-ejecuta solo lo
  que depende de él, que es lo que hace soportable iterar con cómputo
  limitado.

- **Un archivo de bloqueo de dependencias** (uv.lock, poetry.lock o un
  requirements.lock generado). El pyproject.toml declara rangos; el lock
  fija versiones exactas. Sin lock, el proyecto se reproduce distinto en
  seis meses y no se sabe por qué.

- seeds.py o equivalente — el manejo centralizado de semillas. Es una
  decisión de diseño, no un detalle: si cada notebook fija su semilla a
  su manera, dos corridas del mismo experimento no son comparables.

**3. Falta el hogar del caché de embeddings — y su convención de
nombres**

El plan declara el caché de embeddings como infraestructura crítica: se
calcula una vez en la nube y todo el trabajo local se apoya en él. En la
estructura propuesta no tiene carpeta. Necesita artifacts/ (excluido de
Git, igual que data/), y algo más importante que la carpeta: **una
convención de nombres que codifique modelo, versión del modelo, split y
hash del dataset**.

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<tbody>
<tr class="odd">
<td><p><strong>Por qué el nombre del caché es una decisión de
diseño</strong></p>
<p>Un caché mal nombrado se reutiliza con el modelo equivocado. Y ese
error <strong>no produce un fallo</strong>: produce un resultado. Se
entrena una cabeza lineal sobre embeddings de otro modelo, la métrica
sale distinta, y se atribuye la diferencia al cambio de hiperparámetro
que se acababa de hacer. Es una de las formas más difíciles de depurar
un experimento, porque nada se rompe.</p></td>
</tr>
</tbody>
</table>

**4. \`reports/\` mezcla dos cosas que deben estar separadas**

reports/ sirve para dos propósitos incompatibles: documentación escrita
a mano (licencias, diccionario de datos, guía de anotación, *model
card*, decisiones de arquitectura) y salidas generadas por código
(figuras, tablas de métricas). Si comparten carpeta, una ejecución del
pipeline puede sobrescribir prosa que costó horas escribir. La
separación correcta es:

- docs/ — prosa versionada, escrita a mano. Nunca la toca un script.

- reports/figures/ y reports/metrics/ — generado por código,
  reproducible, y por tanto desechable.

**5. Faltan módulos que el plan trata como de primera clase**

| **Módulo a añadir** | **Por qué no puede quedar dentro de otro**                                                                                                                                                                 |
|---------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| taxonomy/           | Es la capa cero de la arquitectura: carga, validación, consulta por nivel de evidencia y resolución de versión. Enterrarlo en utils/ contradice la decisión de que la taxonomía es un artefacto gobernado. |
| data/provenance.py  | La matriz de control de fuga debe ser **código ejecutable con tests** (tarea F2.10), no un documento. Su función es hacer imposible construir un conjunto de entrada que incluya un campo bloqueado.       |
| calibration/        | Calibración, umbrales por atributo y curva cobertura-precisión son un bloque con identidad propia, y es el bloque del que depende el mecanismo de revisión humana.                                         |
| recommender/        | El recomendador es una familia de modelos distinta del etiquetador — factorización matricial y reordenamiento frente a clasificación multi-etiqueta. Compartir models/ los mezcla sin ningún beneficio.    |
| serving/            | La API y la lógica de inferencia optimizada (ONNX/OpenVINO) son código de producción con dependencias propias. Conviene poder instalar el paquete sin arrastrarlas.                                        |

**6. \`utils/\` es la única decisión que cuestionaría de frente**

utils/ se convierte, en todo proyecto y sin excepción, en el vertedero
donde acaba lo que no se supo dónde poner. Al sexto mes contiene veinte
funciones sin relación entre sí y nadie se atreve a tocarlo porque no se
sabe quién las usa. La alternativa cuesta lo mismo y envejece mucho
mejor: **módulos con nombre específico** en la raíz del paquete — io.py,
logging.py, seeds.py, paths.py. Si una función no encaja en ninguno, eso
es la señal de que falta un módulo con nombre propio, no de que sobre un
cajón.

**7. Dos ajustes en \`notebooks/\`**

**El primero es de orden.** La secuencia propuesta pone 01_eda_hm antes
de 02_taxonomia_y_mapeo, y el plan pide taxonomía antes de datos. La
contradicción es solo aparente y se resuelve partiendo el EDA en dos: la
taxonomía necesita el **inventario de esquema** (qué campos hay, de qué
tipo, con qué cardinalidad), que es barato; el EDA de **distribuciones**
necesita la taxonomía, porque las distribuciones se analizan agrupadas
por atributo. De ahí el orden propuesto abajo.

**El segundo es de cobertura.** La lista termina en
04_evaluacion_modelo, y deja sin notebook las tres piezas que más peso
tienen en el resultado final: la evaluación humana (F6), el experimento
de recomendación (F8, que está en el MVP y es el diferenciador del
proyecto) y la búsqueda semántica (F7).

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<tbody>
<tr class="odd">
<td><p><strong>La regla que hace funcionar la frontera notebook /
código</strong></p>
<p>Un notebook puede contener narrativa, gráficas y llamadas a
funciones. <strong>En el momento en que una celda define una función que
se usa dos veces, esa función se muda a `src/`.</strong> Es la regla
operativa concreta detrás de la separación de carpetas, y sin ella la
separación existe en el árbol de directorios pero no en la
práctica.</p></td>
</tr>
</tbody>
</table>

**8. Piezas menores que suman más de lo que cuestan**

- .github/workflows/ci.yml — ejecutar tests y linter en cada push. Son
  veinte líneas y es lo que hace que un repositorio se lea como
  profesional.

- data/README.md — cómo obtener los datos, dado que no se pueden
  redistribuir. Es el sustituto de incluirlos: convierte el repositorio
  en reproducible **por instrucción** cuando no puede serlo por datos.
  En este proyecto no es opcional.

- .env.example — si se usa una API externa para el modelo generativo,
  con la clave real fuera de Git.

- docs/decisions/ — registros de decisión de arquitectura, breves. Es
  donde viven las decisiones que después nadie recuerda por qué se
  tomaron, como el nivel de evidencia de un atributo o el criterio de
  muestreo.

- tests/fixtures/ — datos sintéticos públicos que imitan la estructura
  de las fuentes reales. Rinde dos veces: permite que CI pruebe el
  pipeline sin tocar datos restringidos, y al ser publicables permiten
  que un tercero ejecute la suite sin obtener H&M.

- docs/backlog.yaml — el backlog como dato validable, no como prosa. Ver
  la sección siguiente.

**9. El backlog pertenece al repositorio, no solo al documento**

Con más de cien tareas, un documento de Word sirve para entender el
razonamiento pero no para trabajar. Y hay tres atributos por tarea que
la tabla del documento no puede alojar sin volverse ilegible: de qué
tareas depende, qué artefactos produce y dónde se registra su cierre. La
salida no es una tabla más ancha — el ancho de página no da — sino
**sacar el backlog de Word**.

Un docs/backlog.yaml con una entrada por tarea (id, fase, bloque, modo,
depends_on, outputs, dod) vive donde ocurre el trabajo y, sobre todo,
**puede validarse**. El test que lo acompaña comprueba tres invariantes
que a mano se pasan por alto:

- Que el grafo de dependencias **no tenga ciclos**.

- Que todo artefacto declarado como entrada **tenga alguna tarea que lo
  produzca**.

- Que **ninguna tarea dependa de una fase posterior** a la suya.

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<tbody>
<tr class="odd">
<td><p><strong>Ese test habría encontrado tres de los defectos de la
versión 1.0 de este backlog</strong></p>
<p>La primera versión tenía tres inconsistencias de dependencia que la
lectura humana de la tabla no detectó: F5.2 exigía un conjunto de
calibración que F2.9 no creaba; F5.6 pedía correcciones humanas que en
F5 no existían; y la condición de cierre de F7.7 referenciaba un
contrato OpenAPI que nace en F9.2. Las tres son violaciones del grafo y
una validación automática las marca en segundos.</p>
<p>Es el mismo principio que el proyecto ya aplica a la taxonomía y a la
matriz de procedencia: <strong>lo que puede ser dato validado no se deja
en prosa confiada.</strong> Y tiene un beneficio adicional: el
backlog.yaml puede <strong>generar</strong> la tabla del documento en
lugar de duplicarla, de modo que las dos nunca se
desincronizan.</p></td>
</tr>
</tbody>
</table>

**Estructura propuesta**

Las adiciones respecto a la propuesta original están marcadas con ◀.

smart-tagging/

├── notebooks/

│ ├── 00_setup_y_licencias.ipynb

│ ├── 01_inventario_esquema.ipynb ◀ separado del EDA

│ ├── 02_taxonomia_y_mapeo.ipynb

│ ├── 03_eda_distribuciones.ipynb ◀ requiere la taxonomía

│ ├── 04_lineas_base.ipynb

│ ├── 05_modelo_tagging.ipynb ◀

│ ├── 06_calibracion_y_umbrales.ipynb ◀

│ ├── 07_evaluacion_humana.ipynb ◀

│ ├── 08_recomendacion_y_valor.ipynb ◀ el diferenciador

│ └── 09_busqueda_semantica.ipynb ◀ extensión

├── src/smart_tagging/

│ ├── taxonomy/ ◀ capa cero

│ ├── data/

│ │ ├── ingest.py

│ │ ├── splits.py

│ │ └── provenance.py ◀ control de fuga

│ ├── features/

│ ├── models/

│ ├── calibration/ ◀

│ ├── recommender/ ◀

│ ├── evaluation/

│ ├── serving/ ◀

│ ├── io.py ◀ en vez de utils/

│ ├── paths.py ◀

│ ├── logging.py ◀

│ └── seeds.py ◀

├── configs/

│ ├── taxonomy.yaml

│ ├── mapping_fashionpedia_hm.yaml ◀

│ ├── output_schema.json ◀ contrato de salida

│ ├── mapping_valores.yaml ◀ mapeo nivel valor

│ ├── success_criteria.yaml ◀ umbrales congelados

│ └── experiments/

├── tests/

│ └── fixtures/ ◀ datos sintéticos

├── docs/ ◀ prosa versionada

│ ├── licencias.md ◀ cláusula literal

│ ├── diccionario_datos.md ◀

│ ├── guia_anotacion.md ◀

│ ├── taxonomy_changelog.md ◀

│ ├── model_card.md ◀

│ ├── manifiesto_datos.md ◀ linaje de descargas

│ ├── guia_anotacion.md ◀

│ ├── backlog.yaml ◀ backlog validable

│ └── decisions/ ◀ ADRs breves

├── reports/

│ ├── figures/ ◀ generado

│ └── metrics/ ◀ generado

├── data/ \# excluido de Git

│ ├── raw/ interim/ processed/ external/ ◀ bronze→silver→gold

│ └── README.md ◀ cómo obtener los datos

├── artifacts/ \# excluido de Git

│ └── embeddings/ ◀ caché, nombres con hash

├── .github/workflows/ci.yml ◀

├── dvc.yaml ◀ pipeline con un comando

├── params.yaml ◀

├── uv.lock (o poetry.lock) ◀ versiones exactas

├── .pre-commit-config.yaml ◀ incluye nbstripout

├── .env.example ◀

├── pyproject.toml

├── README.md

└── .gitignore

**Conclusión sobre el enfoque**

La estructura propuesta acierta en lo que decide el resultado: paquete
instalable, configuración fuera del código, taxonomía como archivo
versionado, datos fuera de Git y tests presentes desde el principio. Eso
ya es un enfoque de nivel profesional, y las adiciones de esta revisión
no cambian ninguna de esas decisiones — las completan.

Si hubiera que quedarse con tres cosas de toda la revisión, serían
estas: **limpiar las salidas de los notebooks** porque en este proyecto
es un requisito de licencia y no una preferencia de higiene; **definir
el pipeline en un archivo** para que la reproducibilidad sea verificable
y no declarativa; y **nombrar el caché de embeddings con el hash de lo
que lo produjo**, porque el error que evita es de los que no se
manifiestan como fallo sino como un resultado creíble y equivocado.

Y un comentario final sobre la forma de abordar el proyecto, más allá
del árbol de carpetas: el orden en que están pensadas las carpetas
revela un criterio correcto — primero el encuadre y la configuración,
después los datos, y solo al final los modelos. Es el mismo orden del
plan y el inverso al que sugiere el entusiasmo. Mantenerlo cuando llegue
la tentación de saltar directo a F4 es, en la práctica, la diferencia
entre un proyecto que se puede defender y una demo que funciona una vez.
