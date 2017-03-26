# pylint: disable=redefined-outer-name,missing-docstring

import subprocess
import pytest  # type: ignore
from pytest_bdd import given, when, then, scenario  # type: ignore

from kbfcli.config import KBFConfig


class KBFCLIExecution(object):
    def __init__(self):
        self.command = ["python", "bin/kbf.py"]
        self._popen = None

    def add_arguments(self, arguments):
        self.command.extend(arguments)

    def execute(self):
        self._popen = subprocess.Popen(self.command, stdout=subprocess.PIPE, stderr=subprocess.PIPE)

    @property
    def execution(self):
        return self._popen


@pytest.fixture
def kbfcli_execution():
    return KBFCLIExecution()


@scenario("cli_application.feature", "Executing Without Parameters")
def test_run_without_params():
    pass


@scenario("cli_application.feature", "Executing With Config File Parameter (good)")
def test_run_with_config_param():
    pass


@scenario("cli_application.feature", "Executing With Config File Parameter (bad)")
def test_run_with_bad_config_param():
    pass


@given("Good Config File Exists")
def config_file(tmpdir):
    config = KBFConfig()
    config_file = tmpdir.join(".kanbanflow.ini")
    config.write(config_file)
    return config_file

@given("Bad Config File Exists", target_fixture="config_file")
def bad_config_file(tmpdir):
    config_file = tmpdir.join(".kanbanflow.ini")
    config_file.write("Some Crap")
    return config_file


@when("I Execute KBF")
def execute_kbf(kbfcli_execution):
    kbfcli_execution.execute()


@when("I Execute KBF With Good Config File")
@when("I Execute KBF With Bad Config File")
def execute_kbf_with_config(config_file, kbfcli_execution):
    config_file_path = str(config_file)
    kbfcli_execution.add_arguments(["--config", config_file_path])
    kbfcli_execution.execute()

@then("KBF Execution Succeeds")
def execution_succeeds(kbfcli_execution):
    execution = kbfcli_execution.execution
    execution.wait()
    assert execution.returncode == 0

@then("KBF Execution Fails With Bad Config File Message")
def execution_fails_with_bad_config(kbfcli_execution):
    execution = kbfcli_execution.execution
    execution.wait()
    assert execution.returncode != 0
    _, error_output = execution.communicate()
    assert b"Invalid config file" in error_output
