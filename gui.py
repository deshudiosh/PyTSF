import remi.gui as gui
from remi import start, App


class PyTsfGui(App):
    def __init__(self, *args):
        super(PyTsfGui, self).__init__(*args)

    def main(self):
        # margin 0px auto allows to center the app to the screen
        container = gui.VBox(width=400, margin='0px auto')
        container.style['background'] = '#808080'
        logo = gui.Label('PyTSF', width='80%', height=60, margin='0px auto')
        logo.style['margin'] = 'auto'

        panel = gui.HBox(width=400, height=100, margin='0px auto')
        dropdown = gui.DropDown()
        refresh = gui.Button('R')
        options = gui.Button("O")
        go = gui.Button("Go!")

        panel.append(dropdown)
        panel.append(refresh)
        panel.append(options)
        panel.append(go)

        container.append(logo)
        container.append(panel)

        # returning the root widget
        return container


def startApp():
    start(PyTsfGui, address="127.0.0.11", debug=True, enable_file_cache=False, multiple_instance=True)