# SPDX-FileCopyrightText: 2024-present kevinassimos <kevin.assimos@acad.ufsm.br>
#
# SPDX-License-Identifier: MIT


def celsius_para_fahrenheit(celsius: float) -> float:
    """
    Converte uma temperatura de Celsius para Fahrenheit.

    :param celsius: Temperatura em graus Celsius.
    :return: Temperatura em graus Fahrenheit.
    """
    return (celsius * 9/5) + 32


def fahrenheit_para_celsius(fahrenheit: float) -> float:
    """
    Converte uma temperatura de Fahrenheit para Celsius.

    :param fahrenheit: Temperatura em graus Fahrenheit.
    :return: Temperatura em graus Celsius.
    """
    return (fahrenheit - 32) * 5/9
