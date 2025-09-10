from nicegui import ui
from components.header import show_header
from pages.home import show_home_page
from pages.add_advert import show_add_advert_page
from pages.edit_advert import show_edit_advert_page
from pages.view_advert import show_view_advert_page


@ui.page("/")
def home_page():
    show_header()
    show_home_page()

@ui.page("/add_advert")
def add_advert_page():
    show_header()
    show_add_advert_page()


@ui.page("/edit_advert")
def edit_advert_page():
    show_header()
    show_edit_advert_page()

@ui.page("/view_advert")
def view_advert_page():
    show_header()
    show_view_advert_page()



ui.run()