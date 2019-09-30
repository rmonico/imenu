#!/usr/bin/python3
# coding:utf-8

import console
import os


class Menu(object):

    def __init__(self):
        self.title = None
        self.header_builder = None
        self._itens = []
        self._variables = os.environ.copy()

    def add_item(self, menu_item):
        self._itens.append(menu_item)

    def _print_item(self, item):
        for i in range(0, item._lines_before):
            print()

        print('{}.  {}'.format(item._shortcut, item._label))

    def run(self):
        result = None

        while result not in ('quit', 'back'):
            console.clear_screen()

            self._draw_menu()

            key = console.getch()

            for item in self._itens:
                if key == item._shortcut:
                    result = item.run(self._variables)
                    break

    def _draw_menu(self):
        if self.header_builder:
            self.header_builder(self._variables)
            print()

        if self.title:
            print('*** {} ***'.format(self.title))
            print()

        for item in self._itens:
            self._print_item(item)


class MenuItem(object):

    def __init__(self, shortcut, label, action=None, lines_before=0):
        self._shortcut = shortcut
        self._label = label
        self._action = None
        self._lines_before = lines_before

    def run(self, environment):
        if self._action and hasattr(self._action, '__call__'):
            result = self._action(environment)

            return result if result else 'ok'
        else:
            return 'ok'


class OSCommandMenuItem(MenuItem):

    def __init__(self, shortcut, label, os_command=None):
        super().__init__(shortcut, label)

        self._command = os_command

    def run(self, environment):
        super().run(environment)

        os.system(self._command.format(**environment))

        console.wait()

        return 'ok'


class InternalCommandMenuItem(MenuItem):

    def __init__(self, shortcut, label, command):
        super().__init__(shortcut, label, lines_before=2)
        self._command = command

    def run(self, environment):
        super().run(environment)

        return self._command


class VariableSetterMenuItem(MenuItem):

    def __init__(self, shortcut, label, variable):
        super().__init__(shortcut, label)

        self.variable = variable

    def run(self, environment):
        super().run(environment)

        print()
        print('Possible commands ::cancel ::remove')
        print('Current {}\'s value: "{}"'.format(self.variable, environment.get(self.variable, '<not defined>')))
        value = input('{} = '.format(self.variable))

        if value == '::remove':
            if self.variable in environment.keys():
                environment.pop(self.variable)
        elif value != '::cancel':
            environment[self.variable] = value

        return 'ok'
