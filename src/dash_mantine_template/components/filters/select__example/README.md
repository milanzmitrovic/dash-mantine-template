
There are following components in this folder:

__init__.py 

- Purpose of this file is to have component() function imported so that it can be referenced in other files as dash_mantine_template.select_example.component()

Callback.py 

- Purpose of this file is to contain callback function that will query database and update properties of UI component.
- It will be run on initial load of application.

CallbackSignature.py 

- Purpose of this file is to define structure of callback i.e. to define inputs, outputs, state and running elements of callback.
- All callbacks should be defined using pattern called "Flexible Callback Signature" - https://dash.plotly.com/flexible-callback-signatures

Component.py 

- Instantiation of UI component defined in global_component's utils/ file.
- It will be used in just one place (bc it has assigned unique ID).

ComponentID.py 

- Place where component ID is defined.

Input.py 

- Instantiate input/state template with specific ID and (if necessary) specific property value.
- input_() and input_dummy() are defined here.
- input_() will be used in signature of all components that depends on select_example i.e. all components that have select_example component as input/state in its CallbackSignature.py file.

Output.py 

- Instantiate output templates with specific IDs.
- All UI component's attributes that should be updated via callback should be instantiated here.
- output__data(), output__value(), output__loading_overlay() are defined here.

Types.py 

- Defined data types that are used in Callback.py file.
