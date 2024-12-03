Feature: PNR Status Enquiry

    As a user
    I want to be able to do enquiry of PNR
    so that I can get latest status of a train ticket


    Scenario: Load PNR Status Enquiry Page
        Given User is on Home Page
        When User clicks PNR Status link
        Then User should be able to load PNR Status Enquiry Page in separate tab

    @buggywillfail
    Scenario Outline: Enquiry with invalid PNR
        Given User is on PNR Page
        When User enters PNR number "<pnr>"
        And User clicks Submit PNR button
        Then User should get warning message for PNR field validation

        Examples:
            | pnr |
            | 123 |
            | 12345678901 |
            | abcdefghij |
            | @#$ |


    Scenario Outline: Enquiry with valid non-existing PNR
        Given User is on PNR Page
        When User enters PNR number "<pnr>"
        And User clicks Submit PNR button
        And User enters valid captcha
        And User clicks Submit Captcha button
        Then User should get warning "<message>" for invalid PNR

        Examples:
            | pnr | message |
            | 1234567890  | Error! PNR No. is not valid  |

    @runthisonly
    Scenario Outline: Enquiry with invalid Captcha
        Given User is on PNR Page
        When User enters PNR number "<pnr>"
        And User clicks Submit PNR button
        And User enters invalid captcha
        And User clicks Submit Captcha button
        Then User should get warning "<message>" for invalid Captcha

        Examples:
            | pnr | message |
            | 1234567890  | Error! Captcha not matched  |


    Scenario Outline: Enquiry with valid existing PNR and valid Captcha
        Given User is on PNR Page
        When User enters PNR number "<pnr>"
        And User clicks Submit PNR button
        And User enters valid captcha
        And User clicks Submit Captcha button
        Then User should be able to see the PNR Status

    Examples:
        | pnr |
        | 8721575927 |
