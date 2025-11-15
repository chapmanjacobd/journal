import asyncio
import qbittorrentapi

qbt_client = qbittorrentapi.Client()

async def fetch_qbt_info():
    return await asyncio.to_thread(qbt_client.app_build_info)

print(asyncio.run(fetch_qbt_info()))
