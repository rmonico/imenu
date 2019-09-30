#!/usr/bin/python3
# coding: utf-8
from imenu_builder import MenuBuilder

def header_builder(environment):
    print("Current PATH: {PATH}".format(**environment))

def main():
    builder = MenuBuilder()

    builder.title('Menu title')

    builder.header(header_builder)

    builder.item().shortcut('l').label('List directory').os_command('ls -la').create()

    builder.item().shortcut('p').label('Show path').os_command('echo {PATH}').create()

    builder.item().shortcut('i').label('Set i variable').set_variable('i').create()

    submenu = builder.item().shortcut('s').label('submenu').sub_menu()

    submenu.title('Sub menu')

    submenu.item().shortcut('1').label('First item').os_command('echo First menu item').create()
    submenu.item().shortcut('2').label('Second item').os_command('echo Second menu item').create()

    submenu.item().back()
    submenu.add_quit_item()

    submenu.create()

    builder.add_quit_item()

    menu = builder.create()

    menu.run()

if __name__ == '__main__':
    main()
