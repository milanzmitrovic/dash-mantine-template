
# General Idea

## A) global_components/ is used to instantiate specific template

- __init __.py --> 

        All functions that should be used as gc.component... are imported here.

- Component.py --> 

      Function that is returning template for UI component.

- Input.py --> 

        Function that is returning template for INPUT part of CallbackSignature.

        When UI component is used as INPUT in callback.

- Output.py --> 

        Function that is returning template for OUTPUT part of CallbackSignature.

        Wdhe UI component is used as OUTPUT in callback.




## B) components/ is used for storing component templates

- __init __.py --> 

      Define function that will be used outside module.
      
      It is usually component() function that is returning UI element.

- Callback.py --> 

      Definition of actuall callback(s) that is updating properties of UI components.

- CallbackSignature.py --> 

      Final version of CallbackSignature that will be used in app.

        - It ha all INPUT/OUTPUT callback signatures defined in Input.py and Output.py grouped in one place.

- Component.py --> 

      Instantiate UI component with appropriate ID and other attributes.

- ComponentID.py --> 

      Define component ID.

- Input.py --> 

      Here are defined all INPUT callback elements that are related to one component.

      When UI component is used as INPUT in callback.

      Later on, all INPUT IDs/Properties are grouped in CallbackSignature.py file.

- Output.py --> 

      Here are defined all OUTPUT callback elements that are related to one component.

      When UI component is used as OUTPUT in callback.

      Later on, all OUTPUT IDs/Properties are grouped in CallbackSignature.py file.

- Running.py --> 

      Define what is happening while callback is being processed.
      
      There should be dmc.LoadingOverlay on top of component.











pagination --> DONE
date_input --> DONE
modal --> DONE
  a) When modal button is hidden.
  b) When modal button is not hidden.
--> There is modal w/o button and button is 
added separately to open/close modal.

... Promeniti imena argumenata - pylint... --> DONE

... Add Running.py everywhere. --> DONE

... Add additional comments.

!!!... Add tests everywhere.... Leave for next commit...

FINISH LINE!!!

