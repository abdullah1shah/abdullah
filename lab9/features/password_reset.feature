Feature: Password Reset
    Scenario: Successful password reset
        Given I am on the password reset page
        When I enter my registered email
        And I click reset password button
        Then I should receive a reset link
        And I should see a confirmation message

    Scenario: Failed password reset
        Given I am on the password reset page
        When I enter an unregistered email
        And I click reset password button
        Then I should see an error message
        And I should not receive a reset link