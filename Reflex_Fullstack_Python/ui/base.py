import reflex as rx

from .nav import navbar


def base_page(child: rx.Component, hide_navbar=False, *args, **kwargs) -> rx.Component:
    #print(f"type of args: {[type(x) for x in args]} \n")
    #print(f"type of kwargs: {[type(y) for y in kwargs]} \n")
    if not isinstance(child, rx.Component):
        child = rx.heading("this is not a vaild child element")
    if hide_navbar:
        return rx.container(
            child,
            rx.logo(),
            rx.color_mode.button(position="bottom-left"),
        )
    return rx.container(
            navbar(),
            child,
            rx.logo(),
            rx.color_mode.button(position="bottom-left", id="my-light-mode-btn"),
            padding="5em",
            id="my-base-container",
    )