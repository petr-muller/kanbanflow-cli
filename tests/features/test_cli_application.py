# pylint: disable=redefined-outer-name,missing-docstring

import subprocess
import pytest  # type: ignore
from pytest_bdd import when, then, scenario  # type: ignore


@scenario("cli_application.feature", "Executing CLI Application Without Parameters")
def test_run_without_params():
    pass


@pytest.fixture
def kbf_without_params():
    return subprocess.Popen(["python", "bin/kbf.py"])


@when("I Execute KBF")
def execute_kbf(kbf_without_params):
    assert kbf_without_params is not None


@then("KBF Execution Succeeds")
def execution_succeeds(kbf_without_params):
    kbf_without_params.wait()
    assert kbf_without_params.returncode == 0
