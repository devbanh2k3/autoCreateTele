import os
import tkinter as tk
import threading
import asyncio
import time
from pyrogram import Client

api_id = 21245336
api_hash = "dcfd9f1e85cee018665e9c310d88b623"


async def create_file_session():
    number_group = int(number_group_entry.get())
    time_sleep = int(time_sleep_entry.get())
    print("Số group cần tạo:", number_group)
    file_names = get_file_names("./Data")

    # In ra tên các file sử dụng đa luồng
    for file_name in file_names:
        app = Client("./Data/"+file_name.replace(".session", ""),
                     api_id=api_id, api_hash=api_hash)
        number = 0
        print("File Session đang chạy:", file_name)
        await app.start()
        me = await app.get_me()

        for i in range(number_group):
            number = i + 1
            data = await app.create_group(f"Group Create by Tool : {number}", me.id)

            await app.send_message(data.id, "1")
        print("Đang trong thời gian nghỉ...")
        time.sleep(time_sleep)

        await app.stop()
    print("Đã hoàn thành tất cả các account")


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

number_group_label = tk.Label(root, text="Nhập số group cần tạo:")
number_group_label.pack()

number_group_entry = tk.Entry(root)
number_group_entry.pack()

time_sleep_label = tk.Label(root, text="Nhập thời gian nghỉ (giây):")
time_sleep_label.pack()

time_sleep_entry = tk.Entry(root)
time_sleep_entry.pack()

submit_button = tk.Button(root, text="Create Session",
                          command=handle_create_session)
submit_button.pack()

root.mainloop()
