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
    try:
        with urllib.request.urlopen(url + "/api/config", timeout=2) as response:
            config = json.loads(response.read())
        with urllib.request.urlopen(url, timeout=2) as response:
            page = response.read(10000)
        return isinstance(config.get("demo"), bool) and b"ATIBOT Academy" in page
    except (OSError, ValueError, urllib.error.URLError):
        return False


def main():
    parser = argparse.ArgumentParser(description="Iniciar ATIBOT en tu ordenador")
    parser.add_argument("--port", type=int, default=8000)
    parser.add_argument("--no-browser", action="store_true")
    args = parser.parse_args()
    if sys.version_info < (3, 11):
        raise SystemExit("Necesitas Python 3.11 o superior.")
    url = f"http://127.0.0.1:{args.port}"
    if is_academy(url):
        print("ATIBOT ya esta funcionando en este ordenador: " + url, flush=True)
        if not args.no_browser:
            webbrowser.open(url)
        return
    server.seed()
    try:
        http = server.make_server("127.0.0.1", args.port)
    except OSError as error:
        if error.errno in (48, 98, 10048):
            raise SystemExit(
                f"El puerto {args.port} esta ocupado. Prueba: python iniciar.py --port {args.port + 1}"
            ) from error
        raise
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
