from pygame_widgets.button import Button


class MyButton(Button):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def change_text(self, text):
        self.text = self.font.render(text, True, self.textColour)

    def change_states_colors(self, inactive_color, hover_color, pressed_color):
        super(MyButton, self).setInactiveColour(inactive_color)
        super(MyButton, self).setHoverColour(hover_color)
        super(MyButton, self).setPressedColour(pressed_color)
