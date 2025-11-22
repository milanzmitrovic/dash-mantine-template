
There are following components in this folder:

__init__.py 

    All functions that are defined inside select/ folder 
    and that should be used externally are imported in 
    __init__.py file so that they can be user as gc.select...

Component.py
    
    *** component()

    --> Template/function for UI component.

    --> It will be imported and instantiated in all 
        places where SELECT component is used (There 
        could be several components of type SELECT, and 
        this is expected actually).

    --> We use template to create specific instance 
        of SELECT component.

Input.py 
    
    *** input_() 
        - Returns callback signature template.
        - Should be configured with component ID
        and (if needed) input trigger property.
    
    *** input_dummy()
        - Update component with initial values.
        - Happens immediatelly after page is loaded.
        - It is used so that there is no hardcoded 
        values/options in component itself.

    --> Defining template for case when component is 
        used as input/state component.

Output.py 
    
    *** output()
        - Returns callback signature template.
        - Should be configured with component ID
        and (if needed) output trigger property.    

    *** output__loading_overlay()
        - Returns callback signature template.
        - Should be configured with component ID only.    
    

    --> Defining template for case when component is 
        used as output component.

Types.py 

    --> Defining data types that are used in 
        template component.

