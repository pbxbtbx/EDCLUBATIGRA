# Acceder online desde el navegador

La aplicación necesita un servidor: GitHub Pages solo sirve archivos estáticos y no ejecuta el backend Python ni conserva SQLite.

## Render: instalación sin abrir Python en tu ordenador

1. Crea o abre tu cuenta en Render y conecta GitHub.
2. Pulsa **Deploy to Render** en el README. Se importará `render.yaml` de este repositorio.
3. Revisa el coste indicado por Render antes de confirmar: esta configuración usa un servicio **Starter y un disco persistente**, que son de pago. No se promete alojamiento gratuito ni se crea una suscripción desde este repositorio.
4. En `ATIGRA_ADMIN_PASSWORD`, introduce una contraseña propia de al menos 8 caracteres **en el formulario seguro de Render**, nunca en GitHub ni en el chat. El usuario docente inicial es `comandante` (se puede cambiar antes del primer arranque mediante `ATIGRA_ADMIN_USERNAME`).
5. Confirma el despliegue en Render y espera a que el servicio aparezca como **Live**.
6. Abre la URL HTTPS que Render muestra en el panel del servicio. Esa es la dirección real para usar la aplicación en el navegador. No existe hasta completar el despliegue; el botón del README es un enlace de instalación, no el enlace de una aplicación ya publicada.
7. Entra como docente con tus credenciales. Crea una clase y los alumnos, y asígnales misiones. Los 36 niveles ya estarán disponibles en el catálogo. Esta instancia online no crea alumnos ni contraseñas demo.
8. Comparte la URL del servicio y comunica las credenciales de cada alumno privadamente. Se necesita teclado físico para las actividades.

Puedes acceder desde otro ordenador sin instalar Python. Render conserva la base en el disco `atigra-data`; los intentos no deben desaparecer al reiniciar el proceso o volver a desplegar. Configura también copias de seguridad. **Eliminar el servicio/disco puede borrar los datos**: conserva una copia antes de hacerlo.

## Railway o servidor propio

El mismo backend de producción funciona con:

```bash
pip install -r requirements.txt
python wsgi.py
```

Configura `PORT` con el puerto del alojamiento (8000 por defecto), `ATIGRA_DB` como ruta en un volumen persistente, `ATIGRA_DEMO=0`, `ATIGRA_ADMIN_USERNAME` y `ATIGRA_ADMIN_PASSWORD`. Con HTTPS, utiliza `ATIGRA_SECURE_COOKIE=1`. En un servidor propio, configura un proxy HTTPS, supervisión del proceso y backups; conserva el encabezado Host original. No expongas un servicio HTTP con cookies Secure activadas: el inicio de sesión requiere HTTPS en ese modo.

El servidor de producción es Waitress, con cuatro hilos y límite de cuerpo de petición de 2 MB. Reutiliza la API y las reglas verificadas de la aplicación. El servidor local original (`python server.py`) sigue disponible sin instalar paquetes.

La contraseña de arranque solo se usa si no existen usuarios. Cambiar esa variable después no cambia una contraseña guardada; utiliza `python manage.py reset-password --username comandante` en la consola privada del alojamiento. No hay un formulario público de registro de docentes ni recuperación por correo.

No se despliega ni se contrata alojamiento al subir estos archivos a GitHub. Hace falta una cuenta de alojamiento y confirmar el servicio allí. La comprobación local de producción no demuestra que el despliegue remoto haya terminado ni que exista una URL pública.

## ¿Se puede usar GitHub Pages?

Pages sirve HTML, CSS y JavaScript, pero no ejecuta Python ni mantiene una base de datos del servidor. Por eso **activar Pages en este repositorio no basta para usar la aplicación completa**: los accesos y la API no funcionarían.

Es posible alojar la interfaz en Pages y la API en otro servicio, pero la aplicación actual usa un solo origen. Separarlos requiere adaptar la URL de la API y configurar de forma segura los orígenes permitidos y las sesiones; sigue haciendo falta un alojamiento para el backend y los datos. No se ha implementado ni desplegado esa separación. Para mantener la autenticación, las clases y el progreso compartido, el despliegue completo de arriba es la ruta preparada.
