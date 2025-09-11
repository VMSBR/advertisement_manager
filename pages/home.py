from nicegui import ui, app


def show_home_page():

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
    sample_adverts = [
        {"id": 1, "title": "Fresh Tomatoes", "description": "Organic tomatoes from local farm", "price": "GHC 50", "category": "Vegetables", "flyer": "/assets/freshtomatoes.jpg"},
        {"id": 2, "title": "Sweet Mangoes", "description": "Juicy mangoes ready to eat", "price": "GHC 30", "category": "Fruits", "flyer": "/assets/sweetmangoes.jpg"},
        {"id": 3, "title": "Brown Rice", "description": "Premium quality brown rice", "price": "GHC 80", "category": "Grains & Legumes", "flyer": "/assets/brownrice.jpg"},
        {"id": 4, "title": "Free Range Eggs", "description": "Fresh eggs from free range chickens", "price": "GHC 25", "category": "Dairy & Eggs", "flyer": "/assets/freerangeeggs.jpg"},
        {"id": 5, "title": "Organic Spinach", "description": "Fresh leafy greens", "price": "GHC 15", "category": "Vegetables", "flyer": "/assets/organicspinach.jpg"},
        {"id": 6, "title": "Cashew Nuts", "description": "Roasted cashew nuts", "price": "GHC 120", "category": "Nuts", "flyer": "/assets/cashewnuts.jpg"},
        {"id": 7, "title": "Sweet Potatoes", "description": "Fresh sweet potatoes", "price": "GHC 40", "category": "Tubers", "flyer": "/assets/sweetpotatoes.jpg"},
        {"id": 8, "title": "Basil Leaves", "description": "Fresh aromatic basil", "price": "GHC 10", "category": "Herbs & Spices", "flyer": "/assets/basilleaves.jpg"}
    ]
    
    # Responsive grid: 1 column on mobile, 2 on tablet, 3 on desktop, 4 on large screens
    with ui.element("div").classes("grid grid-cols-1 sm:grid-cols-2 md:grid-cols-3 lg:grid-cols-4 gap-6 p-4 max-w-7xl mx-auto"):
        for advert in sample_adverts:
            with ui.card().classes(
                "p-4 rounded-xl shadow-lg hover:shadow-xl transition-all duration-300 bg-white"
            ):
                ui.image(advert.get("flyer", "/assets/sample.jpg")).classes(
                    "w-full h-40 object-cover rounded-lg mb-3"
                )
                ui.label(advert["title"]).classes(
                    "text-lg font-semibold font-poppins mb-2 text-[#2E4A3F]"
                )
                ui.label(advert["description"]).classes(
                    "text-gray-600 mb-2 text-sm"
                )
                ui.label(f"Category: {advert['category']}").classes(
                    "text-xs text-[#8B5E3C] font-medium mb-2"
                )
                ui.label(advert["price"]).classes("text-lg font-bold text-[#2E4A3F] mb-3")
                with ui.row().classes("gap-2 w-full"):
                    ui.button(
                        "View", on_click=lambda a=advert: ui.navigate.to(f"/view_advert?id={a['id']}")
                    ).classes("px-3 py-1 rounded-md text-sm flex-1").style("background-color: #16a34a; color: white;").props("no-caps")
                    ui.button(
                        "Edit", on_click=lambda a=advert: ui.navigate.to(f"/edit_advert?id={a['id']}")
                    ).classes("px-3 py-1 rounded-md text-sm flex-1").style("background-color: #22c55e; color: white;").props("no-caps")
