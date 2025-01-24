"""Welcome to Reflex! This file outlines the steps to create a basic app."""

# Environment: fullstack_rx0_6_8_py3_12
# Python version: 3.12.8
# Reflex version: 0.6.8

#NOTE - Youtube Video Tutorial
# [Build Full Stack Web Apps in Pure Python with Reflex - No Javascript Required](https://www.youtube.com/watch?v=ITOZkzjtjUA)


#NOTE - 
# rx.input(
#        value=f"{cls.expected_quantity}",
#        on_change=cls.set_expected_quantity,
#        placeholder="請輸入預期數量",
#        type="number",
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

#LINK - Build Full Stack Web Apps in Pure Python with Reflex - No Javascript Required
# https://www.youtube.com/watch?v=ITOZkzjtjUA


#NOTE - uv 
# [Using uv in Docker](https://docs.astral.sh/uv/guides/integration/docker/)
# [An example of using uv in Docker images](https://github.com/astral-sh/uv-docker-example)
# [Dockerfile](https://github.com/astral-sh/uv-docker-example/blob/main/Dockerfile)
# [如何使用 Python 套件管理工具「uv」取代 pip 來加速 Docker Image 的建立](https://jumping-code.com/2024/08/23/uv-pip-docker-image/)
# [Production-ready Python Docker Containers with uv](https://hynek.me/articles/docker-uv/)
# [典食盛津 生魚丼 手作壽司](https://hoolee.tw/dianshi-sushi/)
# [東京純豆腐 Tokyo Sundubu 高雄SOGO店](https://sweetday.tw/%E6%9D%B1%E4%BA%AC%E7%B4%94%E8%B1%86%E8%85%90/)
# [預防骨質疏鬆　你有做「對」運動嗎？](https://www.commonhealth.com.tw/blog/3513)
# [健身新手指南：重訓增強骨密度，打造健康骨骼](https://striver.fitness/rehabilitation-exercises/work-out-increase-bone-density/)
# [勞工因火車或汽車誤時，應不視為遲到或曠職 - 勞動基準法 第 12 條（民國 73 年 07 月 30 日版）](https://laws.mol.gov.tw/FLAW/FLAWDOC03.aspx?searchmode=global&datatype=etype&no=FE107887&keyword=%E5%85%B6%E4%BB%96)
# [[心得] 楊双子《花開少女華麗島》](https://www.ptt.cc/bbs/book/M.1547796029.A.8CB.html) https://petermiblog.blogspot.com/2019/01/blog-post.html?m=1
# [【重點書評】自我的公眾史：讀楊双子《臺灣漫遊錄》](https://www.unitas.me/archives/14559)


#NOTE - SQL
# [Learn SQL with Python (Part 1)](https://www.patricksoftwareblog.com/learn_sql_with_python_part1.html)
# [Learn SQL with Python (Part 2)](https://www.patricksoftwareblog.com/learn_sql_with_python_part2.html)
# [Learn SQL with Python (Part 3)](https://www.patricksoftwareblog.com/learn_sql_with_python_part3.html)

#NOTE - Async
# [Python Concurrency: Threads, Processes, and asyncio Explained](https://newvick.com/python-concurrency/)

# [How to get from high school math to cutting-edge ML/AI: a detailed 4-stage roadmap with links to the best learning resources that I’m aware of.](https://www.justinmath.com/how-to-get-from-high-school-math-to-cutting-edge-ml-ai/)
# [如何從高中數學進階到前沿機器學習/人工智能：一份詳細的四階段路線圖，附帶我所知的最佳學習資源鏈接。](https://readit.plus/a/M9gWa)


import reflex as rx

from rxconfig import config

from .ui.base import base_page


class State(rx.State):
    """The app state."""
    label="This is my label."

    @rx.event
    def handle_title_input_change(self, val):
        self.label = val
    
    @rx.event
    def did_click(self):
        print("Hello world did click")
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

    toggle_show: bool = True

    @rx.event
    def change_toggle_state(self):
        self.toggle_show = not (self.toggle_show)

    ################
    
    
    #def handle_heading_change(self, )







def index() -> rx.Component:
    # Welcome Page (Index)
    return base_page(
        rx.vstack(
            rx.heading(State.label, size="9"), # My personal practice
            rx.text(
                "Get started by editing ",
                rx.code(f"{config.app_name}/{config.app_name}.py"),
                size="5",
            ),
            # <input type='text' value='My value' />
            rx.input(
                value=State.label,
                on_click=State.did_click,
                on_change=State.handle_title_input_change,
                ), # Here on_change is trigger
            
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
            rx.button("Toggle", on_click=State.change_toggle_state),
            rx.cond(State.toggle_show,
            rx.text(f"Text 1", color="green"),
            rx.text(f"Text 2", color="yellow"),
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