import os
import tkinter as tk
import asyncio
from pyrogram import Client

api_id = 21245336
api_hash = "dcfd9f1e85cee018665e9c310d88b623"


async def create_file_session():
    code = code_entry.get()
    print("Tên File Session:", code)
    folder_path = "./Data"
    file_path = os.path.join(folder_path, code+".session")

    if os.path.exists(file_path):
        print("Tên đã tồn tại. Vui lòng nhập tên khác.")
        return

    app = Client("./Data/" + code, api_id=api_id, api_hash=api_hash)
    await app.start()
    info = await app.get_me()
    print(info.id)
    await app.stop()


def handle_create_session():
    asyncio.run(create_file_session())


def get_file_names(directory):
    file_names = []
    for filename in os.listdir(directory):
        if os.path.isfile(os.path.join(directory, filename)):
            file_names.append(filename)
    return file_names


root = tk.Tk()
root.title("Tạo File Session")
window_width = 400
window_height = 300
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
x = (screen_width - window_width) // 2
y = (screen_height - window_height) // 2
root.geometry(f"{window_width}x{window_height}+{x}+{y}")

code_label = tk.Label(
    root, text="Nhập tên file (Không dấu không kí tự đặc biệt):")
code_label.pack()

code_entry = tk.Entry(root)
code_entry.pack()

submit_button = tk.Button(root, text="Create Session",
                          command=handle_create_session)
submit_button.pack()

root.mainloop()
