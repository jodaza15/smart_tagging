**PLAN DE PROYECTO DE CIENCIA DE DATOS**

**Sistema de Smart Tagging con IA**

para catálogos de Ecommerce de moda

*Vitrina técnica end-to-end construida sobre datasets públicos, con la
estructura de un proyecto de ciencia de datos de una compañía retail:
del caso de negocio y la taxonomía de atributos, al modelo multimodal,
la búsqueda semántica, la medición del valor en recomendación y el
empaquetado como producto.*

| **Campo**           | **Detalle**                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
|---------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Documento           | Planeación técnica y de negocio — **versión 1.2**                                                                                                                                                                                                                                                                                                                                                                                                                              |
| Dominio             | Retail / Ecommerce de moda — Product Data & Content Intelligence                                                                                                                                                                                                                                                                                                                                                                                                               |
| Fecha               | 12 de septiembre de 2026                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| Naturaleza          | Demostrador (showcase) con datos públicos de uso no comercial y educativo; no producción con datos propietarios                                                                                                                                                                                                                                                                                                                                                                |
| Alcance del plan    | Objetivo general, objetivos específicos, arquitectura, fuentes de datos, modelos, métricas, fases, riesgos y gobierno                                                                                                                                                                                                                                                                                                                                                          |
| Cambios v1.1        | Licencias de H&M y Fashionpedia definidas (7.3 y 7.4, con estrategia de publicación). Cómputo definido: hardware sin GPU dedicada, plan híbrido local + nube gratuita (sección 12).                                                                                                                                                                                                                                                                                            |
| Cambios v1.2        | Revisión crítica de debilidades metodológicas. Nuevo: niveles de evidencia de atributos (7.6), matriz de procedencia y control de fuga (7.7), monitoreo sin etiquetas (10.5), frontera de MVP (13.2). Reformulado: H3 con régimen de metadata incompleta (5.3), acuerdo humano-máquina con estadístico corregido por azar (10.2), criterios de éxito con congelación previa (11), línea base como método local y no como comparación de cifras entre publicaciones (9.1 y 11). |
| Fuentes de sustento | Salminen et al. (2019); Sharma & Karnick (2016); Pixyle.ai (plataforma y blog); Browntape; documento interno de sugerencia de proyecto                                                                                                                                                                                                                                                                                                                                         |

**Contenido**

**1. Resumen ejecutivo**

**2. Contexto y caso de negocio**

> *El problema operativo · la consecuencia comercial · tres hallazgos
> académicos que cambian el diseño*

**3. Objetivo general**

**4. Objetivos específicos (OE1–OE7)**

**5. Preguntas de investigación e hipótesis**

> *Experimento 1: exactitud · Experimento 2: descubrimiento semántico ·
> Experimento 3: valor de negocio*

**6. Alcance — dentro y fuera**

**7. Fuentes de datos**

> *Arquitectura de fuentes · candidatas · licencias · estrategia de
> publicación · domain shift · niveles de evidencia · matriz de
> procedencia*

**8. Arquitectura técnica**

> *Diagrama de capas · decisiones y justificación · stack tecnológico*

**9. Modelos**

> *Tagging (L0–L5) · búsqueda semántica · recomendación*

**10. Métricas**

> *Calidad del tagging · acuerdo humano-máquina · descubrimiento y
> recomendación · operativas y de negocio · monitoreo sin etiquetas*

**11. Criterios de éxito del proyecto**

**12. Cómputo: hardware disponible y estrategia híbrida**

**13. Fases, entregables y definición de terminado (F0–F10)**

> *Fases y criterio de cierre · frontera del MVP y extensiones
> condicionadas*

**14. Riesgos y mitigaciones**

**15. Gobierno de datos, ética y documentación**

**16. Empaquetado y monetización: benchmark de mercado**

**17. Referencias**

**A. Apéndice — Estado de verificación: resuelto, definido y abierto**

**1. Resumen ejecutivo**

El proyecto construye un **sistema de Smart Tagging** para un catálogo
de ecommerce de moda: un servicio que recibe la imagen de un producto (y
su texto cuando existe) y devuelve **atributos estructurados sobre una
taxonomía controlada** — categoría de prenda, color, patrón, silueta,
detalles de construcción, material aparente, ocasión de uso — con una
puntuación de confianza por atributo.

La diferencia frente a un ejercicio de clasificación de imágenes es que
el proyecto **no termina en la métrica del modelo**. Se estructura en
tres experimentos encadenados que responden tres preguntas de negocio
distintas:

1.  Calidad: ¿puede la IA etiquetar el catálogo con precisión comparable
    a la de un anotador humano?

2.  Descubrimiento: ¿los atributos generados por IA permiten encontrar
    productos mejor que la metadata tradicional?

3.  Valor: ¿enriquecer un sistema de recomendación con esos atributos
    mejora su desempeño frente a una línea base sin ellos?

La respuesta a la tercera pregunta es la que convierte el proyecto en
una vitrina profesional: el resultado a comunicar no es *"afiné un
modelo y obtuve 91% de accuracy"*, sino *"añadir atributos visuales
generados por IA mejoró MAP@12 en X%, con el mayor efecto en productos y
clientes con interacción histórica escasa"*.

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<tbody>
<tr class="odd">
<td><p><strong>Delimitación honesta del alcance de las
conclusiones</strong></p>
<p>Los datasets públicos disponibles contienen transacciones, no
exposición: no hay impresiones ni clickstream. Por lo tanto el proyecto
<strong>no podrá afirmar un incremento causal en CTR, tasa de conversión
o ventas</strong>; solo podrá demostrar mejora en desempeño de
recomendación y de recuperación de información, más un ahorro operativo
estimado en horas de anotación. Esta delimitación se declara desde la
planeación y debe mantenerse en toda comunicación de
resultados.</p></td>
</tr>
</tbody>
</table>

El sustento metodológico proviene de los dos trabajos académicos del
folder del proyecto — uno sobre auto-tagging multi-etiqueta de contenido
con evaluación de acuerdo humano-máquina (Salminen et al., 2019,
*Journal of Business Research*) y otro sobre tagging automático de
productos de ecommerce por características visuales (Sharma & Karnick,
2016, NAACL-HLT) — y el sustento de producto proviene del benchmarking
de **Pixyle.ai**, compañía cuyo negocio completo es exactamente este
servicio, complementado con las recomendaciones de implementación de
**Browntape**.

**2. Contexto y caso de negocio**

**2.1 El problema operativo: el catálogo mal etiquetado**

El etiquetado manual de catálogo falla por tres razones documentadas de
forma consistente en la industria y en la literatura:

| **Falla**                     | **Evidencia documentada**                                                                                                                                                                                            | **Fuente**                                      |
|-------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-------------------------------------------------|
| Costo y tiempo                | ≈3 minutos por producto para un anotador; 1.000 productos ≈ 50 horas. A USD 20/hora, ≈USD 1.000 por lote de 1.000 SKU. Pixyle cuantifica el desperdicio en 20–40 h por cada 1.000 SKU.                               | Pixyle.ai (plataforma y blog)                   |
| Inconsistencia y error humano | "No todos etiquetan la misma imagen con los mismos tags", lo que genera discrepancia en los tags asignados y excluye resultados útiles de la búsqueda. El proceso es falible y las taxonomías cambian con el tiempo. | Sharma & Karnick (2016); Salminen et al. (2019) |
| Escalabilidad                 | Manejable en inventarios pequeños, impracticable al crecer el volumen. En el caso estudiado por Salminen et al., 8.651 de 21.709 páginas (39,8%) permanecían sin clasificar.                                         | Browntape; Salminen et al. (2019)               |

**2.2 La consecuencia comercial**

El atributo faltante no es un problema de datos: es un producto que el
cliente no encuentra. Browntape reporta que **75%** de los consumidores
abandona la compra tras una experiencia de búsqueda decepcionante,
**48%** acude a un competidor tras una búsqueda infructuosa y **85%**
registra daño en la percepción de marca tras una búsqueda fallida — en
un contexto donde el tiempo medio de permanencia en una página es de
**54 segundos**.

Del lado del beneficio, Pixyle reporta para su plataforma **95%** de
incremento de productividad, **8–12%** de uplift en conversión, **10x**
de retorno sobre la inversión y capacidad de procesamiento de **336.000
imágenes diarias**, con un caso (Otrium) de **90%** de mejora en
eficiencia y **0,2 segundos por imagen**.

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<tbody>
<tr class="odd">
<td><p><strong>Cómo tratar estas cifras en el proyecto</strong></p>
<p>Son cifras <strong>reportadas por el proveedor</strong> y por un
portal de la industria, no resultados replicables en este proyecto. Su
uso legítimo aquí es doble: (a) justificar la existencia del proyecto y
(b) definir las dimensiones de valor que el demostrador debe intentar
medir con sus propios datos — tiempo por imagen, costo por 1.000 SKU,
completitud de atributos, desempeño de búsqueda y recomendación. Ninguna
de ellas se reportará como resultado propio.</p></td>
</tr>
</tbody>
</table>

**2.3 Dos hallazgos académicos que cambian el diseño del proyecto**

**Hallazgo 1 — El ground truth humano está incompleto**

Salminen et al. encontraron que los creadores de contenido asignaban de
forma sesgada tres etiquetas por pieza (μ real = 3,54), mientras el
modelo asignaba un rango más amplio, típicamente 2–5 (μ predicho =
4,10). Su interpretación: los límites cognitivos del anotador humano
reducen su capacidad de seleccionar etiquetas relevantes cuando el
inventario disponible es grande —799 opciones en su caso—, lo que
produce un ground truth incompleto y, por tanto, **una medición
artificialmente baja del desempeño del modelo**.

Consecuencia de diseño: el proyecto no puede evaluarse únicamente contra
la metadata original del catálogo. Debe incluir una **evaluación de
acuerdo humano-máquina** sobre una muestra, como control de la calidad
del propio ground truth.

**Hallazgo 2 — La taxonomía se mueve (concept drift)**

En el mismo trabajo, un modelo entrenado solo con datos de 2017 y
evaluado en 2018 cayó de F1 0,700 a 0,625 (−10,7%), y el coeficiente de
Jaccard entre los tópicos latentes de ambos años fue de **0,41**,
evidencia de un desplazamiento considerable. Los autores recomiendan
monitorear el desempeño de forma continua y reentrenar cuando caiga por
debajo de un umbral definido por dominio, advirtiendo que **no existe un
valor universal de F1**; en clasificación de contenido online consideran
0,70 satisfactorio.

Consecuencia de diseño: la arquitectura debe incluir versionado de
taxonomía, monitoreo de deriva y disparador de reentrenamiento desde la
planeación, no como añadido posterior. En moda esto es más agudo que en
noticias: la temporada es el drift.

**Hallazgo 3 — La línea base visual pura es más débil de lo que sugiere
la intuición**

Sharma & Karnick, usando características de 4.096 dimensiones de la
última capa totalmente conectada de una red VGG-19 y un KNN ponderado
por inversa de distancia sobre el dataset de productos de Amazon,
obtuvieron en la categoría de prendas y confección **F1 0,345 con
precisión 0,603 y recall 0,242** (K=5). En electrónica llegaron a F1
0,407 y en deportes a 0,336, con un patrón consistente: **la precisión
sube y el recall baja al aumentar K** (en deportes, precisión 0,819 con
recall 0,210 en K=7). Su sistema de recuperación respondía 1.000
consultas en 0,081–0,095 segundos.

Consecuencia de diseño: con etiquetas ruidosas y un espacio de tags
grande (1.664 tags en prendas, 886 en electrónica, 2.224 en deportes),
el recall es el cuello de botella, no la precisión. El proyecto debe
reportar **precisión y recall por separado y por atributo**, y el diseño
del umbral de aceptación es una decisión de producto — cuánta cobertura
se sacrifica por cuánta confiabilidad —, no un hiperparámetro más.

**3. Objetivo general**

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<tbody>
<tr class="odd">
<td><p><strong>Objetivo general</strong></p>
<p>Diseñar, construir y evaluar un sistema de Smart Tagging multimodal
para catálogo de ecommerce de moda que, a partir de la imagen del
producto y su texto asociado, prediga atributos estructurados sobre una
taxonomía controlada, y demostrar cuantitativamente —con datasets
públicos— que esos atributos generados por IA (i) alcanzan calidad
comparable a la anotación humana, (ii) mejoran el descubrimiento de
producto mediante búsqueda semántica y (iii) mejoran el desempeño de un
sistema de recomendación frente a una línea base que no los utiliza;
cuantificando además el ahorro operativo frente al etiquetado
manual.</p></td>
</tr>
</tbody>
</table>

El objetivo está formulado para ser **falsable**: cada uno de los tres
componentes tiene métrica asociada y criterio de aceptación (sección
11). Si el componente (iii) no mejora, el proyecto sigue siendo un
resultado válido y reportable — el hallazgo sería que en este dataset el
valor del Smart Tagging se concentra en descubrimiento y eficiencia
operativa, no en recomendación. Un resultado nulo bien medido es un
entregable; un resultado positivo mal medido no lo es.

**4. Objetivos específicos**

Siete objetivos específicos, cada uno con entregable verificable y
criterio de aceptación. Los umbrales que dependen de la dificultad real
de la tarea se fijan al cerrar la línea base de la Fase 3: comprometer
un número antes de conocer esa dificultad produce objetivos decorativos.

| **ID** | **Objetivo específico**                                                                                                                                                                                                                                            | **Entregable**                                                                                                                  | **Criterio de aceptación**                                                                                                                                                                                                                       |
|--------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| OE1    | Diseñar la taxonomía de atributos y la ontología del sistema, con mapeo entre la taxonomía experta de Fashionpedia y la metadata comercial de H&M, **clasificando cada atributo por nivel de evidencia disponible**.                                               | Esquema de atributos versionado (JSON/YAML), tabla de mapeo, **tabla de niveles de evidencia A/B/C** y diccionario de datos.    | Cada atributo tiene vocabulario controlado, cardinalidad, definición operativa y **nivel de evidencia asignado** (7.6). Ningún atributo queda sin nivel: lo que no tiene ground truth se declara nivel C, no se omite.                           |
| OE2    | Construir el pipeline reproducible de ingesta, limpieza y preparación, con EDA del desbalance de atributos y del desplazamiento temporal.                                                                                                                          | Pipeline versionado (código + DVC), reporte de EDA, splits congelados.                                                          | Ejecutable de punta a punta con un comando; splits con separación temporal explícita; distribución de frecuencia por atributo documentada.                                                                                                       |
| OE3    | Entrenar y comparar modelos de tagging multi-etiqueta: métodos de la literatura **reimplementados como línea base local**, enfoques zero-shot con modelos de visión-lenguaje y ajuste fino. Reportar por separado las pistas imagen-sola, texto-solo y multimodal. | Tabla comparativa de modelos con métricas por atributo, por nivel de evidencia y por pista de entrada, con costo computacional. | Al menos 4 enfoques sobre los mismos splits; el mejor supera la línea base local en F1 ponderado con significancia por bootstrap. **Ninguna comparación con cifras absolutas publicadas en otros dominios** (9.1).                               |
| OE4    | Construir el servicio de búsqueda semántica sobre embeddings y compararlo contra búsqueda por metadata tradicional, **con juicios de relevancia humanos ciegos al método**.                                                                                        | Índice vectorial, endpoint de búsqueda y set de consultas con juicios de relevancia obtenidos por pooling a ciegas.             | NDCG@10 comparado sobre juicios humanos ciegos, no sobre reglas derivadas de la metadata; latencia p95 por debajo de 300 ms.                                                                                                                     |
| OE5    | Cuantificar el valor de negocio comparando un recomendador base contra uno enriquecido con atributos IA y embeddings de imagen, **en régimen de metadata completa y de metadata incompleta simulada**.                                                             | Dos recomendadores entrenados, informe de A/B offline, ablaciones en ambas direcciones y análisis por segmento.                 | Diferencia en MAP@12 con intervalo de confianza, desagregada por cold-start y por régimen de completitud de metadata. Un resultado nulo bien medido cumple el objetivo.                                                                          |
| OE6    | Diseñar e implementar el mecanismo de confianza y revisión humana, incluyendo la calibración del umbral por atributo y **el protocolo de anotación**.                                                                                                              | Módulo de calibración, cola de revisión, curva cobertura-precisión y guía de anotación con piloto.                              | Umbral por atributo documentado; porcentaje del catálogo auto-etiquetado reportado al nivel de precisión objetivo. **Ninguna predicción de modelo generativo se autoacepta** sin validación humana (nivel L5 de la sección 9.1).                 |
| OE7    | Empaquetar el sistema como producto: API documentada, observabilidad, **monitoreo operable sin etiquetas** y propuesta de modelo de monetización con benchmark de mercado.                                                                                         | API con contrato OpenAPI, dashboard de deriva, protocolo de auditoría muestral, documento de producto y pricing.                | API desplegada y consumible; **señales de deriva sin etiquetas activas y auditoría humana periódica definida en cadencia y tamaño de muestra** (sección 10.5); modelo de negocio con supuestos explícitos y separados de los hechos verificados. |

**5. Preguntas de investigación e hipótesis**

El proyecto se organiza como tres experimentos encadenados. Cada uno
tiene una hipótesis que puede rechazarse o no con los datos disponibles.

**5.1 Experimento 1 — Exactitud del Smart Tagging**

imagen del producto ──▶ modelo de tagging ──▶ atributos + confianza

│

comparación contra metadata real

│

Precision · Recall · F1 · mAP

**Pregunta:** ¿puede la IA automatizar la clasificación de atributos de
catálogo con precisión suficiente para operar con intervención humana
mínima?

**H1:** un modelo multimodal con ajuste fino supera en F1 ponderado a la
línea base visual de la literatura (características de red convolucional
profunda + KNN ponderado por inversa de distancia).

**5.2 Experimento 2 — Descubrimiento semántico de activos**

"conjunto negro de running para mujer"

│

codificador de texto ──▶ embedding ──▶ similitud vectorial

│

top-K productos

**Pregunta:** ¿los atributos y embeddings generados por Smart Tagging
permiten encontrar producto mejor que la metadata tradicional?

**H2:** la búsqueda semántica sobre embeddings más atributos IA obtiene
mayor NDCG@10 que la búsqueda por filtros de metadata original, con la
ventaja concentrada en consultas de lenguaje natural compuesto (color +
prenda + ocasión).

**5.3 Experimento 3 — Valor de negocio en recomendación**

MODELO A — LÍNEA BASE MODELO B — SMART TAGGING

historial del cliente historial del cliente

\+ +

metadata del producto metadata del producto

\+

atributos generados por IA

\+

embeddings de imagen

│ │

▼ ▼

MAP@12 (base) vs. MAP@12 (enriquecido)

**Pregunta:** ¿enriquecer la representación del producto con atributos
generados por IA mejora la recomendación, y bajo qué condiciones?

**H3a (control):** con la metadata del catálogo completa y limpia, el
recomendador enriquecido iguala o supera marginalmente al base en
MAP@12, y la ganancia se concentra en productos y clientes con
interacción histórica escasa.

**H3b (hipótesis principal):** en régimen de **metadata incompleta
simulada** —una fracción del catálogo con sus atributos comerciales
enmascarados, imitando producto recibido de proveedor sin ficha— los
atributos generados por IA recuperan una parte medible del desempeño
perdido frente a un recomendador que solo ve los huecos.

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<tbody>
<tr class="odd">
<td><p><strong>Por qué H3 tiene dos mitades, y por qué la segunda es la
importante</strong></p>
<p>En H&amp;M la metadata está completa y limpia. Un atributo predicho
desde la imagen es, por tanto, <strong>redundante</strong> con una
columna que ya existe en el archivo, y añadir una feature redundante
rara vez mueve un recomendador. Si el experimento se plantea solo con
H3a, el resultado más probable es un efecto pequeño o nulo — <strong>y
no porque el Smart Tagging no sirva, sino porque este dataset no tiene
el problema que el Smart Tagging resuelve</strong>.</p>
<p>El problema real de la industria es la metadata <em>ausente</em>: el
39,8% de contenido sin clasificar que documentan Salminen et al., o los
datos de proveedor incompletos que Pixyle usa como argumento central de
venta. Enmascarar metadata y medir cuánto recuperan los atributos de IA
es lo que convierte el Experimento 3 en una prueba de la hipótesis de
negocio, y no en una comprobación de redundancia.</p>
<p>El enmascaramiento <strong>se declara siempre como
simulación</strong>, con su mecanismo, su fracción y su criterio de
selección documentados. Es una intervención del analista sobre los
datos, no una condición observada.</p></td>
</tr>
</tbody>
</table>

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<tbody>
<tr class="odd">
<td><p><strong>Por qué MAP@12</strong></p>
<p>Es la métrica oficial de la competencia de Kaggle asociada al dataset
principal, lo que permite contextualizar el resultado frente a
soluciones públicas conocidas en lugar de reportar un número sin
referencia. Se usa como métrica común a H3a y H3b para que ambos
regímenes sean comparables entre sí.</p></td>
</tr>
</tbody>
</table>

**6. Alcance**

**6.1 Dentro del alcance**

- Taxonomía de atributos de moda y su mapeo entre una fuente experta y
  una fuente comercial.

- Predicción multi-etiqueta de atributos a partir de imagen, y
  multimodal (imagen + texto) donde el texto exista.

- Búsqueda semántica texto→imagen e imagen→imagen sobre índice
  vectorial.

- Recomendación offline comparativa, con evaluación segmentada por
  cold-start.

- Calibración de confianza, umbral de aceptación y flujo de revisión
  humana.

- API de inferencia, observabilidad, monitoreo de deriva y
  reentrenamiento disparado por umbral.

- Estimación de ahorro operativo (horas evitadas y costo de cómputo) y
  propuesta de modelo de monetización.

**6.2 Fuera del alcance (declarado explícitamente)**

| **Fuera del alcance**                                                                                                        | **Razón**                                                                                                                                                                                                                                                                         |
|------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Atribución causal de uplift en CTR, tasa de conversión o ventas.                                                             | Los datasets públicos disponibles registran transacciones, no impresiones ni clickstream. Sin datos de exposición no hay contrafactual. Es la limitación estructural más importante del proyecto.                                                                                 |
| Pruebas A/B en línea con tráfico real.                                                                                       | No hay acceso a un ecommerce en operación. Toda la evaluación es offline.                                                                                                                                                                                                         |
| Generación de imágenes de producto o de contenido visual de campaña.                                                         | El proyecto estructura contenido existente; no lo crea. Mantener el foco es parte de lo que hace defendible el resultado.                                                                                                                                                         |
| Despliegue en producción con datos propietarios de una compañía real.                                                        | El proyecto es un demostrador con datos públicos. La arquitectura se diseña para ser portable, pero no se ejecuta contra un catálogo comercial.                                                                                                                                   |
| Uso comercial de los datasets.                                                                                               | H&M autoriza uso no comercial, académico y educativo; DeepFashion restringe a investigación no comercial. El demostrador se mantiene en uso educativo y de investigación (sección 7.3).                                                                                           |
| **Publicación o redistribución de los datos** — imágenes, CSV, embeddings, splits — y demo pública servida con datos de H&M. | Las reglas de H&M prohíben transmitir, publicar o redistribuir los datos a personas que no hayan aceptado formalmente las reglas. La autorización de uso no comercial **no** habilita la redistribución: son dos permisos distintos. La sección 7.4 fija qué se publica y qué no. |

**7. Fuentes de datos**

La estrategia de datos es deliberadamente **combinada**. No existe un
dataset público que contenga simultáneamente imágenes de producto,
atributos anotados por expertos, impresiones y conversiones; asumir que
existe es el primer error que hunde este tipo de proyecto. Lo que sí se
puede construir es una arquitectura de dos fuentes con roles distintos:
una aporta la **inteligencia visual y la taxonomía experta**, la otra
aporta el **contexto comercial y el comportamiento del cliente**.

**7.1 Arquitectura de fuentes: rol de cada dataset**

FASHIONPEDIA

(imágenes complejas + atributos expertos)

│

▼

┌──────────────────────────────┐

│ MODELO DE SMART TAGGING │

│ CLIP / SigLIP · VLM │

│ detección · segmentación │

└──────────────────────────────┘

│

▼

taxonomía de atributos

│

┌───────────────┴────────────────┐

▼ ▼

evaluación en imágenes H&M

Fashionpedia │

(calidad pura) ▼

atributos generados por IA

│

┌─────────────┴─────────────┐

▼ ▼

búsqueda semántica recomendación

│

transacciones H&M

│

▼

impacto de negocio

**7.2 Fuentes candidatas**

| **Dataset**                                           | **Contenido relevante**                                                                                                                                                                                                                                                                      | **Rol en el proyecto**                                                                                                                                                                                                                                                  |
|-------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **H&M Personalized Fashion Recommendations** (Kaggle) | Imágenes de producto, articles.csv (article_id, product_type, colour, graphical_appearance, department, garment_group, description), customers.csv (customer_id, age) y transactions_train.csv (customer_id, article_id, date, price, sales_channel). El dataset completo ronda los 34,6 GB. | **Fuente principal.** Es la única candidata que une catálogo con imagen, metadata comercial y comportamiento transaccional real. Su metadata se convierte en ground truth: se oculta al modelo y se le pide predecirla desde la imagen sola.                            |
| **Fashionpedia**                                      | 48.825 imágenes de street style, eventos, pasarela y compra en línea. 27 categorías principales de prenda, 19 partes de prenda y 294 atributos finos organizados en 9 super-categorías, con máscaras de segmentación exhaustivas. Formato COCO extendido con campo de atributos.             | **Fuente auxiliar de inteligencia visual.** Sus imágenes son mucho más complejas que un producto sobre fondo neutro, y su taxonomía fue construida por expertos en moda — esto resuelve gratis la parte más difícil de un proyecto real de Smart Tagging: la ontología. |
| **DeepFashion** (MMLab, CUHK)                         | Más de 800.000 imágenes, 50 categorías y ~1.000 atributos descriptivos. Incluye pares consumer-to-shop: la misma prenda fotografiada por un consumidor y en la ficha de producto.                                                                                                            | **Opcional / stretch.** Su valor específico es entrenar visual search y shop-the-look. Restringido a uso de investigación no comercial, lo que limita su papel en un demostrador público.                                                                               |
| **Amazon Reviews 2023** (McAuley Lab)                 | Reviews, interacciones, metadata de producto, precios, descripciones, categorías, imágenes y relaciones tipo *bought together*. Categorías Amazon_Fashion y Clothing_Shoes_and_Jewelry, con versión 5-core más manejable.                                                                    | **Alternativa / extensión multimodal.** Permite sumar texto de reviews como tercera modalidad. Además, la versión 2015 de este dataset es la que usaron Sharma & Karnick, lo que habilita una comparación directa con su línea base publicada.                          |

La decisión recomendada, coherente con el documento de sugerencia del
proyecto, es **H&M como fuente principal y Fashionpedia como fuente
auxiliar**. La razón es que esa combinación es la única que permite
recorrer el arco completo del proyecto — visión por computador, modelos
multimodales, embeddings, búsqueda vectorial, sistemas de recomendación,
experimentación y métricas de negocio — dentro de un solo caso
coherente, en lugar de producir tres mini-proyectos desconectados.

**7.3 Licencias: términos definidos**

Los términos de las dos fuentes principales están definidos y son la
restricción de diseño más importante del proyecto después de la ausencia
de datos de exposición.

| **Fuente**                                 | **Qué autoriza**                                                                                                   | **Qué restringe**                                                                                                                                                                                                                                             | **Consecuencia operativa**                                                                                                                                                                                          |
|--------------------------------------------|--------------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **H&M** (Kaggle)                           | Uso no comercial, académico y educativo de los datos.                                                              | Prohíbe transmitir, publicar o redistribuir los datos a personas que no hayan aceptado formalmente las reglas de la competencia.                                                                                                                              | El proyecto puede **construirse y ejecutarse** con H&M sin problema. No puede **publicar** imágenes, CSV, embeddings, splits ni una demo pública servida con esos datos.                                            |
| **Fashionpedia** — anotaciones y ontología | Creative Commons Attribution 4.0 (CC BY 4.0): uso, adaptación y redistribución, incluso comercial, con atribución. | Obliga a dar atribución al proyecto Fashionpedia en cualquier uso o derivado.                                                                                                                                                                                 | La taxonomía y las anotaciones **sí** pueden publicarse y reutilizarse. Es el activo redistribuible del proyecto, y refuerza la decisión de invertir en la capa 0.                                                  |
| **Fashionpedia** — imágenes                | Nada por sí mismo: el proyecto declara que **no es titular del copyright de las imágenes**.                        | El uso debe cumplir los términos de cada fuente original — Flickr, Unsplash, Burst by Shopify, Freestocks, Kaboompics y Pexels — y el usuario acepta responsabilidad plena por el uso del dataset, incluidas las copias de imágenes con copyright que genere. | Una demo pública con imágenes de Fashionpedia exige **revisión activo por activo**, no basta aceptar la licencia de las anotaciones. Fuera del alcance del demostrador salvo con un subconjunto revisado uno a uno. |
| **Fashionpedia** — software del dataset    | BSD 2-Clause: redistribución en fuente y binario, incluido uso comercial.                                          | Conservar el aviso de copyright y las condiciones; sin garantía.                                                                                                                                                                                              | Las utilidades de carga y evaluación del dataset pueden incorporarse al repositorio conservando el aviso.                                                                                                           |
| **DeepFashion**                            | Investigación no comercial.                                                                                        | Restringido a ese fin.                                                                                                                                                                                                                                        | Se mantiene como opcional. Si se usa, aplica la misma regla de no publicación de datos.                                                                                                                             |
| **Amazon Reviews 2023**                    | Por verificar en la fuente primaria.                                                                               | Por verificar.                                                                                                                                                                                                                                                | No se incorpora hasta que sus términos estén verificados y registrados en el diccionario de datos.                                                                                                                  |

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<tbody>
<tr class="odd">
<td><p><strong>La distinción que decide el diseño de la
vitrina</strong></p>
<p><strong>Permiso de uso y permiso de redistribución son dos cosas
distintas.</strong> Que el proyecto sea de portafolio, educativo y sin
ánimo de lucro satisface la primera condición de H&amp;M —uso no
comercial, académico y educativo— pero <strong>no levanta la prohibición
de redistribuir</strong>: esa cláusula no depende de si se cobra dinero,
sino de a quién llegan los datos. Una demo pública que sirve imágenes o
embeddings de H&amp;M a visitantes anónimos los entrega a personas que
no aceptaron las reglas, con o sin ánimo de lucro.</p>
<p>La consecuencia no es que el proyecto deje de ser público: <strong>el
proyecto es público, los datos no</strong>. Código, notebooks, informe,
métricas, gráficas y model card se publican íntegros; los archivos de
datos y sus derivados no salen del entorno de trabajo. La sección 7.4 lo
detalla activo por activo.</p>
<p>Esta es la lectura conservadora de la cláusula, y quien decide es el
responsable del proyecto: no constituye asesoría legal. Lo que el plan
exige es que la cláusula se lea en su texto literal y se pegue en el
repositorio antes de descargar los datos (Fase F0), de modo que la
decisión quede documentada frente a la fuente y no frente a un
resumen.</p></td>
</tr>
</tbody>
</table>

**7.4 Estrategia de publicación: qué se publica y qué no**

Esta tabla es el contrato de publicación del proyecto. Cada artefacto
tiene una decisión tomada de antemano, para que la pregunta no se
resuelva por improvisación el día que se arme el repositorio.

| **Artefacto**                                                        | **Decisión**                                     | **Razón**                                                                                                                                                                   |
|----------------------------------------------------------------------|--------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Código, notebooks y pipeline completo                                | **Se publica**                                   | Es trabajo propio. No contiene datos de las fuentes restringidas y es lo que demuestra la capacidad técnica.                                                                |
| Informe técnico, métricas agregadas, tablas y gráficas de resultados | **Se publica**                                   | Son resultados derivados agregados, no los datos. Es el entregable de valor del portafolio.                                                                                 |
| Taxonomía, esquema de atributos y tabla de mapeo                     | **Se publica** con atribución a Fashionpedia     | Las anotaciones y la ontología están bajo CC BY 4.0, que permite redistribución con atribución.                                                                             |
| Model card, análisis de errores y curvas de calibración              | **Se publica**                                   | Documentación del modelo, no datos de entrada.                                                                                                                              |
| Imágenes de H&M, articles.csv, customers.csv, transactions_train.csv | **No se publica**                                | Redistribución prohibida por las reglas de H&M, independientemente del ánimo de lucro.                                                                                      |
| Embeddings, features derivadas y splits calculados sobre H&M         | **No se publica**                                | Son datos derivados que permiten reconstruir información del dataset. Se tratan con la misma restricción que el dato crudo.                                                 |
| Demo pública servida con datos de H&M                                | **No se publica**                                | Entregaría datos a visitantes que no aceptaron las reglas. La demo corre en local o en el entorno donde los datos ya residen.                                               |
| Imágenes de Fashionpedia en una demo pública                         | **No se publica** sin revisión activo por activo | Fashionpedia no es titular del copyright; cada imagen responde a los términos de Flickr, Unsplash, Burst, Freestocks, Kaboompics o Pexels.                                  |
| Pesos del modelo ajustado sobre H&M                                  | **Zona gris — decisión diferida a F0**           | No es dato crudo, pero sí un derivado entrenado sobre datos restringidos. Requiere leer qué dice la cláusula sobre trabajos derivados antes de publicarlos.                 |
| Demo pública con catálogo propio                                     | **Se publica**                                   | Fotografías propias o imágenes con licencia redistribuible verificada una a una, etiquetadas por el modelo. Da el impacto visual del showcase sin tocar datos restringidos. |

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<tbody>
<tr class="odd">
<td><p><strong>El efecto secundario favorable</strong></p>
<p>Ejecutar el trabajo sobre H&amp;M <strong>dentro del entorno donde
los datos ya residen</strong> —los notebooks de la propia plataforma que
los aloja— resuelve dos problemas con una sola decisión: el dato nunca
se mueve, lo que encaja de forma natural con la cláusula de
redistribución, y aparece el acceso a GPU que el hardware local no tiene
(sección 12). La restricción de licencia y la restricción de cómputo
tienen la misma solución.</p></td>
</tr>
</tbody>
</table>

**7.5 El riesgo de datos que más se subestima: el domain shift**

Fashionpedia contiene personas vestidas en escenas reales; H&M contiene
producto sobre fondo neutro. Un modelo entrenado en la primera y
aplicado a la segunda **cambia de dominio**, y el desempeño cae por
razones que no tienen nada que ver con la calidad del modelo. El plan lo
trata como un riesgo de primer orden (sección 14) con tres mitigaciones
previstas: medir el desempeño cruzado de forma explícita antes de sacar
conclusiones, usar la segmentación de prenda para recortar la región de
interés y homogeneizar el fondo, y reservar un subconjunto anotado
manualmente de H&M como set de calibración del dominio destino.

El precedente metodológico está en Salminen et al., que evaluaron su
modelo entrenado en artículos web sobre un canal distinto —títulos y
descripciones de YouTube, mucho más cortos— y midieron el resultado
contra codificación humana independiente en lugar de asumir
transferencia. Ese es el patrón a replicar.

**7.6 Niveles de evidencia de los atributos**

La taxonomía que hace valioso al sistema es **más rica que los atributos
verificables** del catálogo principal. H&M permite verificar categoría
de producto, color, apariencia gráfica, departamento y grupo de prenda;
no permite verificar material aparente ni ocasión de uso. Si esa
asimetría no se declara, el proyecto termina afirmando que "el modelo
predice silueta y material" sin ground truth que lo sostenga — que es la
forma más rápida de perder credibilidad ante un revisor técnico.

La solución es clasificar cada atributo por el tipo de evidencia
disponible y **no mezclar nunca sus métricas en una misma cifra**.

| **Nivel**                         | **Definición**                                                                                                                                                | **Métricas admisibles**                                                                                                 | **Uso en el informe**                                                                                                                                                               |
|-----------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **A — Verificable en H&M**        | Atributos con columna correspondiente en la metadata comercial: categoría de producto, color, apariencia gráfica, departamento, grupo de prenda.              | Precision, Recall, F1 (macro/micro/ponderado), mAP, Hamming loss, subset accuracy, calibración. El repertorio completo. | **Es la cifra titular.** El resumen ejecutivo cita únicamente el nivel A, porque es el único con ground truth comercial sobre el dominio destino.                                   |
| **B — Evaluable en Fashionpedia** | Atributos finos anotados por expertos —partes de prenda, detalles de construcción, silueta— evaluables en el dominio de Fashionpedia, no en el de H&M.        | El repertorio completo, pero **etiquetadas como métricas en dominio Fashionpedia**.                                     | Se reportan en tabla separada. Su traslado al catálogo de H&M es un **supuesto** sujeto al domain shift de la sección 7.5, no un resultado. Nunca se promedian con las del nivel A. |
| **C — Sin etiqueta disponible**   | Atributos de la taxonomía sin ground truth en ninguna fuente: ocasión de uso, material aparente, atributos de cola larga propuestos por el modelo generativo. | **Solo precisión sobre muestra revisada por humanos**, a un nivel de confianza declarado.                               | Se reportan como precisión-en-muestra, con el tamaño de muestra y su intervalo. Alimentan la demo y el producto, no las conclusiones cuantitativas del proyecto.                    |

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<tbody>
<tr class="odd">
<td><p><strong>El punto que se pasa por alto: en el nivel C el recall es
inmedible</strong></p>
<p>No es difícil de medir: <strong>no se puede medir</strong>. Sin
etiquetas de referencia no existe forma de saber qué atributos correctos
omitió el modelo, así que el denominador del recall no existe. En
consecuencia <strong>cualquier F1 reportado sobre el nivel C es una
cifra inventada</strong>, porque una de sus dos mitades no es
calculable. Lo único honesto en ese nivel es: "de las N predicciones
revisadas por humanos, el X% resultó correcto".</p>
<p>Esto tiene una consecuencia de producto, no solo de medición: en los
atributos de nivel C el sistema no puede prometer cobertura, solo
confiabilidad de lo que afirma. Es exactamente el tipo de límite que
conviene declarar antes de que lo pregunte un cliente.</p></td>
</tr>
</tbody>
</table>

**7.7 Matriz de procedencia y control de fuga de información**

El plan admite entradas de imagen y de texto mientras usa la metadata de
H&M como verdad. Eso abre un riesgo de fuga que, si no se controla,
produce métricas excelentes y vacías: si la descripción del artículo
contiene la palabra "t-shirt" y el objetivo es product_type, el modelo
no está viendo nada, está leyendo la respuesta.

**Los dos canales de fuga**

- **Texto → objetivo.** El campo description puede contener literalmente
  el valor del atributo objetivo. Es el canal obvio.

- **Campo → campo.** Es el canal que se pasa por alto y es igual de
  grave: product_type, garment_group y department están fuertemente
  correlacionados entre sí. Usar uno como entrada para predecir otro es
  fuga, aunque no haya texto libre involucrado.

Por eso el control no es una regla general sino una **matriz congelada
antes de entrenar**, con una fila por atributo objetivo:

| **Atributo objetivo**    | **Campos bloqueados como entrada**                                                         | **Entradas permitidas**                                         |
|--------------------------|--------------------------------------------------------------------------------------------|-----------------------------------------------------------------|
| product_type             | description, garment_group, department, product_group y cualquier campo derivado de ellos. | Imagen. Texto solo en la pista diagnóstica, declarada como tal. |
| colour                   | description, campos de color derivados, graphical_appearance si codifica color.            | Imagen.                                                         |
| graphical_appearance     | description, colour si el patrón está implícito en él.                                     | Imagen.                                                         |
| Atributos de nivel B y C | No aplica ground truth de H&M; se declara la fuente de evaluación.                         | Imagen; texto si se declara y se reporta por separado.          |

**Tres pistas reportadas por separado**

- **Imagen sola — es el titular honesto.** Corresponde al caso de
  negocio real: el proveedor envía una fotografía y poco más. Es también
  la pista que hace comparable el proyecto con el producto de
  referencia, que se describe como visual-primero.

- **Texto solo — es un diagnóstico, no un competidor.** Aísla cuánto del
  desempeño proviene del texto que el catálogo ya tiene. Si texto solo
  iguala a multimodal, la visión no está aportando nada: ese es un
  hallazgo reportable, no un fracaso.

- **Multimodal — es el techo.** Útil para conocer el máximo alcanzable,
  siempre que la matriz de procedencia garantice que no hay fuga dentro
  de él.

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<tbody>
<tr class="odd">
<td><p><strong>El argumento de producto que refuerza la
decisión</strong></p>
<p>La descripción del artículo es lo que el referente de mercado
<strong>vende como salida</strong>, no como entrada: su suite base
genera títulos y descripciones a partir de la imagen. Usar la
descripción como entrada para predecir atributos invierte el producto y
resuelve un problema que en un despliegue real no se tiene. La pista
imagen-sola no es solo la más limpia metodológicamente: es la única que
describe el sistema que se quiere construir.</p></td>
</tr>
</tbody>
</table>

**8. Arquitectura técnica**

La arquitectura se organiza en capas con una regla: **la taxonomía es la
capa cero**, no un subproducto del modelo. Browntape lo pone como primer
paso de implementación — definir una taxonomía completa con agrupaciones
lógicas antes de preparar datos o elegir modelo — y es también el orden
que sigue Pixyle, que se posiciona como *"un sistema de inteligencia, no
un sistema de registro"*: la taxonomía y el PIM del cliente son el
registro; el modelo aporta inteligencia sobre ese registro.

**8.1 Diagrama de capas**

┌─────────────────────────────────────────────────────────────────────┐

│ CAPA 0 · TAXONOMÍA Y ONTOLOGÍA │

│ esquema de atributos versionado · vocabulario controlado · │

│ cardinalidad · mapeo Fashionpedia ↔ H&M · diccionario de datos │

└─────────────────────────────────────────────────────────────────────┘

│

┌─────────────────────────────────▼───────────────────────────────────┐

│ CAPA 1 · INGESTA Y ALMACENAMIENTO │

│ bronze (crudo) → silver (limpio) → gold (listo para modelo) │

│ Parquet · versionado con DVC · splits congelados y auditables │

└─────────────────────────────────────────────────────────────────────┘

│

┌─────────────────────────────────▼───────────────────────────────────┐

│ CAPA 2 · REPRESENTACIÓN │

│ codificador de imagen · codificador de texto · almacén de │

│ embeddings · caché de features (evita recomputar en cada corrida) │

└─────────────────────────────────────────────────────────────────────┘

│

┌─────────────────────────────────▼───────────────────────────────────┐

│ CAPA 3 · MOTOR DE TAGGING │

│ cabezas multi-etiqueta · clasificación zero-shot · VLM como │

│ respaldo para atributos raros · calibración de confianza · │

│ umbral por atributo │

└─────────────────────────────────────────────────────────────────────┘

│

┌────────────────────┼────────────────────┐

▼ ▼ ▼

┌────────────────────┐ ┌──────────────────┐ ┌────────────────────────┐

│ CAPA 4 · BÚSQUEDA │ │ CAPA 5 · SERVICIO│ │ CAPA 6 · HUMAN-IN-THE- │

│ índice vectorial │ │ API REST │ │ LOOP │

│ (FAISS / Qdrant) │ │ lote + en línea │ │ cola de baja confianza │

│ texto→imagen │ │ contrato OpenAPI │ │ revisión y corrección │

│ imagen→imagen │ │ de atributos │ │ realimenta el dataset │

└────────────────────┘ └──────────────────┘ └────────────────────────┘

│ │ │

└────────────────────┼────────────────────┘

▼

┌─────────────────────────────────────────────────────────────────────┐

│ CAPA 7 · CONSUMIDORES │

│ búsqueda semántica del sitio · recomendador · sincronización │

│ con PIM/DAM · generación de descripciones y alt-text │

└─────────────────────────────────────────────────────────────────────┘

│

┌─────────────────────────────────▼───────────────────────────────────┐

│ CAPA 8 · MLOPS Y OBSERVABILIDAD │

│ MLflow (experimentos y registro) · CI │

│ BUCLE RÁPIDO, sin etiquetas: deriva de embeddings de entrada · │

│ deriva de predicciones · deriva de confianza · volumen de │

│ cola · tasa fuera de taxonomía → alerta temprana │

│ BUCLE LENTO, con etiquetas: auditoría humana muestral periódica │

│ → estimación de F1 con intervalo → reentrenamiento │

└─────────────────────────────────────────────────────────────────────┘

**8.2 Decisiones de arquitectura y su justificación**

| **Decisión**                                                                                       | **Justificación**                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
|----------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| La taxonomía es un artefacto versionado independiente del código del modelo.                       | Las taxonomías cambian con el tiempo y con la temporada (Salminen et al. documentan Jaccard 0,41 entre tópicos de años consecutivos). Si la taxonomía vive incrustada en el código, cada cambio de temporada rompe el sistema. Versionarla permite reentrenar contra una versión conocida y auditar qué cambió.                                                                                                                                                               |
| Los embeddings se calculan una vez y se persisten; no se recalculan por experimento.               | La extracción de características es la operación más costosa del pipeline. Cachearla convierte iteraciones de horas en iteraciones de minutos y es la diferencia entre poder probar cuatro enfoques y poder probar uno.                                                                                                                                                                                                                                                       |
| El motor de tagging es multi-etiqueta nativo, no una colección de clasificadores uno-contra-todos. | Ambos papers llegan a la misma conclusión por vías distintas: Salminen et al. descartan uno-contra-todos por ineficiencia computacional (un modelo por keyword, todos activos en inferencia) y Sharma & Karnick descartan SVM por la misma razón de escala, notando que no escala a un número grande de categorías de tags.                                                                                                                                                   |
| La confianza se calibra y el umbral se fija por atributo, no global.                               | Salminen et al. optimizaron un umbral de probabilidad de 0,48 para maximizar F1. Pero el costo de un falso positivo no es igual en todos los atributos: equivocar el color es visible para el cliente, equivocar la "ocasión de uso" casi no. El umbral es una decisión de producto por atributo.                                                                                                                                                                             |
| La cola de revisión humana realimenta el dataset de entrenamiento.                                 | Es el mecanismo que convierte el sistema en algo que mejora con el uso, y es también el que hace creíble la propuesta de producto: ninguna compañía retail acepta un sistema de atributos sin control de calidad humano sobre los casos dudosos.                                                                                                                                                                                                                              |
| El monitoreo de deriva es parte del entregable mínimo, no una fase posterior.                      | Recomendación explícita de Salminen et al.: monitorear de forma continua y reentrenar cuando el desempeño caiga bajo un umbral definido por dominio. En moda el ciclo es estacional y predecible, lo que permite anticipar el reentrenamiento en lugar de reaccionar a él.                                                                                                                                                                                                    |
| **El monitoreo se divide en dos bucles, y el F1 viene del lento.**                                 | En producción no hay etiquetas, así que **el F1 no es observable en vivo**: una "alerta por caída de F1" es un control que no se puede implementar. El bucle rápido vigila señales que sí existen sin etiquetas (deriva de entrada, de predicción y de confianza, volumen de cola, tasa fuera de taxonomía) y sirve de alerta temprana; el bucle lento produce el F1 real desde una auditoría humana muestral con cadencia y tamaño definidos. La sección 10.5 detalla ambos. |

**8.3 Stack tecnológico propuesto**

| **Componente**                               | **Herramienta propuesta**                                                     | **Alternativa**                                     |
|----------------------------------------------|-------------------------------------------------------------------------------|-----------------------------------------------------|
| Lenguaje y cómputo numérico                  | Python, PyTorch                                                               | JAX                                                 |
| Modelos de visión-lenguaje                   | Hugging Face transformers + open_clip                                         | timm para backbones puros                           |
| **Inferencia local sin GPU dedicada**        | **OpenVINO** (soporta gráficos integrados Intel) u **ONNX Runtime**           | PyTorch en CPU — funciona, pero más lento           |
| Procesamiento de datos                       | **DuckDB** sobre Parquet para las transacciones; Polars para transformaciones | pandas con lectura por trozos si la memoria aprieta |
| Versionado de datos y modelos                | DVC + Git                                                                     | LakeFS                                              |
| Seguimiento de experimentos                  | MLflow                                                                        | Weights & Biases                                    |
| Índice vectorial                             | FAISS (local) o Qdrant (con servicio)                                         | pgvector si se quiere todo en Postgres              |
| Recomendación                                | implicit (ALS, BPR), LightGBM como ranker                                     | RecBole, Merlin                                     |
| Servicio de inferencia                       | FastAPI + Uvicorn; contenedor Docker                                          | BentoML, TorchServe                                 |
| Orquestación de pipeline                     | Prefect o Makefile + DVC pipelines                                            | Airflow (sobredimensionado para este alcance)       |
| Demo y visualización                         | Streamlit o Gradio                                                            | Aplicación web propia                               |
| Anotación de la muestra de validación humana | Label Studio                                                                  | CVAT                                                |

**9. Modelos**

La estrategia de modelado es **escalonada**: primero una línea base
reproducida de la literatura para tener un punto de comparación honesto,
luego enfoques zero-shot que no requieren entrenamiento, luego ajuste
fino, y finalmente modelos de visión-lenguaje generativos para los
atributos de cola larga. Empezar por el modelo más grande es la forma
más común de terminar sin saber si valió la pena.

**9.1 Experimento 1 — Modelos de tagging**

| **Nivel**                                                        | **Enfoque**                                                                                                                                                                                                                                          | **Por qué está en el plan**                                                                                                                                                                                                                                                                                                                                                                        | **Referencia de desempeño**                                                                                                                                                                                                |
|------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| L0 — Línea base trivial                                          | Predicción por frecuencia: asignar siempre los atributos más comunes del catálogo.                                                                                                                                                                   | Establece el piso. Con distribuciones tan desbalanceadas como las de un catálogo de moda, esta línea base es engañosamente fuerte en accuracy y sirve para detectar métricas mal elegidas.                                                                                                                                                                                                         | Se calcula en el proyecto.                                                                                                                                                                                                 |
| L1 — Método de literatura **reimplementado localmente** (visual) | Características de 4.096 dimensiones de la última capa totalmente conectada de una CNN profunda (VGG-19) con transfer learning + KNN ponderado por inversa de distancia, multi-etiqueta, **entrenado y evaluado sobre los splits de este proyecto**. | Reproduce el **método** de Sharma & Karnick para tener una línea base fuerte y publicada. Lo que se compara son métodos sobre los mismos datos, **nunca la cifra de este proyecto contra la cifra de su paper** — ver la advertencia bajo la tabla.                                                                                                                                                | Su cifra publicada (prendas: F1 0,345 · P 0,603 · R 0,242 en K=5) se usa solo como **contexto cualitativo** del comportamiento precisión-recall. Ellos probaron también VGG-16 y GoogLeNet; VGG-19 dio su mejor resultado. |
| L1b — Línea base de literatura (texto)                           | TF-IDF sobre título + descripción + cuerpo, con red neuronal multi-etiqueta; PCA a dimensión √n para los modelos que lo requieren.                                                                                                                   | Reproduce el método de Salminen et al. y aísla cuánto del desempeño viene del texto que el catálogo ya tiene, antes de atribuirle mérito a la visión.                                                                                                                                                                                                                                              | Publicado: NN F1 0,627 → 0,700 optimizado, vs. KNN 0,577 y Random Forest 0,458. TF-IDF (0,640) superó a TF (0,626) y a Doc2Vec (0,516). Texto completo \> solo título.                                                     |
| L2 — Zero-shot multimodal                                        | Codificadores contrastivos imagen-texto (familia CLIP / SigLIP) con plantillas de prompt por atributo, sin entrenamiento.                                                                                                                            | Es el enfoque que hace viable el proyecto con cómputo limitado y el que mejor refleja la práctica actual de la industria. También produce los embeddings que alimentan los experimentos 2 y 3.                                                                                                                                                                                                     | Se mide en el proyecto; la versión y el checkpoint exacto deben validarse al momento de ejecución.                                                                                                                         |
| L3 — Sondeo lineal y ajuste fino eficiente                       | Cabezas lineales o MLP multi-etiqueta sobre embeddings congelados; luego adaptadores de bajo rango (LoRA) sobre el codificador de imagen.                                                                                                            | Aprovecha el caché de embeddings de la capa 2: entrenar una cabeza sobre features precalculadas cuesta minutos. Es el mejor retorno por hora de GPU del proyecto.                                                                                                                                                                                                                                  | Se mide en el proyecto.                                                                                                                                                                                                    |
| L4 — Segmentación y atributos localizados                        | Detección y segmentación de prenda y de partes de prenda, con predicción de atributos por región segmentada.                                                                                                                                         | Es lo que habilita atributos de detalle —cuello, manga, escote, silueta— que son justamente los que Pixyle vende y los que Fashionpedia anota con máscaras. Sin localización, el modelo predice sobre la imagen completa y confunde la prenda con el fondo o con otra prenda.                                                                                                                      | Fashionpedia provee máscaras exhaustivas para 27 categorías principales y 19 partes de prenda.                                                                                                                             |
| L5 — VLM generativo, **como asistente y no como clasificador**   | Modelo de visión-lenguaje instruido para emitir atributos en JSON validado contra el esquema de la capa 0, más descripciones y alt-text. Sus salidas entran a la cola de revisión humana; **no se autoaceptan**.                                     | Cubre la cola larga (nivel C) donde un clasificador supervisado no tiene datos. Pero la validación de esquema verifica **forma, no verdad**: un JSON válido puede ser semánticamente falso, y la confianza auto-reportada de un VLM está mal calibrada, así que no hay señal sobre la cual poner umbral. Su rol útil es otro: proponer candidatos de taxonomía y pre-rellenar la cola de revisión. | Se mide como **reducción de tiempo por anotación** con y sin pre-relleno, y como precisión sobre muestra revisada. Los modelos concretos y sus versiones se validan en ejecución; este plan no los fija.                   |

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<tbody>
<tr class="odd">
<td><p><strong>Regla de comparación</strong></p>
<p>Todos los enfoques se evalúan sobre <strong>los mismos splits
congelados</strong> y con <strong>las mismas métricas</strong>, y cada
uno reporta además su costo: segundos por imagen y horas de GPU. Un
modelo que gana 2 puntos de F1 a 40 veces el costo de inferencia no es
el modelo ganador en un contexto de catálogo con cientos de miles de SKU
— Sharma &amp; Karnick reportaron tiempos de recuperación de 0,081–0,095
s para 1.000 consultas precisamente porque en ecommerce la latencia es
parte del resultado.</p></td>
</tr>
</tbody>
</table>

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<tbody>
<tr class="odd">
<td><p><strong>Lo que NO se puede concluir de la tabla
anterior</strong></p>
<p>Las cifras publicadas de Sharma &amp; Karnick <strong>no son un
umbral a superar</strong>, y compararlas con los resultados de este
proyecto sería inválido por tres razones acumulativas. Sus etiquetas
provienen de metadata de Amazon parseada y ruidosa; su dominio es otro;
y su espacio de clases es de ~1.664 tags en prendas frente a unos pocos
campos de vocabulario controlado en H&amp;M.</p>
<p>Pero la razón de fondo es más profunda que las tres: <strong>difiere
la forma de la tarea</strong>. Ellos resuelven un problema
multi-etiqueta sobre un espacio grande de tags ruidosos; H&amp;M plantea
varios problemas multi-clase independientes con vocabulario limpio por
campo. No son dos mediciones de lo mismo, y ni con idéntico F1 serían
comparables.</p>
<p>Lo que sí transfiere de su trabajo es el <strong>patrón
cualitativo</strong>: precisión sube y recall baja al aumentar K (en
deportes, precisión 0,819 con recall 0,210), de donde se sigue que el
recall es el cuello de botella y que el umbral es una decisión de
producto. Eso es lo que el plan hereda; el número, no.</p></td>
</tr>
</tbody>
</table>

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<tbody>
<tr class="odd">
<td><p><strong>Dónde corre cada nivel, dado el hardware
disponible</strong></p>
<p>L0, L1b, L3 (sondeo lineal) y toda la evaluación corren <strong>en
local sobre CPU</strong>, porque operan sobre embeddings o vectores
TF-IDF ya calculados. L1 (extracción de características de la CNN), L2
(zero-shot a escala), L3 (LoRA) y L4 (segmentación) requieren
<strong>GPU en la nube gratuita</strong>. L5 queda como experimento
acotado por API sobre muestra. La sección 12 detalla el reparto y las
restricciones que impone.</p></td>
</tr>
</tbody>
</table>

**9.2 Experimento 2 — Búsqueda semántica**

- **Recuperación:** similitud coseno sobre embeddings normalizados en
  índice vectorial, con búsqueda aproximada (HNSW o IVF-PQ) para medir
  el compromiso entre latencia y recall.

- **Consultas:** dos familias — atributos sueltos ("vestido floral") y
  lenguaje natural compuesto ("conjunto negro de running para mujer"),
  que es donde se espera la ventaja frente a filtros de metadata.

- **Línea base de comparación:** búsqueda por filtros sobre la metadata
  original del catálogo, que es exactamente lo que un ecommerce tiene
  hoy. Sin esta línea base, el número de NDCG no dice nada.

- **Ground truth de relevancia: juicios humanos obtenidos por pooling a
  ciegas.** Ver la advertencia de circularidad a continuación — este
  punto cambió respecto a versiones anteriores del plan.

- **Reranking (opcional):** un reordenador cruzado sobre los top-K
  candidatos, para medir cuánto queda por ganar después de la
  recuperación por embeddings.

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<tbody>
<tr class="odd">
<td><p><strong>La circularidad que invalidaría este
experimento</strong></p>
<p>Si la relevancia se define con reglas derivadas de la metadata,
entonces la búsqueda por filtros compite <strong>contra su propia
definición</strong> y puede acercarse al 100% por construcción. Un
ground truth híbrido no basta: mientras la cifra titular monte sobre
reglas de metadata, el sesgo favorece al baseline y el resultado no
significa nada.</p>
<p>El mecanismo correcto es <strong>evaluación por pooling a
ciegas</strong>: se toman los top-K de ambos sistemas, se unen, se
barajan y se juzga la relevancia sin que el evaluador sepa qué sistema
produjo cada resultado. Es práctica estándar en recuperación de
información y es la única forma de que la comparación sea limpia. Las
reglas de metadata pueden usarse para generar volumen de candidatos,
pero no como verdad.</p>
<p><strong>Y la circularidad reaparece en las consultas</strong> si se
redactan desde el vocabulario controlado de la metadata. Las consultas
deben escribirse como las teclearía un comprador, <strong>incluyendo
términos que no existen en ese vocabulario</strong> — que es
precisamente donde la búsqueda semántica debería ganar. Si todas las
consultas usan palabras que ya están en los filtros, se está midiendo el
mejor caso del baseline y ocultando la ventaja real del
sistema.</p></td>
</tr>
</tbody>
</table>

**9.3 Experimento 3 — Recomendación**

| **Modelo**                                    | **Entradas**                                                                                                                           | **Rol**                                                                                                                                                                                        |
|-----------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Popularidad reciente por segmento             | Transacciones, fecha, canal de venta                                                                                                   | Línea base mínima. En datasets de retail con fuerte estacionalidad suele ser sorprendentemente competitiva; ignorarla lleva a sobrestimar el modelo propio.                                    |
| Co-visitación / ítem-ítem                     | Co-ocurrencia de artículos en el historial del cliente                                                                                 | Línea base colaborativa sin factores latentes, robusta y rápida de calcular.                                                                                                                   |
| Factorización matricial implícita (ALS / BPR) | Matriz cliente × artículo de transacciones                                                                                             | **Modelo A — línea base.** Solo señal colaborativa más metadata original.                                                                                                                      |
| Recuperación + ranker con features            | Candidatos de los modelos anteriores; features de cliente, artículo, atributos IA y embeddings de imagen; ranker por gradient boosting | **Modelo B — enriquecido.** Es la arquitectura estándar de dos etapas en recomendación de retail y la que permite aislar el aporte marginal de los atributos IA mediante ablación de features. |
| Dos torres (opcional)                         | Torre de cliente y torre de artículo, esta última alimentada con embeddings de imagen y atributos                                      | Extensión si el cómputo lo permite; permite recuperación densa y manejo natural de productos nuevos.                                                                                           |

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<tbody>
<tr class="odd">
<td><p><strong>El detalle que decide si el Experimento 3 es
creíble</strong></p>
<p>La partición de transacciones debe ser <strong>temporal</strong>,
nunca aleatoria: entrenar con un periodo y evaluar en el periodo
siguiente, replicando la forma en que el modelo operaría. Una partición
aleatoria filtra futuro hacia el pasado y produce métricas infladas que
no sobreviven a ninguna revisión técnica. Además, el análisis debe
desagregarse por frecuencia de interacción del artículo y del cliente,
porque H3a predice que la ganancia está concentrada en el segmento de
baja interacción — y un promedio global puede esconder por completo ese
efecto.</p></td>
</tr>
</tbody>
</table>

**9.3.1 Ablaciones obligatorias, en las dos direcciones**

Sin ablación no se puede atribuir una mejora a los atributos de IA:
podría venir de los embeddings, de la metadata original, de la
popularidad o del resto de la ingeniería de features. Y una ablación en
una sola dirección tampoco alcanza, porque **añadir features de forma
acumulativa confunde efectos de orden**.

| **Dirección**                                | **Configuraciones**                                                                              | **Qué mide**                                                                                                                                                                                 |
|----------------------------------------------|--------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **Acumulativa** (hacia arriba)               | Solo colaborativo → + metadata original → + atributos IA → + embeddings de imagen → + ambos.     | El aporte incremental de cada grupo **dado lo anterior**. Responde: ¿vale la pena añadir esto sobre lo que ya tengo?                                                                         |
| **Leave-one-out** (desde el modelo completo) | Modelo completo menos atributos IA; completo menos embeddings; completo menos metadata original. | La contribución marginal de cada grupo **dados todos los demás**. Responde: ¿qué pierdo si quito esto? Es la pregunta que importa cuando las features son parcialmente redundantes entre sí. |

**9.3.2 El régimen de metadata incompleta**

Segunda mitad del experimento, correspondiente a H3b. Se enmascara la
metadata comercial de una fracción del catálogo —simulando producto
recibido de proveedor sin ficha— y se mide cuánto del desempeño perdido
recuperan los atributos generados por IA.

- **Mecanismo documentado:** fracción enmascarada, criterio de selección
  de los artículos afectados (aleatorio estratificado, o sesgado hacia
  artículos nuevos para imitar el caso real) y campos suprimidos.

- **Tres configuraciones por nivel de enmascaramiento:** con metadata
  completa (referencia), con metadata enmascarada y sin sustituto, y con
  metadata enmascarada más atributos de IA como sustituto.

- **Declaración explícita:** es una intervención del analista sobre los
  datos, no una condición observada. Se reporta siempre como simulación,
  y el informe no traslada su resultado a una afirmación sobre el
  catálogo real de H&M.

- **Lectura esperada:** si los atributos IA recuperan una parte medible
  del desempeño perdido, eso es evidencia directa de la propuesta de
  valor del Smart Tagging — y es una evidencia que el régimen de
  metadata completa no puede producir por construcción.

**10. Métricas**

Las métricas se organizan en cinco niveles. El error clásico en este
tipo de proyecto es reportar solo el primero; el error opuesto —prometer
el cuarto sin los datos para calcularlo— es peor, porque invalida todo
lo demás.

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<tbody>
<tr class="odd">
<td><p><strong>Regla transversal de reporte</strong></p>
<p>Toda métrica de esta sección se reporta <strong>desagregada por nivel
de evidencia del atributo</strong> (A, B o C, según la sección 7.6) y
<strong>por pista de entrada</strong> (imagen sola, texto solo,
multimodal, según la sección 7.7). Nunca se promedian niveles distintos
en una misma cifra, y en el nivel C solo se reporta precisión sobre
muestra revisada: allí el recall no es calculable, de modo que un F1 de
nivel C sería una cifra inventada.</p></td>
</tr>
</tbody>
</table>

**10.1 Nivel 1 — Calidad del tagging**

| **Métrica**                                                | **Definición y uso**                                                                                                        | **Por qué está aquí**                                                                                                                                                                                                                     |
|------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Precision, Recall y F1 **por atributo**                    | Calculadas de forma independiente para cada atributo del esquema, no solo agregadas.                                        | Sharma & Karnick muestran que precisión y recall se mueven en direcciones opuestas al variar K (en deportes, precisión 0,819 con recall 0,210). Un F1 agregado esconde exactamente la información que se necesita para decidir el umbral. |
| F1 macro, micro y **ponderado**                            | Macro trata todos los atributos igual; micro pondera por volumen; ponderado promedia el F1 de cada etiqueta por su soporte. | Salminen et al. usan F1 ponderado explícitamente por el desbalance de la distribución de keywords. Un catálogo de moda tiene la misma forma: pocos atributos muy frecuentes y una cola larga.                                             |
| mAP (mean Average Precision)                               | Promedio del área bajo la curva precisión-recall por atributo.                                                              | Es la métrica que no depende de un umbral, y por tanto la correcta para comparar modelos antes de decidir el punto de operación.                                                                                                          |
| Hamming loss y subset accuracy                             | Fracción de etiquetas mal asignadas; y fracción de productos con el conjunto de etiquetas exactamente correcto.             | Subset accuracy es la métrica severa y la más cercana a "el SKU quedó bien etiquetado". Hamming loss captura el error parcial.                                                                                                            |
| Tasa de cobertura (success rate)                           | Porcentaje de productos a los que el modelo asigna al menos una etiqueta con confianza sobre el umbral.                     | Salminen et al. reportan 99,6% en web y 96,1% en YouTube. Es la métrica operativa: un modelo preciso que no se atreve a etiquetar el 40% del catálogo no resuelve el problema de negocio.                                                 |
| Error de calibración esperado (ECE) y curvas de fiabilidad | Mide si una confianza de 0,8 corresponde efectivamente a un 80% de aciertos.                                                | Sin calibración, el umbral de aceptación y la cola de revisión humana no tienen fundamento. Es el prerrequisito de OE6.                                                                                                                   |
| Número medio de etiquetas asignadas vs. humanas            | Comparación de la distribución de cantidad de etiquetas por producto entre modelo y anotador.                               | Es el diagnóstico de Salminen et al. (μ predicho 4,10 vs. μ real 3,54) que reveló el sesgo de anclaje humano y el ground truth incompleto.                                                                                                |

**10.2 Nivel 2 — Acuerdo humano-máquina**

Este nivel es lo que separa un proyecto de visión por computador de un
proyecto de ciencia de datos aplicada, y se replica del diseño de
Salminen et al.

muestra aleatoria de productos del catálogo

│

┌──────────────┼──────────────┐

▼ ▼ ▼

anotador 1 anotador 2 anotador 3 ──▶ acuerdo humano-humano

│

se reemplaza un anotador por el modelo ──▶ acuerdo humano-máquina

│

▼

brecha = acuerdo(h-h) − acuerdo(h-m)

En el estudio de referencia, el acuerdo entre tres codificadores humanos
fue de **77,7%** y el acuerdo promedio al reemplazar a un humano por la
máquina fue de **70,4%**: una brecha de **10,4 puntos porcentuales** que
los autores interpretaron como evidencia de generalización razonable,
dado que los propios humanos no coinciden entre sí.

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<tbody>
<tr class="odd">
<td><p><strong>Criterio derivado para este proyecto</strong></p>
<p>Reportar siempre las dos cifras juntas. Un acuerdo humano-máquina del
70% sin el dato del 78% humano-humano al lado es una cifra que se lee
como mediocre; con el contexto, se lee como desempeño cercano al techo
de la tarea. Esta es la comparación que un comité técnico en una
compañía retail va a pedir, y la que convierte "el modelo tiene F1 de
0,7" en "el modelo etiqueta casi tan consistentemente como una
persona".</p></td>
</tr>
</tbody>
</table>

**10.2.1 Por qué aquí NO se usa el porcentaje simple de acuerdo**

Salminen et al. usan porcentaje simple y lo justifican de forma
explícita: con un inventario de 799 keywords, la probabilidad de que dos
evaluadores coincidan por azar es pequeña. **Esa justificación no se
sostiene en este proyecto.** En moda el vocabulario controlado por
atributo es corto —ocho o diez colores, unas pocas categorías de
prenda—, así que el acuerdo por azar es alto y el porcentaje simple
infla el resultado de forma sistemática.

Heredar su elección de métrica sin heredar su justificación sería un
error metodológico. El proyecto usa un **estadístico corregido por
azar** —alfa de Krippendorff o kappa de Fleiss, según la estructura de
la tarea— y reporta el porcentaje simple solo como cifra secundaria
comparable con la literatura, etiquetada como tal.

**10.2.2 Protocolo de anotación**

"Tres anotadores" no es un protocolo. Si el acuerdo va a cargar con la
credibilidad del proyecto, el procedimiento tiene que ser reproducible y
defendible.

| **Elemento**         | **Especificación**                                                                                                                                                                                                                                |
|----------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Guía de anotación    | Documento con definición operativa de cada atributo, valores admitidos, casos límite resueltos y ejemplos positivos y negativos. Se versiona junto a la taxonomía.                                                                                |
| Piloto               | Ronda previa sobre una muestra pequeña para detectar ambigüedades de la guía. Se mide el acuerdo del piloto, se corrige la guía y solo entonces se anota la muestra definitiva.                                                                   |
| Perfil de anotadores | Para atributos de nivel A basta criterio general. Para atributos finos —silueta, escote, tipo de manga, material aparente— se requieren anotadores con criterio de moda: un evaluador sin ese criterio produce ruido, no desacuerdo informativo.  |
| Muestra              | **Estratificada por frecuencia de atributo y por dificultad**, no aleatoria. Una muestra aleatoria contendría casi ningún ejemplo de los atributos de cola, que es justo donde el acuerdo por atributo importa más y donde quedaría incalculable. |
| Tamaño               | Derivado de la precisión deseada del estimador de acuerdo, con suficientes instancias por atributo para calcularlo a nivel de atributo y no solo agregado.                                                                                        |
| Adjudicación         | Los desacuerdos se resuelven en una ronda de adjudicación documentada, con el criterio de resolución registrado.                                                                                                                                  |
| Reporte              | Acuerdo **por atributo** además del agregado, con el estadístico corregido por azar y su intervalo.                                                                                                                                               |

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<tbody>
<tr class="odd">
<td><p><strong>El beneficio que este ejercicio paga dos
veces</strong></p>
<p>La adjudicación produce, para esa muestra, un ground truth
<strong>mejor que la metadata original del catálogo</strong>. Eso
habilita dos cosas de una sola inversión: sirve como patrón oro para la
evaluación de nivel A, y al compararlo con la metadata de H&amp;M
permite <strong>cuantificar cuán incompleta está</strong> esa metadata —
que es el hallazgo 1 de Salminen et al. (μ predicho 4,10 vs. μ real
3,54) convertido en una medición propia sobre el dominio de moda, en
lugar de una cita prestada de otro dominio.</p></td>
</tr>
</tbody>
</table>

**10.3 Nivel 3 — Descubrimiento y recomendación**

| **Ámbito**                         | **Métricas**                                                                                                                          | **Notas de medición**                                                                                                                                                                                                  |
|------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Búsqueda semántica                 | Precision@K, Recall@K, NDCG@K (K = 5, 10, 20), MRR; latencia p50 y p95; recall del índice aproximado frente a búsqueda exacta.        | Siempre contra la línea base de filtros por metadata, y **siempre sobre juicios humanos obtenidos por pooling a ciegas**, no sobre reglas derivadas de la metadata (sección 9.2). Desagregado por familia de consulta. |
| Recomendación                      | **MAP@12** (métrica oficial del dataset principal), Recall@12, NDCG@12; cobertura de catálogo y novedad de las recomendaciones.       | Partición temporal obligatoria. Diferencia entre modelo A y B con intervalo de confianza por bootstrap sobre clientes, no solo la diferencia puntual.                                                                  |
| Análisis de segmento               | MAP@12 desagregado por cuantil de frecuencia de interacción del artículo y del cliente; desempeño específico en artículos nuevos.     | Es donde se prueba H3a. Si la ganancia global es pequeña pero la de cold-start es grande, ese es el hallazgo del proyecto y debe reportarse como tal.                                                                  |
| **Régimen de metadata incompleta** | MAP@12 en tres configuraciones: metadata completa, metadata enmascarada sin sustituto, y enmascarada con atributos IA como sustituto. | Es donde se prueba **H3b**, la hipótesis principal del Experimento 3. Se reporta siempre declarado como simulación, con la fracción y el mecanismo de enmascaramiento documentados (sección 9.3.2).                    |
| Ablación de features               | En dos direcciones: acumulativa (colaborativo → +metadata → +tags IA → +embeddings) y leave-one-out desde el modelo completo.         | Sin ablación no se puede afirmar que la ganancia viene del Smart Tagging. Sin la dirección leave-one-out no se distingue el aporte propio de una feature del efecto del orden en que se añadió (sección 9.3.1).        |

**10.4 Nivel 4 — Métricas operativas y de negocio (proxy)**

| **Métrica**                           | **Cómo se calcula en este proyecto**                                                                                                    | **Referencia de industria**                                                                                                                               |
|---------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------|
| Segundos por imagen y throughput      | Medición directa de inferencia en lote y en línea, por modelo.                                                                          | Pixyle reporta 0,2 s por imagen y capacidad de 336.000 imágenes diarias.                                                                                  |
| Horas humanas evitadas por 1.000 SKU  | Estimación: (tiempo manual por producto × 1.000) − (tiempo de inferencia + tiempo de revisión de la cola de baja confianza).            | Pixyle: ≈3 min por producto manual, ≈50 h por 1.000 productos; 20–40 h desperdiciadas por 1.000 SKU.                                                      |
| Costo por 1.000 SKU                   | Costo real de cómputo del proyecto (GPU-hora × tarifa) más el costo de la revisión humana residual, contra el costo manual equivalente. | Pixyle: USD ≈1.000 por lote manual de 1.000 productos a USD 20/hora; hasta 80% de reducción de costo con IA.                                              |
| Completitud de atributos del catálogo | Porcentaje de pares (SKU, atributo) poblados antes y después del sistema.                                                               | Es el equivalente medible del problema que Salminen et al. cuantifican como 39,8% de contenido sin clasificar.                                            |
| Tasa de revisión manual               | Porcentaje de predicciones que caen bajo el umbral y entran a la cola humana.                                                           | Métrica propia del proyecto; define el costo operativo del sistema en régimen.                                                                            |
| Consistencia del etiquetado           | Varianza de atributos asignados a productos visualmente equivalentes (duplicados o variantes de color del mismo modelo).                | Mide directamente el problema de "discrepancia en los tags" que describen Sharma & Karnick, y que la anotación manual no puede resolver por construcción. |

**10.5 Nivel 5 — Monitoreo en producción sin etiquetas**

Un sistema en operación no tiene etiquetas: nadie anota manualmente el
catálogo para que el modelo pueda medirse. Por lo tanto **el F1 no es
observable en vivo**, y cualquier diseño que dependa de una "alerta por
caída de F1" describe un control que no se puede implementar. El
monitoreo real se organiza en dos bucles con cadencias distintas.

| **Bucle**                  | **Señales**                                                                                                                                                                                                                                                                                         | **Cadencia**                                     | **Función**                                                                                                                                                              |
|----------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|--------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **Rápido — sin etiquetas** | Distancia entre la distribución de embeddings de entrada actual y la de referencia; desplazamiento de la distribución de atributos predichos; desplazamiento de la distribución de confianza; volumen y composición de la cola de baja confianza; tasa de productos que no encajan en la taxonomía. | Continua o diaria.                               | **Alerta temprana.** No mide desempeño, mide que algo cambió en la entrada o en el comportamiento del modelo. Es la señal que dispara una auditoría fuera de calendario. |
| **Lento — con etiquetas**  | F1 y precisión por atributo estimados sobre una muestra revisada por humanos, con intervalo de confianza.                                                                                                                                                                                           | Periódica, anclada al calendario de colecciones. | **Es la única fuente legítima de F1 en producción.** Alimenta la decisión de reentrenamiento.                                                                            |

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<tbody>
<tr class="odd">
<td><p><strong>Dos detalles sin los cuales el monitoreo
miente</strong></p>
<p><strong>La muestra de auditoría se extrae de la población completa,
nunca de la cola de revisión.</strong> La cola está sesgada por
construcción hacia los casos difíciles —es su razón de existir—, así que
estimar F1 con ella subestima el desempeño de forma sistemática y
produce reentrenamientos innecesarios. Son dos muestras distintas con
dos propósitos distintos.</p>
<p><strong>La cadencia y el tamaño de muestra se fijan de
antemano</strong> para que la estimación tenga un intervalo de confianza
utilizable. Una auditoría que produce un número sin margen de error es
peor que no tener número, porque invita a reaccionar ante ruido.</p>
<p>Un detalle favorable de este dominio: en moda la deriva es
<strong>estacional y en parte predecible</strong>. Eso permite programar
las auditorías alrededor de los cambios de colección —donde se espera el
desplazamiento— en lugar de esperar pasivamente una alerta.</p></td>
</tr>
</tbody>
</table>

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<tbody>
<tr class="odd">
<td><p><strong>Métricas que este proyecto NO va a reportar</strong></p>
<p>Tasa de conversión, CTR, valor promedio de pedido, tasa de devolución
y cualquier variante de uplift en ventas. Los datasets disponibles no
contienen impresiones ni clickstream, por lo que no existe contrafactual
para calcularlas. Las cifras de la industria citadas en la sección 2
(8–12% de uplift en conversión, 30% de incremento en conversión, 20% de
reducción de devoluciones) permanecen como <strong>contexto de mercado
atribuido a su fuente</strong>, nunca como resultado del proyecto.
Confundir estas dos cosas es el fallo más frecuente —y el más costoso en
credibilidad— en portafolios de ciencia de datos aplicada.</p></td>
</tr>
</tbody>
</table>

**11. Criterios de éxito del proyecto**

Los criterios se dividen en dos grupos: los que pueden fijarse hoy
porque dependen del diseño, y los que se calibran al cerrar la línea
base porque dependen de la dificultad real de la tarea. Comprometer hoy
un F1 objetivo sería inventar un número.

**Criterios fijables ahora**

| **Criterio**            | **Umbral**                                                                                                                            | **Verificación**                                    |
|-------------------------|---------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------|
| Reproducibilidad        | El pipeline completo se ejecuta de punta a punta desde un repositorio limpio con un comando documentado.                              | Ejecución en entorno nuevo por un tercero, o en CI. |
| Trazabilidad de datos   | Cada split, dataset y modelo tiene versión y hash registrados; la taxonomía está versionada.                                          | Auditoría del repositorio DVC/MLflow.               |
| Comparabilidad          | Los 4+ enfoques de tagging se evalúan sobre los mismos splits y métricas, con costo computacional reportado.                          | Tabla comparativa única en el informe.              |
| Honestidad metodológica | Partición temporal en el experimento de recomendación; intervalos de confianza en toda diferencia reportada; limitaciones declaradas. | Revisión del informe contra esta lista.             |
| Evaluación humana       | Muestra anotada por al menos tres personas con acuerdo humano-humano y humano-máquina reportados juntos.                              | Entregable de anotación + cálculo de acuerdo.       |
| Sistema operable        | API desplegada que responde con atributos y confianza; monitoreo con alerta por caída de desempeño.                                   | Demo funcional + captura del dashboard.             |
| Licencias resueltas     | Términos de uso de cada dataset verificados en la fuente primaria y citados en el repositorio antes de la descarga.                   | Sección de licencias del repositorio.               |

**Criterios a calibrar al cerrar la línea base (Fase 3)**

| **Criterio**                                          | **Punto de anclaje para la calibración**                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
|-------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| F1 ponderado objetivo del modelo de tagging (nivel A) | **El anclaje es la línea base local, no una cifra de otra publicación.** Los umbrales se fijan como mejora relativa sobre el método de literatura reimplementado y evaluado en los mismos splits (L1 y L1b de la sección 9.1). Las cifras publicadas en otros dominios —0,70 de Salminen et al. en contenido de texto, 0,345 de Sharma & Karnick en prendas de Amazon— **no son umbrales a superar**: los propios autores del primero advierten que no existe un valor universal de F1 y que el umbral es específico del dominio, y el segundo mide una tarea de forma distinta (sección 9.1).                                                  |
| Brecha máxima aceptable de acuerdo humano-máquina     | **Relativa al techo humano medido en este catálogo, no un valor fijo.** La brecha de 10,4 puntos porcentuales de Salminen et al. (77,7% vs. 70,4%) es de tópicos de noticias, y trasladarla crea un riesgo invertido: en atributos finos de moda el acuerdo humano-humano será probablemente **más bajo** —¿"midi" o "maxi"?, ¿"beige" o "taupe"?—, de modo que un techo humano bajo hace fácil cumplir una brecha fija por la razón equivocada. El criterio correcto es que el acuerdo humano-máquina caiga **dentro del intervalo de confianza del acuerdo humano-humano** medido con el estadístico corregido por azar de la sección 10.2.1. |
| Mejora mínima en MAP@12                               | Se fija tras medir la varianza del estimador por bootstrap. Un criterio definido antes de conocer la varianza no distingue una mejora real de ruido. Se fijan dos criterios distintos: uno para H3a (metadata completa) y uno para H3b (metadata enmascarada).                                                                                                                                                                                                                                                                                                                                                                                  |
| Porcentaje de catálogo auto-etiquetado sin revisión   | Se deriva de la curva cobertura-precisión una vez calibrada la confianza, **y solo para atributos de nivel A y B**. En nivel C no hay cobertura medible, únicamente precisión sobre muestra (sección 7.6). La referencia de industria (96–99,6% de cobertura en Salminen et al.) es de contenido de texto y no es trasladable sin medición propia.                                                                                                                                                                                                                                                                                              |

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<tbody>
<tr class="odd">
<td><p><strong>Regla de congelación: el criterio se fija antes de ver el
modelo final</strong></p>
<p>Los umbrales se calibran al cerrar la línea base en F3 y <strong>se
congelan en el repositorio con marca de tiempo antes de entrenar el
modelo final</strong>. Sin esa congelación, "calibrar después de la
línea base" degenera en elegir el criterio que el resultado obtenido
satisface — que es racionalización a posteriori con apariencia de
método.</p>
<p>La diferencia entre calibrar y racionalizar no está en el momento del
cálculo sino en el orden respecto a la observación del resultado: el
criterio debe existir, escrito y versionado, mientras el resultado final
todavía es desconocido. Si tras ver el resultado hay razones legítimas
para revisar un umbral, se revisa — pero se documenta el cambio, su
motivo y la cifra anterior, y ambas aparecen en el informe.</p></td>
</tr>
</tbody>
</table>

**12. Cómputo: hardware disponible y estrategia híbrida**

**12.1 El hardware real y lo que implica**

| **Recurso**              | **Disponible**                                                                                   | **Lectura para el proyecto**                                                                                                                                           |
|--------------------------|--------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| GPU                      | Gráficos integrados Intel Iris Xe. **Sin VRAM dedicada.**                                        | No hay entrenamiento de redes profundas en local. Es una unidad de inferencia modesta, no de entrenamiento.                                                            |
| Memoria                  | ≈15,8 GB de memoria compartida accesibles a los gráficos, de los cuales 1,2 GB en uso en reposo. | La memoria es compartida entre sistema, aplicaciones y gráficos: **es el recurso escaso del proyecto**, y el presupuesto real de trabajo está por debajo de esa cifra. |
| Aceleración aprovechable | OpenVINO y ONNX Runtime tienen soporte para gráficos integrados Intel.                           | Permiten inferencia local razonable de codificadores medianos. Es el camino para la demo y para el servicio de inferencia, no para el entrenamiento.                   |

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<tbody>
<tr class="odd">
<td><p><strong>La consecuencia directa</strong></p>
<p>El plan no puede asumir GPU local. Pero esto <strong>no recorta los
tres experimentos</strong>: los reordena. El entrenamiento y la
extracción masiva de embeddings se hacen en GPU gratuita en la nube; el
resto del proyecto —que es la mayor parte— es trabajo de CPU y memoria:
sondeo lineal sobre embeddings ya calculados, factorización matricial,
LightGBM, evaluación, calibración, búsqueda vectorial y la demo. La
restricción real que aparece no es la GPU, es <strong>la memoria de 16
GB frente a un dataset de ~34,6 GB</strong>.</p></td>
</tr>
</tbody>
</table>

**12.2 Reparto del trabajo**

| **Dónde**                                                                  | **Qué se hace ahí**                                                                                                                                                                                                                            | **Por qué ahí**                                                                                                                                                                                                                                                                                                                                                                                           |
|----------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **Nube gratuita con GPU** — notebooks de la plataforma que aloja los datos | Extracción de embeddings de todo el subconjunto de imágenes; inferencia zero-shot a escala; LoRA y ajuste fino de la cabeza y del codificador; segmentación si entra en el alcance.                                                            | Es donde hay GPU sin costo **y** donde los datos de H&M ya residen, lo que evita moverlos y encaja con la cláusula de redistribución (sección 7.4). Dos restricciones, una sola solución.                                                                                                                                                                                                                 |
| **Local (CPU + Iris Xe)**                                                  | Sondeo lineal y cabezas multi-etiqueta sobre embeddings cacheados; recomendación (ALS/BPR y ranker por gradient boosting); toda la evaluación, calibración y análisis de errores; índice vectorial; API de inferencia con OpenVINO/ONNX; demo. | Nada de esto necesita GPU. Con los embeddings ya calculados, entrenar una cabeza multi-etiqueta o un ranker es cuestión de minutos en CPU. Es también donde se itera con libertad, sin límite de sesión.                                                                                                                                                                                                  |
| **API externa de pago (opcional y acotada)**                               | Modelo de visión-lenguaje generativo para la cola larga de atributos y para descripciones, sobre una muestra pequeña.                                                                                                                          | Un VLM local queda descartado por memoria. Se usa como experimento acotado con presupuesto declarado, sobre muestra, no sobre el catálogo. **Advertencia:** enviar imágenes de H&M a un servicio externo es una transmisión de datos a un tercero; antes de hacerlo hay que verificar si la cláusula de redistribución lo permite. Si hay duda, este experimento se hace únicamente con imágenes propias. |

**12.3 Decisiones de ingeniería que el hardware vuelve obligatorias**

1.  **El caché de embeddings es infraestructura crítica, no una
    optimización.** Se calcula una vez en la nube, se persiste, y todo
    el trabajo posterior se apoya en él. Sin esto el proyecto no es
    ejecutable con este hardware.

2.  **Subconjunto estratificado desde el primer día.** El catálogo
    completo no cabe en memoria. Se define un subconjunto con
    representación controlada por categoría de producto y por frecuencia
    de atributo, y se documenta el criterio de muestreo como parte del
    entregable de F2 — un subconjunto bien muestreado y declarado es
    metodología; uno improvisado es un sesgo no medido.

3.  **Las transacciones se consultan, no se cargan.** DuckDB sobre
    Parquet permite agregaciones y construcción de features sin traer el
    histórico completo a memoria. Cargar transactions_train.csv con
    pandas en 16 GB compartidos es la primera forma de bloquear la
    máquina.

4.  **Checkpointing agresivo en la nube.** Las sesiones gratuitas
    expiran. Todo artefacto —embeddings, pesos, métricas— se persiste en
    cuanto se produce, y el pipeline se diseña para reanudar desde el
    último punto guardado en lugar de reiniciar.

5.  **El costo de inferencia local se mide y se reporta.** La métrica de
    segundos por imagen de la sección 10.4 se calcula sobre este
    hardware con OpenVINO. Es una cifra honesta y además interesante:
    demuestra que el servicio corre en una máquina sin GPU dedicada, que
    es un argumento de producto real.

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<tbody>
<tr class="odd">
<td><p><strong>Lo que este hardware sí descarta del plan</strong></p>
<p>Ajuste fino de codificadores grandes en local, VLM ejecutados
localmente, entrenamiento desde cero (que de todos modos era la opción
incorrecta — el transfer learning es lo indicado, como señalan Sharma
&amp; Karnick) y recomendación sobre el histórico completo en memoria.
Ninguno de estos era necesario para responder las tres preguntas de
investigación; conviene tenerlo por escrito para no reintroducirlos por
ambición a mitad del proyecto.</p></td>
</tr>
</tbody>
</table>

**13. Fases, entregables y definición de terminado**

**13.1 Fases y criterio de cierre**

El plan se organiza por fases con dependencia lógica y criterio de
cierre (*definition of done*), sin calendario rígido. Cada fase produce
un artefacto verificable: si una fase no deja artefacto, no está
terminada. La sección 13.2 marca cuáles de estas fases forman el MVP
comprometido y cuáles son extensiones.

<table>
<colgroup>
<col style="width: 13%" />
<col style="width: 32%" />
<col style="width: 27%" />
<col style="width: 27%" />
</colgroup>
<thead>
<tr class="header">
<th><strong>Fase</strong></th>
<th><strong>Actividades</strong></th>
<th><strong>Entregables</strong></th>
<th><strong>Definición de terminado</strong></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><p><strong>F0</strong></p>
<p>Encuadre y licencias</p></td>
<td>Pegar en el repositorio el <strong>texto literal</strong> de la
cláusula de datos de H&amp;M y de los términos de Fashionpedia. Resolver
la zona gris de publicación de pesos ajustados. Definir la pregunta de
negocio y las tres hipótesis. Montar el repositorio, DVC y MLflow.
Configurar el entorno de nube gratuita y el entorno local con
OpenVINO/ONNX.</td>
<td>Documento de encuadre; sección de licencias con texto literal;
<strong>contrato de publicación (tabla 7.4) en el README</strong>;
repositorio y entornos inicializados.</td>
<td>La cláusula está citada literalmente y no de segunda mano; el
contrato de publicación está escrito antes de que exista algún archivo
que publicar. Ninguna descarga antes de este cierre.</td>
</tr>
<tr class="even">
<td><p><strong>F1</strong></p>
<p>Taxonomía y ontología</p></td>
<td>Diseñar el esquema de atributos con vocabulario controlado y
cardinalidad. Mapear Fashionpedia ↔︎ H&amp;M. Definir qué campos son
ground truth y cuáles se ocultan al modelo.</td>
<td>Esquema versionado (JSON/YAML); tabla de mapeo; diccionario de
datos.</td>
<td>Todo atributo tiene definición operativa, valores admitidos y fuente
de verdad. Es la capa 0 de la arquitectura y bloquea todo lo demás.</td>
</tr>
<tr class="odd">
<td><p><strong>F2</strong></p>
<p>Datos y EDA</p></td>
<td>Ingesta a bronze/silver/gold. Análisis de distribución y desbalance
por atributo. Análisis temporal de transacciones y detección de deriva
estacional. Congelar splits con separación temporal.</td>
<td>Pipeline reproducible; reporte de EDA; splits congelados con
hash.</td>
<td>El pipeline corre de punta a punta con un comando; la distribución
de cada atributo está documentada; los splits no cambian después de este
punto.</td>
</tr>
<tr class="even">
<td><p><strong>F3</strong></p>
<p>Línea base</p></td>
<td>Reproducir la línea base trivial, la visual (CNN profunda + KNN
ponderado) y la textual (TF-IDF + red multi-etiqueta). Precomputar y
persistir embeddings.</td>
<td>Tabla de línea base; caché de embeddings; <strong>calibración de los
umbrales objetivo</strong> de la sección 11.</td>
<td>Existe un número contra el cual comparar todo lo que sigue, obtenido
con un método publicado y no con una estimación.</td>
</tr>
<tr class="odd">
<td><p><strong>F4</strong></p>
<p>Modelo de tagging</p></td>
<td>Zero-shot multimodal con ingeniería de prompts por atributo. Sondeo
lineal y ajuste fino eficiente. Segmentación y atributos localizados si
el cómputo lo permite. VLM para cola larga.</td>
<td>Modelo registrado en MLflow; tabla comparativa con métricas y costo;
análisis de errores por atributo.</td>
<td>Al menos cuatro enfoques comparados sobre los mismos splits;
diferencia frente a línea base con significancia verificada por
bootstrap.</td>
</tr>
<tr class="even">
<td><p><strong>F5</strong></p>
<p>Calibración y human-in-the-loop</p></td>
<td>Calibrar confianza (ECE, curvas de fiabilidad). Fijar umbral por
atributo. Construir la cola de revisión y el ciclo de realimentación al
dataset.</td>
<td>Módulo de calibración; curva cobertura-precisión; cola de revisión
operativa.</td>
<td>Cada atributo tiene umbral justificado; la tasa de revisión manual
está medida y documentada.</td>
</tr>
<tr class="odd">
<td><p><strong>F6</strong></p>
<p>Evaluación humana</p></td>
<td>Redactar la guía de anotación. Correr el piloto y corregir la guía.
Muestrear de forma estratificada por frecuencia y dificultad. Anotar con
evaluadores independientes, con criterio de moda para los atributos
finos. Adjudicar desacuerdos. Calcular acuerdo por atributo con
estadístico corregido por azar.</td>
<td>Guía de anotación versionada; informe del piloto; dataset anotado y
adjudicado; informe de acuerdo por atributo con intervalos;
<strong>medición de la incompletitud de la metadata de H&amp;M</strong>
contra el conjunto adjudicado.</td>
<td>El acuerdo humano-humano y el humano-máquina se reportan juntos, por
atributo, con estadístico corregido por azar (10.2.1). El tamaño de
muestra está justificado por la precisión deseada del estimador, no
elegido a conveniencia.</td>
</tr>
<tr class="even">
<td><p><strong>F7</strong></p>
<p>Búsqueda semántica</p></td>
<td>Construir el índice vectorial. Definir familias de consultas y
ground truth de relevancia. Comparar contra búsqueda por filtros de
metadata. Medir latencia.</td>
<td>Índice + endpoint; set de consultas anotado; informe
comparativo.</td>
<td>NDCG@10 reportado contra la línea base de metadata, desagregado por
familia de consulta, con latencia p95.</td>
</tr>
<tr class="odd">
<td><p><strong>F8</strong></p>
<p>Valor de negocio</p></td>
<td>Entrenar modelo A (base) y modelo B (enriquecido). Evaluar MAP@12
con partición temporal. Ablación de features. Desagregación por
cold-start.</td>
<td>Dos recomendadores; informe de A/B offline con intervalos de
confianza; análisis de segmento.</td>
<td>La diferencia está reportada con intervalo de confianza y la
ablación aísla el aporte de los atributos IA.</td>
</tr>
<tr class="even">
<td><p><strong>F9</strong></p>
<p>Producto y MLOps</p></td>
<td>API con contrato OpenAPI, sirviendo con OpenVINO/ONNX en el hardware
local. Contenerización. Dashboard con las señales de deriva <strong>sin
etiquetas</strong> del bucle rápido. Protocolo de auditoría muestral del
bucle lento, con cadencia y tamaño de muestra definidos. Medición de
segundos por imagen en este hardware. Documento de producto y
monetización.</td>
<td>Servicio desplegado; dashboard de deriva; protocolo de auditoría
documentado; documento de producto y pricing.</td>
<td>La API responde atributos con confianza; las señales de deriva sin
etiquetas están activas; <strong>el F1 proviene de la auditoría muestral
y no de una inferencia en vivo</strong> (10.5); la muestra de auditoría
se extrae de la población, no de la cola.</td>
</tr>
<tr class="odd">
<td><p><strong>F10</strong></p>
<p>Comunicación y publicación</p></td>
<td>Informe técnico final. Demo interactiva <strong>con catálogo propio
de imágenes redistribuibles</strong>. Resumen ejecutivo de una página.
Model card. Auditoría del repositorio contra el contrato de publicación
de la sección 7.4 antes de hacerlo público.</td>
<td>Informe; demo pública; resumen ejecutivo; <em>model card</em>;
checklist de publicación firmado.</td>
<td>Un lector técnico puede replicar el resultado y un lector de negocio
entiende qué se demostró y qué no. <strong>Ningún archivo de datos de
H&amp;M, ni derivado suyo, está en el repositorio público</strong> —
verificado archivo por archivo, no por confianza.</td>
</tr>
</tbody>
</table>

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<tbody>
<tr class="odd">
<td><p><strong>Orden que no debe alterarse</strong></p>
<p>F1 (taxonomía) antes de F2 (datos), y F3 (línea base) antes de F4
(modelo). Es exactamente el orden que recomienda Browntape — definir
taxonomía, preparar datos, elegir solución, entrenar, validar, integrar
— y la razón es práctica: sin taxonomía cerrada no se sabe qué se está
prediciendo, y sin línea base cualquier resultado del modelo grande es
un número sin referencia.</p></td>
</tr>
</tbody>
</table>

**13.2 Frontera del MVP y extensiones condicionadas**

Once fases que abarcan tagging, segmentación, búsqueda, recomendación,
API, MLOps y monetización son demasiadas para un proyecto individual, y
el resultado previsible de intentarlo todo es una demo superficial en
todo y convincente en nada. Por eso el alcance se parte en dos con una
frontera explícita.

| **Bloque**                                 | **Fases**                                                                                                                                                                       | **Justificación**                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
|--------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **MVP comprometido**                       | F0, F1, F2, F3, F4, F5, F6 y **F8**.                                                                                                                                            | Cubre las preguntas de investigación Q1 (calidad del tagging) y Q3 (valor de negocio), que son las dos que sostienen el proyecto. F8 entra al MVP porque **es el diferenciador**: es lo que separa este trabajo de un ejercicio de visión por computador y lo que lo conecta con negocio. Además es barato en el hardware disponible —factorización matricial y gradient boosting en CPU sobre subconjunto estratificado, con los embeddings ya cacheados— y con la reformulación de H3b es la fase más informativa del plan. |
| **Primera extensión**                      | F7 (búsqueda semántica) y F9 (producto y MLOps).                                                                                                                                | Q2 (descubrimiento) es valiosa pero mucho más reemplazable: hay abundantes demostradores públicos de búsqueda por embeddings, y su ground truth de relevancia exige el protocolo de juicios ciegos de la sección 9.2, que es costoso en tiempo humano. F9 aporta credibilidad de ingeniería, no evidencia de la hipótesis.                                                                                                                                                                                                    |
| **Extensiones condicionadas a resultados** | Segmentación y atributos localizados (L4), modelo de visión-lenguaje generativo (L5), recomendador de dos torres, MLOps de nivel producción, módulos de descripción y alt-text. | Se abordan únicamente con el MVP cerrado y publicado. Cada una es un proyecto en sí misma y ninguna es necesaria para responder Q1 ni Q3.                                                                                                                                                                                                                                                                                                                                                                                     |
| **Cierre y comunicación**                  | F10.                                                                                                                                                                            | Se ejecuta sobre el alcance que efectivamente se cerró, no sobre el planeado. El informe describe lo hecho y declara lo omitido; un alcance recortado y declarado es un proyecto terminado, un alcance completo a medias no lo es.                                                                                                                                                                                                                                                                                            |

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<tbody>
<tr class="odd">
<td><p><strong>El control que ataca el modo de fallo real</strong></p>
<p>El proyecto no se hunde por elegir mal el alcance: se hunde porque
<strong>F4 se expande indefinidamente</strong>, ya que siempre hay otro
modelo que probar y cada intento parece que va a mejorar la cifra. Por
eso F4 cierra con los cuatro enfoques comprometidos en OE3 y una regla
explícita de cierre, con caja de esfuerzo por fase. Añadir un quinto
enfoque es una decisión que se toma después de cerrar F8, no en medio de
F4.</p>
<p>La misma regla protege a F6: el protocolo de anotación se ejecuta una
vez sobre la muestra dimensionada, no se amplía porque los resultados
sean interesantes.</p></td>
</tr>
</tbody>
</table>

**14. Riesgos y mitigaciones**

| **Riesgo**                                                                                                                                                                                    | **Impacto**                                                                                                                | **Mitigación**                                                                                                                                                                                                                                                         |
|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **Redistribución involuntaria de datos restringidos.** Un CSV, un .npy de embeddings o una carpeta de imágenes que entra al repositorio público por descuido o por un git add amplio.         | Crítico — incumple la cláusula de H&M y compromete el proyecto completo, no solo ese archivo.                              | Contrato de publicación escrito en F0 (sección 7.4); .gitignore que excluya por extensión y por carpeta de datos desde el primer commit; datos fuera del árbol del repositorio; auditoría archivo por archivo en F10 antes de publicar. La confianza no es un control. |
| **Confundir permiso de uso con permiso de redistribución.** Asumir que "es educativo y sin ánimo de lucro" habilita publicar los datos.                                                       | Alto — es el error de razonamiento que produce el riesgo anterior.                                                         | Queda explícito en la sección 7.3: son dos permisos distintos y el segundo no se deriva del primero. La cláusula literal en el README es el recordatorio permanente.                                                                                                   |
| **Imágenes de terceros en la demo pública.** Fashionpedia no es titular del copyright de sus imágenes.                                                                                        | Medio-alto — responsabilidad trasladada al usuario del dataset por sus propios términos.                                   | Demo pública únicamente con catálogo propio o con imágenes de licencia redistribuible verificada activo por activo. Nunca servir archivos de imagen de Fashionpedia directamente.                                                                                      |
| **Hardware sin GPU dedicada y memoria compartida de ≈16 GB** frente a un dataset de ≈34,6 GB.                                                                                                 | Alto — bloquea la ejecución si se planifica como si hubiera GPU.                                                           | Reparto local/nube de la sección 12; caché de embeddings como infraestructura; subconjunto estratificado documentado; DuckDB sobre Parquet en lugar de cargar el histórico en memoria; checkpointing agresivo por expiración de sesiones gratuitas.                    |
| **DeepFashion** restringido a investigación no comercial; **Amazon Reviews 2023** con términos aún sin verificar.                                                                             | Medio — limita su incorporación.                                                                                           | DeepFashion se mantiene opcional bajo la misma regla de no publicación. Amazon no se incorpora hasta verificar y registrar sus términos.                                                                                                                               |
| **Domain shift** entre imágenes de escena (Fashionpedia) y de producto sobre fondo neutro (H&M).                                                                                              | Alto — degrada el desempeño por razones ajenas al modelo y puede llevar a conclusiones equivocadas.                        | Medir el desempeño cruzado explícitamente antes de concluir; usar segmentación para recortar la prenda; reservar un subconjunto anotado de H&M como set de calibración del dominio destino.                                                                            |
| **Ground truth incompleto.** La metadata original omite atributos que el modelo predice correctamente y que se cuentan como falsos positivos.                                                 | Alto — subestima sistemáticamente el desempeño real.                                                                       | Es el hallazgo de Salminen et al. (μ 4,10 vs. 3,54). Se mitiga con la evaluación humana de F6 y reportando la distribución de número de etiquetas modelo vs. humano.                                                                                                   |
| **Desbalance extremo de atributos.** Cola larga con muy pocos ejemplos por atributo.                                                                                                          | Medio-alto — el modelo ignora la cola y el F1 macro se desploma.                                                           | F1 ponderado como métrica principal (siguiendo a Salminen et al.); exclusión documentada de atributos por debajo de un soporte mínimo; VLM zero-shot para la cola larga, donde el supervisado no tiene datos.                                                          |
| **Fuga temporal** en la partición de transacciones.                                                                                                                                           | Crítico — produce métricas infladas que no sobreviven revisión.                                                            | Partición temporal obligatoria y documentada; verificación explícita de que ninguna feature del set de entrenamiento se calcula con datos posteriores al corte.                                                                                                        |
| **Concept drift estacional.** La taxonomía y la distribución de atributos cambian con la temporada.                                                                                           | Medio — degrada el modelo en producción.                                                                                   | Referencia: caída de F1 0,700 → 0,625 y Jaccard 0,41 entre años consecutivos en Salminen et al. Mitigación: taxonomía versionada, monitoreo de deriva y disparador de reentrenamiento por umbral desde F9.                                                             |
| **Volumen de datos vs. cómputo disponible.** El dataset principal ronda 34,6 GB.                                                                                                              | Medio — bloquea iteración en escenarios de cómputo limitado.                                                               | Subconjunto estratificado desde el inicio; embeddings precalculados y persistidos; el caché de features es infraestructura, no optimización.                                                                                                                           |
| **Sobre-reclamación de resultados.** Presentar mejora en MAP@12 como uplift en ventas.                                                                                                        | Crítico para la credibilidad del proyecto.                                                                                 | Declaración de alcance en la sección 6.2 y la lista de métricas no reportables en la sección 10.4, repetidas en el informe final y en la *model card*.                                                                                                                 |
| **Mezcla de niveles de evidencia.** Reportar en una misma cifra atributos verificables contra metadata y atributos sin ground truth.                                                          | Alto — produce afirmaciones no sostenibles ("el modelo predice material") que invalidan el resto del informe por contagio. | Niveles A/B/C asignados en OE1 y tablas de métricas separadas por nivel (sección 7.6). El resumen ejecutivo cita solo nivel A. En nivel C, precisión sobre muestra y nunca F1, porque el recall no es calculable.                                                      |
| **Fuga de información** entre entradas de texto o entre campos correlacionados de la metadata y el atributo objetivo.                                                                         | Crítico — produce métricas excelentes y vacías, y es difícil de detectar a posteriori porque el resultado parece bueno.    | Matriz de procedencia congelada antes de entrenar, cubriendo texto→objetivo **y campo→campo** (sección 7.7). Reporte separado de las pistas imagen-sola, texto-solo y multimodal, con la imagen-sola como titular.                                                     |
| **Circularidad en el ground truth de relevancia** de búsqueda: definir la relevancia con reglas de metadata y comparar contra el buscador por filtros.                                        | Alto — el baseline compite contra su propia definición y la comparación no significa nada.                                 | Juicios humanos por pooling a ciegas, con los resultados de ambos sistemas mezclados y barajados. Consultas redactadas fuera del vocabulario controlado (sección 9.2).                                                                                                 |
| **Redundancia de la metadata en H&M.** Los atributos IA duplican columnas que ya existen, así que el Experimento 3 puede dar nulo por diseño del dataset y no por falta de valor del sistema. | Alto — se interpretaría como fracaso de la hipótesis cuando es una limitación del dato.                                    | Régimen de metadata incompleta simulada (H3b, sección 9.3.2), que es donde el Smart Tagging puede mostrar su valor real. Ablaciones en las dos direcciones para atribuir correctamente cualquier mejora.                                                               |
| **Acuerdo humano-máquina inflado por azar** al usar porcentaje simple sobre vocabularios cortos.                                                                                              | Medio-alto — una cifra de acuerdo inflada es peor que ninguna, porque sostiene una conclusión falsa.                       | Estadístico corregido por azar (alfa de Krippendorff o kappa de Fleiss) como métrica principal (sección 10.2.1). El porcentaje simple solo como cifra secundaria etiquetada.                                                                                           |
| **Alucinación del modelo generativo** con JSON válido y contenido semánticamente falso, sin confianza calibrada sobre la cual filtrar.                                                        | Medio-alto — falsa confianza justo en el nivel de atributos con menos ground truth.                                        | El VLM no autoacepta nada: opera como proponente de candidatos y pre-rellenador de la cola humana, y se evalúa por reducción de tiempo de anotación y precisión sobre muestra (nivel L5, sección 9.1).                                                                 |
| **Expansión indefinida de F4.** Siempre hay otro modelo que probar.                                                                                                                           | Alto — es el modo de fallo concreto por el que un plan amplio termina en demo superficial.                                 | Frontera de MVP explícita (sección 13.2), cierre de F4 con los cuatro enfoques comprometidos y caja de esfuerzo por fase. Un quinto enfoque se decide después de cerrar F8.                                                                                            |
| **Racionalización a posteriori de los criterios de éxito**, eligiendo el umbral que el resultado obtenido satisface.                                                                          | Alto — invalida los criterios sin que se note.                                                                             | Regla de congelación de la sección 11: umbrales calibrados en F3, escritos y versionados con marca de tiempo antes de entrenar el modelo final. Toda revisión posterior se documenta con la cifra anterior.                                                            |
| **Sesgo de representación.** Los datasets pueden sub-representar tipos de cuerpo, tonos de piel, tallas o segmentos demográficos.                                                             | Medio-alto — reputacional y ético; puede producir un sistema que etiqueta peor a ciertos segmentos.                        | Análisis de desempeño desagregado donde los metadatos lo permitan; declaración de limitaciones en la *model card*; no afirmar equidad no medida.                                                                                                                       |
| **Alcance que se expande** (visual search, shop-the-look, generación de descripciones, FAQ).                                                                                                  | Medio — el proyecto queda a medias en todo.                                                                                | Los tres experimentos son el alcance comprometido. Todo lo demás está etiquetado como opcional o *stretch* y solo se aborda con los tres experimentos cerrados.                                                                                                        |

**15. Gobierno de datos, ética y documentación**

**15.1 Gobierno**

- **Taxonomía como activo gobernado:** propietario definido, versionado
  semántico, registro de cambios y política de deprecación de atributos.
  Un atributo no se elimina, se marca obsoleto.

- **Linaje de datos:** todo artefacto —dataset, split, modelo, métrica—
  con versión y hash trazables desde el informe final hasta el archivo
  crudo.

- **Separación de ground truth:** los campos de metadata usados como
  verdad se declaran y se ocultan al modelo de forma verificable; una
  fuga aquí invalida el Experimento 1 completo.

- **Datos de cliente:** customers.csv contiene identificadores y edad.
  Se usan solo agregados y se documenta que no se realiza
  reidentificación ni enriquecimiento con fuentes externas.

- **Contrato de publicación:** la tabla de la sección 7.4 vive en el
  README del repositorio y se audita en F10. Los datos residen fuera del
  árbol del repositorio y el .gitignore excluye extensiones y carpetas
  de datos desde el primer commit.

- **Atribución obligatoria:** las anotaciones y la ontología de
  Fashionpedia están bajo CC BY 4.0, lo que exige atribuir al proyecto
  en el repositorio, el informe y cualquier derivado de la taxonomía.
  Las utilidades del dataset bajo BSD 2-Clause conservan su aviso de
  copyright.

- **Transmisión a terceros:** enviar imágenes de H&M a una API externa
  es una transmisión de datos. Solo se hace si la cláusula literal lo
  permite; en caso de duda, el experimento con API se limita a imágenes
  propias.

**15.2 Ética y limitaciones declaradas**

El sistema describe prendas, no personas. Esa frontera se hace explícita
en el diseño: los atributos del esquema se limitan a características del
producto —categoría, color, patrón, silueta, material aparente, detalles
de construcción— y **no incluyen inferencias sobre atributos de la
persona que aparece en la imagen**, ni atractivo, ni tipo de cuerpo, ni
características demográficas. En datasets de street style como
Fashionpedia esa tentación existe y es donde este tipo de proyecto se
vuelve problemático.

La *model card* del entregable final documenta: datos de entrenamiento y
su procedencia, atributos soportados y su desempeño individual,
condiciones bajo las que el modelo se degrada (dominio distinto, prendas
fuera de la taxonomía, oclusión), sesgos conocidos y no medidos, y usos
explícitamente no soportados.

**15.3 Documentación del proyecto**

| **Artefacto**                | **Contenido**                                                                                | **Audiencia**           |
|------------------------------|----------------------------------------------------------------------------------------------|-------------------------|
| README del repositorio       | Cómo ejecutar el pipeline de punta a punta; estructura del proyecto; licencias de los datos. | Técnica                 |
| Diccionario de datos         | Cada campo, su origen, tipo, valores admitidos y si es ground truth.                         | Técnica y de datos      |
| Informe técnico              | Metodología, resultados de los tres experimentos, análisis de errores, limitaciones.         | Técnica                 |
| Model card                   | Desempeño por atributo, condiciones de degradación, sesgos, usos no soportados.              | Técnica y de riesgo     |
| Resumen ejecutivo (1 página) | Qué se demostró, con qué evidencia, qué NO se demostró y qué costaría llevarlo a producción. | Negocio                 |
| Demo interactiva             | Subir una imagen, ver atributos y confianza, buscar por texto, ver recomendaciones.          | Negocio y reclutamiento |

**16. Empaquetado y monetización: benchmark de mercado**

Esta sección responde a la pregunta de cómo una compañía estructura y
monetiza este servicio. El referente analizado es **Pixyle.ai**, cuyo
negocio es precisamente el Smart Tagging para moda.

**16.1 Cómo estructura Pixyle su oferta**

| **Dimensión**            | **Estructura observada**                                                                                                                                                                                                                                                                                                                                                                                      |
|--------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Arquitectura de producto | Dos suites: **Data Foundations** (atributos estructurados, títulos, descripciones) y **Discovery Engine** (FAQs, tags de búsqueda, contenido SEO, texto alternativo). Sobre ellas, módulos adicionales: localización multi-idioma, campos personalizados, variantes de título y descripción, operaciones sobre activos visuales, adaptación a marketplace y mayorista, y almacenamiento de activos digitales. |
| Posicionamiento          | "Un sistema de inteligencia, no un sistema de registro": complementa la infraestructura existente del cliente en lugar de reemplazarla. Es una decisión estratégica —reduce drásticamente la fricción de adopción— y explica el énfasis en integraciones.                                                                                                                                                     |
| Integraciones            | PIM (Akeneo, inRiver, Salsify), plataformas de ecommerce (Shopify, Magento, Webflow) y DAM (Bynder, Cloudinary). Plataforma dirigida por API.                                                                                                                                                                                                                                                                 |
| Diferenciación           | "Nativo de moda por diseño", entrenado exclusivamente con datos de moda desde 2018, con taxonomía propia de más de 30.000 atributos y sinónimos específicos de moda, y procesamiento visual-primero.                                                                                                                                                                                                          |
| Argumento de valor       | 95% de incremento de productividad, 8–12% de uplift en conversión, 10x de retorno, 336.000 imágenes procesadas al día, hasta 80% de reducción de costo frente al etiquetado manual. Casos: Otrium con 90% de mejora en eficiencia; un revendedor que pasó de 2,5% a 15–20% de ingresos.                                                                                                                       |
| Cliente objetivo         | Marcas y retailers de moda, incluyendo operaciones de escala empresarial con catálogos multi-SKU complejos y problemas de calidad de datos de proveedores.                                                                                                                                                                                                                                                    |

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<tbody>
<tr class="odd">
<td><p><strong>Vacío de información sobre precios</strong></p>
<p>No fue posible verificar los precios ni la estructura de tarifas de
Pixyle con la información disponible públicamente: la compañía no
publica una página de precios accesible. Lo que sí se puede afirmar es
la <strong>estructura de empaquetado</strong> (dos suites más módulos
adicionales sobre una plataforma dirigida por API) y la <strong>unidad
natural de consumo</strong> que se deduce de sus propias métricas — la
imagen procesada. Cualquier cifra de precio en este plan sería
inventada, y por eso no aparece.</p></td>
</tr>
</tbody>
</table>

**16.2 Lecciones aplicables al diseño de este proyecto**

1.  **El producto es el atributo estructurado, no el modelo.** La suite
    base de Pixyle vende atributos, títulos y descripciones; el modelo
    es el medio. El demostrador debe entregar un contrato de datos
    limpio (esquema de atributos con confianza), no solo un notebook con
    métricas.

2.  **La modularidad es la forma del negocio.** Suites más add-ons
    permiten vender un módulo y expandir después. En el proyecto esto se
    traduce en una arquitectura donde tagging, búsqueda semántica y
    generación de descripciones son servicios separados sobre la misma
    capa de representación — lo que además es la decisión técnica
    correcta.

3.  **La integración es la barrera real de adopción.** Un sistema que no
    escribe en el PIM del cliente no se usa. El demostrador debe al
    menos exponer el contrato de sincronización, aunque no se integre
    con un PIM real.

4.  **La especialización de dominio es el foso defensivo.** Una
    taxonomía de más de 30.000 atributos de moda no se replica con un
    modelo generalista. Esto valida la decisión de F1: invertir en la
    taxonomía es invertir en lo que diferencia el sistema.

5.  **El throughput es parte de la propuesta de valor.** 336.000
    imágenes diarias y 0,2 segundos por imagen son argumentos de venta,
    no notas al pie de ingeniería. De ahí que el costo computacional sea
    métrica de primer nivel en la sección 10.4.

**16.3 Modelo de monetización propuesto para el demostrador**

Propuesta hipotética, con supuestos declarados y sin cifras de precio
por las razones anteriores. Se incluye porque un proyecto de vitrina
gana mucho al mostrar que el autor entiende cómo se vende lo que
construyó.

| **Componente**                                      | **Unidad de cobro propuesta**                       | **Racional**                                                                                                                                         |
|-----------------------------------------------------|-----------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------|
| Tagging de catálogo (lote)                          | Por imagen o SKU procesado, con tramos por volumen. | Es la unidad que el cliente ya entiende porque es la unidad de su costo manual (≈3 min por producto). Permite comparación directa con el status quo. |
| Tagging en tiempo real (API)                        | Por llamada, con cuota mensual incluida.            | Separa el caso de uso de carga masiva inicial del de nuevos ingresos continuos, que es recurrente y predecible.                                      |
| Búsqueda semántica y visual                         | Suscripción por catálogo activo.                    | El valor escala con el tamaño del catálogo indexado, no con el número de consultas.                                                                  |
| Módulos de contenido (descripciones, alt-text, SEO) | Por activo generado o suscripción por idioma.       | Replica la estructura de add-ons observada en el referente de mercado.                                                                               |
| Taxonomía personalizada y onboarding                | Servicio profesional único.                         | El mapeo a la taxonomía propia del cliente es trabajo humano especializado y no se automatiza; cobrarlo aparte evita subsidiarlo con la suscripción. |
| Revisión humana asistida                            | Por elemento revisado o bolsa de horas.             | Convierte la cola de baja confianza —una limitación técnica— en una línea de servicio.                                                               |

**17. Referencias**

**Documentos académicos (folder del proyecto)**

- Salminen, J., Yoganathan, V., Corporan, J., Jansen, B. J., & Jung,
  S.-G. (2019). *Machine learning approach to auto-tagging online
  content for content marketing efficiency: A comparative analysis
  between methods and content type.* Journal of Business Research, 101,
  203–217. jansen_autotagging.pdf

- Sharma, V., & Karnick, H. (2016). *Automatic tagging and retrieval of
  E-Commerce products based on visual features.* Proceedings of
  NAACL-HLT 2016, 22–28. smart-tagging.pdf

**Fuentes de industria**

- Pixyle.ai — Plataforma: https://www.pixyle.ai/platform

- Pixyle.ai — *From Hours to Seconds: The Real Cost of Manual vs AI
  Tagging in Fashion Retail*:
  https://www.pixyle.ai/blog/the-real-cost-of-manual-vs-ai-tagging-in-fashion-retail

- Browntape — *Scaling E-commerce: The Power of AI and Automation in
  Product Tagging*:
  https://browntape.com/scaling-e-commerce-the-power-of-ai-and-automation-in-product-tagging/

**Fuentes de datos**

- H&M Personalized Fashion Recommendations (Kaggle) — datos:
  https://www.kaggle.com/competitions/h-and-m-personalized-fashion-recommendations/data
  · **reglas oficiales:**
  https://www.kaggle.com/competitions/h-and-m-personalized-fashion-recommendations/rules

- Fashionpedia: https://fashionpedia.github.io/home/index.html —
  **licencia y términos:**
  https://fashionpedia.github.io/home/data_license.html — repositorio de
  descarga: https://github.com/cvdfoundation/fashionpedia

- Atribución requerida por CC BY 4.0: las anotaciones y la ontología
  utilizadas provienen del proyecto Fashionpedia.

- DeepFashion (MMLab, CUHK):
  https://mmlab.ie.cuhk.edu.hk/projects/DeepFashion.html

- Amazon Reviews 2023 (McAuley Lab):
  https://amazon-reviews-2023.github.io/

**Documento interno**

- Sugerencia_projecto.txt — documento de sugerencia de fuentes de datos
  y estructura de experimentos, base de las secciones 5 y 7 de este
  plan.

**Apéndice A. Estado de verificación: resuelto, definido y abierto**

Conforme al criterio de no afirmar lo que no puede verificarse, se
registra el estado de cada punto crítico: lo que quedó **resuelto** en
esta versión con verificación en la fuente primaria, lo que quedó
**definido** por decisión del responsable del proyecto pero aún sin
lectura literal de la fuente, y lo que sigue **abierto**. Cada punto
abierto tiene asignada la fase en la que debe cerrarse.

| **Punto**                                                                         | **Estado**                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      | **Cierre**                                                                                                                                                                                                                       |
|-----------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **Licencia de Fashionpedia.**                                                     | **RESUELTO (v1.1).** Anotaciones y ontología bajo CC BY 4.0; imágenes no son propiedad del proyecto y responden a los términos de Flickr, Unsplash, Burst by Shopify, Freestocks, Kaboompics y Pexels; el usuario acepta responsabilidad plena, incluidas las copias de imágenes con copyright. Software del dataset bajo BSD 2-Clause. Verificado en la página oficial de licencia.                                                                                                                                                            | Incorporado en las secciones 7.3 y 7.4. Pendiente solo la revisión activo por activo si se usan imágenes en la demo pública.                                                                                                     |
| **Términos de uso y redistribución de H&M.**                                      | **DEFINIDO (v1.1) — texto literal pendiente.** Los términos adoptados como restricción de trabajo son: uso no comercial, académico y educativo, con prohibición de transmitir, publicar o redistribuir los datos a personas que no hayan aceptado formalmente las reglas. **Esta formulación proviene del responsable del proyecto, no de una lectura directa:** el intento de recuperar la página de reglas devolvió solo metadatos, porque la plataforma renderiza el texto en el cliente y puede exigir aceptación previa de la competencia. | F0 — abrir la página de reglas en el navegador, leer la cláusula de datos y **pegar su texto literal en el repositorio**. Si el texto difiere de esta formulación, las secciones 6.2, 7.3, 7.4 y 14 se corrigen en consecuencia. |
| **Escenario de cómputo.**                                                         | **RESUELTO (v1.1).** Sin GPU dedicada: gráficos integrados Intel Iris Xe con ≈15,8 GB de memoria compartida. Estrategia híbrida definida en la sección 12.                                                                                                                                                                                                                                                                                                                                                                                      | Cerrado. F0 configura los dos entornos (nube gratuita con GPU y local con OpenVINO/ONNX).                                                                                                                                        |
| Publicación de los pesos del modelo ajustado sobre H&M.                           | **Zona gris abierta.** No es dato crudo, pero es un derivado entrenado sobre datos restringidos.                                                                                                                                                                                                                                                                                                                                                                                                                                                | F0 — decidir al leer qué dice la cláusula literal sobre trabajos derivados. Por defecto, no se publican hasta que la lectura lo respalde.                                                                                        |
| Conteos exactos de filas de articles.csv, customers.csv y transactions_train.csv. | No verificado en la fuente primaria. El único dato confirmado es el tamaño aproximado de 34,6 GB.                                                                                                                                                                                                                                                                                                                                                                                                                                               | F2 — se obtienen al descargar y se registran en el diccionario de datos.                                                                                                                                                         |
| Tamaños de los splits train/val/test de Fashionpedia.                             | No publicados en la página del dataset ni en el repositorio.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    | F2 — derivar de los archivos de anotación descargados.                                                                                                                                                                           |
| Términos de uso de Amazon Reviews 2023.                                           | Sin verificar.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  | Antes de cualquier incorporación. No se usa hasta registrarlos.                                                                                                                                                                  |
| Precios y estructura de tarifas de Pixyle.ai.                                     | No verificable. La compañía no publica página de precios accesible; la URL de precios devuelve error 404 y los directorios de software consultados no ofrecen la cifra.                                                                                                                                                                                                                                                                                                                                                                         | No bloquea el proyecto. Si se requiere, solicitar cotización directa. Ninguna cifra estimada debe presentarse como dato de mercado.                                                                                              |
| Modelos de visión-lenguaje concretos, versiones y checkpoints a utilizar.         | Deliberadamente no fijados. El panorama de modelos cambia con rapidez y fijar hoy un checkpoint produciría una recomendación desactualizada al ejecutar.                                                                                                                                                                                                                                                                                                                                                                                        | F4 — seleccionar mediante comparación empírica sobre los splits congelados, con el costo computacional como criterio junto al desempeño.                                                                                         |
| Umbrales objetivo de F1, MAP@12 y cobertura.                                      | No fijados por diseño: dependen de la dificultad real de la tarea, desconocida antes de la línea base.                                                                                                                                                                                                                                                                                                                                                                                                                                          | F3 — calibrar con los anclajes de la sección 11 y **congelarlos versionados antes de entrenar el modelo final**.                                                                                                                 |
| Nivel de evidencia definitivo de cada atributo de la taxonomía.                   | Abierto. La asignación A/B/C depende del mapeo final entre Fashionpedia y H&M, que se cierra en F1.                                                                                                                                                                                                                                                                                                                                                                                                                                             | F1 — ningún atributo queda sin nivel asignado; lo que no tiene ground truth se declara nivel C, no se omite.                                                                                                                     |
| Tamaño de muestra y perfil de anotadores para la evaluación humana.               | Abierto. El tamaño se deriva de la precisión deseada del estimador de acuerdo, y el perfil exige criterio de moda para atributos finos.                                                                                                                                                                                                                                                                                                                                                                                                         | F6 — dimensionar antes del piloto y dejarlo fijado; no ampliar la muestra a mitad del ejercicio.                                                                                                                                 |
| Fracción y mecanismo de enmascaramiento para el régimen H3b.                      | Abierto. Debe imitar el caso real (producto de proveedor sin ficha) sin dejar de ser reproducible.                                                                                                                                                                                                                                                                                                                                                                                                                                              | F8 — definir y documentar antes de entrenar, y declarar siempre como simulación.                                                                                                                                                 |

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<tbody>
<tr class="odd">
<td><p><strong>Nota sobre el alcance de este apéndice</strong></p>
<p>Este plan no constituye asesoría legal. Su función es dejar por
escrito qué términos se adoptaron como restricción de trabajo, de dónde
vienen y cuáles siguen sin verificarse en la fuente primaria, de modo
que las decisiones del proyecto puedan auditarse contra los documentos
originales y no contra un resumen.</p></td>
</tr>
</tbody>
</table>
