Feature: Student Registration System

  Scenario: Successful student registration
    Given the student enters valid registration details
    When the student submits the registration form
    Then the registration should be successful

  Scenario: Registration with missing email
    Given the student leaves the email field empty
    When the student submits the registration form
    Then an error message should be displayed