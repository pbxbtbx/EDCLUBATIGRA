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
