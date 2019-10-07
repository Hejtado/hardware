import argparse
import sys
import yaml

from app import create_app


def load_config(config_file):
    with open(config_file, 'r') as stream:
        try:
            return yaml.safe_load(stream)
        except yaml.YAMLError as exc:
            print(exc)


parser = argparse.ArgumentParser(description='Hejtado Hardware Microservice')
parser.add_argument('-c', '--config-file', help='Config file',
                    type=str, default='config.yml')
parser.add_argument('-d', '--debug', help='Enable Debug Mode',
                    action='store_true', default='True')

args = parser.parse_args(args=sys.argv[1:])
debug = args.debug
config = load_config(args.config_file)
connection_section = config['connection']
thermometers_section = config['thermometers']

flask_section = config['flask']
flask_port = flask_section['port']
flask_host = flask_section['host']

def main():
    app = create_app()
    app.run(port=flask_port, host=flask_host, debug=debug)

if __name__ == "__main__":
    main()