from nicegui import ui


def show_edit_advert_page():
    ui.label("Edit Advert").classes(
        "text-3xl font-bold text-[#2E4A3F] mt-6 mb-6 text-center"
    )

    with ui.card().classes("w-[50%] mx-auto p-6 bg-[#F5F5DC] rounded-xl shadow-lg"):
        ui.input("Title").classes("w-full mb-4")
        ui.textarea("Description").classes("w-full mb-4")
        ui.input("Price (GHC)").classes("w-full mb-4")
        ui.select(
            [
                "Fruits",
                "Vegetables",
                "Grains & Legumes",
                "Herbs & Spices",
                "Dairy & Eggs",
                "Meat & Poultry",
                "Nuts",
            ],
            label="Category",
        ).classes("w-full mb-4")
        ui.upload(label="Replace Image").classes("w-full mb-4")

        ui.button("Update Advert").classes(
            "bg-[#8B5E3C] text-white px-6 py-2 rounded-lg hover:bg-[#2E4A3F]"
        )
