from nicegui import ui
import requests
from utils.api import base_url


def show_edit_advert_page(advert_id):
    # Fetch the existing advert data
    response = requests.get(f"{base_url}/adverts/{advert_id}")
    if response.status_code != 200:
        ui.notify("Failed to load advert data", type="negative")
        ui.navigate.to("/")
        return
        
    advert = response.json()["data"]
    form_data = advert.copy()
    image_content = None
    
    def handle_image_upload(e):
        nonlocal image_content
        image_content = e.content

    def handle_update():
        # Prepare the data for update
        update_data = {
            "title": form_data.get("title"),
            "description": form_data.get("description"),
            "price": form_data.get("price"),
            "category": form_data.get("category"),
            "quantity": form_data.get("quantity", ""),
        }
        
        # Check required fields
        if not all([update_data["title"], update_data["description"], update_data["price"], update_data["category"]]):
            ui.notify("Please fill in all required fields", type="negative")
            return
            
        try:
            # If there's a new image, include it in the update
            files = {}
            if image_content:
                files = {"file": ("image.jpg", image_content, "image/jpeg")}
            
            # Send the update request
            response = requests.put(
                f"{base_url}/adverts/{advert_id}",
                data=update_data,
                files=files if files else None
            )
            
            if response.status_code == 200:
                ui.notify("Advert updated successfully!", type="positive")
                ui.navigate.to(f"/view_advert/{advert_id}")
            else:
                ui.notify(f"Failed to update advert: {response.text}", type="negative")
                
        except Exception as e:
            ui.notify(f"An error occurred: {str(e)}", type="negative")

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
                # Current image preview
                with ui.row().classes("w-full justify-center mb-4"):
                    if advert.get("flyer"):
                        ui.image(advert["flyer"].replace("http://localhost:8000", "")).classes("max-h-48 rounded-lg")
                
                # Image upload
                ui.upload(
                    label="Upload New Image (Optional)",
                    on_upload=handle_image_upload,
                    auto_upload=True,
                    max_file_size=5_000_000,  # 5MB
                ).classes("w-full mb-4")

                # Form fields
                title_input = ui.input(
                    "Title",
                    value=form_data.get("title", ""),
                    placeholder="Enter advert title",
                ).classes("w-full mb-4")
                title_input.on("input", lambda e: form_data.update({"title": e.value}))
                
                desc_input = ui.textarea(
                    "Description",
                    value=form_data.get("description", ""),
                    placeholder="Describe your product in detail",
                ).classes("w-full mb-4")
                desc_input.on("input", lambda e: form_data.update({"description": e.value}))
                
                price_input = ui.input(
                    "Price (GHC)",
                    value=form_data.get("price", ""),
                    placeholder="Enter price",
                    validation={"Please enter a valid price": lambda value: value and value.replace('.', '', 1).isdigit()}
                ).classes("w-full mb-4")
                price_input.on("input", lambda e: form_data.update({"price": e.value}))
                
                qty_input = ui.input(
                    "Quantity",
                    value=form_data.get("quantity", ""),
                    placeholder="Enter quantity (e.g., 25 kg)",
                ).classes("w-full mb-4")
                qty_input.on("input", lambda e: form_data.update({"quantity": e.value}))

                # Category selection
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
                    value=form_data.get("category", ""),
                ).classes("w-full mb-6")
                # Submit button
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
