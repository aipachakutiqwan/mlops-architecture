import unittest
from unittest.mock import patch
from unittest.mock import MagicMock
from src.api.core import log_management


class TestLogManagement(unittest.TestCase):

    def test_configure_logging(self):
        # plan
        config = {'work_dir': None}
        log_config = {'TEST': None}
        # do
        with\
                patch('src.api.core.log_management.os.path') as os_path,\
                patch('src.api.core.log_management.logging.config') as logging_config,\
                patch('src.api.core.log_management.os.makedirs') as os_makedirs:
            os_path.return_value = None
            os_path.join = MagicMock(return_value=None)
            log_management.configure_logging(config, log_config)

            # check
            logging_config.dictConfig.assert_called_once_with(log_config)
            os_makedirs.assert_called_once_with(None, exist_ok=True)

    def test_filter(self):
        with self.subTest():
            # plan
            record = MagicMock()
            # do
            target = log_management.CorrIdFilter()
            ret = target.filter(record)

            # check
            self.assertEqual(record.corrId, 'no-corr')

        with self.subTest():
            # plan
            corr = 111

            # do
            record.args = {'corrId': corr}
            target = log_management.CorrIdFilter()
            ret = target.filter(record)

            # check
            self.assertEqual(record.corrId, corr)
