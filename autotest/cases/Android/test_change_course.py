# -*- coding: utf-8 -*-
__author__ = 'Anderson'

from ptest.decorator import TestClass, Test, BeforeMethod, AfterMethod
from ptest.plogger import preporter

from autotest.pages.Android.courseoverviewpage import Course
from autotest.pages.Android.loginpage import Login
from autotest.pages.Android.managecoursepage import ManageCourse
from globals import get_current_package
from setupenv import setup_env, clear_catch


@TestClass(run_mode='singleline')
class LoginTest:
    @BeforeMethod(description="Prepare test data.")
    def setup_data(self):
        setup_env()
        self.login = Login()
        self.username = 'stest39700'
        self.password = '1'
        print("start to test")
        self.course = Course(self.login.driver)
        self.changecourse=ManageCourse(self.login.driver)


    @Test()
    def chang_ge_level(self):
        self.login.login_action(self.username,self.password)
        self.course.change_course_action()
        self.changecourse.change_level_on_GE(4)
        self.course.logout_action()

    @AfterMethod(always_run=True, description="Clean up")
    def after(self):
        preporter.info("cleaning up")
        clear_catch(get_current_package())
        self.login.driver.quit()
