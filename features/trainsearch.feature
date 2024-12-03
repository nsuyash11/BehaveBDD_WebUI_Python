Feature: Search Trains

    As a User
    I want to be able to Search for Trains
    So that I can book relevant tickets for my Journey

    Background: Load Home Page
        Given  User is on Home Page

    
    Scenario Outline: Search with invalid from station, all other fields valid
        When User enters invalid fromstation as "<fromstation>" and other fields "<tostation>", "<quota>", "<jdate>", "<travelclass>"
        And User clicks Search button
        Then User should get appropriate warning error "<message>" for station input

        Examples:
            | fromstation | tostation            | quota   | jdate      | travelclass | message |
            | empty       | THANE - TNA (MUMBAI) | GENERAL | 11/09/2024 | All         | input   |
            | space       | THANE - TNA (MUMBAI) | GENERAL | 11/09/2024 | All         | input   |
            | THANE       | THANE - TNA (MUMBAI) | GENERAL | 11/09/2024 | All         | input   |
            | TNA         | THANE - TNA (MUMBAI) | GENERAL | 11/09/2024 | All         | input   |
            | @#$         | THANE - TNA (MUMBAI) | GENERAL | 11/09/2024 | All         | input   |


    Scenario Outline: Search with invalid to station, all other fields valid
        When User enters invalid tostation as "<tostation>" and other fields "<fromstation>", "<quota>", "<jdate>", "<travelclass>"
        And User clicks Search button
        Then User should get appropriate warning error "<message>" for station input

        Examples:
            | tostation | fromstation          | quota   | jdate      | travelclass | message |
            | empty     | THANE - TNA (MUMBAI) | GENERAL | 11/09/2024 | All         | input   |
            | space     | THANE - TNA (MUMBAI) | GENERAL | 11/09/2024 | All         | input   |
            | THANE     | THANE - TNA (MUMBAI) | GENERAL | 11/09/2024 | All         | input   |
            | TNA       | THANE - TNA (MUMBAI) | GENERAL | 11/09/2024 | All         | input   |
            | @#$       | THANE - TNA (MUMBAI) | GENERAL | 11/09/2024 | All         | input   |


    Scenario Outline: Search with invalid date, all other fields valid
        When User enters invalid date as "<jdate>" and other fields "<fromstation>", "<tostation>", "<quota>", "<travelclass>"
        And User clicks Search button
        Then User should get appropriate warning error "<message>" for date input

        Examples:
            | fromstation                | tostation            | quota   | jdate             | travelclass | message |
            | RATNAGIRI - RN (RATNAGIRI) | THANE - TNA (MUMBAI) | GENERAL | empty             | All         | date    |
            | RATNAGIRI - RN (RATNAGIRI) | THANE - TNA (MUMBAI) | GENERAL | space             | All         | date    |
            | RATNAGIRI - RN (RATNAGIRI) | THANE - TNA (MUMBAI) | GENERAL | @#$               | All         | date    |
            | RATNAGIRI - RN (RATNAGIRI) | THANE - TNA (MUMBAI) | GENERAL | 11 September 2024 | All         | date    |
            | RATNAGIRI - RN (RATNAGIRI) | THANE - TNA (MUMBAI) | GENERAL | 11/09/2023        | All         | date    |
            | RATNAGIRI - RN (RATNAGIRI) | THANE - TNA (MUMBAI) | GENERAL | 11/09/2025        | All         | date    |


    Scenario Outline: Search for non-existing train route
        When User enters non-existing train route "<fromstation>" with "<tostation>" and other fields "<quota>", "<jdate>", "<travelclass>" valid
        And User clicks Search button
        And User confirms indirect journey search
        Then User should get appropriate results "<message>" on train search list page

        Examples:
            | fromstation | tostation               | quota   | jdate      | travelclass | message  |
            | UKSHI - UKC | JAMTARA - JMT (ASANSOL) | GENERAL | 11/09/2024 | All         | 0 result |


    Scenario Outline: Search for existing valid inputs
        When User enters existing train route "<fromstation>" with "<tostation>" and other fields "<quota>", "<jdate>", "<travelclass>" valid
        And User clicks Search button
        Then User should get appropriate results on train search list page

        Examples:
            | fromstation                | tostation            | quota   | jdate      | travelclass |
            | RATNAGIRI - RN (RATNAGIRI) | THANE - TNA (MUMBAI) | GENERAL | 11/09/2024 | All         |
