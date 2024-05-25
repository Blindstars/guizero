from tkinter import Label, StringVar
from . import utilities as utils
from .base import TextWidget

class Text(TextWidget):

    def __init__(
        self,
        master,
        text="",
        size=None,
        color=None,
        bg=None,
        font=None,
        grid=None,
        align=None,
        visible=True,
        enabled=None,
        width=None,
        height=None,
        weight=None):

        self._text = str(text)
        tk = Label(master.tk, text=text)
        super().__init__(master, tk, grid, align, visible, enabled, width, height)

        # setup defaults
        if bg:
            self.bg = bg
        
        if size is not None:
            self.text_size = size

        if font is not None:
            self.font = font

        if color is not None:
            self.text_color = color

        if weight is not None:
            self.text_weight = weight

    # PROPERTIES
    # ----------------------------------
    # The text value
    @property
    def value(self):
        return (self._text)

    @value.setter
    def value(self, value):
        self.tk.config(text=value)
        self._text = str(value)

    # The font size
    @property
    def size(self):
        return self.text_size

    @size.setter
    def size(self, size):
        self.text_size = size

    # The font weight
    @property
    def weight(self):
        return self.text_weight

    @weight.setter
    def weight(self, weight):
        self.text_weight = weight

    @property
    def description(self):
        """
        Returns the description for the widget.
        """
        return "[Text] object with text '{}'".format(self.value)

    # METHODS
    # -------------------------------------------

    # Clear text (set to empty string)
    def clear(self):
        self._text = ""
        self.tk.config(text="")

    # Append some text onto the end of the existing text
    def append(self, text):
        new_text = self._text + str(text)
        self._text = new_text
        self.tk.config(text=new_text)

