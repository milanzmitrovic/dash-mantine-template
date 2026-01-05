There are following components in this folder:

__init__.py 

- Purpose of this file is to have component() function imported so that it can be referenced in other files as dash_mantine_template.modal_example.component()

Callback.py 

- Purpose of this file is to contain callback function that will set initial state of modal.
- Modal typically starts closed and is controlled externally by other components.
- If modal content needs to be populated from database, additional outputs would be added here.

CallbackSignature.py 

- Purpose of this file is to define structure of callback i.e. to define inputs, outputs, state and running elements of callback.
- All callbacks should be defined using pattern called "Flexible Callback Signature" - https://dash.plotly.com/flexible-callback-signatures

Component.py 

- Instantiation of UI component defined in global_component's modal/ folder.
- It will be used in just one place (bc it has assigned unique ID).
- Defines the modal content (title, children, size, etc.)

ComponentID.py 

- Place where component ID is defined.

Input.py 

- Instantiate input/state template with specific ID and (if necessary) specific property value.
- input_() and input_dummy() are defined here.
- input_() can be used in other components to react to modal opening/closing.

Output.py 

- Instantiate output templates with specific IDs.
- output__opened() is the main output - this is what external components update to open/close the modal.
- button__example will use this output to control the modal.

Types.py 

- Defined data types that are used in Callback.py file.

Running.py

- Modal doesn't use loading overlay, returns empty list.

## Usage Example

```python
# In your main layout
from dash_mantine_template import modal_example, button_example

layout = dmc.Container([
    button_example.component(),  # This button opens the modal
    modal_example.component(),   # The modal itself
])
```

## Control Flow

1. User clicks button__example
2. button__example's callback is triggered
3. Callback outputs to modal_example's 'opened' property
4. Sets opened=True
5. Modal appears!
6. User closes modal (X, Escape, or click outside)
7. Modal's opened property becomes False
8. Modal disappears

