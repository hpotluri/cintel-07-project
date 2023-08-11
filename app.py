import asyncio
from book_server import get_books_server_functions
from book_ui_input import get_books_inputs
from book_ui_output import get_books_outputs
from continuous_book import update_csv_book
from continuous_book import update_csv_bookNoAPI


from shiny import App, ui   # pip install shiny
import shinyswatch          # pip install shinyswatch
from util_logger import setup_logger

logger, logname = setup_logger(__file__)

app_ui = ui.page_navbar(
    shinyswatch.theme.lumen(),
    ui.nav(
        "BookReport",
        ui.layout_sidebar(
            get_books_inputs(),
            get_books_outputs(),
        ),
    ),
    ui.nav(ui.a("About", href="https://github.com/hpotluri")),
    ui.nav(ui.a("GitHub", href="https://github.com/hpotluri/cintel-07-project")),
    ui.nav(ui.a("App", href="https://hpotluri.shinyapps.io/cintel-07-project")),
    ui.nav(ui.a("Plotly Express", href="https://plotly.com/python/line-and-scatter/")),
    ui.nav(ui.a("BookAPI", href="https://openweathermap.org/api")),
    ui.nav(ui.a("File_Reader", href="https://shiny.rstudio.com/py/api/reactive.file_reader.html")),
    title=ui.h1("Case Dashboard"),
)

async def update_csv_files():
    while True:
        logger.info("Calling continuous updates ...")
        #task1 = asyncio.create_task(update_csv_book())
        task1 = asyncio.create_task(update_csv_bookNoAPI())
        await asyncio.gather(task1)
        await asyncio.sleep(60)  # wait for 60 seconds

def server(input, output, session):
    """Define functions to create UI outputs."""
    logger.info("Starting server ...")
    asyncio.create_task(update_csv_files())
    
    logger.info("Starting continuous updates ...")

    get_books_server_functions(input, output, session)


app = App(app_ui, server, debug=True)