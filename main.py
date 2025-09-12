from nicegui import ui, app
from components.header import show_header
from pages.home import show_home_page
from pages.add_advert import show_add_advert_page
from pages.edit_advert import show_edit_advert_page
from pages.view_advert import show_view_advert_page

# Load various Google Fonts and custom CSS utilities
ui.add_head_html(
    """
<link href="https://fonts.googleapis.com/css2?family=Poppins:wght@300;400;600&family=Roboto:wght@400;700&family=Lobster&display=swap" rel="stylesheet">
<style>
  .font-poppins { font-family: 'Poppins', sans-serif; }
  .font-roboto { font-family: 'Roboto', sans-serif; }
  .font-lobster { font-family: 'Lobster', cursive; }
  
  /* Text truncation utilities */
  .line-clamp-2 {
    display: -webkit-box;
    -webkit-line-clamp: 2;
    -webkit-box-orient: vertical;
    overflow: hidden;
    text-overflow: ellipsis;
  }
  
  .line-clamp-3 {
    display: -webkit-box;
    -webkit-line-clamp: 3;
    -webkit-box-orient: vertical;
    overflow: hidden;
    text-overflow: ellipsis;
  }
  
  /* Enhanced card hover effects */
  .card-hover-glow:hover {
    box-shadow: 0 25px 50px -12px rgba(34, 197, 94, 0.25);
  }
  
  /* Smooth gradient animations */
  .gradient-animate {
    background-size: 200% 200%;
    animation: gradientShift 3s ease infinite;
  }
  
  @keyframes gradientShift {
    0% { background-position: 0% 50%; }
    50% { background-position: 100% 50%; }
    100% { background-position: 0% 50%; }
  }
  
  /* Better button hover states */
  .btn-primary:hover {
    transform: translateY(-2px);
    box-shadow: 0 10px 20px rgba(22, 163, 74, 0.3);
  }
  
  .btn-secondary:hover {
    background: linear-gradient(135deg, #16a34a, #22c55e) !important;
    color: white !important;
    border-color: transparent !important;
  }
  
  /* Override NiceGUI default button colors */
  .q-btn {
    background: linear-gradient(135deg, #16a34a, #22c55e) !important;
    color: white !important;
    border: none !important;
  }
  
  .q-btn:hover {
    background: linear-gradient(135deg, #22c55e, #16a34a) !important;
    transform: translateY(-2px);
    box-shadow: 0 10px 20px rgba(22, 163, 74, 0.3);
  }
</style>
"""
)

#  Expose the assets folder to the nicegui server
app.add_static_files("/assets", "assets")

# Add media type for PNG files
app.add_media_files("/assets", "assets")


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
def view_advert_page(id=""):
    show_header()
    show_view_advert_page(id)


ui.run()
