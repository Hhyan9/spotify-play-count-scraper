thonpython
import requests
import logging

OEMBED_URL = "https://open.spotify.com/oembed"

class AlbumParser:
    def parse(self, url: str) -> dict:
        """Extract album metadata using Spotify oEmbed."""
        try:
            resp = requests.get(OEMBED_URL, params={"url": url}, timeout=10)
            resp.raise_for_status()
            data = resp.json()
        except Exception as e:
            logging.error(f"OEmbed fetch failed for {url}: {e}")
            raise

        return {
            "type": "album",
            "album_url": url,
            "album_name": data.get("title"),
            "thumbnail": data.get("thumbnail_url"),
            "provider": data.get("provider_name"),
            "tracks": [],
        }