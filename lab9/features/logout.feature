Feature: Logout
    Scenario: Successful logout from dashboard
        Given I am logged in
        When I click the logout button
        Then I should be logged out
        And I should be redirected to login page

    Scenario: Session timeout logout
        Given I am logged in
        When my session expires
        Then I should be logged out
        And I should see a session timeout message