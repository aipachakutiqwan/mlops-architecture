import unittest
from unittest.mock import patch
from unittest.mock import MagicMock
from src.api.core import event_handlers


class TestEventHandlers(unittest.TestCase):

    def test_start_app_handler(self):
        # plan
        app = 'TEST'
        app_config = {}
        # do
        with\
                patch('src.api.core.event_handlers.logging.info') as logging_info,\
                patch('src.api.core.event_handlers._startup_model') as startup_model:

            ret = event_handlers.start_app_handler(app, app_config)
            ret()

            # check
            self.assertTrue(ret)
            logging_info.assert_called_once_with('Running app start handler.')
            startup_model.assert_called_once_with(app, app_config)
