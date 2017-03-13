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
import datetime
import httplib

from classes.driver import Driver

cpf 		= "YOUR CPF GOES HERE"			# ex:12345678900 (no separating dots and no dashes)
password	= "YOUR PASSWORD GOES HERE"
date 		= "DATE WORKED GOES HERE" 		#ex: 07/03/2017


bot = Driver("https://tratamento.certponto.com.br")
bot.go_and_login(cpf, password)
bot.pick_current_month()
bot.scroll_down()
bot.show_more_records()
bot.punch_in(date)
