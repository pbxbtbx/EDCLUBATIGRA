"""Start the local academy and open the user's browser. No hosting required."""

import argparse
import json
import sys
import threading
import urllib.error
import urllib.request
import webbrowser

import server


def is_academy(url):
    """Only reuse this installation and loaded build, never a stale server."""
    try:
        with urllib.request.urlopen(url + "/api/config", timeout=1) as response:
            config = json.loads(response.read())
        return (
            config.get("build") == server.BUILD_ID
            and config.get("installation") == server.INSTALLATION_ID
        )
    except (OSError, ValueError, urllib.error.URLError):
        return False


def main():
    parser = argparse.ArgumentParser(description="Iniciar ATIBOT en tu ordenador")
    parser.add_argument("--port", type=int, default=8000)
    parser.add_argument("--no-browser", action="store_true")
    args = parser.parse_args()
    if sys.version_info < (3, 11):
        raise SystemExit("Necesitas Python 3.11 o superior.")
    if not 1 <= args.port <= 65535:
        raise SystemExit("El puerto debe estar entre 1 y 65535.")
    print("ATIBOT - version " + server.BUILD_ID, flush=True)
    for port in range(args.port, min(args.port + 20, 65536)):
        url = f"http://127.0.0.1:{port}"
        if is_academy(url):
            print("ATIBOT ya esta funcionando en este ordenador: " + url, flush=True)
            if not args.no_browser:
                webbrowser.open(url)
            return
        try:
            http = server.make_server("127.0.0.1", port)
            break
        except OSError as error:
            if error.errno not in (48, 98, 10048):
                raise
            print(
                f"El puerto {port} pertenece a otra instancia o version. Buscando un puerto libre...",
                flush=True,
            )
    else:
        raise SystemExit(
            "No hay un puerto local libre. Cierra las ventanas antiguas de ATIBOT y vuelve a iniciar."
        )
    # Check critical runtime requirements before opening a browser or accepting logins.
    server.madrid_timezone()
    server.seed()
    print("\nATIBOT listo en tu ordenador: " + url, flush=True)
    print("Mantén esta ventana abierta. Pulsa Ctrl+C para detenerlo.", flush=True)
    print("Los datos se guardan en: " + str(server.DB_PATH), flush=True)
    if not args.no_browser:
        # The listener is already bound. serve_forever will answer once the browser connects.
        threading.Timer(0.3, lambda: webbrowser.open(url)).start()
    try:
        http.serve_forever()
    except KeyboardInterrupt:
        print("\nATIBOT detenido. Tu progreso esta guardado.", flush=True)
    finally:
        http.server_close()


if __name__ == "__main__":
    main()
