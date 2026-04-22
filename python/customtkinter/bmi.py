# Author: Harel Haram
# Date: 2026-02-14
# Description: Calculate the BMI through CustomTkinter

# Import the entire bible itself
import customtkinter

# Prepare to witness the creation of my peak appearance
BMI_MOSQUITO_LIMIT = 1.9
BMI_UNDERWEIGHT_START = 2.0
BMI_NORMAL_START = 18.5
BMI_OVERWEIGHT_START = 25.0
BMI_OBESITY_1_START = 30.0
BMI_OBESITY_2_START = 35.0
BMI_OBESITY_3_START = 40.0

customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("dark-blue")

# Parameters of the windows
root_gui = customtkinter.CTk()
root_gui.geometry("400x250")
root_gui.title("BMI System")
root_gui.resizable(False, False)

label_font = customtkinter.CTkFont(family="Verdana", size=30, weight="bold")

# My beloved GUI Whitelabol from TEMU
label_intro = customtkinter.CTkLabel(
    root_gui, text="BMI Calculator", text_color="#0067DD", font=label_font
)
label_intro.pack(padx=10, pady=10)


# Calculus Gynasius
def calc() -> None:
    try:
        root_gui.geometry("450x250")
        height = float(label_height.get())
        weight = float(label_weight.get())
        bmi = weight / (height**2)

        if bmi < BMI_MOSQUITO_LIMIT:
            classification = "Mosquito"
        elif BMI_UNDERWEIGHT_START <= bmi < BMI_NORMAL_START:
            classification = "Taller"
        elif BMI_NORMAL_START <= bmi < BMI_OVERWEIGHT_START:
            classification = "Normaller"
        elif BMI_OVERWEIGHT_START <= bmi < BMI_OBESITY_1_START:
            classification = "Pre-Obesity"
        elif BMI_OBESITY_1_START <= bmi < BMI_OBESITY_2_START:
            classification = "Obesity Level I"
        elif BMI_OBESITY_2_START <= bmi < BMI_OBESITY_3_START:
            classification = "Obesity Level II"
        elif bmi >= BMI_OBESITY_3_START:
            classification = "Obesity Level III"
        else:
            classification = "Unknown"

        label_result.configure(
            text=f"Your BMI is {bmi:.2f}, and ur classified as {classification}",
            text_color="#71B3FF",
        )
    except ValueError:
        root_gui.geometry("600x250")

        label_result.configure(
            text="Error 003: Too bad mister, my recommendation for you is to "
            "feel the wrath of Napoleon, you punk",
            text_color="#B30000",
        )
    pass


# Note: CustomTkinter has its own calculation methods instead of the common Python strategy

# Inputting and entering
label_weight = customtkinter.CTkEntry(
    root_gui,
    placeholder_text="Body Weight:",
    corner_radius=30,
    width=300,
    placeholder_text_color="#BFD5FF",
)
label_height = customtkinter.CTkEntry(
    root_gui,
    placeholder_text="Body Height:",
    corner_radius=30,
    width=300,
    placeholder_text_color="#BFD5FF",
)
label_weight.pack(padx=10, pady=10)
label_height.pack(padx=10, pady=10)

# Do the button
label_button = customtkinter.CTkButton(
    root_gui,
    text="Confirm input",
    fg_color="#0067DD",
    hover=True,
    hover_color="#002857",
    command=calc,
)
label_button.pack(padx=10, pady=10)

label_result = customtkinter.CTkLabel(root_gui, text="")
label_result.pack(padx=10, pady=10)

# Rendering the silly windows
root_gui.mainloop()
