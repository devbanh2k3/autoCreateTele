from pyrogram import Client

# Create a new Client instance
api_id = 21245336
api_hash = "dcfd9f1e85cee018665e9c310d88b623"


app = Client("./Data/congtien copy", api_id=api_id, api_hash=api_hash)

number = 0


async def main():
    async with app:
        # Send a message, Markdown is enabled by default
        info = await app.get_users("me")
        for i in range(2):
            number = i + 1
            await app.create_group(f"Group Title {number}", info.id)


app.run(main())
