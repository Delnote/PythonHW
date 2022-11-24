*** Settings ***
Resource  resources.robot
Test Setup  Open Browser And Login
Test Teardown  Close Browser Window

*** Test Cases ***
Login test
    [Documentation]  User can login
    Validate Logged In

Add Monitor To Cart test
    [Documentation]  User can add monitor to cart
    Go To Monitors
    Select Most Expensive Monitor
    Verify Product
    Add Product To Cart
    Go To Cart
    Verify Product In Cart

