There are following components in this folder:

__init__.py 

- Purpose of this file is to have component() function imported so that it can be referenced in other files as dash_mantine_template.date_input_example.component()

Callback.py 

- Purpose of this file is to contain callback function that will query database and update properties of UI component.
- It will be run on initial load of application.
- Sets default date value, minimum and maximum selectable dates based on business logic.

CallbackSignature.py 

- Purpose of this file is to define structure of callback i.e. to define inputs, outputs, state and running elements of callback.
- All callbacks should be defined using pattern called "Flexible Callback Signature" - https://dash.plotly.com/flexible-callback-signatures

Component.py 

- Instantiation of UI component defined in global_component's date_input/ folder.
- It will be used in just one place (bc it has assigned unique ID).

ComponentID.py 

- Place where component ID is defined.

Input.py 

- Instantiate input/state template with specific ID and (if necessary) specific property value.
- input_() and input_dummy() are defined here.
- input_() will be used in signature of all components that depend on date_input_example i.e. all components that have date_input_example component as input/state in its CallbackSignature.py file.
- input_() typically triggers when user selects a date (property='value').

Output.py 

- Instantiate output templates with specific IDs.
- All UI component's attributes that should be updated via callback should be instantiated here.
- output__value(), output__minDate(), output__maxDate(), output__loading_overlay() are defined here.

Types.py 

- Defined data types that are used in Callback.py file.

Running.py

- Instantiate running component for loading overlay state management.

## Usage Example

```python
# In your main layout
from dash_mantine_template import date_input_example

layout = dmc.Container([
    date_input_example.component(),
    # ... other components that depend on date selection
])

# In another component that needs to respond to date changes
from dash_mantine_template.date_input_example import input_

@callback(
    inputs={'selected_date': input_()},
    output=...
)
def update_data_based_on_date(selected_date: str):
    # selected_date will be in format "YYYY-MM-DD"
    # Query data for the selected date
    data = query_database_by_date(selected_date)
    return data
```

## Date Format Notes

- The component returns dates as strings in "YYYY-MM-DD" format by default
- You can change this using the `valueFormat` parameter in Component.py
- Common formats: "DD/MM/YYYY", "MM/DD/YYYY", "YYYY-MM-DD"
- Use Python's `datetime.strptime()` to parse the string into a date object if needed

