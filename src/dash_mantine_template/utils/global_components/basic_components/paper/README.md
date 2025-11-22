
There are following components in this folder:

__init__.py 

    All functions that are defined inside paper/ folder 
    and that should be used externally are imported in 
    __init__.py file so that they can be user as gc.paper...

Component.py
    
    *** component()

    --> Template/function for UI component.

    --> It will be imported and instantiated in all 
        places where PAPER component is used (There 
        could be several components of type PAPER, and 
        this is expected actually).

    --> We use template to create specific instance 
        of PAPER component.

Input.py 
    
    This file does not exist. Why?
    
    PAPER component is not meant 
    to be used neither as input nor as 
    output of callback.

    It is just meant to be as a holder 
    for other components.


Output.py 
    
    This file does not exist. Why?
    
    PAPER component is not meant 
    to be used neither as input nor as 
    output of callback.

    It is just meant to be as a holder 
    for other components.

Types.py 

    --> Defining data types that are used in 
        template component.
