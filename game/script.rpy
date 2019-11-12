# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define e = Character("Eileen")

image main_C = "character.jpg"

image main_C_Sleep = "Sleep.jpg"

image main_C_Meeting = "meeting.jpg"

# The game starts here.

label start:

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    scene Sleep

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.

    show main_C

    # These display lines of dialogue.

    e "You are sleeping."

    e "It is 7 a.m. you have a meeting at 8."

    menu:
        "You are sleepy and decided:"
        "Get up right now":
            "You get up."
            jump meeting
        "Keep sleeping":
            "You are keep sleeping."
            jump end

    # This ends the game.

    return
label end:
    scene lazy
    show main_C_Sleep
    e "You keep sleeping and miss the meetting... You are lazy..."

label meeting:
    scene meeting
    show main_C_Meeting
    e "You went to meeting and ..."
