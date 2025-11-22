
There are following components in this folder:

__init__.py 

    All functions that are defined inside menu/ folder 
    and that should be used externally are imported in 
    __init__.py file so that they can be user as gc.menu...

Component.py
    
    *** component()
    
    --> Template/function for UI component.
    
    --> It will be imported and instantiated in all 
        places where MENU component is used 
        (There could be several components of type MENU, 
        and this is expected actually).
    
    --> We use template to create specific instance 
        of MENU component.

Input.py 
    
    This component does not have input signatures.

    This component is self contained i.e. there is 
    no need for callback logic for it to work.

    Button for opening dmc.Modal() works out of the 
    box i.e. logic is built into Mantine JS code.

Output.py 
    
    This component does not have output signatures.

    This component is self contained i.e. there is 
    no need for callback logic for it to work.

    Button for opening dmc.Modal() works out of the 
    box i.e. logic is built into Mantine JS code.

Types.py 

    --> Defining data types that are used in 
        template component.

