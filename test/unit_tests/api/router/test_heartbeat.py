import unittest
from unittest.mock import patch
from src.api.router import heartbeat


class TestHeartbeat(unittest.TestCase):

    def test_get_heartbeat(self):
        # plan

        # do
        with\
                patch('src.api.router.heartbeat.HeartbeatResponse') as m1:
            m1.return_value = True
            ret = heartbeat.get_heartbeat()

            # check
            self.assertTrue(ret)
