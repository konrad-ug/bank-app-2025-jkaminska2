Feature: Account registry

Scenario: User is able to create 2 accounts
    Given Account registry is empty
    When I create an account using name: "kurt", last name: "cobain", pesel: "89092909246"
    And I create an account using name: "tadeusz", last name: "szcześniak", pesel: "79101011234"
    Then Number of accounts in registry equals: "2"
    And Account with pesel "89092909246" exists in registry
    And Account with pesel "79101011234" exists in registry

Scenario: User is able to update surname of already created account
    Given Account registry is empty
    And I create an account using name: "nata", last name: "haydamaky", pesel: "95092909876"
    When I update "surname" of account with pesel: "95092909876" to "filatov"
    Then Account with pesel "95092909876" has "surname" equal to "filatov"

Scenario: User is able to update name of already created account
    Given Account registry is empty
    And I create an account using name: "john", last name: "doe", pesel: "12345678910"
    When I update "name" of account with pesel: "12345678910" to "sean"
    Then Account with pesel "12345678910" has "name" equal to "sean"

Scenario: Created account has all fields correctly set
    Given Account registry is empty
    When I create an account using name: "annie", last name: "white", pesel: "11111111111"
    Then Account with pesel "11111111111" has "name" equal to "annie"
    And Account with pesel "11111111111" has "surname" equal to "white"

Scenario: User is able to delete created account
    Given Account registry is empty
    And I create an account using name: "parov", last name: "stelar", pesel: "01092909876"
    When I delete account with pesel: "01092909876"
    Then Account with pesel "01092909876" does not exist in registry
    And Number of accounts in registry equals: "0"

Scenario: Incoming transfer increases balance
    Given Account registry is empty
    And I create an account using name: "parov", last name: "stelar", pesel: "01092909876"
    When I make incoming transfer of "100" to account "01092909876"
    Then Account with pesel "01092909876" has balance equal to "100"

Scenario: Outgoing transfer decreases balance
    Given Account registry is empty
    And I create an account using name: "annie", last name: "white", pesel: "11111111111"
    When I make incoming transfer of "200" to account "11111111111"
    And I make outgoing transfer of "100" from account "11111111111"
    Then Account with pesel "11111111111" has balance equal to "100"
