There are following components in this folder:

__init__.py 

- Purpose of this file is to have component() function imported so that it can be referenced in other files as dash_mantine_template.button_example.component()

Component.py 

- Instantiation of UI component defined in global_component's button/ folder.
- It will be used in just one place (bc it has assigned unique ID).
- Simple button with text "Open Modal"

ComponentID.py 

- Place where component ID is defined.

Input.py 

- Instantiate input/state template with specific ID.
- input_() is defined here and returns button's n_clicks input.

Types.py 

- Defined data types that are used in Callback.py file.


