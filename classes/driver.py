#!/usr/bin/env python
# -*- coding: UTF-8 -*-

#################################################
#
# Made with LUV on March 8, 2017 by:
# Plinio Freire <plinio.freire@gmail.com>
# Vinicius Silva <viniciuspontocom@gmail.com>
#
#################################################

from calendar import monthrange
import datetime, time

from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class Driver(object):
    """Instantiates a Selenium webdriver"""

    def __init__(self, url):
        super(Driver, self).__init__()
        self.driver         = webdriver.Firefox()
        self.wait           = WebDriverWait(self.driver, 15)
        self.wait_longer    = WebDriverWait(self.driver, 25)
        self.wait_even_more = WebDriverWait(self.driver, 35)
        self.action         = ActionChains(self.driver)
        self.driver.get(url)


    def _validate_date_format(self, day):
        if len(day) == 10:              # Ex: '01/02/2017'
           split_day = day.split('/')   # Ex: ['01', '02', '2017']

           if (len(split_day) == 3 and
              len(split_day[2]) == 4):
                return True
        else:
            print "Error: Invalid date!"
            return False


    def go_and_login(self, cpf, password):
        assert "CERTPONTO" in self.driver.title

        if self.wait.until(EC.element_to_be_clickable((By.XPATH, "//button[contains(@class,'button-btn-access')]"))):
            access_btn = self.driver.find_element_by_xpath("//button[contains(@class,'button-btn-access')]")
            access_btn.send_keys(Keys.ENTER)

        if self.wait.until(EC.element_to_be_clickable((By.XPATH, "//input[@placeholder='CPF']"))):
            cpf_input = self.driver.find_element_by_xpath("//input[@placeholder='CPF']")
            cpf_input.clear()
            cpf_input.send_keys(cpf)
            password_input = self.driver.find_element_by_xpath("//input[@placeholder='Senha']")
            password_input.clear()
            password_input.send_keys(password)
            sign_in_btn = self.driver.find_element_by_xpath("//button[contains(text(), 'Entrar')]")
            sign_in_btn.send_keys(Keys.ENTER)


    def pick_current_month(self):
        #TODO: Refactor the date and time declarations below into a new class
        now = datetime.datetime.now()
        holidays = [datetime.date(2017, 3, 8)] # you can add more here
        num_days = monthrange(now.year, now.month)[1] # number of days in a month

        try:
            first_day = datetime.date(now.year, now.month, 1).strftime('%d/%m/%Y')
            last_day = datetime.date(now.year, now.month, num_days).strftime('%d/%m/%Y')
        except(ValueError):
            print "Error!"

        if self.wait.until(EC.element_to_be_clickable((By.XPATH, "//input[contains(@ng-click, '" +first_day+ "')]"))):
            clock_btn = self.driver.find_element_by_xpath(
                "//input[contains(@ng-click, 'redirectTreatmentIndividual(\"" +first_day+ "\",\"" +last_day+ "\")')]"
            )
            clock_btn.send_keys(Keys.ENTER)


    def show_more_records(self):
        #TODO: Refactor the date and time declarations below into a new class
        now = datetime.datetime.now()
        holidays = [datetime.date(2017, 3, 8)] # you can add more here
        num_days = monthrange(now.year, now.month)[1] # number of days in a month

        try:
            first_day = datetime.date(now.year, now.month, 1).strftime('%d/%m/%Y')
        except(ValueError):
            print "Error!"

        time.sleep(3)
        if self.wait.until(EC.element_to_be_clickable((By.XPATH, "//*[contains(text(), '" +first_day+ "')]"))):
            total_regs = self.driver.find_element_by_xpath("//select[@name='totalRegistryPage']")
            total_regs.send_keys('50');


    def scroll_up(self, pos=250):
        self.driver.execute_script("window.scrollTo(0,"+str(pos)+")");


    def scroll_down(self, pos=0):
        self.driver.execute_script("window.scrollTo("+str(pos)+",0)");


    def add_entry(self, punch_in_time):
            #TODO: validate punch_in_time
            pass

    def close_sidebar(self):
        if self.wait.until(EC.element_to_be_clickable((By.XPATH, "//input[contains(@ng-click, 'closeSideNav()')]"))):
            close = self.driver.find_element_by_xpath("//input[contains(@ng-click, 'closeSideNav()')]")
            close.send_keys(Keys.ENTER)


    def punch_in(self, worked_day):
        if self._validate_date_format(worked_day):
            day = self.driver.find_element_by_xpath("//*[contains(text(), '" +worked_day+ "')]")
            day.click()

            time_entries = ['09:00', '18:00']
            #TODO: validate punch_in_time
            #TODO: refactor the code below into the "add_entry" method
            for i,entry in enumerate(time_entries, start=0):
                if self.wait.until(EC.element_to_be_clickable((By.XPATH, "//input[@title='Adicionar']"))):
                    add = self.driver.find_element_by_xpath("//input[@title='Adicionar']")
                    add.send_keys(Keys.NULL)
                    add.send_keys(Keys.ENTER)
                    enter = self.driver.find_elements_by_xpath("//input[@placeholder='HH:MM']")[i]
                    enter.send_keys(entry)
                    just = self.driver.find_elements_by_xpath("//select[contains(@ng-options, 'justificationList')]")[i]
                    just.send_keys('problem')
                    desc = self.driver.find_elements_by_xpath("//textarea[contains(@ng-change, 'limitLengthJustification')]")[i]
                    desc.send_keys("Sistema nao roda em Linux.")
                    save = self.driver.find_elements_by_xpath("//input[@title='Salvar']")[i]
                    save.send_keys(Keys.ENTER)
                    time.sleep(6)
            self.close_sidebar()
