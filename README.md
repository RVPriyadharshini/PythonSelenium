---------------------------------------------PythonSelenium--------------------------------------------
Created the page object model framework using selenium Python for OrangeHRM application
**pytest-HTML** report used in the framework  
Below testcases are covered as part of the Framework
1) Successful Employee login to OrangeHRM portal
      # Python test case name in the Testcase directory - "**test_login.py**"
2) Invalid Employee login to OrangeHRM portal
      # Python test case name in the Testcase directory - "**test_login.py**"
3) Add , Edit and Delete a new employee in the PIM module
      # Python test case name in the Testcase directory - "**test_EmployeeValidation.py**"
4) Forget password link validation on login page
      # Python test case name in the Testcase directory - "**test_ForgetPasswordLinkValidation.py**"
5) Header validation on Admin page
      # Python test case name in the Testcase directory - "**test_AdminHeaderValidation.py**"
6) Main Menu validation on Admin page
      # Python test case name in the Testcase directory - "**test_ValidateAdminMenuItems.py**"

Created Dictionaries in the project based on POM model
  a) PageObjects  - Dictionary to add the Individual Python file which contains the all methods/functions of the each page
        #AdminPage  - Contains all Admin page methods
        #HomePage   - Contains all Home page methods
        #LoginPage  - Contains all Login page methods
  b) Reports  -  Dictionary to add the report , Currently using pytest HTML report and its adding in the testcases dictionary by default
  c) Screenshot - Dictionary to add the screenshots either fail or pass based on the method used in the testcases
  d) test_cases  - Dictionary to add the test cases for the orange HRM application
        #test_login.py  - Validate login successfull and failure
        #test_EmployeeValidation.py -  Validate add, edit and delete employee
        #test_ForgetPasswordLinkValidation.py  -  Validate the forgot password link page
        #test_AdminHeaderValidation.py  -  Validate the Admin headers
        #test_ValidateAdminMenuItems.py  -  Validate the Admin Main menu
  e) TestData -  Dictionary to add the common test data which used in the test cases
  f) TestLocators  -  Dicitonary to add all the page locators in one place and differntiated by the comments in the python file
  g) Utilities -  Dictionary to add the common methods
  
  
Executing the testcase in terminal using pytest commands

To execute all testcases in the test_case dictionary  - pytest -v -ra --html=report.html

