# SPDX-FileCopyrightText: 2024-present kevinassimos <kevin.assimos@acad.ufsm.br>
#
# SPDX-License-Identifier: MIT
# tests/test_converter.py
import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))

from conversor_temperatura.converter import celsius_para_fahrenheit, fahrenheit_para_celsius

def test_celsius_para_fahrenheit():
    assert celsius_para_fahrenheit(0) == 32
    assert celsius_para_fahrenheit(100) == 212
    assert celsius_para_fahrenheit(-40) == -40

def test_fahrenheit_para_celsius():
    assert fahrenheit_para_celsius(32) == 0
    assert fahrenheit_para_celsius(212) == 100
    assert fahrenheit_para_celsius(-40) == -40
