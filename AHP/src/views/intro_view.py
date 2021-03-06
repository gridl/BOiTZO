# ======================================================================================================================
# PROJECT NAME:             Easy AHP Tool
# FILE NAME:                intro_view
# FILE VERSION:             1.0
# DATE:                     25.03.2018
# AUTHOR:                   Piotr Skalski [github.com/SkalskiP]
# ======================================================================================================================
# File contains function used to create app view used visible at the very beginning of app.
# ======================================================================================================================


from ..utils.views_names import ViewsNames


def intro_view(router):
        
    with open("./data/intro.txt") as f:
        content = f.readlines()
        
    for index, line in enumerate(content):
        router.screen.addstr(index + 1, 4, line)
        
    router.screen.getch()
    router.current_view = ViewsNames.LUNCH_MENU
