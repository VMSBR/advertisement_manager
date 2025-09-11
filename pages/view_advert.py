from nicegui import ui
from urllib.parse import parse_qs
from utils.api import base_url
import requests


def show_view_advert_page(id):
    response = requests.get(f"{base_url}/adverts/{id}")
    json_data = response.json()
    advert = json_data["data"]

    def handle_delete():
        # Here you would call backend API to delete
        ui.notify("Advert deleted successfully!", type="positive")
        ui.navigate.to("/")

    # Fullscreen background with overlay
    with ui.element("div").style(
        "background-image: url(/assets/view.jpg); "
        "background-size: cover; background-position: center; "
        "width: 100%; min-height: 100vh; position: relative;"
    ).classes("flex justify-center items-center"):

        # Overlay (semi-transparent dark layer)
        ui.element("div").style(
            "background: rgba(0,0,0,0.5); position: absolute; inset: 0; z-index: -1;"
        )

        # Foreground container (centers label + form together)
        with ui.column().classes(
            "items-center w-full mb-10 sm:w-[90%] md:w-[70%] lg:w-[60%]"
        ):

            # Title sits on top of the card
            ui.label("Advert Details").classes(
                "text-3xl font-bold text-white text-center mt-6 mb-6"
            )

            # Centered card
            with ui.card().classes("w-full p-6 bg-white rounded-xl shadow-lg"):
                ui.image(advert["flyer"]).classes(
                    "w-full h-48 sm:h-60 object-cover rounded-lg mb-4"
                )
                ui.label(advert["title"]).classes("text-2xl font-bold text-[#2E4A3F]")
                ui.label(advert["description"]).classes("text-gray-600 mb-2")
                ui.label(f"Category: {advert['category']}").classes(
                    "font-semibold text-[#8B5E3C]"
                )
                ui.label(f"Price: {advert['price']}").classes(
                    "font-bold text-[#2E4A3F] mt-2"
                )
                ui.label(f"Quantity: {advert['quantity']}").classes(
                    "font-semibold text-[#2E4A3F] mt-2"
                )

                with ui.row().classes("gap-4 mt-4 flex-wrap w-full"):
                    ui.button(
                        "Edit", on_click=lambda: ui.navigate.to("/edit_advert")
                    ).classes("px-4 py-2 rounded-md flex-1").style(
                        "background-color: #16a34a; color: white;"
                    ).props(
                        "no-caps"
                    )

                    def handle_delete():
                        response = requests.delete(f"{base_url}/adverts/{id}")
                        if response.status_code == 200:
                            ui.navigate.to("/")

                    ui.button("Delete", on_click=handle_delete).classes(
                        "px-4 py-2 rounded-md flex-1"
                    ).style("background-color: #dc2626; color: white;").props("no-caps")

                # Back to home button
                ui.button("Back to Home", on_click=lambda: ui.navigate.to("/")).classes(
                    "px-4 py-2 rounded-md w-full mt-2"
                ).style("background-color: #22c55e; color: white;").props("no-caps")
