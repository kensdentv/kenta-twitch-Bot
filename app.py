from dotenv import load_dotenv
load_dotenv()

import asyncio


import modules.obs_manager
# import modules.vrc_osc_manager
import modules.notif_manager as notif
import modules.twitch_manager as twitch
import modules.spotify_manager as spotify

async def __init__():
    print('Starting Twitch manager...')
    task1 = asyncio.create_task( twitch.main() )
    task2 = asyncio.create_task( notif.main() )

    await asyncio.gather(task1, task2)

    try: await asyncio.Event().wait()  # This will keep the program running
    except KeyboardInterrupt: print("Script interrupted by user.")
    finally: print("Cleaning up before shutdown...")


try: asyncio.run(__init__())
except KeyboardInterrupt: print("Program terminated.")






