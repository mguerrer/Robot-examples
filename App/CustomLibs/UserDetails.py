userDetails = {"qa_admin"             : "Tester6285",
               "auto_user"            : "Indigo4!",               
               "biq_stg_admin"        : "Tester0824",
               "biq_stg_admin2"       : "Tester252",
               "ft_2733_hd"           : "Tester0524",
               "paygo_user"           : "Tester1124",
               "2733-test"            : "Tester3566",
               "hd_amazon"            : "Tester6281",
               "dev_admin"            : "Tester2565",
               "qa_hd_2733"           : "Tester3566",
               "qa_enduser1_2733"     : "Tester3565",
               "uat_reseller"         : "Tester3565",
               "uat_reseller_client1" : "Tester3565",
               "hd_reseller_user_2"   : "Tester3565",
               "qa_admin1"            : "Tester0995"}

def get_password(username):
    """
    This function is used to login in BIQ when BIQ login page is already opened
    :param username:
    :return:
    """
    password = userDetails[username]
    return  password