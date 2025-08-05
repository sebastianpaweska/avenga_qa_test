import click
import sys
import os
import pytest
import logging
import logging.config
import yaml
import shutil
import time
import subprocess

from datetime import datetime
from allure_combine import combine_allure

from consts.paths import Paths


def set_logger():
    log_dir = Paths.LOG_DIRECTORY
    os.makedirs(log_dir, exist_ok=True)

    with open(Paths.LOGGING_CONFIG, 'r') as f:
        config = yaml.safe_load(f)

    config['handlers']['fileHandler']['filename'] = str(Paths.LOG_FILE)

    logging.config.dictConfig(config)
    return logging.getLogger()

def generate_allure_report():
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    allure_dir = f"{Paths.ALLURE_DIRECTORY}"
    allure_reports_dir = f"{Paths.ALLURE_REPORTS_DIRECTORY}"
    report_dir = f"{Paths.REPORT_DIRECTORY}"

    subprocess.run(["allure", "generate", allure_dir, "-o", allure_reports_dir, "--clean"], check=True)
    combine_allure(allure_reports_dir, report_dir, remove_temp_files=True)
    report_path = os.path.join(report_dir, "complete.html")
    test_report_path = os.path.join(report_dir, f"test_report_{timestamp}.html")
    os.rename(report_path, test_report_path)

def prepare_directories():
    if os.path.exists(Paths.ALLURE_DIRECTORY):
        shutil.rmtree(Paths.ALLURE_DIRECTORY)
    if os.path.exists(Paths.ALLURE_REPORTS_DIRECTORY):
        shutil.rmtree(Paths.ALLURE_REPORTS_DIRECTORY)
    os.makedirs(Paths.ALLURE_DIRECTORY, exist_ok=True)
    os.makedirs(Paths.ALLURE_REPORTS_DIRECTORY, exist_ok=True)
    os.makedirs(Paths.REPORT_DIRECTORY, exist_ok=True)
    time.sleep(1)  # allure throws an error if dir is not created, needs short sleep here

@click.group
def cli():
    pass

@cli.command("run")
@click.option('--marker', default=None, help='Run tests with this pytest marker')
def run(marker):
    logger = set_logger()
    logger.info("Logger initialized")

    prepare_directories()

    args = ["-v", "-s", "tests"]
    if marker:
        args.append("-m")
        args.append(marker)
    args.append(f"--alluredir={Paths.ALLURE_DIRECTORY}")
    retcode = pytest.main(args=args)
    generate_allure_report()

    # Close all loggers before exit
    for handler in logging.root.handlers[:]:
        handler.flush()
        handler.close()
        logging.root.removeHandler(handler)

    sys.exit(retcode)


if __name__ == "__main__":
    cli()