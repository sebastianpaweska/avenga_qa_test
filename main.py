import click
import sys
import os
import pytest
import logging
import logging.config
import yaml

from consts.paths import Paths


def set_logger():
    log_dir = Paths.LOG_DIRECTORY
    os.makedirs(log_dir, exist_ok=True)

    with open(Paths.LOGGING_CONFIG, 'r') as f:
        config = yaml.safe_load(f)

    config['handlers']['fileHandler']['filename'] = str(Paths.LOG_FILE)

    logging.config.dictConfig(config)
    return logging.getLogger()

@click.group
def cli():
    pass

@cli.command("run")
@click.option('--marker', default=None, help='Run tests with this pytest marker')
def run(marker):
    logger = set_logger()
    logger.info("Logger initialized")
    args = ["-v", "-s", "tests"]
    if marker:
        args.append(f"-m {marker}")
    retcode = pytest.main(args=args)
    sys.exit(retcode)


if __name__ == "__main__":
    cli()