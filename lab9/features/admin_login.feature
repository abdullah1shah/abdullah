Feature: Admin Login
    Scenario: Successful admin login
        Given I am on the admin login page
        When I enter valid admin credentials
        And I click the login button
        Then I should be logged in as admin
        And I should see the admin dashboard

    Scenario: Failed admin login
        Given I am on the admin login page
        When I enter invalid admin credentials
        And I click the login button
        Then I should see an error message
        And I should remain on the login page