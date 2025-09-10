from nicegui import ui


def show_view_advert_page():
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
                ui.image("/assets/view1.jpg").classes(
                    "w-full h-48 sm:h-60 object-cover rounded-lg mb-4"
                )
                ui.label("Title").classes("text-2xl font-bold text-[#2E4A3F]")
                ui.label("Detailed description of the advert goes here...").classes(
                    "text-gray-600 mb-2"
                )
                ui.label("Category: Vegetables").classes("font-semibold text-[#8B5E3C]")
                ui.label("Price: GHC 150").classes("font-bold text-[#2E4A3F] mt-2")
                ui.label("Quantity: 25 kg").classes("font-semibold text-[#2E4A3F] mt-2")

                with ui.row().classes("gap-4 mt-4 flex-wrap"):
                    ui.button("Edit", on_click=lambda: ui.open("/edit_advert")).classes(
                        "bg-[#8B5E3C] text-white px-4 py-2 rounded-md"
                    )
                    ui.button("Delete").classes("bg-red-600 text-white px-4 py-2 rounded-md")
