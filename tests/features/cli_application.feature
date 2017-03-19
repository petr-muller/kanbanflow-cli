Feature: A CLI application exists

Scenario: Executing Without Parameters
    When I Execute KBF
    Then KBF Execution Succeeds

Scenario: Executing With Config File Parameter (good)
    Given Good Config File Exists
    When I Execute KBF With Good Config File
    Then KBF Execution Succeeds

Scenario: Executing With Config File Parameter (bad)
    Given Bad Config File Exists
    When I Execute KBF With Bad Config File
    Then KBF Execution Fails With Bad Config File Message

Scenario: Executing With Config File Parameter (missing)
    When I Execute KBF With Missing Config File
    Then KBF Execution Fails With Missing Config File Message
