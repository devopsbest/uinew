# -*- coding: utf-8 -*-
__author__ = 'Anderson'

from ptest.decorator import TestClass, Test, BeforeMethod, AfterMethod
from ptest.plogger import preporter

from autotest.pages.Android.loginpage import Login
from setupenv import setup_env
from autotest.pages.Android.courseoverviewpage import Course


@TestClass(run_mode='singleline')
class LoginTest:
    @BeforeMethod(description="Prepare test data.")
    def setup_data(self):
        # setup_env()
        self.login = Login()
        self.username = 'stest41516'
        self.password = '1'
        print("start to test")

    @Test()
    def check_login_success(self):
        self.login.login_action(self.username, self.password)
        Course(self.login.driver).logout()


    @Test()
    def check_logout_success(self):
        Course(self.login.driver).logout()

    @AfterMethod(always_run=True, description="Clean up")
    def after(self):
        preporter.info("cleaning up")
        self.login.driver.quit()
        # self.login.driver.close_app()
