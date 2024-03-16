"""
Entrance and configuration Fast API class
"""
import os
from fastapi import FastAPI
from src.api.core.config import get_app_config_parameters
from src.api.core.event_handlers import start_app_handler
from src.api.core.log_management import configure_logging
from src.api.router.router import API_ROUTER

APP_CONFIG_FILE = os.environ.get('APP_CONFIG_FILE', 'config/app_config.yaml')
LOG_CONFIG_FILE = os.environ.get('LOG_CONFIG_FILE', 'config/log_config.yaml')


def get_app(arg_app_config_file: str, arg_log_config_file: str) -> FastAPI:
    """
    Entrance function for the API where some configurations are done.

    Args:
        :param  arg_app_config_file: model architecture
        :param  arg_log_config_file: train loader data

    Returns:
        FastAPI configured
    """
    config = get_app_config_parameters(arg_app_config_file)
    log_config = get_app_config_parameters(arg_log_config_file)
    fast_app = FastAPI(title=config['app_name'], version=config['app_version'],
                       debug=config['is_debug'], swagger_ui_parameters={"syntaxHighlight.theme": "obsidian"})
    fast_app.include_router(API_ROUTER, prefix=config['api_prefix'])
    fast_app.add_event_handler('startup', start_app_handler(fast_app, config))
    configure_logging(config, log_config)
    return fast_app


APP = get_app(arg_app_config_file=APP_CONFIG_FILE, arg_log_config_file=LOG_CONFIG_FILE)
