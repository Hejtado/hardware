import argparse
import sys

from hejtado.hardware.app import create_app


def main(args=sys.argv[1:]):
    parser = argparse.ArgumentParser(description='Hejtado Hardware Microservice')
    parser.add_argument('--config-file', help='Config file',
                        type=str, default=None)

    args = parser.parse_args(args=args)

    app = create_app(args.config_file)

    host = app.config.get('host', '0.0.0.0')
    port = app.config.get('port', 5000)
    debug = app.config.get('DEBUG', False)


if __name__ == "__main__":
    main()