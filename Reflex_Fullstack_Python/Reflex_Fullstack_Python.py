"""Welcome to Reflex! This file outlines the steps to create a basic app."""

# Environment: fullstack_rx0_6_8_py3_12
# Python version: 3.12.8
# Reflex version: 0.6.8

#NOTE - Youtube Video Tutorial
# [Build Full Stack Web Apps in Pure Python with Reflex - No Javascript Required](https://www.youtube.com/watch?v=ITOZkzjtjUA)

#import reflex as rx
#
#from rxconfig import config
#
#
#class State(rx.State):
#    """The app state."""
#
#    ...
#
#
#def index() -> rx.Component:
#    # Welcome Page (Index)
#    return rx.container(
#        rx.color_mode.button(position="top-right"),
#        rx.vstack(
#            rx.heading("Welcome to Reflex!", size="9"),
#            rx.text(
#                "Get started by editing ",
#                rx.code(f"{config.app_name}/{config.app_name}.py"),
#                size="5",
#            ),
#            rx.link(
#                rx.button("Check out our docs!"),
#                href="https://reflex.dev/docs/getting-started/introduction/",
#                is_external=True,
#            ),
#            spacing="5",
#            justify="center",
#            min_height="85vh",
#        ),
#        rx.logo(),
#    )
#
#
#app = rx.App()
#app.add_page(index)

#############################################################


import reflex as rx

from rxconfig import config


def index() -> rx.Component:
    return rx.text(f"Hello, World")


app = rx.App(
    theme=rx.theme(
        appearance="dark",
        has_background=True,
        panel_background="solid",
        scaling="90%",
        radius="medium",
        accent_color="sky",
    )
)

app.add_page(index)