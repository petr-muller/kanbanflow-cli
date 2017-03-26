# pylint: disable=missing-docstring,no-self-use,too-few-public-methods

import kbfcli


class TestRun(object):
    def test_run(self):
        kbfcli.run_kbf_client([])
