#!/usr/bin/python3
# coding:utf-8

import console


class Menu(object):

    def __init__(self):
        self.title = None
        self._itens = []

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
                  item.run()



    def _draw_menu(self):
        if self.title:
            print('*** {} ***'.format(self.title))

        if self._itens and len(self._itens) > 0:
            print()

            for item in self._itens:
                self._print_item(item)


class MenuItem(object):

    def __init__(self, shortcut, label, lines_before=0):
        self._lines_before = lines_before
        self._shortcut = shortcut
        self._label = label


class OSCommandMenuItem(MenuItem):

    def __init__(self, shortcut, label, os_command=None):
        super().__init__(shortcut, label)


class InternalCommandMenuItem(MenuItem):

    def __init__(self, shortcut, label, command):
        super().__init__(shortcut, label, lines_before=2)
