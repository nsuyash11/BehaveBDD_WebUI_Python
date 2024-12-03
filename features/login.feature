Feature: Login Functionality
    As a registered user
    I want to be able to log in to the IRCTC website
    So that I can access my account and perform ticket booking related transactions

    Background: Load Login Page
        Given User is on Login Page

    Scenario Outline: Login with all valid matching credentials - Username, Password and Captcha
        When User enters valid credentials in "<username>", "<password>", captcha
        And User clicks Sign In button
        Then User should be able to log in successfully

        Examples:
            | username | password |
            | validuid | validpwd |


    Scenario Outline: Login with invalid username, valid password, valid captcha
        When User enters invalid "<username>", valid "<password>", valid captcha
        And User clicks Sign In button
        Then User should get proper warning error "<message>" for login User

        Examples:
            | username                           | password | message                    |
            | empty                              | random   | Please Enter Valid User ID |
            | space                              | random   | Please Enter Valid User ID |
            | @#$                                | random   | Invalid User               |
            | thisisveryveryveryveryverylonguser | random   | Invalid User               |
            | randomuser                         | random   | Bad Credentials            |


    Scenario Outline: Login with valid username, invalid password, valid captcha
        When User enters valid "<username>", invalid "<password>", valid captcha
        And User clicks Sign In button
        Then User should get proper warning error "<message>" for login Password

        Examples:
            | username | password                               | message                     |
            | random   | empty                                  | Please Enter Valid Password |
            | random   | space                                  | Please Enter Valid Password |
            | random   | @#$                                    | Bad Credentials             |
            | random   | thisisveryveryveryveryverylongpassword | Bad Credentials             |
            | random   | random@123                             | Bad Credentials             |


    Scenario Outline: Login with valid username, valid matching password, invalid captcha
        When User enters valid "<username>", valid matching "<password>", invalid "<captcha>"
        And User clicks Sign In button
        Then User should get proper warning error "<message>" for login Captcha

        Examples:
            | username | password | captcha                               | message                    |
            | random   | validpwd | empty                                 | Please Enter Valid Captcha |
            | random   | validpwd | space                                 | Please Enter Valid Captcha |
            | random   | validpwd | @#$                                   | Invalid Captcha....        |
            | random   | validpwd | thisisveryveryveryveryverylongcaptcha | Invalid Captcha....        |
            | random   | validpwd | abc12                                 | Invalid Captcha....        |


    Scenario: Login with all blank fields
        When User keeps username, password, captcha fields blank
        And User clicks Sign In button
        Then User should get proper warning error message for all blank entries

    @runthisonly
    Scenario: User requests forgotten account details
        When User clicks Forgot Account Details link
        Then User should be directed to Forgot Account Details Page

    @runthisonly
    Scenario: User wants to Register an account
        When User clicks Register button
        Then User should be directed to Account Registration Page

