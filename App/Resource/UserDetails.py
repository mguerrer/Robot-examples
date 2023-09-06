userDetails = {"qa_admin": "Tester6287",
               "auto_user": "Magenta4!",
               "aes_hd_1":  "Tester6286",
               "auto_user_lock"       : "Tester1234",    
               "autouser_V2_default"  : "Tester2565",    
               "biq_stg_admin"        : "Tester0824",
               "biq_stg_admin2"       : "Tester252",
               "ft_2733_hd"           : "Tester0524",
               "paygo_user"           : "Tester1124",
               "2733-test"            : "Tester3570",
               "hd_amazon"            : "Tester6285",
               "dev_admin"            : "Tester2565",
               "qa_hd_2733"           : "Tester3571",
               "qa_enduser1_2733"     : "Tester3565",
               "uat_reseller"         : "Tester3565",
               "uat_reseller_client1" : "Tester3565",
               "hd_reseller_user_2"   : "Tester3565",
               "auto_eu_4405_998708"  : "Tester1111",
               "auto_hd_4405_998708"  : "Tester1111",
               "auto_user3"           : "Tester12345",
               "qa_admin1"            : "Tester0995",
               "mysettings_non_premium": "Test1234"}

def get_password(username):
    """
    This function is used to login in BIQ when BIQ login page is already opened
    :param username:
    :return:
    """
    password = userDetails[username]
    return  password

def get_users():
    names = []
    for user in userDetails:
        names.append( user )
    return names