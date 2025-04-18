from obswebsocket import obsws, requests
import time
import winsound


host = "localhost"
port = 4455

print('Starting OBS...')
ws = obsws(host, port)
ws.connect()

def get_scene_item_by_name(scene_name: str, source_name: str):
    # Get scene items
    scene_item_list = ws.call(requests.GetSceneItemList(**{"sceneName": scene_name}))
    scene_items = scene_item_list.getSceneItems()

    # Look For Item
    for item in scene_items:
        if not item["sourceName"] == source_name: continue
        return item

    

def flash_item(scene_name: str, source_name: str, duration: int = 3):

    selected_item = get_scene_item_by_name(scene_name, source_name)

    # Toggle Item On
    if selected_item is None: return
    ws.call(requests.SetSceneItemEnabled(**{"sceneName": scene_name, "sceneItemId": selected_item["sceneItemId"], "sceneItemEnabled": True}))
    time.sleep(duration)
    ws.call(requests.SetSceneItemEnabled(**{"sceneName": scene_name, "sceneItemId": selected_item["sceneItemId"], "sceneItemEnabled": False}))

def activate_filter(filter_name: str, source_name: str, state: bool):
    # Toggle Item On
    ws.call(requests.SetSourceFilterEnabled(**{"sourceName": source_name, "filterName": filter_name, "filterEnabled": state}))

def big_center_screen(scene_name: str):
    vtuber = get_scene_item_by_name(scene_name, "Layer - VTuber")
    vtuber_big = get_scene_item_by_name(scene_name, "BIG")

    ws.call(requests.SetSceneItemEnabled(**{"sceneName": scene_name, "sceneItemId": vtuber["sceneItemId"], "sceneItemEnabled": False}))
    ws.call(requests.SetSceneItemEnabled(**{"sceneName": scene_name, "sceneItemId": vtuber_big["sceneItemId"], "sceneItemEnabled": True}))
    winsound.PlaySound('./assets/sounds/vineboom.wav', winsound.SND_ASYNC)
    time.sleep(1)
    ws.call(requests.SetSceneItemEnabled(**{"sceneName": scene_name, "sceneItemId": vtuber["sceneItemId"], "sceneItemEnabled": True}))
    ws.call(requests.SetSceneItemEnabled(**{"sceneName": scene_name, "sceneItemId": vtuber_big["sceneItemId"], "sceneItemEnabled": False})) 