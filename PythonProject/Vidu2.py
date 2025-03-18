import asyncio
import websockets

async def chat():
    uri = "ws://localhost:8765"
    async with websockets.connect(uri) as websocket:
        print("da ket noi")
        while True:
            message = input("Ban: ")
            await websocket.send(message)

            response = await  websocket.recv()
            print(f"Nguoi la: {response}")
asyncio.run(chat())