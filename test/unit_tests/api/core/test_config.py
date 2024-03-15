import unittest
import tempfile
import json
from unittest.mock import patch
from unittest.mock import mock_open
from src.api.core import config


class TestConfig(unittest.TestCase):

    def setUp(self):
        self._app_config_file = tempfile.TemporaryFile()
        self._app_config_file.write(json.dumps(self._return_config_file()).encode('utf-8'))

    def tearDown(self):
        self._app_config_file.close()

    def _return_config_file(self):
        return "app_name: 'mlops-architecture'\r\n" \
                     "api_prefix: '/api'\r\n" \
                     "is_debug: true\n" \
                     "log_filename: 'logs/mlops-architecture.log'\n" \
                     "work_dir: './logs'\n" \
                     

    def test_get_app_config_parameters(self):
        # do
        with \
                patch('src.api.core.config.logging.info'), \
                patch('src.api.core.config.open', mock_open(read_data='')), \
                patch('src.api.core.config.logging.exception'), \
                patch('src.api.core.config.yaml.safe_load') as safe_load:
            safe_load.return_value = self._return_config_file()
            ret = config.get_app_config_parameters(self._app_config_file)

            # check
            self.assertEqual(ret, self._return_config_file())
