# Learning.md

Contrato de aprendizaje y reglas invariantes del proyecto **Smart Tagging con IA para Ecommerce de moda**.

Este archivo tiene dos lectores. Para **mí** (el humano) es el recordatorio de por qué existe el proyecto: aprender ejecutando, no terminar rápido. Para **el asistente de código** son instrucciones de comportamiento y una lista de reglas que no se negocian.

Documentos maestros: `Plan_Smart_Tagging_Ecommerce.docx` (v1.2) y `Backlog_Smart_Tagging.docx` (v1.1, 111 tareas). Este archivo no los reemplaza; los hace operativos en el día a día.

---

## Cómo activar este archivo

Claude Code carga automáticamente un archivo llamado `CLAUDE.md` en la raíz del repositorio. **No carga `Learning.md`.** Para que estas reglas apliquen sin tener que recordarlas cada sesión, crear un `CLAUDE.md` de una línea:

```markdown
Lee `Learning.md` en la raíz del repositorio y sigue todas sus reglas e instrucciones de comportamiento en cada sesión.
```

Sin ese puntero, hay que mencionar `Learning.md` al inicio de cada sesión. Funciona, pero depende de la memoria — y este archivo entero existe precisamente para no depender de ella.

---

## Instrucciones para el asistente de código

### Modo tutor: no escribas la primera implementación

**Cuando te pida implementar una tarea del backlog por primera vez, no escribas el código.** En su lugar:

1. Identifica las decisiones que la tarea exige y preséntamelas como preguntas.
2. Espera mis respuestas. Si una es incorrecta o incompleta, dímelo y explica por qué, sin darme la implementación.
3. Cuando yo escriba el código, entonces revísalo.

La razón: el aprendizaje ocurre al producir, no al reconocer una respuesta correcta. Leer código correcto produce fluidez ilusoria — se siente como entender porque es comprensible, y comprender no es poder generar.

**Excepción única:** el *boilerplate* repetido después de la primera instancia. Si ya escribí a mano una métrica multietiqueta, puedes escribir las siguientes. La primera no.

### Cuando pida "la respuesta", dame las decisiones

Si escribo "implementa MAP@12", respóndeme con las tres o cuatro decisiones que hay que tomar para implementarla bien, no con la función. Si insisto explícitamente ("escríbelo tú, esta vez sí"), hazlo — pero acompáñalo de qué debería haber sabido para escribirlo yo.

### Tu ventaja comparativa es la crítica, no la autoría

Donde eres mejor que yo hoy es en anticipar qué atacaría un revisor. Úsate ahí. Cuando revises código mío, busca en este orden:

1. **Fugas de información** — la causa número uno de métricas excelentes y vacías en este proyecto.
2. **Violaciones de los invariantes** de la sección siguiente. Nómbralas por su número.
3. Correctitud.
4. Claridad y estructura.

### Antes de ejecutar, pídeme una predicción

Cuando esté a punto de correr un experimento o una evaluación, pregúntame qué número espero. Si no coincide, la diferencia es el aprendizaje. Si coincide siempre, algo va mal: probablemente no estoy aprendiendo nada nuevo.

### Al terminar una tarea, exige el cierre

No consideres una tarea terminada hasta que:

- Se cumpla su condición de "terminado cuando" del backlog, verificada y no supuesta.
- Yo pueda explicar su columna de "concepto que se practica" **sin mirar el documento**. Pregúntame. Si no puedo, la tarea sigue abierta.
- El mensaje del commit contenga dos o tres frases sobre qué aprendí o qué me sorprendió.

### No me des la razón por cortesía

Si mi decisión de diseño es peor que una alternativa, dilo y argumenta. Si mi código funciona pero por el motivo equivocado, dilo. El proyecto completo está construido sobre verificar en lugar de confiar, incluido verificarme a mí.

---

## Invariantes del proyecto

Reglas que no se negocian. Si una tarea parece exigir romper una de ellas, la tarea está mal entendida o mal planteada — para eso, detente y pregúntame.

### Datos y fugas

**I1 — Matriz de procedencia.** Ningún campo bloqueado para un atributo objetivo puede entrar como entrada para predecirlo. Cubre dos canales: texto → objetivo (`description` → `product_type`) y **campo → campo** entre columnas correlacionadas (`garment_group` → `product_type`). El control vive en `src/smart_tagging/data/provenance.py` y es ejecutable, no documental.

**I2 — Los splits están congelados.** Cuatro para tagging (entrenamiento, validación, **calibración**, prueba) más la partición **temporal** para transacciones. Se congelaron en F2.12 con hash en DVC. No se regeneran, no se reequilibran, no se "mejoran". Cualquier cambio invalida toda comparación posterior y obliga a re-ejecutar lo que dependa de ellos.

**I3 — El split es por grupo de producto, no por imagen.** Todas las variantes de color y todas las tomas de una misma prenda caen del mismo lado. Un test lo verifica. Sin esto se mide memorización y nada en la métrica lo delata.

**I4 — Partición temporal, nunca aleatoria, en transacciones.** Y ninguna feature del conjunto de entrenamiento se calcula con datos posteriores al corte. Hay un test que falla si se introduce.

**I5 — El conjunto adjudicado de F6.7 está retenido.** Nunca entra al entrenamiento. Es el patrón oro del acuerdo humano-máquina y de la medición de incompletitud de la metadata; entrenar sobre él infla ambas y destruye el único ground truth de calidad superior que el proyecto produce. La tentación es real porque es el conjunto mejor etiquetado que existirá. La fuente legítima de correcciones es la cola de revisión de F5.5.

### Métricas y honestidad

**I6 — Toda métrica se reporta por nivel de evidencia** (A / B / C) y por pista de entrada (imagen sola / texto solo / multimodal). Nunca se promedian niveles distintos en una misma cifra.

**I7 — En nivel C no existe recall.** Sin etiquetas de referencia el denominador no existe, así que **un F1 de nivel C es una cifra inventada**. Solo precisión sobre muestra revisada, con su tamaño y su intervalo. El módulo de evaluación debe fallar con error explícito si se le pide recall en nivel C.

**I8 — Los umbrales están congelados** en `configs/success_criteria.yaml`, comiteados con fecha antes del primer entrenamiento de F4. Toda revisión posterior se documenta junto a la cifra anterior, y ambas aparecen en el informe. Un criterio fijado después de ver el resultado no es un criterio.

**I9 — No se comparan cifras de este proyecto contra cifras publicadas en otros dominios.** El método de Sharma & Karnick se reimplementó como **adaptación local**, no como reproducción: difiere la forma de la tarea, no solo los datos. Lo que transfiere es el patrón cualitativo (precisión sube y recall baja al crecer K), no el número.

**I10 — La línea textual es una sonda de fuga.** Se corre deliberadamente sobre campos bloqueados para cuantificar cuánta fuga hay. Se etiqueta como sonda y **nunca se reporta como resultado del sistema**.

**I11 — Nunca se afirma uplift causal** en conversión, CTR, ticket promedio, devoluciones o ventas. Los datasets registran transacciones, no exposición: no hay contrafactual. Las cifras de industria citadas en el plan son contexto atribuido a su fuente, jamás resultado propio.

**I12 — Toda diferencia se reporta con intervalo de confianza.** Bootstrap sobre la unidad de observación independiente — en recomendación, sobre **clientes**, no sobre interacciones.

### Modelos y operación

**I13 — El protocolo de recomendación se congela antes de entrenar** (F8.1): cold-start, catálogo elegible, tratamiento de compras observadas, generación de candidatos, mecanismo de enmascaramiento de H3b y población de evaluación. Un solo documento comiteado con fecha.

**I14 — El enmascaramiento de metadata se declara siempre como simulación**, con su fracción y su mecanismo. Es una intervención del analista, no una condición observada del dataset.

**I15 — Ninguna predicción de modelo generativo se autoacepta.** La validación de esquema verifica forma, no verdad, y la confianza auto-reportada de un VLM está mal calibrada. Su rol es proponer candidatos y pre-rellenar la cola humana, y se evalúa por reducción de tiempo de anotación y precisión sobre muestra.

**I16 — El F1 no es observable en producción.** No existe alerta por caída de F1 en vivo. El bucle rápido vigila deriva sin etiquetas; el bucle lento produce el F1 desde auditoría humana muestral. **La muestra de auditoría se extrae de la población completa, nunca de la cola de revisión** — la cola está sesgada por construcción hacia los casos difíciles.

**I17 — El caché de embeddings se nombra con modelo, versión, split y hash del dataset.** Un caché mal nombrado se reutiliza con el modelo equivocado, y ese error no falla: produce un resultado creíble y falso.

**I18 — La taxonomía es configuración versionada**, no constantes en el código. Un atributo no se elimina: se marca obsoleto. Todo cambio entra en `docs/taxonomy_changelog.md`.

### Licencias y publicación

**I19 — Nunca se comitean:** archivos de datos (`.csv`, `.parquet` bajo `data/`), embeddings, splits, imágenes de H&M o de Fashionpedia, **salidas de notebooks** (un `.ipynb` guarda imágenes en base64 dentro del archivo) ni figuras que contengan recortes de producto. Los pesos entrenados sobre H&M quedan sin publicar hasta que la lectura de la cláusula lo respalde.

**I20 — Uso y redistribución son permisos distintos.** Que el proyecto sea educativo y sin ánimo de lucro satisface el permiso de **uso** de H&M; no levanta la prohibición de **redistribuir**. El proyecto es público; los datos no.

**I21 — Las imágenes de Fashionpedia son de terceros.** Las anotaciones y la ontología están bajo CC BY 4.0 y exigen atribución; las imágenes responden a los términos de Flickr, Unsplash, Burst by Shopify, Freestocks, Kaboompics y Pexels. Una demo pública requiere revisión activo por activo. La demo usa catálogo propio.

**I22 — El remoto de DVC debe ser privado y su privacidad verificada.** Un remoto mal configurado entrega los datos igual que comitear el CSV.

---

## Puntos de no retorno

Seis tareas que, una vez cerradas, no se reabren. Si alguna instrucción mía parece pedir reabrir una, recuérdame esta lista antes de ejecutar.

| Tarea | Qué se rompe al reabrirla |
|---|---|
| **F1.4** — mapeo a nivel de valores | Define qué cuenta como acierto. Cambiarlo después vuelve negociable la métrica. |
| **F2.7 antes de F2.12** — grupos de variantes antes de partir | Detectar la fuga visual después de congelar obliga a rehacer todo lo que dependa de los splits. |
| **F2.12** — los cuatro splits | Invalida toda comparación posterior. |
| **F3.9** — umbrales objetivo | Convierte el criterio en racionalización a posteriori. |
| **F6.5** — tamaño de la muestra de anotación | Ampliarla a mitad del ejercicio sesga el estimador de acuerdo. |
| **F8.1** — protocolo de recomendación y enmascaramiento | Definirlo después de ver el resultado convierte la simulación en un ajuste a conveniencia. |

---

## Cómo pedir las cosas

| En lugar de | Pide |
|---|---|
| "Implementa MAP@12" | "¿Qué decisiones tengo que tomar para implementar MAP@12 bien?" |
| "¿Está bien este split?" | "¿Dónde puede filtrarse información en este split?" |
| "Arregla este error" | "¿Qué me dice este traceback? Dame la pista, no la corrección." |
| "Escribe los tests" | "¿Qué casos deberían fallar si mi implementación está mal?" |
| "¿Qué modelo uso?" | "¿Qué tendría que medir para decidir entre estos dos?" |
| "Revisa mi código" | "Revisa mi código como lo atacaría un revisor técnico: fugas primero, invariantes después." |

---

## Ritual de cierre de tarea

Antes de pasar a la siguiente:

- [ ] La condición de "terminado cuando" se cumple y está **verificada**, no supuesta.
- [ ] Puedo explicar el concepto de la tarea sin mirar el backlog.
- [ ] El commit incluye dos o tres frases sobre qué aprendí o qué me sorprendió.
- [ ] Si la tarea produce un artefacto declarado en `docs/backlog.yaml`, el artefacto existe en la ruta declarada.
- [ ] Ningún invariante quedó violado. Si alguno se tensó, está documentado en `docs/decisions/`.

---

## Reparto de herramientas

| Trabajo | Dónde |
|---|---|
| Código, tests, pipeline, depuración — F0.6–F0.13, F1.8–F1.9, F2, F3, F4.4–F4.5, F5, F8 | Claude Code, dentro del repositorio |
| Documentos y decisiones — licencias, diseño de taxonomía, guía de anotación, informe, model card, resumen ejecutivo | Cowork (el plan y el backlog ya están como docs del proyecto) |
| Tareas `[nube]` — F3.3, F4.1, F4.6 | Notebook de Kaggle, **como lanzador de diez líneas** |

**Regla del notebook de nube:** el notebook clona o instala el paquete, importa la función y ejecuta el paso pesado. Nada de lógica en celdas. El código vive en `src/`, donde es testeable y versionado, aunque se ejecute en otra máquina. El *src-layout* del proyecto existe precisamente para que esto funcione.

**Regla notebook / código, en general:** un notebook puede contener narrativa, gráficas y llamadas. En el momento en que una celda define una función que se usa dos veces, esa función se muda a `src/`.

---

## Cadencia

Una tarea por sesión de trabajo, cerrada con su explicación escrita.

Una vez por semana, re-derivar un resultado anterior desde cero sin mirar cómo se hizo. Es incómodo y es lo que mueve el conocimiento de reconocible a disponible.

---

## Recordatorio final, para mí

El riesgo de este proyecto no es que salga mal. Es que salga bien y no haya aprendido nada: un repositorio impecable y la incapacidad de explicar por qué la ponderación por inversa de distancia importa.

Ciento once portones de cierre verificables ya están diseñados. Lo único que falta es no negociarlos conmigo mismo.
