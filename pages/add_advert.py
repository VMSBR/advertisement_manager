from nicegui import ui
import json


def show_add_advert_page():
    # Form data storage
    form_data = {}

    def handle_submit():
        # Collect form data
        if all(
            [
                form_data.get("title"),
                form_data.get("description"),
                form_data.get("price"),
                form_data.get("category"),
            ]
        ):
            # Here you would send data to backend API
            ui.notify("Advert submitted successfully!", type="positive")
            # Reset form or redirect
            ui.navigate.to("/")
        else:
            ui.notify("Please fill in all required fields", type="negative")

    # Fullscreen background with overlay
    with ui.element("div").style(
        "background-image: url(/assets/add.jpg); "
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
            ui.label("Post a New Advert").classes(
                "text-3xl font-bold text-white text-center mt-" "6 mb-6"
            )

            # Centered card
            with ui.card().classes("w-full p-6 bg-[#F5F5DC] rounded-xl shadow-lg"):
                title_input = ui.input("Title", placeholder="Enter advert title")
                title_input.classes("w-full mb-4")
                title_input.on("input", lambda e: form_data.update({"title": e.value}))
                desc_input = ui.textarea(
                    "Description", placeholder="Describe your product in detail"
                )
                desc_input.classes("w-full mb-4")
                desc_input.on(
                    "input", lambda e: form_data.update({"description": e.value})
                )
                price_input = ui.input("Price (GHC)", placeholder="Enter price")
                price_input.classes("w-full mb-4")
                price_input.on("input", lambda e: form_data.update({"price": e.value}))
                qty_input = ui.input(
                    "Quantity", placeholder="Enter quantity (e.g., 25 kg)"
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
                    value=None,
                ).classes("w-full mb-6")
                category_select.on(
                    "update:model-value",
                    lambda e: form_data.update({"category": e.value}),
                )

                image_upload = ui.upload(label="Upload Image", auto_upload=True)
                image_upload.classes("w-full mb-4")
                image_upload.on("upload", lambda e: form_data.update({"flyer": e.name}))

                ui.button("Submit Advert", on_click=handle_submit).classes(
                    "px-6 py-2 rounded-lg w-full"
                ).style("background-color: #16a34a; color: white;").props("no-caps")

                # Cancel button
                ui.button("Cancel", on_click=lambda: ui.navigate.to("/")).classes(
                    "px-6 py-2 rounded-lg w-full mt-2"
                ).style("background-color: #4ade80; color: white;").props("no-caps")
