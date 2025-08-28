from aiohttp import ClientSession

async def fetch_json(session, url):
    async with session.get(url) as resp:
        resp.raise_for_status()
        return await resp.json()


async def get_asset_url(session: ClientSession, api_url, prerelease=False):
    """
    Get the asset download URL from a GitHub release API endpoint.
    """
    releases = await fetch_json(session, api_url)

    # pick release
    for release in releases:
        if prerelease and release["prerelease"]:
            chosen = release
            break
        if not prerelease and not release["prerelease"]:
            chosen = release
            break
    else:
        return None

    # take first asset
    if not release["assets"]:
        return None
    return release["assets"][0]["browser_download_url"]