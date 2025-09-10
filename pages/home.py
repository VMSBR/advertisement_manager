from nicegui import ui,app


def show_home_page():
    # Big container
    with ui.element("div").classes("relative w-full h-screen"):

        # Background carousel
        with ui.carousel().props("arrows autoplay swipe infinite").classes(
            "absolute inset-0 w-full h-full z-[-2]"
        ):
            ui.carousel_slide().classes("w-full h-full").style(
                "background-image: url(/assets/homee.jpg); background-size: cover; background-position: center;"
            )
            ui.carousel_slide().classes("w-full h-full").style(
                "background-image: url(/assets/home.jpg); background-size: cover; background-position: center;"
            )
            ui.carousel_slide().classes("w-full h-full").style(
                "background-image: url(/assets/homeee.jpg); background-size: cover; background-position: center;"
            )

        # Overlay (semi-transparent dark layer)
        ui.element("div").style(
            "background: rgba(0,0,0,0.5); position: absolute; inset: 0; z-index: -1;"
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

    with ui.grid(columns=3).classes("gap-20 p-1"):
        for i in range(6):
            with ui.card().classes(
                "p-4 rounded-xl shadow-lg hover:shadow-xl transition"
            ):
                ui.image("/assets/sample.jpg").classes(
                    "w-full h-40 object-cover rounded-lg mb-3"
                )
                ui.label(f"Name {i+1}").classes(
                    "text-lg font-semibold font-poppins mb-2"
                )
                ui.label("Short description of the product...").classes(
                    "text-gray-600 mb-3"
                )
                ui.label("Price").classes("text-lg font-bold text-[#2E4A3F] mb-3")
                with ui.row().classes("justify-between"):
                    ui.button(
                        "View", on_click=lambda: ui.navigate.to("/view_advert")
                    ).classes("bg-green text-white px-4 py-2 rounded-md")
                    ui.button(
                        "Edit", on_click=lambda: ui.navigate.to("/edit_advert")
                    ).classes("bg-green text-white px-4 py-2 rounded-md")
