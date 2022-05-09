@login
Feature: Log in to the application
        As a user
        I want to log in to the application
        So that I can use it's features

        @login @common-login
        Scenario: Log in with correct credentials
        Given I am on the PfizerPro home page,
        And I click on the login link,
        When I enter my username and password,
        And I click the login button,
        Then I should be logged in to the application.
        
        @login @incorrect-password
        Scenario: Log in with incorrect credentials
        Given I am on the PfizerPro home page,
        And I click on the login link,
        When I enter my email and incorrect password,
        And I click the login button,
        Then I should not be logged in to the application.

        @login @incorrect-email
        Scenario: Log in with incorrect email
        Given I am on the PfizerPro home page,
        And I click on the login link,
        When I enter an incorrect email and password,
        And I click the login button,
        Then I should not be logged in to the application.

        @login @empty-email
        Scenario: Log in with empty email and password
        Given I am on the PfizerPro home page,
        And I click on the login link,
        When I enter an empty email and password,
        And I click the login button,
        Then Nothing will happen.

        @login @not-an-email
        Scenario: Not an email address
        Given I am on the PfizerPro home page,
        And I click on the login link,
        When I enter a not an email address and password,
        And I click the login button,
        Then Log in button will be disabled,
        And Email field will be highlighted.

        @forgot-password @forgotten-password
        Scenario: Forgotten password
        Given I am on the PfizerPro home page,
        And I click on the login link,
        When I click the forgotten password link,
        Then I should be on the forgotten password page.

        @forgot-password @reset-password
        Scenario: Request new password
        Given I am on the PfizerPro home page,
        And I click on the login link,
        When I click the forgotten password link,
        And I enter my email address,
        And I click the request new password button,
        Then I should receive an email with a link to reset my password.

        @forgot-password @request-new-password-with-invalid-email
        Scenario: Request new password with invalid email
        Given I am on the PfizerPro home page,
        And I click on the login link,
        When I click the forgotten password link,
        And I enter an invalid email address,
        And I click the request new password button,
        Then The email input field will be highlighted,
        And The request new password button will be disabled.

        @forgot-password @request-new-password-with-empty-email
        Scenario: Request new password with empty email
        Given I am on the PfizerPro home page,
        And I click on the login link,
        When I click the forgotten password link,
        And I do not enter an email address,
        And I click the request new password button,
        Then The request new password button will be disabled.

        @forgot-password @return-from-forgotten-password-page
        Scenario: Return from request new password page
        Given I am on the PfizerPro home page,
        And I click on the login link,
        When I click the forgotten password link,
        And I click the return button,
        Then I should be on the login page.

        @forgot-password @close-forgotten-password-page
        Scenario: Close request new password page
        Given I am on the PfizerPro home page,
        And I click on the login link,
        When I click the forgotten password link,
        And I click the close button,
        Then I should be on the home page.

        @login @return-from-login-page
        Scenario: Return from login page
        Given I am on the PfizerPro home page,
        And I click on the login link,
        When I click the return button,
        Then I should be on the home page.


