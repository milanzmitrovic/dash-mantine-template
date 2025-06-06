"""
Purpose of charts/ sub-folder inside component_ids/ folder
is to organize IDs of elements that are being used to update
and control Dash components.

Folder structure of component_ids/ folder strictly mimics
folder structure of components/ folder.

Why is important to have dataclasses in which component IDs
will be defined?

    - It is easier for IDE to keep track of variables.
    - It is safer to change some ID in the future i.e.
    you can easily see in which callbacks specific ID
    was used.
    - It would be difficult to create duplicated IDs and
    even if that happens, it will be possible to see which
    one is duplicate.

Dataclasses representing IDs of components should be
organized in such a way that location of component in
components/ folder (where ID is used) corresponds to
location in component_ids/ folder.
    - It should NOT be organized as per callback logic
    i.e. it is not important where is stored callback
    that uses respective ID.
"""
