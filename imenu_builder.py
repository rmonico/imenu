from imenu import Menu, OSCommandMenuItem, InternalCommandMenuItem, VariableSetterMenuItem, SubMenuItem


class MenuBuilder(object):

    def __init__(self, parent_builder=None):
        self._parent_builder = parent_builder
        self.reset()

    def reset(self):
        self._menu = Menu()
        return self

    def header(self, header_builder):
        self._menu.header_builder = header_builder

    def title(self, title):
        self._menu.title = title
        return self

    def item(self):
        return MenuItemBuilder(self)

    def add_item(self, menu_item):
        self._menu.add_item(menu_item)
        return self

    def create(self):
        if self._parent_builder:
            self._parent_builder._add_submenu(self._menu)

            return self._parent_builder
        else:
            return self._menu


class MenuItemBuilder(object):

    def __init__(self, menu_builder=None):
        self._menu_builder = menu_builder
        self._os_command = None
        self._variable = None
        self._sub_menu = None

    def shortcut(self, shortcut):
        self._shortcut = shortcut
        return self

    def label(self, label):
        self._label = label
        return self

    def os_command(self, os_command):
        self._os_command = os_command
        return self

    def set_variable(self, variable):
        self._variable = variable
        return self

    def sub_menu(self):
        return MenuBuilder(self)

    def _add_submenu(self, sub_menu):
        self._sub_menu = sub_menu

        self.create()

    def back(self):
        back_menu_item = InternalCommandMenuItem('x', 'Back', 'back')
        self._menu_builder.add_item(back_menu_item)

        return self._menu_builder

    def quit(self):
        quit_menu_item = InternalCommandMenuItem('q', 'Quit', 'quit')
        self._menu_builder.add_item(quit_menu_item)

        return self._menu_builder

    def create(self):
        if self._os_command:
            self._menu_builder.add_item(self._create_os_command_menu_item())
        elif self._variable:
            self._menu_builder.add_item(
                self._create_variable_setter_menu_item())
        elif self._sub_menu:
            self._menu_builder.add_item(self._create_sub_menu_item())

        return self._menu_builder

    def _create_os_command_menu_item(self):
        return OSCommandMenuItem(self._shortcut, self._label, os_command=self._os_command)

    def _create_variable_setter_menu_item(self):
        return VariableSetterMenuItem(self._shortcut, self._label, variable=self._variable)

    def _create_sub_menu_item(self):
        return SubMenuItem(self._shortcut, self._label, submenu=self._sub_menu)
