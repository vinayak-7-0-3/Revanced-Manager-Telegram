import os
import asyncio

from aiohttp import ClientSession, ClientError

from .errors import DownloaderError


async def download_file(session: ClientSession, url: str, path: str, retries=3):
    os.makedirs(os.path.dirname(path), exist_ok=True)
    
    for attempt in range(1, retries + 1):
        try:
            async with session.get(url) as response:
                if response.status == 200:
                    with open(path, 'wb') as f:
                        while True:
                            chunk = await response.content.read(1024 * 4)
                            if not chunk:
                                break
                            f.write(chunk)
                    return None
                else:
                    return f"HTTP Status: {response.status}"
        except ClientError as e:
            if attempt == retries:
                raise DownloaderError(f"Connection failed after {retries} attempts: {str(e)}")
            await asyncio.sleep(2 ** attempt)  # Exponential backoff
        except asyncio.TimeoutError:
            if attempt == retries:
                raise DownloaderError("Download failed due to timeout.")
            await asyncio.sleep(2 ** attempt)