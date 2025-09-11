from nicegui import ui
import json
from urllib.parse import parse_qs


def show_edit_advert_page():
    # Get the advert ID from URL parameters
    query_params = parse_qs(ui.context.client.request.url.query or "")
    advert_id = int(query_params.get("id", [1])[0])  # Default to 1 if no ID

    # Sample adverts data (same as other pages)
    all_adverts = [
        {
            "id": 1,
            "title": "Fresh Tomatoes",
            "description": "Organic tomatoes from local farm",
            "price": "50",
            "category": "Vegetables",
            "quantity": "10 kg",
            "flyer": "/assets/freshtomatoes.jpg",
        },
        {
            "id": 2,
            "title": "Sweet Mangoes",
            "description": "Juicy mangoes ready to eat",
            "price": "30",
            "category": "Fruits",
            "quantity": "8 kg",
            "flyer": "/assets/sweetmangoes.jpg",
        },
        {
            "id": 3,
            "title": "Brown Rice",
            "description": "Premium quality brown rice",
            "price": "80",
            "category": "Grains & Legumes",
            "quantity": "20 kg",
            "flyer": "/assets/brownrice.jpg",
        },
        {
            "id": 4,
            "title": "Free Range Eggs",
            "description": "Fresh eggs from free range chickens",
            "price": "25",
            "category": "Dairy & Eggs",
            "quantity": "2 dozen",
            "flyer": "/assets/freerangeeggs.jpg",
        },
        {
            "id": 5,
            "title": "Organic Spinach",
            "description": "Fresh leafy greens",
            "price": "15",
            "category": "Vegetables",
            "quantity": "3 kg",
            "flyer": "/assets/organicspinach.jpg",
        },
        {
            "id": 6,
            "title": "Cashew Nuts",
            "description": "Roasted cashew nuts",
            "price": "120",
            "category": "Nuts",
            "quantity": "5 kg",
            "flyer": "/assets/cashewnuts.jpg",
        },
        {
            "id": 7,
            "title": "Sweet Potatoes",
            "description": "Fresh sweet potatoes",
            "price": "40",
            "category": "Tubers",
            "quantity": "15 kg",
            "flyer": "/assets/sweetpotatoes.jpg",
        },
        {
            "id": 8,
            "title": "Basil Leaves",
            "description": "Fresh aromatic basil",
            "price": "10",
            "category": "Herbs & Spices",
            "quantity": "500g",
            "flyer": "/assets/basilleaves.jpg",
        },
    ]

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
