#!/usr/bin/env python3.8

import socket

"""
Author: Jared Dyreson
Function: Client class that can communicate with another
"""


class Client():
    def __init__(self, name: str):
        if not(isinstance(name, str)):
            raise ValueError

        self.name = name
        self.answer = None
        self.is_winner = False

    def get_answer(self, equation: str):
        if not(isinstance(equation, str)):
            raise ValueError

        try:
            return int(input(f'{self.name.upper()} --> what is {equation} ? : '))
        except Exception as error:
            print(f'error received: {error}')


