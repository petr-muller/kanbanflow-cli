# pylint: disable=missing-docstring,no-self-use,too-few-public-methods,redefined-outer-name

import io
import configparser
import pytest  # type: ignore
import kbfcli.config


@pytest.fixture
def config_file():
    return kbfcli.config.KBFConfig()


class TestConfigFile(object):
    def test_sanity(self):
        config = kbfcli.config.KBFConfig()
        assert config is not None

    def test_invalid(self, mocker):
        mocked_instance = mocker.MagicMock()
        mocked_instance.read.side_effect = configparser.MissingSectionHeaderError("some_path", 1, 1)

        mocked_parser = mocker.MagicMock()
        mocked_parser.return_value = mocked_instance

        mocker.patch('configparser.ConfigParser', mocked_parser)

        with pytest.raises(kbfcli.config.KBFConfigError):
            kbfcli.config.KBFConfig("invalid config file path")

    def test_write(self, config_file):
        writable = io.StringIO()
        config_file.write(writable)
        written = writable.getvalue()
        assert written == "[boards]\n\n"

    def test_boards(self, config_file):
        assert config_file.boards() == {}
