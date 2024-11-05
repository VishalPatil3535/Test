import configparser

config = configparser.RawConfigParser()
config.read("C:\\Users\\vishalp\\pytestpython\\CourseraProject\\Configurations\\config.ini")

class read_config:
    @staticmethod
    def get_login_url():
        url = config.get('Login_page','base_url')
        return url

    @staticmethod
    def get_login_username():
        username = config.get('Login_page','email')
        return username

    @staticmethod
    def get_login_password():
        password = config.get('Login_page', 'password')
        return password

    @staticmethod
    def get_login_invalid_username():
        invalid_username = config.get('Login_page', 'invalid_email')
        return invalid_username

    @staticmethod
    def get_error_msg():
        error_msg = config.get('Login_page', 'error_msg')
        return error_msg
