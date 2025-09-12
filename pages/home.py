from nicegui import ui, app
import requests
from utils.api import base_url
from functools import partial
import re


def format_quantity(quantity):
    """
    Standardize quantity display to always show in kg format.
    Handles various input formats and converts to consistent kg display.
    """
    if not quantity:
        return "0 kg"

    # Convert to string and clean up
    qty_str = str(quantity).strip().lower()

    # Extract number from the string
    number_match = re.search(r"(\d+(?:\.\d+)?)", qty_str)
    if not number_match:
        return f"{quantity} kg"  # Return original if no number found

    number = float(number_match.group(1))

    # Convert different units to kg
    if "g" in qty_str and "kg" not in qty_str:
        # Convert grams to kg
        number = number / 1000
    elif "ton" in qty_str or "tonne" in qty_str:
        # Convert tonnes to kg
        number = number * 1000
    elif "lb" in qty_str or "pound" in qty_str:
        # Convert pounds to kg
        number = number * 0.453592
    elif "dozen" in qty_str:
        # Keep dozen as is, don't convert to kg
        return f"{int(number)} dozen"
    elif "piece" in qty_str or "pcs" in qty_str:
        # Keep pieces as is
        return f"{int(number)} pieces"

    # Format the number nicely
    if number == int(number):
        return f"{int(number)} kg"
    else:
        return f"{number:.1f} kg"


def show_home_page():
    response = requests.get(f"{base_url}/adverts")
    json_data = response.json()

    # Debug: Print API response to see image URLs
    print("API Response:", json_data)
    if json_data.get("data") and len(json_data["data"]) > 0:
        print("First advert flyer URL:", json_data["data"][0].get("flyer"))

    # Big container
    with ui.element("div").classes("relative w-full h-screen"):

        # Background carousel
        with ui.carousel().props("arrows autoplay swipe infinite").classes(
            "absolute inset-0 w-screen h-screen z-[-2]"
        ).style("width: 100vw; height: 100vh;"):
            ui.carousel_slide().classes("w-screen h-screen").style(
                "background-image: url(/assets/homee.jpg); background-size: cover; background-position: center; width: 100vw; height: 100vh;"
            )
            ui.carousel_slide().classes("w-screen h-screen").style(
                "background-image: url(/assets/home.jpg); background-size: cover; background-position: center; width: 100vw; height: 100vh;"
            )
            ui.carousel_slide().classes("w-screen h-screen").style(
                "background-image: url(/assets/homeee.jpg); background-size: cover; background-position: center; width: 100vw; height: 100vh;"
            )

        # Overlay (lighter semi-transparent layer for text readability)
        ui.element("div").style(
            "background: rgba(0,0,0,0.2); position: absolute; inset: 0; z-index: -1;"
        )

        # Foreground content (your UI)
        with ui.element("div").classes(
            "h-screen w-screen flex flex-col justify-center items-center relative text-white"
        ):
            with ui.column().classes(
                "relative text-center bg-black/10 h-full w-full flex flex-col items-center justify-center"
            ):
                ui.label("Akwaaba to").classes("font-lobster italic text-4xl")
                ui.html("<h1>AGROKASA</h1>").classes("font-poppins text-7xl")
                ui.html(
                    "Ghana's trusted agricultural marketplace where farmers showcase their harvest,<br>"
                    "customers discover fresh and affordable produce,<br>"
                    "and communities grow together.<br>"
                    "We connect you to quality farm products while empowering local farmers and supporting healthy living."
                ).classes("text-lg md:text-2xl")

    # NEW SECTION: How it Works (Styled for Ad Platform)
    with ui.element("div").classes("w-full flex flex-col items-center py-16"):
        ui.label("How it Works").classes("text-3xl font-bold text-gray-800 mb-2")
        ui.label("Follow these simple steps to post and discover adverts").classes(
            "text-gray-600 mb-12"
        )

        # Responsive grid: 1 column on small, 2 on medium, 4 on large screens
        with ui.element("div").classes(
            "grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-4 gap-20"
        ):
            steps = [
                ("1", "Create an Account"),
                ("2", "Post Your Advert"),
                ("3", "Get Noticed by Buyers"),
                ("4", "Connect & Close Deals"),
            ]

            for number, text in steps:
                with ui.element("div").classes("flex flex-col items-center"):
                    # Circle with gradient + dotted border
                    with ui.element("div").classes(
                        "w-24 h-24 flex items-center justify-center rounded-full "
                        "bg-gradient-to-br from-green-500 to-green-700 text-white text-3xl font-bold "
                        "border-4 border-dotted border-green-400 shadow-md"
                    ):
                        ui.label(number)
                    ui.label(text).classes("mt-3 text-gray-700 text-center font-medium")

    # Available Adverts Section
    with ui.element("div").classes("w-full flex flex-col items-center py-16"):
        ui.label("AVAILABLE ADVERTS").classes(
            "text-3xl text-center font-bold relative items-center flex flex-col justify-center font-poppins text-gray-800 "
        )

    # Sample adverts data (would come from backend API)
    sample_adverts = []

    # Responsive grid: 1 column on mobile, 2 on tablet, 3 on desktop, 4 on large screens
    with ui.element("div").classes(
        "grid grid-cols-1 sm:grid-cols-2 md:grid-cols-3 lg:grid-cols-4 gap-8 p-6 max-w-7xl mx-auto"
    ):
        for advert in json_data["data"]:
            with ui.card().classes("w-full p-6 bg-white rounded-xl shadow-lg"):
                ui.image(advert["flyer"]).classes(
                    "w-full h-48 sm:h-60 object-cover rounded-lg mb-4"
                )
                # Category badge overlay
                with ui.element("div").classes(
                    "absolute top-3 left-3 bg-gradient-to-r from-green-500 to-green-600 "
                    "text-white px-3 py-1 rounded-full text-xs font-semibold shadow-md z-10"
                ):
                    ui.label(advert["category"])

                # Card content with better spacing
                with ui.element("div").classes("p-5"):
                    # Title with better typography
                    ui.label(advert["title"]).classes(
                        "text-xl font-bold font-poppins mb-3 text-gray-800 "
                        "line-clamp-2 leading-tight"
                    )

                    # Description with proper truncation
                    ui.label(advert["description"]).classes(
                        "text-gray-600 mb-3 text-sm leading-relaxed line-clamp-2"
                    )

                    # Category display
                    ui.label(f"Category: {advert['category']}").classes(
                        "text-xs text-[#8B5E3C] font-medium mb-3 bg-orange-50 px-2 py-1 rounded-md inline-block"
                    )

                    # Price and quantity section with icons
                    with ui.element("div").classes("space-y-2 mb-4"):
                        with ui.element("div").classes(
                            "flex items-center justify-between"
                        ):
                            ui.label("Price").classes(
                                "text-xs text-gray-500 uppercase tracking-wide"
                            )
                            ui.label(f"GHC {advert['price']}").classes(
                                "text-xl font-bold text-gray-700"
                            )

                        with ui.element("div").classes(
                            "flex items-center justify-between"
                        ):
                            ui.label("Quantity").classes(
                                "text-xs text-gray-500 uppercase tracking-wide"
                            )
                            ui.label(format_quantity(advert["quantity"])).classes(
                                "text-sm font-semibold text-gray-700 bg-gray-100 px-2 py-1 rounded-md"
                            )

                    # Action buttons with improved styling
                    with ui.row().classes("gap-3 w-full mt-4"):
                        ui.button(
                            "View",
                            on_click=partial(
                                ui.navigate.to, f"/view_advert?id={advert['id']}"
                            ),
                        ).classes(
                            "flex-1 px-4 py-2 rounded-lg text-sm font-medium "
                            "transition-all duration-300 btn-primary"
                        ).style(
                            "background: linear-gradient(135deg, #16a34a, #22c55e) !important; color: white !important; border: none !important;"
                        ).props(
                            "no-caps flat"
                        )

                        ui.button(
                            "Edit",
                            on_click=lambda a=advert: ui.navigate.to(
                                f"/edit_advert?id={a['id']}"
                            ),
                        ).classes(
                            "flex-1 px-4 py-2 rounded-lg text-sm font-medium "
                            "transition-all duration-300 btn-secondary border-2"
                        ).style(
                            "background: linear-gradient(135deg, #16a34a, #22c55e) !important; color: white !important; border: none !important;"
                        ).props(
                            "no-caps flat"
                        )
