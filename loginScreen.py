import customtkinter
from app import MainScreen
from PIL import Image


class LoginScreen(customtkinter.CTk):
    # noinspection PyUnusedLocal
    def __init__(self, *args, **kwargs):
        super().__init__(**kwargs)
        self.isAttempted = False
        self.geometry(f"{400}x{600}")
        self.title("Neo Stellar Ground Controller v1.0b")
        self.resizable(False, False)

        def get_input():
            user_input = login_name.get()
            user_pass = login_password.get()

            if user_input == "admin" and user_pass == "admin":
                print("Login Success")
                print(f"{user_input}, {user_pass}")
                open_main_screen(self)
                self.withdraw()
            else:
                if not self.isAttempted:
                    error_label = customtkinter.CTkLabel(self, text="Invalid Username / Password", text_color="red")
                    error_label.pack()
                    self.isAttempted = True

        def open_main_screen(window):
            if window.toplevel_window is None or not window.toplevel_window.winfo_exists():
                window.toplevel_window = MainScreen(window)  # create window if its None or destroyed
            else:
                window.toplevel_window.focus()  # if window exists focus it

        self.toplevel_window = None

        img = customtkinter.CTkImage(light_image=Image.open("src/login_icon.png"), size=(60, 60))
        image_label = customtkinter.CTkLabel(self, image=img, text="")
        image_label.pack()

        login_name = customtkinter.CTkEntry(self)
        login_name.pack()

        login_password = customtkinter.CTkEntry(self, show="*")
        login_password.pack()

        login_button = customtkinter.CTkButton(self, text="Login", command=get_input)
        login_button.pack()
