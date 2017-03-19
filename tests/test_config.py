# pylint: disable=missing-docstring,no-self-use,too-few-public-methods,redefined-outer-name

import io
import pytest  # type: ignore
import kbfcli.config


@pytest.fixture
def config_file():
    return kbfcli.config.KBFConfig()


class TestConfigFile(object):
    def test_sanity(self):
        config = kbfcli.config.KBFConfig()
        assert config is not None

    def test_write(self, config_file):
        writable = io.StringIO()
        config_file.write(writable)
        written = writable.getvalue()
        assert written == "[boards]\n\n"
