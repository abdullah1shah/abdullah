Feature: User Login
    Scenario: Successful user login
        Given I am on the login page
        When I enter valid user credentials
        And I click the login button
        Then I should be logged in
        And I should see the dashboard

    Scenario: Failed user login
        Given I am on the login page
        When I enter invalid credentials
        And I click the login button
        Then I should see an error message
        And I should remain on the login page