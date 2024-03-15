"""
Creates logger with formatters and handlers
"""
import logging
import logging.config
import os


class CorrIdFilter(logging.Filter):
    """
    A simple log filter to ensure corr-id is populated
    """

    def filter(self, record):
        record.corrId = record.args.get("corrId") if 'corrId' in record.args else "no-corr"
        return True


def configure_logging(config, log_config):
    """
    Creates the request logger with formatters and handlers.

    Args:
        :param  config: configuration dictionary
        :param  log_config: log configuration file

    Returns:
        FastAPI configured
    """

    log_dir = os.path.join(config['work_dir'])
    try:
        os.makedirs(log_dir, exist_ok=True)
    except Exception as exc:
        raise RuntimeError('Log folder cannot be created!', exc)

    logging.config.dictConfig(log_config)
