from nicegui import ui
import requests
from utils.api import base_url


def show_edit_advert_page():

    # Sample adverts data (same as other pages)
    all_adverts = []

    # Find the specific advert by ID and use as form data
    selected_advert = next(
        (advert for advert in all_adverts if advert["id"] == advert_id), all_adverts[0]
    )
    form_data = selected_advert.copy()

    def handle_update():
        # Collect form data
        if all(
            [
                form_data.get("title"),
                form_data.get("description"),
                form_data.get("price"),
                form_data.get("category"),
            ]
        ):
            # Here you would send updated data to backend API
            ui.notify("Advert updated successfully!", type="positive")
            ui.navigate.to("/view_advert")
        else:
            ui.notify("Please fill in all required fields", type="negative")

    # Fullscreen background with overlay
    with ui.element("div").style(
        "background-image: url(/assets/edit.jpg); "
        "background-size: cover; background-position: center; "
        "width: 100%; min-height: 100vh; position: relative;"
    ).classes("flex justify-center items-center"):

        # Overlay (semi-transparent dark layer)
        ui.element("div").style(
            "background: rgba(0,0,0,0.5); position: absolute; inset: 0; z-index: -1;"
        )

        # Foreground container (centers label + form together)
        with ui.column().classes(
            "items-center w-full mb-10 sm:w-[90%] md:w-[70%] lg:w-[50%]"
        ):

            # Title sits on top of the form
            ui.label("Edit Advert").classes(
                "text-3xl font-bold text-white text-center mt-6 mb-6"
            )

            # Centered card
            with ui.card().classes("w-full p-6 bg-[#F5F5DC] rounded-xl shadow-lg"):
                title_input = ui.input(
                    "Title",
                    value=form_data.get("title", ""),
                    placeholder="Enter advert title",
                )
                title_input.classes("w-full mb-4")
                title_input.on("input", lambda e: form_data.update({"title": e.value}))
                desc_input = ui.textarea(
                    "Description",
                    value=form_data.get("description", ""),
                    placeholder="Describe your product in detail",
                )
                desc_input.classes("w-full mb-4")
                desc_input.on(
                    "input", lambda e: form_data.update({"description": e.value})
                )
                price_input = ui.input(
                    "Price (GHC)",
                    value=form_data.get("price", ""),
                    placeholder="Enter price",
                )
                price_input.classes("w-full mb-4")
                price_input.on("input", lambda e: form_data.update({"price": e.value}))
                qty_input = ui.input(
                    "Quantity",
                    value=form_data.get("quantity", ""),
                    placeholder="Enter quantity (e.g., 25 kg)",
                )
                qty_input.classes("w-full mb-4")
                qty_input.on("input", lambda e: form_data.update({"quantity": e.value}))

                category_select = ui.select(
                    [
                        "Fruits",
                        "Vegetables",
                        "Grains & Legumes",
                        "Herbs & Spices",
                        "Dairy & Eggs",
                        "Meat & Poultry",
                        "Nuts",
                        "Tubers",
                        "Seedlings",
                    ],
                    label="Category",
                    value=form_data.get("category"),
                ).classes("w-full mb-6")
                category_select.on(
                    "update:model-value",
                    lambda e: form_data.update({"category": e.value}),
                )

                image_upload = ui.upload(label="Replace Image", auto_upload=True)
                image_upload.classes("w-full mb-4")
                image_upload.on("upload", lambda e: form_data.update({"flyer": e.name}))

                ui.button("Update Advert", on_click=handle_update).classes(
                    "px-6 py-2 rounded-lg w-full"
                ).style("background-color: #16a34a; color: white;").props("no-caps")

                # Cancel button
                ui.button(
                    "Cancel", on_click=lambda: ui.navigate.to("/view_advert")
                ).classes("px-6 py-2 rounded-lg w-full mt-2").style(
                    "background-color: #4ade80; color: white;"
                ).props(
                    "no-caps"
                )
