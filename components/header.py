from nicegui import ui


def show_header():
    with ui.header().classes("bg-white px-6 py-4"):
        with ui.row().classes("justify-between w-full items-center"):
            ui.label("AGROKASA").classes(
                "text-2xl font-bold text-green font-lobster italic"
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
