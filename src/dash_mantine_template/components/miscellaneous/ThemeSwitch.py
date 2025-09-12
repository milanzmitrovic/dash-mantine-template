from enum import Enum

import dash_mantine_components as dmc
from dash import Input, Output, callback, clientside_callback
from dash_iconify import DashIconify
from pydantic import ConfigDict, validate_call

from ...component_ids.containers.DummyOutputs import (
    OnThemeChange,
    ThemeClientsideCallback,
)
from ...component_ids.miscellaneous.ThemeSwitch import (
    ThemeSwitchComponent,
)
from ...utils.database.SqlAlchemy import sql_connector
from ...utils.logging.Logger import logger


def theme_switch():
    return dmc.Switch(
        offLabel=DashIconify(
            icon="radix-icons:moon",
            width=15,
            color=dmc.DEFAULT_THEME["colors"]["yellow"][8],
        ),
        onLabel=DashIconify(
            icon="radix-icons:sun",
            width=15,
            color=dmc.DEFAULT_THEME["colors"]["yellow"][6],
        ),
        id=ThemeSwitchComponent.id.value,
        persistence=True,
        color="grey",
    )


clientside_callback(
    """
    (switchOn) => {

        // Main logic is implemented here.
        // Setting value dark/light to 
        // attribute data-mantine-color-scheme 
        // of HTML scheme.
        document.documentElement.setAttribute('data-mantine-color-scheme', switchOn ? 'light' : 'dark');


        // Purpose of this part is to remove CSS files that 
        // has been preloaded when page is being refreshed.
        // Those CSS files are only necessary when refreshing 
        // page in order to to remove WHITE/BLACK background in 
        // browser untill Mantine style/theme is loaded.
        const cssFilesToRemove = ['dark.css', 'light.css'];
        const links = document.querySelectorAll('link[rel="stylesheet"]');
        links.forEach(link => {
            const href = link.getAttribute('href');
            if (href && cssFilesToRemove.some(file => href.includes(file))) {
            link.parentNode.removeChild(link);
            console.log(`Removed: ${href}`);
            }
        });

        // This is just due to sth must be returned 
        // by Dash callback as per design.
       return window.dash_clientside.no_update
    }
    """,
    Output(ThemeClientsideCallback.id.value, ThemeClientsideCallback.property.value),
    Input(ThemeSwitchComponent.id.value, ThemeSwitchComponent.property.value),
)


class Theme(Enum):
    DARK = False
    LIGHT = True


# This we can use for dynamically
# changing charts based on background
# color that user chose.
@callback(
    Output(OnThemeChange.id.value, OnThemeChange.property.value),
    Input(ThemeSwitchComponent.id.value, ThemeSwitchComponent.property.value),
)
@validate_call(config=ConfigDict(arbitrary_types_allowed=True), validate_return=True)
def on_theme_change(input_: Theme):
    """
    false --> light
    true --> dark

    """
    # This is example how logging
    # should be used in project template.
    logger.info(input_)
    logger.critical(111)
    logger.info(222)
    logger.warning(3333)
    logger.error(4444)
    logger.debug(7777)

    ddl_statement = """

        CREATE TABLE IF NOT EXISTS users (
            id SERIAL PRIMARY KEY,
            name TEXT,
            age INTEGER
        );

                
    """
    result_ = sql_connector.ddl_statement(ddl_query=ddl_statement)
    print(result_)
    # --- --- --- #

    create_statement = "INSERT INTO users (name, age) VALUES (:name, :age)"
    create_params = {"name": "Alice", "age": 30}

    result_c = sql_connector.create_statement(
        sql_query=create_statement, parameters=create_params
    )
    print(result_c.rowcount)

    # --- --- --- #

    read_query = "SELECT * FROM users where name = :name"
    read_params = {"name": "Alice"}

    result_r = sql_connector.read_statement(
        sql_query=read_query, parameters=read_params
    )
    print(list(result_r.keys()))
    for i in result_r:
        print(i)

    # --- --- --- #

    update_query = "UPDATE users SET age = :age WHERE name = :name"
    update_params = {"age": 40, "name": "Alice"}

    result_u = sql_connector.update_statement(
        sql_query=update_query, parameters=update_params
    )
    print(result_u.rowcount)

    # --- --- --- #

    delete_query = "DELETE FROM users WHERE name = :name"
    delete_params = {"name": "Alice"}

    result_d = sql_connector.delete_statement(
        sql_query=delete_query, parameters=delete_params
    )
    print(result_d.rowcount)

    return f"[{input_}]"
