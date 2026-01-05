There are following components in this folder:

__init__.py 

    All functions that are defined inside modal/ folder 
    and that should be used externally are imported in 
    __init__.py file so that they can be used as gc.modal...

Component.py
    
    *** component()

    --> Template/function for UI component.

    --> It will be imported and instantiated in all 
        places where MODAL component is used (There 
        could be several components of type MODAL, and 
        this is expected actually).

    --> We use template to create specific instance 
        of MODAL component.
    
    --> IMPORTANT: Modal has NO button inside. It is controlled
        externally via the 'opened' property by other components
        (typically buttons).

Input.py 
    
    *** input_() 
        - Returns callback signature template.
        - Should be configured with component ID
        and (if needed) input trigger property.
        - Default property is 'opened' (modal open/close state)
        - Can be used to trigger actions when modal opens/closes
    
    *** input_dummy()
        - Update component with initial values.
        - Happens immediately after page is loaded.
        - It is used so that there is no hardcoded 
        values in component itself.
        - Typically used to populate modal content from database.

    --> Defining template for case when component is 
        used as input/state component.

Output.py 
    
    *** output()
        - Returns callback signature template.
        - Should be configured with component ID
        and (if needed) output trigger property.
        - Default property is 'opened' (controls modal visibility)
        - This is what external buttons typically update
    

    --> Defining template for case when component is 
        used as output component.

Types.py 

    --> Defining data types that are used in 
        template component.

## Usage Pattern

The modal is designed to be controlled by external components:

1. Create a modal instance with unique ID
2. Create a button (or other trigger) instance
3. Button's callback outputs to modal's 'opened' property
4. Clicking button sets opened=True, opening the modal
5. Closing modal (X button, escape, outside click) sets opened=False

