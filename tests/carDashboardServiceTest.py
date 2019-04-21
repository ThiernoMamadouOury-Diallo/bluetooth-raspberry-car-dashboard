# coding: utf-8

import random
import unittest
from services import CarDashboardService

class carDashboardServiceTest(unittest.TestCase):

    """This test cases are used for validating CarDashboardService functions"""

    def test_getFuelLevel(self):
        """Test getFuelLevel check message format of operation"""
        
        excepted_message = "Niveau du carburant est de %s Litre" % 15
        
        self.assertEqual(excepted_message, CarDashboardService.getFuelLevel())


    def test_getEngineTemperature(self):
        """Test getEngineTemperature check message format of operation"""
        
        excepted_message = "La temperature du moteur est de 30 ° Celsius"
        
        self.assertEqual(excepted_message, CarDashboardService.getEngineTemperature())

    