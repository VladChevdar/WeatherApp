# Vlad Chevdar | CS302 | Aug 23
# The purpose of this file is to test weather display functions

import pytest
import io
import unittest
from unittest.mock import patch, Mock
from User import User
from Weather import Weather, DetailedReport, BriefReport, FunnyReport

class TestWeather(unittest.TestCase):

    def setUp(self):
        self.weather = Weather()
        self.location = 'Portland, Oregon'

    def set_weather_attributes(self, report):
        report._location = 'Portland, Oregon'
        report._temperature = 75.0
        report._description = 'clear sky'
        report._wind_speed = 10.0
        report._humidity = 80
        report._pressure = 1000
        report._temp_min = 70.0
        report._temp_max = 80.0
        report._visibility = 10000 # 6.2 miles
        report._wind_direction = 90
        report._cloudiness = 20
        report._sunrise = 1629252065 # 19:01:05
        report._sunset = 1629301854 # 08:50:54

    def test_detailed_report_display(self):
        report = DetailedReport()
        self.set_weather_attributes(report)

        with patch('sys.stdout', new_callable=io.StringIO) as fake_stdout:
            report.display()
            output = fake_stdout.getvalue()

        expected_output = (
            '\n📍 Location: Portland, Oregon\n-|- Weather Details -|- \n\n'
            '🌡 Temperature: 75.0°F\n🌥 Description: clear sky\n💨 Wind Speed: 10.0 mph\n'
            '💧 Humidity: 80%\n📊 Pressure: 1000 hPa\n🔽 Min Temperature: 70.0°F\n'
            '🔼 Max Temperature: 80.0°F\n👓 Visibility: 6.2 miles\n🧭 Wind Direction: 90°\n'
            '☁ Cloudiness: 20%\n🌅 Sunrise: 19:01:05\n🌇 Sunset: 08:50:54\n'
        )
        self.assertEqual(output, expected_output), 'Mismatch in detailed weather report'

    def test_funny_report_display(self):
        report = FunnyReport()
        self.set_weather_attributes(report)

        with patch('sys.stdout', new_callable=io.StringIO) as fake_stdout:
            report.display()
            output = fake_stdout.getvalue()

        expected_output = (
            '\n📍 Location: Portland, Oregon\n-|- Weather Details -|- \n\n'
            '🌡 Temperature: 75.0°F 😅 It\'s that confusing weather where you regret both wearing and not wearing a jacket!\n'
            '🌥 Description: clear sky 😂 Clear skies! Perfect for spotting UFOs.\n'
            '🌅 Sunrise: 19:01:05 - 😴 Up before the sun? You deserve a medal... or at least some strong ☕️!\n'
            '🌇 Sunset: 08:50:54 - 🛌 The sun\'s taking a break, and it didn\'t even ask for our permission!\n'
        )
        self.assertEqual(output, expected_output), 'Mismatch in funny weather report'

    def test_brief_report_display(self):
        report = BriefReport()
        self.set_weather_attributes(report)

        with patch('sys.stdout', new_callable=io.StringIO) as fake_stdout:
            report.display()
            output = fake_stdout.getvalue()

        expected_output = (
            '\n📍 Location: Portland, Oregon\n-|- Weather Details -|- \n\n'
            '🌡 Temperature: 75.0°F\n🌥 Description: clear sky\n💨 Wind Speed: 10.0 mph\n'
            '🌅 Sunrise: 19:01:05\n🌇 Sunset: 08:50:54\n'
        )
        self.assertEqual(output, expected_output), 'Mismatch in brief weather report'

if __name__ == '__main__':
    unittest.main()
