# ATIBOT Academy · Atigra Makers

Aplicación de mecanografía educativa ejecutable, con backend real, autenticación, base de datos y gestión docente. Identidad magenta `#cc0b4e`, verde `#45ae46`, superficies espaciales y el **logo oficial facilitado por el usuario** y ATIBOT adaptado a partir de su imagen, con expresiones curiosa, pensativa y sorprendida y ojos abiertos de fondo blanco.

## Ejecutar en tu ordenador

Requiere **Python 3.11 o posterior**, con SQLite incluido. Se incluye un respaldo de la zona horaria IANA de Madrid para Windows. No necesita Node, paquetes de Python, claves API, CDN ni servicios externos para funcionar.

```bash
cd /workspace/EDCLUBATIGRA
python3 server.py
```

El servidor escucha en el puerto 8000, solo en la máquina local por defecto. Para un alojamiento accesible desde otra máquina:

```bash
python3 server.py --host 0.0.0.0 --port 8000
```

El proceso debe permanecer activo. Su reinicio conserva los datos en `data/atigra.sqlite3`. `python3 server.py --init-only` inicializa sin arrancar y es repetible: no sobrescribe usuarios ni resultados existentes. El directorio `data/` no se versiona.

## Inicio sencillo en Windows

1. [Descarga el ZIP](https://github.com/pbxbtbx/EDCLUBATIGRA/archive/refs/heads/main.zip) y pulsa **Extraer todo**.
2. Abre la carpeta extraída donde se encuentra `server.py`.
3. Haz doble clic en **`INICIAR_WINDOWS.bat`**. No lo escribas dentro de la ventana de Python que muestra `>>>`.
4. El navegador se abrirá automáticamente con la aplicación. Mantén abierta la ventana de inicio.
5. Entra con `profe.demo` o `nova.demo`, contraseña `AtigraDemo2026!`.

Requiere Python 3.11 o superior instalado en ese ordenador. No necesita hosting, cuenta de Render ni conexión para usar las misiones. El progreso se guarda en `data/`; conserva esa carpeta al actualizar. Si el navegador no se abre, escribe `http://127.0.0.1:8000` en Chrome, Edge o Firefox **en ese mismo ordenador**. Esta dirección no es un enlace público y solo funciona donde está arrancado el programa.

En Mac puedes ejecutar `python3 iniciar.py` en la carpeta del proyecto o usar `INICIAR_MAC.command` si el sistema permite ejecutarlo. `python iniciar.py --port 8001` permite elegir otro puerto. `--no-browser` arranca sin abrir una ventana de navegador, útil para comprobaciones automáticas. El lanzador comprueba la versión y la carpeta de la instancia antes de reutilizarla. Si el puerto está ocupado por otra versión, elige automáticamente otro y abre esa dirección: usa la pestaña nueva que abre el programa.

## Probar un juego sin iniciar sesión

En la pantalla de entrada pulsa el botón verde **«Probar un juego sin cuenta»**. Se abre **Defensa del castillo orbital · Escudo de aprendiz**. Escribe el texto mostrado: cada palabra completa carga los escudos y aleja el meteorito; ATIBOT cambia de expresión durante la misión.

Se puede pausar, corregir con Retroceso, terminar y repetir. El resultado muestra precisión, PPM, tiempo y errores corregidos. La prueba funciona sin credenciales y **no crea usuarios, sesiones, ejecuciones ni intentos en la base de datos**, ni otorga puntos o desbloqueos. Las misiones del alumnado y su progreso persistente siguen requiriendo autenticación. La prueba es local en la memoria de esa pestaña y se pierde al cerrarla.

La identidad incluye la frase «Si puedes imaginarlo y soñarlo, puedes crearlo y programarlo» en la bienvenida y en el pie de la aplicación. La interfaz inglesa tiene su traducción, conservando el idioma del texto de la misión iniciada.

## Sala de juegos: más variedad y movimiento

Pulsa **«Elegir juego y nivel»** en la bienvenida o **«Sala de juegos»** desde tu panel. Hay **18 retos de práctica libre**: seis modalidades con tres dificultades (Inicio, Aventura y Desafío), con textos distintos en español e inglés. Son adicionales al catálogo de 36 niveles del curso; no sustituyen asignaciones ni modifican el historial existente.

| Juego | Qué ocurre al escribir | Cambios por dificultad |
| --- | --- | --- |
| Castillo orbital | Se cargan escudos, aparecen recompensas y se desvían meteoritos | 1, 2 o 3 meteoritos; palabras, instrucciones y una alerta completa |
| Carrera de naves | La nave acelera suavemente, cruza balizas y llega a una estación | Más balizas y textos con rutas, números y signos |
| Puente de runas | Los bloques emergen y ATIBOT cruza el abismo | 6, 10 o 14 runas; secuencias, frases y un enigma |
| Dragón mecánico | Se recuperan engranajes, cobra color y mueve sus alas articuladas | Más piezas y descripciones cada vez más largas |
| Exploración | ATIBOT avanza, recoge cristales y descubre una base | Más recursos; palabras, instrucciones y una bitácora |
| Portal | Los anillos giran en sentidos distintos y se ilumina el núcleo | 2, 3 o 4 anillos; códigos, coordenadas y un texto final |

El movimiento se interpola con un solo `requestAnimationFrame` por escena. Al pausar o perder foco se detienen tanto la escritura como el escenario. Al cambiar de juego se cancela el bucle anterior. La preferencia de movimiento reducido, incluido el ajuste del sistema, elimina el movimiento continuo y las partículas; el progreso se representa de forma estática. El texto y las teclas no se reconstruyen en cada pulsación, para evitar trabajo innecesario durante la escritura.

Las misiones asignadas usan las mismas escenas mejoradas; su variante visual se deriva del orden (posiciones 0–5, 6–11 y 12 en adelante). Esto no cambia textos, requisitos ni puntuaciones del servidor. La celebración final no añade tiempo al cronómetro. La sala libre muestra métricas locales, pero no guarda intentos, puntos o desbloqueos. Repetir conserva el reto elegido y el idioma de su contenido.

Prueba de navegador específica: `python3 tests/browser_arcade.py`. Necesita las mismas herramientas opcionales Playwright y Chromium que el recorrido original.

## Si el botón de entrada parece no responder

1. Usa la versión actualizada y cierra la ventana de inicio anterior antes de volver a ejecutar `INICIAR_WINDOWS.bat`.
2. No abras `web/index.html` directamente: entra desde el navegador que abre el lanzador.
3. Escribe `nova.demo` y `AtigraDemo2026!`, o pulsa el acceso rápido **Alumno · Nova**.
4. El formulario muestra un mensaje si falta algún dato, las credenciales son incorrectas o el servidor no responde. Si ocurre, copia ese mensaje para poder diagnosticarlo.

La aplicación incluye la zona horaria de Madrid de respaldo para Windows; no hace falta instalar `tzdata` por separado. Conserva tu carpeta `data/` al actualizar para mantener el progreso.

## Demostración

Al inicializar por primera vez se crean una clase y tres alumnos **ficticios**, sin intentos ni puntuaciones inventados:

| Rol | Usuario | Contraseña de demostración |
| --- | --- | --- |
| Docente | `profe.demo` | `AtigraDemo2026!` |
| Alumno | `nova.demo` | `AtigraDemo2026!` |
| Alumno | `leo.demo` | `AtigraDemo2026!` |
| Alumno | `luna.demo` | `AtigraDemo2026!` |

El docente puede crear clases y cuentas, comunicar las credenciales privadamente, mover alumnos, retirarlos de una clase y restablecer contraseñas. Los alumnos no necesitan correo. Cada alumno pertenece a una clase como máximo; sus datos históricos sobreviven a los cambios de clase. El correo es un identificador alternativo de acceso: no se envían mensajes ni se ofrece recuperación por correo.

## Arquitectura

- `server.py`: API HTTP, autorización por propietario, sesiones, validación de eventos, puntuación, clasificación e inicialización.
- `web/`: interfaz JavaScript, HTML y CSS, con catálogo libre en `arcade.js` y controlador de escenas en `motion.js`, adaptable a ordenador y tablet. Sin compilación ni bibliotecas externas.
- SQLite con claves foráneas y WAL: usuarios, clases, inscripciones, planetas, niveles, asignaciones, sesiones, ejecuciones, intentos y snapshots semanales.
- `manage.py`: administración local de cuentas docentes y restablecimiento de contraseñas.
- `tests/`: pruebas de reglas, API, persistencia, permisos y flujo de navegador.

Esta arquitectura permite una primera versión local verificable con una instalación mínima. `python server.py` usa `ThreadingHTTPServer` para desarrollo; `python wsgi.py` usa Waitress para hosting: para uso público hay que añadir terminación HTTPS, supervisión, límites de tráfico, copias de seguridad y un servidor HTTP de producción y usar el punto de entrada WSGI con Waitress. No se ha desplegado en un servicio externo.

## Funcionalidades

### Alumno

- Mapa de seis planetas, estados disponibles/bloqueados/completados y continuación de la siguiente misión.
- **36 niveles: 18 en español y 18 en inglés**, con fila central, superior, inferior, palabras, mayúsculas/signos y frases. La clase demo empieza con los 18 españoles; el docente puede asignar los ingleses o contenido propio.
- Seis modalidades que comparten entrada, cronómetro, historial y reglas, con interacciones visuales distintas:
  - Castillo: completar palabras carga un escudo y aleja un meteorito.
  - Carrera: completar palabras mueve la nave hacia la meta.
  - Puente: completar secuencias construye segmentos de runas y mueve a ATIBOT.
  - Dragón: completar palabras recupera piezas y devuelve el color al dragón.
  - Exploración: completar instrucciones mueve a ATIBOT y recoge recursos.
  - Portal: cada carácter correcto carga y amplía el portal.
- Práctica sin presión: sin cuenta atrás ni castigos; conserva el intento y muestra una valoración orientativa de 1 a 5 ATIBOTS, pero no da desbloqueos ni puntos de clase.
- Historial, mejor intento por puntuación, evolución, precisión, PPM, tiempo activo, errores, ATIBOTS acumulados e insignias derivadas del progreso real.
- Clasificación de clase opcional, historial semanal y reconocimientos individuales.
- ES/EN en navegación, formularios, instrucciones y resultados. El idioma de interfaz no cambia el contenido asignado.

### Docente

- Crear/editar/archivar clases; activar u ocultar clasificación.
- Crear cuentas con alias, usuario, contraseña y correo opcional. Mover/retirar alumnos y restablecer contraseñas sin leer las anteriores.
- Crear niveles y editar los propios: nombre, planeta, modalidad, texto, idioma, PPM, precisión, orden y publicación/borrador. Los niveles comunes se copian antes de editar, evitando afectar a otros docentes.
- Asignar a clase o alumno, ajustar orden, requisito explícito, precisión mínima y participación en reto semanal. Las asignaciones individuales prevalecen sobre las de clase para ese alumno.
- Retirar una asignación conserva intentos. Eliminar contenido definitivamente es una acción diferente, permitida solo para niveles propios nunca usados ni asignados. Con historial, usar borrador.
- Parámetros de valoración editables por clase: peso de precisión, umbrales y límites por precisión. Los intentos conservan la valoración calculada con la configuración de su ejecución.
- Seguimiento por clase/alumno, filtros por fechas, misión e idioma, fecha de actividad, tiempo, errores, gráficos, historial y mejores resultados. Promedios de intentos completos evaluados separados de los promedios de mejores marcas; prácticas e incompletos identificados.
- Exportación CSV de la selección, con protección frente a fórmulas introducidas como texto. Fechas de filtro y visualización en `Europe/Madrid`.

## Motor y valoración

El servidor reconstruye el texto a partir de eventos, valida sus tiempos y calcula los resultados; ignora puntuaciones enviadas por el cliente.

- Precisión: entradas correctas / todas las entradas de caracteres × 100. Corregir con Retroceso no borra errores del contador.
- PPM netas: (caracteres del texto completado / 5) / minutos activos.
- Velocidad: `min(100, PPM / objetivo × 100)`.
- Puntuación inicial: `0.75 × precisión + 0.25 × velocidad`.
- Umbrales: 50, 65, 80 y 95 para 2, 3, 4 y 5 ATIBOTS.
- Al completar cualquier juego se muestran cinco espacios de ATIBOTS, con los conseguidos iluminados. En práctica la valoración es orientativa con las reglas iniciales; en misiones evaluadas se respeta la configuración de clase y la puntuación del servidor.
- **MAKER SUPREMO**: precisión exactamente del 100 % y velocidad al menos igual al objetivo del nivel (100 % de velocidad). Corregir un error impide esta distinción.
- Precisión <80%: máximo 2; <90%: máximo 3; 5 exige ≥97% y alcanzar el objetivo.
- Desbloqueo inicial: superar 90% en el requisito previo. Una misión se puede repetir aunque otro intento ya la haya superado. Basta cualquier intento completo evaluado que cumpla el umbral.
- El mejor intento es el de mayor puntuación; el historial completo permanece disponible. Las valoraciones acumuladas suman las mejores por misión.

El cronómetro empieza en la primera entrada de carácter, se detiene al perder foco, ocultar pestaña o pulsar pausa y no permite escribir hasta reanudar. Retroceso elimina el último carácter; las teclas mantenidas no se repiten. La entrada compuesta se registra al finalizar la composición y se normaliza a Unicode NFC, incluyendo `ñ`, `Ñ`, tildes y signos. No se contabiliza la composición intermedia. El pegado y arrastre están bloqueados en la interfaz. Las entradas incorrectas se muestran y se corrigen con Retroceso. Un abandono registra el intento incompleto sin valoración ni puntos. Cerrar la pestaña bruscamente puede dejar una ejecución sin intento final; nunca otorga puntos.

La clasificación suma **un mejor intento completo por alumno y misión durante la semana**, solo si la misión participa en el reto. No acumula puntos por repetir. Ordena por puntuación, precisión media de los mejores intentos y menor tiempo activo. La semana es lunes a domingo en `Europe/Madrid`, también en cambios de horario de verano. Retirar una misión o desmarcar el reto afecta a la semana actual; las semanas anteriores conservan la elegibilidad registrada al completar los intentos y se materializan en snapshots al consultar su historial. Ocultar la tabla no elimina los datos.

## Configuración y administración

Variables opcionales documentadas en `.env.example`. No hay secretos requeridos para la ejecución local. Exportarlas en el shell: **el servidor no carga automáticamente `.env`**.

| Variable | Valor inicial | Uso |
| --- | --- | --- |
| `ATIGRA_DB` | `data/atigra.sqlite3` junto al código | Archivo de datos; ruta absoluta recomendada fuera de desarrollo |
| `ATIGRA_HOST` | `127.0.0.1` | Dirección de escucha |
| `ATIGRA_PORT` | `8000` | Puerto |
| `ATIGRA_DEMO` | `1` | Crear datos demo en base nueva y mostrar atajos de acceso |
| `ATIGRA_SECURE_COOKIE` | `0` | `1` cuando el servicio se sirve exclusivamente mediante HTTPS |

Crear una instancia sin cuentas demo y añadir un docente:

```bash
export ATIGRA_DB=/ruta/persistente/atigra.sqlite3
export ATIGRA_DEMO=0
python3 manage.py init-clean
python3 manage.py create-teacher --username docente --alias Comandante
python3 server.py
```

La contraseña se solicita sin eco, con confirmación; no se recibe como argumento ni se guarda en texto plano. Para rotar una contraseña, también la del docente demo:

```bash
python3 manage.py reset-password --username profe.demo
```

`ATIGRA_DEMO=0` **no elimina cuentas demo existentes**. Para una instalación nueva sin ellas, usar un archivo de base nuevo. Evitar publicar una base con las credenciales conocidas de demostración. Las copias de SQLite deben hacerse con su API de backup, o con el servidor detenido; no copiar solo el archivo principal mientras WAL está activo.

## Seguridad y límites concretos

Contraseñas con scrypt y sal aleatoria; sesión opaca aleatoria en cookie HttpOnly/SameSite=Strict, vencimiento de 12 horas, CSRF en mutaciones, comprobación de origen y limitación básica de intentos de acceso. Restablecer contraseña revoca sesiones y ejecuciones abiertas. Las operaciones de escritura se serializan en transacciones para impedir dobles envíos concurrentes. Los recursos y la API solo usan el mismo origen. No hay publicidad, chat ni perfiles públicos.

La API comprueba el rol y propietario de clase/alumno/contenido, y los alumnos solo reciben sus asignaciones e intentos. La tabla semanal solo devuelve alias y métricas. Los controles antimanipulación comprueban propiedad y uso único de la ejecución, texto exacto completado, eventos de un carácter, tiempos ordenados, duración frente al reloj del servidor y velocidad máxima plausible (220 PPM). **Esto no demuestra que una persona haya tecleado: un cliente modificado puede fabricar eventos plausibles.** Es protección básica, no un sistema competitivo resistente a automatización.

El logo SVG oficial se conserva sin modificar en `web/assets/atigra-makers-oficial.svg`. Las tres expresiones de ATIBOT se generaron a petición del usuario a partir de su imagen y se sirven como un sprite PNG transparente. Su procedencia se describe en `web/assets/README.md`. Los escenarios mantienen dibujos CSS y algunos pictogramas del sistema. El estilo retro utiliza fuentes monoespaciadas locales; no necesita descargar fuentes. Sonido de recompensa generado localmente, inicialmente silenciado; movimiento reducible y respetando la preferencia del sistema. Foco visible, enlaces de salto, etiquetas y diálogo con confinamiento de foco. No se ha realizado una auditoría exhaustiva con lector de pantalla ni evaluación pedagógica con menores.

## Comprobaciones

Pruebas sin dependencias:

```bash
python3 -m unittest discover -s tests -v
node --check web/app.js  # opcional: Node solo para validar sintaxis durante desarrollo
```

Prueba de navegador opcional, con Playwright para Python y Chromium instalado:

```bash
python3 tests/browser_smoke.py
```

La prueba usa `/usr/bin/chromium` disponible en este entorno, crea una base temporal y arranca/detiene su propio servidor. En una máquina sin Playwright/Chromium se marca explícitamente como omitida; no valida el navegador allí. Las pruebas de servidor también usan una base temporal. No cambian la base demo ni los resultados del usuario.

Validado en el entorno actual: 18 pruebas de reglas/API (valoración, límites, errores corregidos, Unicode, semanas/DST, acceso, CSRF, persistencia tras salir, cuentas, asignaciones, eliminación, prácticas, clasificación, antimanipulación, CSV y recursos). El flujo Chromium cubre seis modalidades, pausa real, Unicode, progreso tras volver a entrar, ES/EN, foco inicial, tablet, creación de clase/alumno/nivel y CSV. Los resultados finales de ejecución se registran en `VALIDATION.md`.

## Usarla online, sin abrir Python

[![Deploy to Render](https://render.com/images/deploy-to-render-button.svg)](https://render.com/deploy?repo=https://github.com/pbxbtbx/EDCLUBATIGRA)

El botón inicia la instalación en tu cuenta de Render; **no es una aplicación ya desplegada**. La configuración incluye un servidor de producción Waitress y un disco persistente. Requiere un plan de pago de Render. Introduce una contraseña docente propia en los ajustes del alojamiento; no se habilitan cuentas demo online. Cuando Render termine, usa la URL HTTPS que muestre su panel.

Instrucciones paso a paso: [DEPLOY.md](DEPLOY.md). También se puede alojar en Railway o en un servidor propio con volumen persistente.
