from enum import Enum
from pathlib import Path
from datetime import datetime

class Paths:
    ROOT_DIRECTORY = Path.cwd()
    HOME_DIRECTORY = Path.home()
    LOG_DIRECTORY = ROOT_DIRECTORY / "logs"
    LOGGING_CONFIG = ROOT_DIRECTORY / "config" / "logging.yaml"
    LOG_FILE = LOG_DIRECTORY / f"{datetime.now().replace(microsecond=0).isoformat().replace(':', '-')}.log"
    REPORT_DIRECTORY = ROOT_DIRECTORY / "reports"
    ALLURE_DIRECTORY = ROOT_DIRECTORY / "allure-results"
    ALLURE_REPORTS_DIRECTORY = ROOT_DIRECTORY / "allure-reports"
