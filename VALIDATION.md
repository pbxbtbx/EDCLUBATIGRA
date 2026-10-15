# Validación · 14 de octubre de 2026

## Resultados ejecutados

- `python3 -m unittest discover -s tests -q`: **18 pruebas ejecutadas, 18 correctas**, sin omisiones. Última ejecución: 5,461 segundos.
- `python3 tests/browser_smoke.py`: **1 recorrido integrado correcto**, Chromium real con Playwright, 21,210 segundos. Se completaron seis misiones, una de cada modalidad; no hubo errores de JavaScript.
- `node --check web/app.js`: correcto.
- `python3 -m py_compile server.py manage.py`: correcto.
- Script reutilizable de instalación: ejecutado en `/workspace/EDCLUBATIGRA`, incluida verificación de Python y zona horaria e inicialización repetible.
- Servidor de desarrollo arrancado en la instancia actual; comprobaciones HTTP locales del HTML y configuración, y acceso autenticado al panel de alumno.

## Cobertura

Puntuación y límites de 1–5 ATIBOTS; precisión con errores corregidos; texto NFC, `ñ`, tildes y mayúsculas; rechazo de eventos inválidos, tiempos imposibles y velocidades inverosímiles; contraseñas derivadas y revocación de sesiones; separación docente/alumno y propietarios; persistencia después de cerrar sesión; creación de clases/cuentas/niveles; retirada de asignaciones conservando historial; eliminación permanente de contenido nunca utilizado; práctica e incompletos sin valoración; clasificación con un mejor resultado por misión, desempates y retirada del reto; historial semanal y límites de semana con horario de verano/invierno de Madrid; CSV y archivos estáticos.

El navegador comprueba además una composición `n` + tilde registrada como un carácter, pegado cancelado, repetición de tecla ignorada, cronómetro detenido durante pausa, seis presentaciones e interacciones, ES/EN, primer acceso mediante teclado, ancho de tablet, creación docente de clase/alumno/misión y descarga CSV. Utiliza texto reducido y requisitos flexibles en su **base temporal** para recorrer las seis modalidades, sin alterar los 36 ejercicios reales ni la base del usuario. Los eventos de composición son sintéticos en un navegador real; no equivalen a probar todos los métodos de entrada de todos los sistemas operativos.

Durante la comprobación se corrigieron dos errores de interfaz: el clic de pausa reanudaba por el orden entre blur y click, y los informes no se recargaban al cambiar idioma. También se cambió el registro de eventos de composición a `addEventListener`, necesario para su ejecución en Chromium. Los recorridos se repitieron después de esas correcciones.

## Estado de entrega y límites

Aplicación local ejecutable con SQLite persistente. El primer recorrido exploratorio de navegador dejó un intento real de validación en la cuenta ficticia Nova de la instancia demo; las suites reproducibles posteriores usan exclusivamente bases temporales.

La configuración `install_script` y `start_skill` se guardó correctamente como **borrador del entorno**, sin cambios en permisos de red ni nuevos secretos. El usuario debe revisar y guardar los cambios en ajustes y publicar el entorno si desea activar esa versión. Guardar el borrador no ejecuta scripts ni constituye publicación. No se comprobó una restauración en una tarea cloud nueva ni un despliegue público.

El backend HTTP es de desarrollo; HTTPS, supervisión y backups deben configurarse antes de uso público. Los controles de eventos y velocidad son básicos y no impiden a un cliente modificado fabricar entradas plausibles. ATIBOT es provisional, no oficial. No se realizó una auditoría completa con lector de pantalla, prueba de carga ni evaluación pedagógica con alumnado real. No se requiere ningún recurso o servicio externo para la ejecución local.

## Preparación adicional para acceso online

Se añadió `wsgi.py`, un adaptador de la misma API para Waitress, `requirements.txt` con Waitress 3.0.2 y un blueprint `render.yaml` con disco persistente. `DEPLOY.md` explica el despliegue desde GitHub, la contraseña de inicialización privada y por qué GitHub Pages no puede ejecutar el backend. El punto de entrada de producción desactiva la creación de demo por defecto y requiere configurar una contraseña docente en el proveedor si no existen usuarios.

La suite se amplió a **23 pruebas correctas**, incluyendo transporte WSGI, autorización, CSRF, origen, métodos, cabeceras, inicialización sin cuentas demo y reinicialización sin sobrescribir credenciales. También se ejecutó el **servidor real Waitress** en una base temporal: acceso docente, clase, cuenta de alumno, asignación, misión con `ñ` y tilde, valoración, clasificación y reinicio conservando sesión e intentos. La prueba local utilizó cookies para HTTP; el blueprint activa cookies Secure para HTTPS en Render.

El blueprint usa un servicio Starter y disco de pago; se debe revisar el coste y confirmar la contratación en Render. No se creó ningún servicio externo, no se introdujeron credenciales reales en el repositorio ni se validó una URL remota. El botón de Render abre la instalación, no una aplicación publicada.

## Inicio local simplificado

Se añadieron `iniciar.py`, `INICIAR_WINDOWS.bat` e `INICIAR_MAC.command`. El lanzador usa el servidor local, abre el navegador del ordenador donde se ejecuta y reutiliza una instancia de ATIBOT ya disponible. No contrata hosting ni requiere las dependencias de producción. La opción `--no-browser` permite verificar el servicio sin abrir una ventana en el entorno cloud.

Una prueba adicional con base temporal comprobó el arranque desde otro directorio, las respuestas HTTP, la creación de SQLite y la detección de una instancia existente. Resultado: **1 prueba nueva correcta**. El servicio local de esta instancia también respondió 200 al HTML y `/api/config` después de arrancar con el lanzador. Los archivos de Windows y Mac no se ejecutaron en sus respectivos sistemas operativos; el programa Python sí se comprobó en Linux. La dirección de loopback de esta máquina no es accesible desde el ordenador del usuario.

## Corrección del acceso y compatibilidad con Windows

Se añadió un respaldo IANA 2026b de `Europe/Madrid` para instalaciones de Python sin zonas horarias del sistema (caso habitual en Windows). Antes, el acceso podía validar las credenciales y fallar al cargar el panel del alumno al calcular la semana. El origen exacto del fallo reportado por el usuario no se pudo confirmar desde su ordenador; esta incompatibilidad se verificó simulando la ausencia de las zonas del sistema.

El formulario ahora muestra mensajes persistentes cuando faltan credenciales, da indicación de carga y recupera el botón tras los errores. Las peticiones tienen un límite de 15 segundos y explican si el servidor no responde o devuelve contenido distinto de la API. Si falla la carga del panel, se limpia el estado de acceso parcial para que el formulario siga siendo utilizable.

Resultados: **26 pruebas de servidor/WSGI/lanzador correctas** (incluyendo panel de alumno y filtros docentes sin zonas IANA del sistema). El recorrido Chromium de seis modalidades pasó en **16,973 segundos**, entrando con el botón real y credenciales escritas, y comprobando campos vacíos, conexión abortada, contraseña incorrecta y reintento correcto. No se ejecutó Windows ni Python 3.15 directamente; el respaldo de zona horaria se validó en pruebas de regresión sobre Linux.

## Diagnóstico de acceso y servidores antiguos

El lanzador ya no considera suficiente que haya una página ATIBOT en el puerto 8000. Compara la versión cargada y un identificador de instalación, y selecciona un puerto libre si encuentra un proceso diferente o antiguo. No detiene procesos ajenos ni borra datos. Comprueba la zona horaria y prepara SQLite antes de abrir el navegador.

Un fallo interno al leer el panel ya no se presenta como «Revisa los campos del formulario». En esos fallos se devuelve una referencia aleatoria y se registra el tipo de excepción y la ubicación del código sin los valores del formulario. La interfaz distingue credenciales rechazadas de credenciales aceptadas con fallo posterior de carga.

Resultado: **28 pruebas correctas**. Las nuevas regresiones simulan un servidor antiguo aún activo (se abre el nuevo en otro puerto y el antiguo permanece intacto) y un fallo interno del panel (500 con referencia, sin exponer el valor de la excepción). El recorrido Chromium completo pasó en **17,925 segundos**, incluida la simulación del mensaje reportado después de aceptar la contraseña y un reintento correcto. No se verificó el ordenador del usuario: la causa concreta de su ejecución sigue sin confirmarse; se comprobó que utiliza una dirección local en el puerto 8000.

## Corrección de la carrera al guardar sesiones

Se reprodujo un fallo real en el servidor HTTP local: `/api/login` enviaba la cookie y el resultado 200 antes de que el contexto SQLite confirmara la transacción. Un GET inmediato al panel podía responder 401 aunque la contraseña fuera correcta. Se observó con `nova.demo` en la instancia local; la misma operación funcionaba con las otras dos cuentas en ese momento.

Las respuestas confirman ahora la transacción antes de enviar cabeceras o cuerpo. El cambio también hace que una operación docente confirmada sea visible para la siguiente consulta. Las excepciones siguen provocando rollback antes de devolver el error.

Una regresión con confirmación artificialmente lenta reproduce **401 con el orden antiguo** y pasa con el orden nuevo. Resultado de la suite actual: **29 pruebas correctas**. Se ajustó el recorrido de navegador para esperar a que aparezca la clase/alumno/nivel después de la recarga asíncrona; cerrar el formulario no implica que haya terminado esa recarga. El recorrido completo pasó después del cambio. Se comprobó además el inicio de sesión y panel con `nova.demo`, `leo.demo` y `luna.demo` en la instancia corregida: las tres devuelven 200 y sus 18 misiones.

La autenticación Git HTTPS continúa sin estar disponible y la comprobación de API GitHub tampoco pudo conectar. Se entrega un ZIP completo de la versión local comprobada; no se afirma que estos últimos commits estén subidos a GitHub. Esto no demuestra el resultado en el ordenador del usuario hasta que ejecute esa versión.

## Identidad oficial, expresiones y prueba pública · 15 de octubre de 2026

Se reemplazó la marca escrita provisional por el SVG oficial adjuntado por el usuario. Se verificó que el archivo servido coincide byte por byte con el original. ATIBOT se adaptó desde la imagen facilitada, con tres expresiones (curioso, pensativo y sorprendido), ojos abiertos con fondo blanco y transparencia real. El sprite RGBA mide 2172 × 724 y conserva tres celdas cuadradas iguales; la selección de expresión es CSS. No se alteró el logo para generar estas variantes.

La frase «Si puedes imaginarlo y soñarlo, puedes crearlo y programarlo» aparece en la bienvenida y en el pie, con traducción en la interfaz inglesa. El personaje pensativo acompaña los consejos, el curioso la bienvenida y las expresiones evolucionan con la misión; la variante sorprendida aparece al completar la prueba.

Se añadió «Probar un juego sin cuenta» en la entrada: una misión real de defensa del castillo, con el motor compartido de pulsaciones, errores corregidos, pausa, composición y animación. La prueba muestra precisión, PPM, tiempo y errores, se puede repetir y no otorga valoración ni puntos oficiales. Su resultado solo existe en memoria; no necesita credenciales ni crea sesiones, ejecuciones o intentos en SQLite.

Resultados: **30 pruebas de servidor/WSGI/lanzador correctas**, incluyendo acceso anónimo a los recursos y rechazo de rutas no autorizadas. El recorrido Chromium completo pasó en **20,541 segundos**, incluyendo el juego público, error corregido, pausa, ES/EN sin cambiar el ejercicio iniciado, resultado, repetición, salida, API privada 401 y verificación directa de cero ejecuciones/intentos tras la prueba. Después continuó con el acceso y las seis modalidades evaluadas, persistencia y gestión docente.

Se inspeccionaron capturas de bienvenida y juego en 1440 px; se verificó ausencia de desbordamiento horizontal en la prueba a 768 px y en la bienvenida a 390 px. El alfa de la esquina del PNG es cero. Las expresiones son adaptaciones solicitadas del personaje proporcionado, no una afirmación de aprobación oficial adicional. Ninguna imagen se genera ni descarga de terceros mientras el usuario juega.

## Escenas fluidas y variedad de niveles · 15 de octubre de 2026

Se sustituyeron los desplazamientos por saltos por un controlador de escenas `motion.js` con un solo bucle `requestAnimationFrame`, interpolación dependiente del tiempo y referencias a nodos guardadas al montar. Las posiciones principales usan transformaciones; el texto y las teclas conservan sus nodos durante la escritura. Se calculan una sola vez los caracteres y los límites de palabras de cada ejercicio. El controlador cancela sus fotogramas, observadores y listeners al desmontar; la pausa congela también el escenario, y una pestaña oculta no programa fotogramas.

Las seis escenas incorporan mecanismos visuales diferentes: escudos y meteoritos, nave vectorial y balizas, runas emergentes, dragón articulado y engranajes, recolección de cristales y anillos de portal. Los objetivos, el contador de palabras, los elementos de escena y la dificultad se muestran junto al ejercicio. La celebración final no se añade al tiempo activo del intento. Movimiento reducido manual o del sistema produce estados estáticos y elimina partículas y movimiento continuo.

El selector Sala de juegos ofrece **18 retos de práctica libre** (seis juegos × tres dificultades), cada uno con nombre y texto propios en ES/EN. No se añadieron ni reemplazaron filas del catálogo curricular: se conservan los 36 niveles originales, asignaciones e intentos. Las misiones asignadas usan las nuevas escenas con una variante visual derivada de su orden. El catálogo libre no genera puntuaciones oficiales, intentos ni ejecuciones en SQLite. Repetir mantiene el reto y el idioma del ejercicio, aunque se cambie el idioma de la interfaz.

Validación ejecutada:

- **30 pruebas de servidor/WSGI/lanzador: correctas**, incluida la entrega de los nuevos archivos JavaScript.
- `tests/browser_smoke.py`: recorrido completo correcto, **26,930 s**; seis modalidades evaluadas, práctica pública, errores corregidos, Unicode, pausa, persistencia, ES/EN, cuentas/clases/niveles y CSV.
- `tests/browser_arcade.py`: correcto, **13,797 s**; finalización real de los 18 retos, diferencias de elementos por dificultad, textos ES/EN distintos, interpolación intermedia de la nave, conservación de nodos de texto, congelación de progreso/fase/cronómetro al pausar, un solo bucle activo, cero bucles en resultados o al salir, movimiento reducido manual y cambios de preferencia del sistema, repetición e idioma, y cero registros persistentes de la sala libre.
- Revisión de capturas de las seis escenas y la sala; ausencia de desbordamiento horizontal a 768 px y 390 px. La sala de escritorio muestra los 18 accesos y usa un diálogo de 1040 px con navegación por teclado heredada del componente modal.
- Sintaxis JavaScript y `git diff --check`: correctos.

Las comprobaciones se hicieron en Chromium/Linux. No se midió una tasa de fotogramas garantizada en los equipos del alumnado ni se ejecutaron navegadores de Windows o Safari. La implementación interpola por tiempo y respeta las preferencias de movimiento; la fluidez efectiva también depende del dispositivo. No se ha desplegado una web pública por estos cambios.

## Valoración con ATIBOTS y MAKER SUPREMO (2026-10-15)

- Todos los resultados completos muestran cinco espacios de ATIBOTS, con entre uno y cinco conseguidos. La práctica calcula una valoración orientativa sin guardar puntos oficiales; las misiones evaluadas mantienen la valoración del servidor y las reglas de clase.
- MAKER SUPREMO exige precisión exactamente del 100 % y PPM al menos iguales al objetivo. Se muestra el porcentaje de velocidad, limitado al 100 %.
- Avanzar lleva al siguiente reto de práctica; Volver y Avanzar tienen colores, tipografías y foco visible distintos.
- `python3 -m unittest discover -s tests -q`: 30 pruebas superadas.
- `python3 tests/browser_arcade.py`: superado en Chromium; 18 retos completos, cinco ATIBOTS y distinción, límites de precisión/velocidad sin redondear, respeto a resultados oficiales, avance efectivo, colores y fuentes distintos, y comprobaciones existentes de animación/accesibilidad.
- `python3 tests/browser_smoke.py`: superado en Chromium; prueba con error corregido, seis modalidades evaluadas, acceso alumno/docente, historial, idiomas y acciones del profesor.
- `node --check web/app.js` y `git diff --check`: sin errores.

## Progreso persistente y cuatro modalidades nuevas (2026-10-15)

- Catálogo único `web/arcade.json`: conserva los 18 retos anteriores y añade cohetes, reacción con tres opciones, recolección de letras y plataformas. Tres dificultades por modalidad y dos idiomas: 30 retos, 60 variantes persistentes, más los 36 niveles originales del curso.
- La inicialización aplica una migración aditiva: relación `arcade_levels` y campos `feedback_score`, `feedback_bots`, `speed_percent`, `maker_supremo`. No sustituye cuentas, contraseñas, asignaciones ni intentos. Los ids del catálogo permanecen estables al reiniciar.
- Alumnos autenticados guardan sus partidas de sala como prácticas. Las valoraciones se calculan en el servidor; no alteran puntos oficiales ni requisitos de desbloqueo. La galería muestra intentos y mejor valoración; alumno y profesor disponen de resumen y gráficos de práctica, historial y exportación de métricas. Un profesor solo accede a su alumnado.
- Decisiones con botones reales y teclado: la letra incorrecta se registra y permite reintentar; la precisión no vuelve al 100 % al corregir. Cohetes y ATIBOT usan interpolación por tiempo, radar giratorio, letras que se recogen y saltos entre plataformas. Las escenas usan el controlador RAF compartido, pausa y movimiento reducido.
- `python3 -m unittest discover -s tests -q`: **32 pruebas superadas**, incluidas migración de una base antigua con progreso, persistencia tras salir, catálogo estable, acceso docente, aislamiento entre alumnos/docentes, CSV, valoración sin aceptar puntos del cliente y práctica de un reto bloqueado sin permitir evaluación.
- `python3 tests/browser_arcade.py`: **superado**, completa los 30 retos y mantiene las verificaciones de animación, pausa, movimiento reducido del sistema, limpieza de bucles y puntuación.
- `python3 tests/browser_smoke.py`: **superado**, evalúa las diez modalidades, comprueba progreso, Unicode, idiomas, acceso docente, tablet, creación de contenido y CSV.
- `python3 tests/browser_progress.py`: **superado**, pulsa botones de decisión, comprueba errores/reintentos, pausa y desactivación de botones, movimiento de cohetes y ATIBOT, pantalla de 375 px, guardado de las cuatro modalidades, gráficos y marcas en galería, informes, CSV y conservación de datos después de detener y reiniciar el proceso servidor.
- Revisadas capturas reales de las cuatro escenas en Chromium. No se afirma una tasa de FPS garantizada ni ejecución en Windows desde este entorno Linux.
- `python3 server.py --init-only`: ejecutado sobre la base local; verificadas 60 variantes de sala y las cuatro columnas de valoración. No se versiona la base ni sus datos.
- Comprobaciones de sintaxis de `app.js`, `arcade.js`, `motion.js` y `git diff --check`: sin errores.
