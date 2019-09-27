from imenu import Menu, OSCommandMenuItem, InternalCommandMenuItem, VariableSetterMenuItem


class MenuBuilder(object):

    def __init__(self):
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

    def add_quit_item(self):
        self.add_item(InternalCommandMenuItem('q', 'Quit', 'quit'))
        return self

    def create(self):
        return self._menu


class MenuItemBuilder(object):

    def __init__(self, menu_builder=None):
        self._menu_builder = menu_builder
        self._os_command = None
        self._variable = None

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

    def create(self):
        if self._os_command:
            self._menu_builder.add_item(self._create_os_command_menu_item())
        elif self._variable:
            self._menu_builder.add_item(
                self._create_variable_setter_menu_item())
        return self._menu_builder

    def _create_os_command_menu_item(self):
        return OSCommandMenuItem(self._shortcut, self._label, os_command=self._os_command)

    def _create_variable_setter_menu_item(self):
        return VariableSetterMenuItem(self._shortcut, self._label, variable=self._variable)
