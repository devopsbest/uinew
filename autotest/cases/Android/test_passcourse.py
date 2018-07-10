# -*- coding: utf-8 -*-
__author__ = 'Anderson'

from ptest.decorator import TestClass, Test, BeforeMethod, AfterMethod

from autotest.pages.Android.courseoverviewpage import Course
from autotest.pages.Android.loginpage import Login
from globals import get_current_package
from setupenv import clear_catch


@TestClass(run_mode='singleline')
class LoginTest:
    @BeforeMethod(description="Prepare test data.")
    def setup_data(self):
    #    setup_env()
        self.login = Login()
        self.username = 'newqa@qp1.org'
        self.password = '11111111'
        print("start to test")
        self.course = Course(self.login.driver)


    @Test()
    def pass_one_lesson(self):
        self.login.login_action(self.username,self.password)
        self.course.pass_one_lesson_action("l3")
        self.course.logout_action()

    @Test()
    def pass_one_unit(self):

        self.login.login_action(self.username,self.password)
        self.course.pass_one_unit_action()
        self.course.logout_action()


    @AfterMethod(always_run=True, description="Clean up")
    def after(self):
        #preporter.info("cleaning up")
        clear_catch(get_current_package())
        self.login.driver.quit()
        # self.login.driver.close_app()
