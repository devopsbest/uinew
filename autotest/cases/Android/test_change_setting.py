__author__ = 'Anderson'

from ptest.decorator import TestClass, Test, BeforeMethod, AfterMethod
from ptest.plogger import preporter

from autotest.pages.Android.changesettings import Settings
from autotest.pages.Android.courseoverviewpage import Course
from autotest.pages.Android.loginpage import Login
from globals import get_current_package
from setupenv import clear_catch


@TestClass(run_mode='singleline')
class LoginTest:
    @BeforeMethod(description="Prepare test data.")
    def setup_data(self):
        #setup_env()
        self.login = Login()
        self.username = 'newqa@qp1.org'
        self.password = '11111111'
        print("start to test")
        self.course = Course(self.login.driver)
        self.setting = Settings(self.login.driver)



    @Test()
    def chang_language(self):
        self.login.login_action(self.username,self.password)
        self.setting.change_language_android("Español")
        self.course.logout_action()

    @AfterMethod(always_run=True, description="Clean up")
    def after(self):
        preporter.info("cleaning up")
        clear_catch(get_current_package())
        self.login.driver.quit()
