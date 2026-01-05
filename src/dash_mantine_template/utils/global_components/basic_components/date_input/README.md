There are following components in this folder:

__init__.py 

    All functions that are defined inside date_input/ folder 
    and that should be used externally are imported in 
    __init__.py file so that they can be used as gc.date_input...

Component.py
    
    *** component()

    --> Template/function for UI component.

    --> It will be imported and instantiated in all 
        places where DATE_INPUT component is used (There 
        could be several components of type DATE_INPUT, and 
        this is expected actually).

    --> We use template to create specific instance 
        of DATE_INPUT component.

Input.py 
    
    *** input_() 
        - Returns callback signature template.
        - Should be configured with component ID
        and (if needed) input trigger property.
        - Default property is 'value' (selected date)
    
    *** input_dummy()
        - Update component with initial values.
        - Happens immediately after page is loaded.
        - It is used so that there is no hardcoded 
        values in component itself.
        - Typically used to set default date, min/max dates
        based on business logic or database values.

    --> Defining template for case when component is 
        used as input/state component.

Output.py 
    
    *** output()
        - Returns callback signature template.
        - Should be configured with component ID
        and (if needed) output trigger property.
        - Default property is 'value' (selected date)
    

    *** output__loading_overlay()
        - Returns callback signature template.
        - Should be configured with component ID only.    
    

    --> Defining template for case when component is 
        used as output component.

Types.py 

    --> Defining data types that are used in 
        template component.
