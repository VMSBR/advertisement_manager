from nicegui import ui, app
from components.header import show_header
from pages.home import show_home_page
from pages.add_advert import show_add_advert_page
from pages.edit_advert import show_edit_advert_page
from pages.view_advert import show_view_advert_page

# Load various Google Fonts
ui.add_head_html(
    """
<link href="https://fonts.googleapis.com/css2?family=Poppins:wght@300;400;600&family=Roboto:wght@400;700&family=Lobster&display=swap" rel="stylesheet">
<style>
  .font-poppins { font-family: 'Poppins', sans-serif; }
  .font-roboto { font-family: 'Roboto', sans-serif; }
  .font-lobster { font-family: 'Lobster', cursive; }
</style>
"""
)

#  Expose the assets folder to the nicegui server
app.add_static_files("/assets", "assets")


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
