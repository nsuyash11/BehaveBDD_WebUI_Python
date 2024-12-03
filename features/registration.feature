Feature: Registration Feature

    As a new non-registered user
    I want to be able to create an account on IRCTC website
    So that I can access the website and perform ticket booking related transactions


    Background: Load Registration Page
        Given User is on Registration Page

    @runthisonly
    Scenario: Register with all blank fields
        When User enters all fields blank
        And User clicks Submit button
        Then User should get appropriate warning message on all fields

    
    Scenario Outline: Register with invalid username and other fields valid
        When User enters invalid username "<username>" and other fields "<fullname>", "<password>", "<email>", "<mobile>" valid
        And User clicks Submit button
        Then User should get appropriate warning message "<message>" for username field

        Examples:
            | username | fullname    | password     | email       | mobile     | message                            |
            | empty    | Daya Shetty | Password$123 | abc@abc.com | 1234567890 | User Name is required.             |
            | space    | Daya Shetty | Password$123 | abc@abc.com | 1234567890 | User Name is invalid.              |
            | @#       | Daya Shetty | Password$123 | abc@abc.com | 1234567890 | User Name is invalid.              |
            | random   | Daya Shetty | Password$123 | abc@abc.com | 1234567890 | User Name [ random ] Not Available |


    Scenario Outline: Register with invalid fullname and all other fields valid
        When User enters invalid fullname "<fullname>" and all other fields "<username>", "<password>", "<email>", "<mobile>" valid
        And User clicks Submit button
        Then User should get appropriate warning "<message>" for invalid fullname field

        Examples:
            | fullname | username    | password     | email       | mobile     | message                                       |
            | empty    | dayashetty5 | Password$123 | abc@abc.com | 1234567890 | Full Name is required.                        |
            | space    | dayashetty5 | Password$123 | abc@abc.com | 1234567890 | Full Name Min 1 character & Max 50 character. |
            | @#$      | dayashetty5 | Password$123 | abc@abc.com | 1234567890 | Name is invalid.                              |


    Scenario Outline: Register with invalid password and all other fields valid
        When User enters invalid password "<password>" and all other fields "<username>", "<fullname>", "<email>", "<mobile>" valid
        And User clicks Submit button
        Then User should get appropriate warning "<message>" for invalid password field

        Examples:
            | password  | username    | fullname    | email       | mobile     | message               |
            | empty     | dayashetty5 | Daya Shetty | abc@abc.com | 1234567890 | Password is required. |
            | space     | dayashetty5 | Daya Shetty | abc@abc.com | 1234567890 | Password is           |
            | !@#$%^&*- | dayashetty5 | Daya Shetty | abc@abc.com | 1234567890 | Password is invalid.  |
            | Aa1@      | dayashetty5 | Daya Shetty | abc@abc.com | 1234567890 | Password is invalid.  |
            | abcd1234  | dayashetty5 | Daya Shetty | abc@abc.com | 1234567890 | Password is invalid.  |
            | abcdABCD  | dayashetty5 | Daya Shetty | abc@abc.com | 1234567890 | Password is invalid.  |
            | ABCD1234  | dayashetty5 | Daya Shetty | abc@abc.com | 1234567890 | Password is invalid.  |


    Scenario Outline: Register with invalid confirm password and all other fields valid
        When User enters invalid confirm password "<cnfpwd>" and all other fields "<username>", "<fullname>", "<password>", "<email>", "<mobile>" valid
        And User clicks Submit button
        Then User should get appropriate warning "<message>" for invalid confirm password field

        Examples:
            | cnfpwd      | password     | username    | fullname    | email       | mobile     | message                                    |
            | empty       | Password@123 | dayashetty5 | Daya Shetty | abc@abc.com | 1234567890 | Confirm password                           |
            | space       | Password@123 | dayashetty5 | Daya Shetty | abc@abc.com | 1234567890 | Password and Confirm password not Matched. |
            | Password@12 | Password@123 | dayashetty5 | Daya Shetty | abc@abc.com | 1234567890 | Password and Confirm password not Matched. |


    Scenario Outline: Register with invalid email and all other fields valid
        When User enters invalid email "<email>" and all other fields "<username>", "<fullname>", "<password>", "<mobile>" valid
        And User clicks Submit button
        Then User should get appropriate warning "<message>" for invalid email field

        Examples:
            | email             | username    | fullname    | password     | mobile     | message                                           |
            | empty             | dayashetty5 | Daya Shetty | Password@123 | 1234567890 | Email is required.                                |
            | space             | dayashetty5 | Daya Shetty | Password@123 | 1234567890 | Email is required.                                |
            | a@b.in            | dayashetty5 | Daya Shetty | Password@123 | 1234567890 | Email Min 10 character & Max 70 character.        |
            | abcde             | dayashetty5 | Daya Shetty | Password@123 | 1234567890 | Email is invalid.                                 |
            | johndoe@gmail.com | dayashetty5 | Daya Shetty | Password@123 | 1234567890 | Email ID is already linked with other IRCTC User. |


    Scenario Outline: Register with invalid mobile and all other fields valid
        When User enters invalid mobile "<mobile>" and all other fields "<username>", "<fullname>", "<password>", "<email>" valid
        And User clicks Submit button
        Then User should get appropriate warning "<message>" for invalid mobile field

        Examples:
            | mobile     | username    | fullname    | password     | email       | message                                             |
            | empty      | dayashetty5 | Daya Shetty | Password@123 | abc@abc.com | Mobile No is required.                              |
            | space      | dayashetty5 | Daya Shetty | Password@123 | abc@abc.com | Mobile No is required.                              |
            | !@#$%^&*   | dayashetty5 | Daya Shetty | Password@123 | abc@abc.com | Mobile No                                           |
            | 123        | dayashetty5 | Daya Shetty | Password@123 | abc@abc.com | Mobile No is invalid.                               |
            | abcdefghij | dayashetty5 | Daya Shetty | Password@123 | abc@abc.com | Mobile No                                           |
            | 0123456789 | dayashetty5 | Daya Shetty | Password@123 | abc@abc.com | Indian Mobile No is invalid.                        |
            | 9876543210 | dayashetty5 | Daya Shetty | Password@123 | abc@abc.com | Mobile No. is already linked with other IRCTC User. |

    @bugraised
    Scenario Outline: Register with invalid captcha and all other fields valid
        When User enters invalid captcha "<captcha>" and all other fields "<username>", "<fullname>", "<password>", "<email>", "<mobile>" valid
        And User clicks Submit button
        Then User should get appropriate warning "<message>" for invalid captcha field

        Examples:
            | captcha | username    | fullname    | password     | email       | mobile     | message |
            | empty   | dayashetty5 | Daya Shetty | Password@123 | abc@abc.com | 1234567890 |         |
            | space   | dayashetty5 | Daya Shetty | Password@123 | abc@abc.com | 1234567890 |         |
            | 12345   | dayashetty5 | Daya Shetty | Password@123 | abc@abc.com | 1234567890 |         |
            | abcde   | dayashetty5 | Daya Shetty | Password@123 | abc@abc.com | 1234567890 |         |


    @no-background
    Scenario: Verify various ways to load Registration page
        Given User is on Home Page
        When User clicks Register link from links in top section
        Then User should be able to load Registration Page

        Given User is on Login Page
        When User clicks Register button
        Then User should be able to load Registration Page

        Given User is anywhere
        When User hits direct Registration Page URL
        Then User should be able to load Registration Page