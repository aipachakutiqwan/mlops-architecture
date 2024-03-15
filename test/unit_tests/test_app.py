import unittest
from unittest.mock import patch
from unittest.mock import MagicMock
from src import app


class TestApp(unittest.TestCase):

    def test_get_app(self):
        # plan
        arg_app_config_file = None
        arg_log_config_file = None
        # do
        with\
                patch('src.app.get_app_config_parameters') as get_app_config_parameters,\
                patch('src.app.FastAPI') as FastAPI,\
                patch('src.app.configure_logging') as configure_logging,\
                patch('src.app.start_app_handler') as start_app_handler:
            get_app_config_parameters.return_value = {'app_name': 'name', 'app_version': 1.0, 'is_debug': False,\
                                                      'api_prefix': 'prefix'}
            FastAPI.return_value = MagicMock()
            start_app_handler.return_value = None
            ret = app.get_app(arg_app_config_file, arg_log_config_file)

            # check
            self.assertIsNotNone(ret)
            self.assertIsInstance(ret, MagicMock)

