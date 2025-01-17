"""Welcome to Reflex! This file outlines the steps to create a basic app."""

# Environment: fullstack_rx0_6_8_py3_12
# Python version: 3.12.8
# Reflex version: 0.6.8

#NOTE - Youtube Video Tutorial
# [Build Full Stack Web Apps in Pure Python with Reflex - No Javascript Required](https://www.youtube.com/watch?v=ITOZkzjtjUA)


#NOTE - 
# rx.input(
        value=f"{cls.expected_quantity}",
        on_change=cls.set_expected_quantity,
        placeholder="請輸入預期數量",
        type="number",
# ), # rx.input


#@rx.event
#    def set_expected_quantity(self, expect_quantity: str):
#        # DeprecationWarning: Mismatched event handler argument types has been deprecated in version 0.6.5 Event handler on_change expects <class 'str'> for argument expect_quantity but got <class 'int'>
#        #self.expected_quantity = expect_quantity
#        if expect_quantity.strip() == "":
#            self.expected_quantity = 0
#        else:
#            try:
#                self.expected_quantity = int(expect_quantity)
#            except ValueError:
#                self.expected_quantity = 0


# References:
#input component event handler #1719
#https://github.com/orgs/reflex-dev/discussions/1719
#https://reflex.dev/docs/events/setters/




import reflex as rx

from rxconfig import config


class State(rx.State):
    """The app state."""
    label="This is my label."

    @rx.event
    def handle_title_input_change(self, val):
        self.label = val

    ################

    text: str = "Click me to edit"
    show_input: bool =False

    @rx.event
    def toggle_input(self):
        self.show_input = not self.show_input

    @rx.event
    def set_text(self, value: str):
        self.text = value

    ################
    
    
    #def handle_heading_change(self, )


def index() -> rx.Component:
    # Welcome Page (Index)
    return rx.container(
        rx.color_mode.button(position="top-right"),
        rx.vstack(
            rx.heading(State.label, size="9"), # My personal practice
            rx.text(
                "Get started by editing ",
                rx.code(f"{config.app_name}/{config.app_name}.py"),
                size="5",
            ),
            rx.input(on_change=State.handle_title_input_change), # Here on_change is trigger
            
            ################
            rx.heading(
                State.text,
                on_click=State.toggle_input,
            ),
            rx.cond(
                State.show_input,
                rx.input(
                    value=State.text,
                    on_change=State.set_text,
                    on_blur=State.toggle_input,
                )
            ),
            ################

            rx.link(
                rx.button("Check out our docs!"),
                href="https://reflex.dev/docs/getting-started/introduction/",
                is_external=True,
            ),
            spacing="5",
            justify="center",
            min_height="85vh",
        ),
        rx.logo(),
    )


app = rx.App()
app.add_page(index)

#############################################################


#import reflex as rx
#from rxconfig import config
#
#def index() -> rx.Component:
#    return rx.text(f"Hello, World")
#
#app = rx.App(
#    theme=rx.theme(
#        appearance="dark",
#        has_background=True,
#        panel_background="solid",
#        scaling="90%",
#        radius="medium",
#        accent_color="sky",
#    )
#)
#app.add_page(index)