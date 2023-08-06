import asyncio


from shiny import App, ui   # pip install shiny
import shinyswatch          # pip install shinyswatch
from util_logger import setup_logger

logger, logname = setup_logger(__file__)

app_ui = ui.page_navbar(
    shinyswatch.theme.lumen(),
    # ui.nav(
    #     "BookReport",
    #     ui.layout_sidebar(
    #         # get_mtcars_inputs(),
    #         # get_mtcars_outputs(),
    #     ),
    # ),
    ui.nav(ui.a("About", href="https://github.com/hpotluri")),
    ui.nav(ui.a("GitHub", href="https://github.com/hpotluri/cintel-07-project")),
    ui.nav(ui.a("App", href="https://hpotluri.shinyapps.io/cintel-07-project")),
    ui.nav(ui.a("Plotly Express", href="https://plotly.com/python/line-and-scatter/")),
    ui.nav(ui.a("BookAPI", href="https://openweathermap.org/api")),
    ui.nav(ui.a("File_Reader", href="https://shiny.rstudio.com/py/api/reactive.file_reader.html")),
    title=ui.h1("Case Dashboard"),
)


def server(input, output, session):
    """Define functions to create UI outputs."""
    logger.info("Starting server ...")

    # Kick off continuous updates when the app starts
    
    logger.info("Starting continuous updates ...")



app = App(app_ui, server, debug=True)