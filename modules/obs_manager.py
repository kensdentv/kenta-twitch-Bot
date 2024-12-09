from obswebsocket import obsws, requests
import time

print('starting OBS')

host = "localhost"
port = 4455

ws = obsws(host, port)
ws.connect()

def flash_item(source_name, duration: int = 3):

    scene_name = "Layer - VTuber"

    # Get scene items
    scene_item_list = ws.call(requests.GetSceneItemList(**{"sceneName": scene_name}))
    scene_items = scene_item_list.getSceneItems()

    # Look For Item
    selected_item = None
    for item in scene_items:
        if not item["sourceName"] == source_name: continue
        selected_item = item
    
    # Toggle Item On
    if selected_item is None: return
    ws.call(requests.SetSceneItemEnabled(**{"sceneName": scene_name, "sceneItemId": selected_item["sceneItemId"], "sceneItemEnabled": True}))
    time.sleep(duration)
    ws.call(requests.SetSceneItemEnabled(**{"sceneName": scene_name, "sceneItemId": selected_item["sceneItemId"], "sceneItemEnabled": False}))

def activate_filter(filter_name: str, source_name: str, state: bool):
    # Toggle Item On
    ws.call(requests.SetSourceFilterEnabled(**{"sourceName": source_name, "filterName": filter_name, "filterEnabled": state}))
