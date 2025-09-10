from nicegui import ui


def show_edit_advert_page():
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
                ui.input("Title").classes("w-full mb-4")
                ui.textarea("Description").classes("w-full mb-4")
                ui.input("Price (GHC)").classes("w-full mb-4")
                ui.input("Quantity").classes("w-full mb-4")

                ui.select(
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
                ).classes("w-full mb-6")

                ui.upload(label="Replace Image").classes("w-full mb-4")

                ui.button("Update Advert").classes(
                    "bg-[#8B5E3C] text-white px-6 py-2 rounded-lg hover:bg-[#2E4A3F]"
                )
