from nicegui import ui
from urllib.parse import parse_qs


def show_view_advert_page():
    # Get the advert ID from URL parameters
    query_params = parse_qs(ui.context.client.request.url.query or '')
    advert_id = int(query_params.get('id', [1])[0])  # Default to 1 if no ID
    
    # Sample adverts data (same as home page)
    all_adverts = [
        {"id": 1, "title": "Fresh Tomatoes", "description": "Organic tomatoes from local farm, freshly harvested and ready for sale. Perfect for cooking and salads.", "price": "GHC 50", "category": "Vegetables", "quantity": "10 kg", "flyer": "/assets/freshtomatoes.jpg"},
        {"id": 2, "title": "Sweet Mangoes", "description": "Juicy mangoes ready to eat, sweet and tropical flavor perfect for snacks or desserts.", "price": "GHC 30", "category": "Fruits", "quantity": "8 kg", "flyer": "/assets/sweetmangoes.jpg"},
        {"id": 3, "title": "Brown Rice", "description": "Premium quality brown rice, rich in nutrients and perfect for healthy meals.", "price": "GHC 80", "category": "Grains & Legumes", "quantity": "20 kg", "flyer": "/assets/brownrice.jpg"},
        {"id": 4, "title": "Free Range Eggs", "description": "Fresh eggs from free range chickens, high quality and nutritious.", "price": "GHC 25", "category": "Dairy & Eggs", "quantity": "2 dozen", "flyer": "/assets/freerangeeggs.jpg"},
        {"id": 5, "title": "Organic Spinach", "description": "Fresh leafy greens, organically grown and packed with vitamins.", "price": "GHC 15", "category": "Vegetables", "quantity": "3 kg", "flyer": "/assets/organicspinach.jpg"},
        {"id": 6, "title": "Cashew Nuts", "description": "Roasted cashew nuts, premium quality and perfectly seasoned.", "price": "GHC 120", "category": "Nuts", "quantity": "5 kg", "flyer": "/assets/cashewnuts.jpg"},
        {"id": 7, "title": "Sweet Potatoes", "description": "Fresh sweet potatoes, naturally sweet and perfect for various dishes.", "price": "GHC 40", "category": "Tubers", "quantity": "15 kg", "flyer": "/assets/sweetpotatoes.jpg"},
        {"id": 8, "title": "Basil Leaves", "description": "Fresh aromatic basil, perfect for cooking and garnishing dishes.", "price": "GHC 10", "category": "Herbs & Spices", "quantity": "500g", "flyer": "/assets/basilleaves.jpg"}
    ]
    
    # Find the specific advert by ID
    advert_data = next((advert for advert in all_adverts if advert['id'] == advert_id), all_adverts[0])
    
    def handle_delete():
        # Here you would call backend API to delete
        ui.notify('Advert deleted successfully!', type='positive')
        ui.navigate.to('/')
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
                ui.image(advert_data['flyer']).classes(
                    "w-full h-48 sm:h-60 object-cover rounded-lg mb-4"
                )
                ui.label(advert_data['title']).classes("text-2xl font-bold text-[#2E4A3F]")
                ui.label(advert_data['description']).classes(
                    "text-gray-600 mb-2"
                )
                ui.label(f"Category: {advert_data['category']}").classes("font-semibold text-[#8B5E3C]")
                ui.label(f"Price: {advert_data['price']}").classes("font-bold text-[#2E4A3F] mt-2")
                ui.label(f"Quantity: {advert_data['quantity']}").classes("font-semibold text-[#2E4A3F] mt-2")

                with ui.row().classes("gap-4 mt-4 flex-wrap w-full"):
                    ui.button("Edit", on_click=lambda: ui.navigate.to("/edit_advert")).classes(
                        "px-4 py-2 rounded-md flex-1"
                    ).style("background-color: #16a34a; color: white;").props("no-caps")
                    ui.button("Delete", on_click=handle_delete).classes(
                        "px-4 py-2 rounded-md flex-1"
                    ).style("background-color: #dc2626; color: white;").props("no-caps")
                
                # Back to home button
                ui.button("Back to Home", on_click=lambda: ui.navigate.to('/')).classes(
                    "px-4 py-2 rounded-md w-full mt-2"
                ).style("background-color: #22c55e; color: white;").props("no-caps")
