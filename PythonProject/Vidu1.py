import asyncio
import websockets

connected_users = set()
async def handle_connection(websocket):

    connected_users.add(websocket)
    print("Da ket noi")

    try:
        async for message in websocket:
            print(f"Tin nhan: {message}")

            for user in connected_users:
                if user != websocket:
                    await user.send(message)
    except websockets.ConnectionClosed:
        print("mat ket noi")
    finally:
        connected_users.remove(websocket)

async def main():
    async with websockets.serve(handle_connection, "localhost", 8765):
        print("May chu dang chay ws://localhost:8765")
        await asyncio.Future()

asyncio.run(main())