There are following components in this folder:

__init__.py 

- Purpose of this file is to have component() function imported so that it can be referenced in other files as dash_mantine_template.pagination_example.component()

Callback.py 

- Purpose of this file is to contain callback function that will query database and update properties of UI component.
- It will be run on initial load of application.
- Calculates total number of pages based on total items and items per page.

CallbackSignature.py 

- Purpose of this file is to define structure of callback i.e. to define inputs, outputs, state and running elements of callback.
- All callbacks should be defined using pattern called "Flexible Callback Signature" - https://dash.plotly.com/flexible-callback-signatures

Component.py 

- Instantiation of UI component defined in global_component's pagination/ folder.
- It will be used in just one place (bc it has assigned unique ID).

ComponentID.py 

- Place where component ID is defined.

Input.py 

- Instantiate input/state template with specific ID and (if necessary) specific property value.
- input_() and input_dummy() are defined here.
- input_() will be used in signature of all components that depend on pagination_example i.e. all components that have pagination_example component as input/state in its CallbackSignature.py file.
- input_() typically triggers when user clicks on a page number (property='value').

Output.py 

- Instantiate output templates with specific IDs.
- All UI component's attributes that should be updated via callback should be instantiated here.
- output__total(), output__value(), output__loading_overlay() are defined here.

Types.py 

- Defined data types that are used in Callback.py file.

Running.py

- Instantiate running component for loading overlay state management.

## Usage Example

```python
# In your main layout
from dash_mantine_template import pagination_example

layout = dmc.Container([
    pagination_example.component(),
    # ... other components that depend on pagination
])

# In another component that needs to respond to page changes
from dash_mantine_template.pagination_example import input_

@callback(
    inputs={'page': input_()},
    output=...
)
def update_table_based_on_page(page: int):
    # Load data for specific page
    offset = (page - 1) * items_per_page
    data = query_database(offset=offset, limit=items_per_page)
    return data
```
