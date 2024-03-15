"""
Middleware to log arrival and completion of a request.
"""
import logging
import time
from uuid import uuid4
from starlette.requests import Request
from src.api.core.config import REQUEST_LOGGER


async def add_process_time_header(request: Request, call_next):

    """
    Middleware to log arrival and completion of a request by
    logging its correlationId and total processing time.

    Args:
        :param  request: request object
        :param  call_next: call_next object

    Returns:
        response
    """
    corr_id = request.headers.get('X-Correlation-ID', "NO_DOC_ID_" + str(uuid4()))
    request.state.corr_id = corr_id
    logger = logging.getLogger(REQUEST_LOGGER)
    logger.info("New request arrived corrId : %s ", corr_id)
    start_time = time.time()
    response = await call_next(request)
    process_time = time.time() - start_time
    logger.info("Total processing time: %s  corrId: %s", process_time, corr_id)
    return response
