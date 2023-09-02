class Locators:
    #LoginPage Locators
    username_input_box = 'username'
    password_input_box = 'password'
    submit_button = '//*[@id="app"]/div[1]/div/div[1]/div/div[2]/div[2]/form/div[3]/button'
    error_msg = '//*[@id="app"]/div[1]/div/div[1]/div/div[2]/div[2]/div/div[1]/div[1]/p'

    #HomePage Locators
    PIM_Link = 'PIM'
    Add_button = '//*[@id="app"]/div[1]/div[2]/div[2]/div/div[2]/div[1]/button'
    First_name = 'firstName'
    Last_name = 'lastName'
    #Emp_Id = "/html/body/div/div[1]/div[2]/div[2]/div/div/form/div[1]/div[2]/div[1]/div[2]/div/div/div[2]/input"
    Employee_name = '//*[@id="app"]/div[1]/div[2]/div[2]/div/div[1]/div[2]/form/div[1]/div/div[1]/div/div[2]/div/div/input'
    Save_Button = '//*[@id="app"]/div[1]/div[2]/div[2]/div/div/form/div[2]/button[2]'
    Edit_SaveBtn = '//*[@id="app"]/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[5]/button'
    Search_Button = '//*[@id="app"]/div[1]/div[2]/div[2]/div/div[1]/div[2]/form/div[2]/button[2]'
    Edit_Employee = '//*[@id="app"]/div[1]/div[2]/div[2]/div/div[2]/div[3]/div/div[2]/div/div/div[9]/div/button[2]/i'
    Delete_Employee = '//*[@id="app"]/div[1]/div[2]/div[2]/div/div[2]/div[3]/div/div[2]/div/div/div[9]/div/button[1]/i'
    DelConfirm_Popup = '//*[@id="app"]/div[3]/div/div/div/div[3]/button[2]'

    #AdminPage Locators
    #Forget_PasswordLink = "//p[text()='Forgot your password? ']"
    Forget_PasswordLink = '//*[@id="app"]/div[1]/div/div[1]/div/div[2]/div[2]/form/div[4]/p'
    username_input_box = 'username'
    #Reset_Password = "//button[text()=' Reset Password ']"
    Reset_password = "/html/body/div/div[1]/div[1]/div/form/div[2]/button[2]"
    Admin_Link = "Admin"
    Get_Title = '//*[@id="app"]/div[1]/div[1]/aside/nav/div[1]/a/div[2]/img'
    User_Management = "//span[contains(@class, 'oxd-topbar-body-nav-tab-item') and text() = 'User Management ']"
    Job_Header = "//span[contains(@class, 'oxd-topbar-body-nav-tab-item') and text() = 'Job ']"
    Organization_Header = "//span[contains(@class, 'oxd-topbar-body-nav-tab-item') and text() = 'Organization ']"
    Qualification_Header = "//span[contains(@class, 'oxd-topbar-body-nav-tab-item') and text() = 'Qualifications ']"
    Nationalities_Header = "Nationalities"
    Corporate_Branding_Header = "Corporate Branding"
    Configuration_Header = "//span[contains(@class, 'oxd-topbar-body-nav-tab-item') and text() = 'Configuration ']"

    #LeftSide Panel
    Leave_Link = "Leave"
    Time_Link = "Time"
    Recruitment_Link = "Recruitment"
    MyInfo_Link = "My Info"
    Performance_Link = "Performance"
    Dashboard_Link = "Dashboard"
    Directory_Link = "Directory"
    Maintenance_Link = "Maintenance"
    Claim_Link = "Claim"
    Buzz_Link = "Buzz"








