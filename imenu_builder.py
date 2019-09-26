from imenu import Menu, OSCommandMenuItem, InternalCommandMenuItem


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
        self.menu_builder = menu_builder

    def shortcut(self, shortcut):
        self.shortcut = shortcut
        return self

    def label(self, label):
        self.label = label
        return self

    def os_command(self, os_command):
        self.os_command = os_command
        return self

    def _create_os_command_menu_item(self):
        return OSCommandMenuItem(self.shortcut, self.label, os_command=self.os_command)

    def create(self):
        if self.os_command:
            self.menu_builder.add_item(self._create_os_command_menu_item())

        return self.menu_builder
