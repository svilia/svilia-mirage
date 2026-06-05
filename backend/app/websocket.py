from fastapi import APIRouter, WebSocket, WebSocketDisconnect
import json

router = APIRouter()

active_connections = []

@router.websocket("/live")
async def websocket_endpoint(websocket: WebSocket):
    await websocket.accept()
    active_connections.append(websocket)
    try:
        while True:
            data = await websocket.receive_text()
            # Broadcast to all
            for connection in active_connections:
                await connection.send_text(f"Live update: {data}")
    except WebSocketDisconnect:
        active_connections.remove(websocket)
