import os


def clear():
    """
    Clears the screen of the terminal.
    """
    os.system("cls" if os.name == "nt" else "clear")


"""
Displays team and project background.
"""


def display_team_background():
    clear()

    print(
        r"""
████████╗███████╗░█████╗░███╗░░░███╗  ██████╗░░█████╗░░█████╗░██╗░░██╗░██████╗░██████╗░░█████╗░██╗░░░██╗███╗░░██╗██████╗░
╚══██╔══╝██╔════╝██╔══██╗████╗░████║  ██╔══██╗██╔══██╗██╔══██╗██║░██╔╝██╔════╝░██╔══██╗██╔══██╗██║░░░██║████╗░██║██╔══██╗
░░░██║░░░█████╗░░███████║██╔████╔██║  ██████╦╝███████║██║░░╚═╝█████═╝░██║░░██╗░██████╔╝██║░░██║██║░░░██║██╔██╗██║██║░░██║
░░░██║░░░██╔══╝░░██╔══██║██║╚██╔╝██║  ██╔══██╗██╔══██║██║░░██╗██╔═██╗░██║░░╚██╗██╔══██╗██║░░██║██║░░░██║██║╚████║██║░░██║
░░░██║░░░███████╗██║░░██║██║░╚═╝░██║  ██████╦╝██║░░██║╚█████╔╝██║░╚██╗╚██████╔╝██║░░██║╚█████╔╝╚██████╔╝██║░╚███║██████╔╝
░░░╚═╝░░░╚══════╝╚═╝░░╚═╝╚═╝░░░░░╚═╝  ╚═════╝░╚═╝░░╚═╝░╚════╝░╚═╝░░╚═╝░╚═════╝░╚═╝░░╚═╝░╚════╝░░╚═════╝░╚═╝░░╚══╝╚═════╝░"""
    )

    print("\nTeam Member List\n")
    print("1) Darrance Beh Heng Shek (Team Lead)")
    print("2) Deron Ho Wen Harn")
    print("3) Izzat Zulqarnain Bin Izaiddin")
    print("4) Tan Ho Chen")
    print("5) Lee Ming Hui Isaac")

    print("\nProject Background\n")
    print(
        "- This project is a final group assessment for the subject CSC1024 - Programming Principles."
    )
    print(
        "- The project is a book management system that allows users to add, update, delete and view books in a database."
    )
    print(
        "- For this project, the team utilized the GitHub platform to collaborate on the project under the guidance of the Team Lead."
    )

    print(
        r"""
          
██████╗░██████╗░░█████╗░░░░░░██╗███████╗░█████╗░████████╗  ░█████╗░██████╗░███████╗██████╗░██╗████████╗░██████╗
██╔══██╗██╔══██╗██╔══██╗░░░░░██║██╔════╝██╔══██╗╚══██╔══╝  ██╔══██╗██╔══██╗██╔════╝██╔══██╗██║╚══██╔══╝██╔════╝
██████╔╝██████╔╝██║░░██║░░░░░██║█████╗░░██║░░╚═╝░░░██║░░░  ██║░░╚═╝██████╔╝█████╗░░██║░░██║██║░░░██║░░░╚█████╗░
██╔═══╝░██╔══██╗██║░░██║██╗░░██║██╔══╝░░██║░░██╗░░░██║░░░  ██║░░██╗██╔══██╗██╔══╝░░██║░░██║██║░░░██║░░░░╚═══██╗
██║░░░░░██║░░██║╚█████╔╝╚█████╔╝███████╗╚█████╔╝░░░██║░░░  ╚█████╔╝██║░░██║███████╗██████╔╝██║░░░██║░░░██████╔╝
╚═╝░░░░░╚═╝░░╚═╝░╚════╝░░╚════╝░╚══════╝░╚════╝░░░░╚═╝░░░  ░╚════╝░╚═╝░░╚═╝╚══════╝╚═════╝░╚═╝░░░╚═╝░░░╚═════╝░"""
    )
    print("\nDarrance Beh Heng Shek (Team Lead)")
    print("- Responsible for Managing the Team and the Project.")
    print(
        "- Ensures that the Project is on Track and that the Team is on Schedule to Meet Project Deadline."
    )
    print(
        "- Gave Guidance and Constructive Feedback to Team Members and Made Sure All Member's Work Meets Quality Standards."
    )
    print(
        "- Responsible for the Update Book Record(s) Functions, ALL Auxilary Functions, ALL Utility Functions, UI/UX Experience."
    )
    print(
        "- Responsible for Compiling Final Program and Bug-Testing The Program."
    )
    print("- Compiled the Final Report and Final Flowchart.")

    print("\nDeron Ho Wen Harn")
    print("- Responsible for the Display Book Record(s) Function.")
    print(
        "- Wrote Report Section and Drew Flowchart for their Responsible Function."
    )

    print("\nIzzat Zulqarnain Bin Izaiddin")
    print("- Responsible for the Search Book Record(s) Function.")
    print(
        "- Wrote Report Section and Drew Flowchart for their Responsible Function."
    )

    print("\nTan Ho Chen")
    print("- Partially Responsible for the Delete Book Record(s) Function.")
    print(
        "- Partially Responsible for Writing Report Section and Drawing Flowchart for their Responsible Function."
    )

    print("\nLee Ming Hui Isaac")
    print("- Responsible for the Add Book Record(s) Function.")
    print(
        "- Wrote Report Section and Drew Flowchart for their Responsible Function."
    )

    input("\n\nInput any Key to Return to Main Menu.\n")


display_team_background()
