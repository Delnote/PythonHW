*** Settings ***
Documentation  Pack of tests for Lecture 14
Library  Collections
Library  SeleniumLibrary

*** Variables ***
${Browser}  Chrome
${URL}  https://www.demoblaze.com/
${LOGIN}  usertesttest
${PASSWORD}  testtest
&{product}
&{LOGIN_LOCATORS}  login_submit=//button[.='Log in']  login=loginusername  password=loginpassword  logout_button=logout2  wellcome_text=nameofuser
&{PRODUCT_PAGE}  product_name=css:h2.name  product_price=css:h3.price-container  add_to_cart=css:[id="tbodyid"] .row a
&{CART_PAGE}  cart_product=css:tr.success:nth-child(1)  product_title=css:tr.success:nth-child(1) td:nth-child(2)  product_price=css:tr.success:nth-child(1) td:nth-child(3)

*** Test Cases ***
#Login test
#    [Documentation]  User can login
#    Open Browser  ${URL}  ${Browser}
#    Maximize Browser Window
#    Open Login Form
#    Validate Login Form
#    login  ${LOGIN}  ${PASSWORD}
#    Validate Logged In

Add Monitor To Cart test
    [Documentation]  User can add monitor to cart
    Open Browser  ${URL}  ${Browser}
    Maximize Browser Window
    Open Login Form
    login  ${LOGIN}  ${PASSWORD}
    Go To Monitors
    Select Most Expensive Monitor
    Verify Product
    Add Product To Cart
    Go To Cart
    Verify Product In Cart

*** Keywords ***
Open Login Form
    Click Element   login2

Validate Login Form
    Element Should Be Enabled  ${LOGIN_LOCATORS.login_submit}
    Element Should Be Enabled  ${LOGIN_LOCATORS.login}
    Element Should Be Enabled  ${LOGIN_LOCATORS.password}

login
    [Arguments]    ${username}  ${password}
    Input Text    loginusername    ${username}
    Input Text    loginpassword    ${password}
    Click Element    //button[.='Log in']
    Wait Until Element Contains  ${LOGIN_LOCATORS.wellcome_text}  Welcome

Validate Logged In
    Element Should Be Enabled    ${LOGIN_LOCATORS.logout_button}
    Element Should Contain    ${LOGIN_LOCATORS.wellcome_text}  Welcome ${LOGIN}

Go To Monitors
    Click Element  //*[.='Monitors']
    Sleep    3000 ms

Select Most Expensive Monitor
    @{prices}=   Get WebElements  css:div.card-block > h5
    ${priceList}=  Create List
    FOR  ${price}  IN  @{prices}
        Append To List  ${priceList}  ${price.text}
    END
    ${maxPrice}=  Evaluate  max(${priceList})
    ${monitor_name}=  Get Text  //h5[.='${maxPrice}']/../..//h4/a
    Set To Dictionary  ${product}  monitor_name=${monitor_name}  maxPrice=${maxPrice}
    Click Element   //h5[.='${product.maxPrice}']/../../a

Verify Product
    Wait Until Element Is Enabled  ${PRODUCT_PAGE.product_name}
    Element Should Contain  ${PRODUCT_PAGE.product_name}  ${product.monitor_name}
    Element Should Contain  ${PRODUCT_PAGE.product_price}  ${product.maxPrice}

Add Product To Cart
    Click Element  ${PRODUCT_PAGE.add_to_cart}
    Alert Should Be Present  Product added.

Go To Cart
    Click Element  id:cartur

Verify Product In Cart
    Wait Until Element Is Enabled  ${CART_PAGE.cart_product}
    Element Should Contain  ${CART_PAGE.product_title}  ${product.monitor_name}
    ${price}=  Get Text  ${CART_PAGE.product_price}
    Should Contain  ${product.maxPrice}  ${price}
