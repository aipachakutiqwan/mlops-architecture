"""
Start up the handler class
"""
import logging
from typing import Callable
from fastapi import FastAPI
from src.handlers.predictor import Predictor


def _startup_model(app: FastAPI, app_config: dict) -> None:
    request_predictor = Predictor(app_config)
    app.state.predictor = request_predictor
    logging.info("Request handler initialized")


def start_app_handler(app: FastAPI, app_config: dict) -> Callable:
    """
    Start up the handler class and set it in the FastAPI config.

    Args:
        :param app: FastAPI class

    Returns:
        FastAPI configured
    """
    def startup() -> None:
        logging.info("Running app start handler.")
        _startup_model(app, app_config)

    return startup
