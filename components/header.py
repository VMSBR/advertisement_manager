from nicegui import ui


def show_header():
    with ui.header().classes("bg-white px-6 py-4"):
        with ui.row().classes("justify-between w-full items-center"):
            # Try absolute path for logo
            with ui.element("div").classes("flex items-center"):
                ui.html(
                    '<img src="/assets/logo.png" alt="AGROKASA" style="height: 80px; width: auto; object-fit: contain;" />'
                )

            # removed text-red from here
            with ui.row().classes(
                "gap-6 font-semibold uppercase font-roboto no-underline"
            ):
                ui.link("Home", "/").classes(
                    "no-underline text-green-600 hover:text-[#E3CAA5]"
                )
                ui.link("Add Advert", "/add_advert").classes(
                    "text-green-600 no-underline hover:text-[#E3CAA5]"
                )
