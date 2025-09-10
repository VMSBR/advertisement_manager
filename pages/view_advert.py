from nicegui import ui


def show_view_advert_page():
    ui.label("Advert Details").classes(
        "text-3xl font-bold text-[#2E4A3F] mt-6 mb-6 text-center"
    )

    with ui.card().classes(
        "w-full sm:w-[90%] md:w-[70%] lg:w-[60%] mx-auto p-6 bg-white rounded-xl shadow-lg"
    ):
        ui.image("/assets/sample.jpg").classes(
            "w-full h-48 sm:h-60 object-cover rounded-lg mb-4"
        )
        ui.label("Advert Title").classes("text-2xl font-bold text-[#2E4A3F]")
        ui.label("Detailed description of the advert goes here...").classes(
            "text-gray-600 mb-2"
        )
        ui.label("Category: Vegetables").classes("font-semibold text-[#8B5E3C]")
        ui.label("Price: GHC 150").classes("font-bold text-[#2E4A3F] mt-2")

        with ui.row().classes("gap-4 mt-4 flex-wrap"):
            ui.button("Edit", on_click=lambda: ui.open("/edit_advert")).classes(
                "bg-[#8B5E3C] text-white px-4 py-2 rounded-md"
            )
            ui.button("Delete").classes("bg-red-600 text-white px-4 py-2 rounded-md")
