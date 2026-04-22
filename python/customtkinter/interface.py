# Author: Harel Haram
# Date: 2026-02-14
# Description: Calculate the terrain of your silly property through CustomTkinter

# Import the entire bible itself
import customtkinter

# Prepare to witness the creation of my peak appearance
customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("dark-blue")

# Parameters of the windows
root_gui = customtkinter.CTk()
root_gui.geometry("600x300")
root_gui.title("Graphic Interface for Educational Purposes")
root_gui.resizable(False, False)

# My beloved GUI Whitelabol from TEMU
label_intro = customtkinter.CTkLabel(
    root_gui, text="Graphic Interface", text_color="green", font=("Verdana", 15)
)
label_intro.pack(padx=10, pady=10)


# Terrain Constants
MIN_LARGE_TERRAIN_AREA = 50


# Calculus Terrainus
# Note: CustomTkinter has its own calculation methods instead of the common Python strategy
def calc() -> None:
    root_gui.geometry("620x600")
    try:
        result = int(label_width.get()) * int(label_length.get())
        if result >= MIN_LARGE_TERRAIN_AREA:
            label_result = customtkinter.CTkLabel(
                root_gui,
                text=f"I've calculated!1!1!1! The result is {result}",
                text_color="green",
                font=("Verdana", 10),
            )
            label_result.pack(padx=5, pady=5)
        else:
            label_result = customtkinter.CTkLabel(
                root_gui,
                text=f"The result is {result}, OMG UR TERRAIN IS SMALL WTF",
                text_color="yellow",
                font=("Verdana", 10),
            )
            label_result.pack(padx=5, pady=5)
        print("Jervis, find out who asked ❗")
    except ValueError:
        label_result = customtkinter.CTkLabel(
            root_gui,
            text="Error 003: Too bad mister, you need to suffer, how dare u not input the numbers",
            text_color="red",
            font=("Verdana", 10),
        )
        label_result.pack(padx=5, pady=5)


# Inputting and entering
label_width = customtkinter.CTkEntry(
    root_gui,
    placeholder_text="Terrain Width:",
    corner_radius=30,
    width=300,
    font=("Verdana", 15),
)
label_length = customtkinter.CTkEntry(
    root_gui,
    placeholder_text="Terrain Length:",
    corner_radius=30,
    width=300,
    font=("Verdana", 15),
)
label_width.pack(padx=10, pady=10)
label_length.pack(padx=10, pady=10)

# Do the button
label_button = customtkinter.CTkButton(
    root_gui,
    text="Confirm Input",
    fg_color="green",
    hover=True,
    hover_color="#105000",
    command=calc,
    font=("Verdana", 15),
)
label_button.pack(padx=10, pady=10)

# Rendering the silly windows
root_gui.mainloop()
