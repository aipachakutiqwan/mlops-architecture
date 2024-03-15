import unittest
import time
from unittest.mock import patch
from unittest.mock import MagicMock
from unittest.mock import AsyncMock


from src.api.core import middlewares


class TestMiddlewares(unittest.IsolatedAsyncioTestCase):

    async def test_add_process_time_header(self):
        # plan
        request = MagicMock()
        request.header.get.return_value = "f058ebd6-02f7-4d3f-942e-904344e8cde5"
        call_next = AsyncMock()
        call_next.return_value = "call_next return"
        # do
        with \
                patch('src.api.core.middlewares.logging.info'), \
                patch('src.api.core.middlewares.logging.error'), \
                patch('src.api.core.middlewares.logging.getLogger') as logging_getLogger, \
                patch('src.api.core.middlewares.time') as time_time, \
                patch('src.api.core.middlewares.uuid4') as uuid4, \
                patch('src.api.core.middlewares.REQUEST_LOGGER') as request_logger:
            time_time.return_value = time.time()
            uuid4.return_value = "abcdefgh12345"
            request_logger.return_value = True
            ret = await middlewares.add_process_time_header(request, call_next)

            # check
            self.assertEqual(ret, call_next.return_value)
            logging_getLogger.assert_called_once()
