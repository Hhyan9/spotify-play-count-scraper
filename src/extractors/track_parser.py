thonpython
import requests
import logging

OEMBED_URL = "https://open.spotify.com/oembed"

class TrackParser:
    def parse(self, url: str) -> dict:
        """Extract track metadata using Spotify oEmbed."""
        try:
            resp = requests.get(OEMBED_URL, params={"url": url}, timeout=10)
            resp.raise_for_status()
            data = resp.json()
        except Exception as e:
            logging.error(f"OEmbed fetch failed for {url}: {e}")
            raise

        return {
            "type": "track",
            "track_url": url,
            "track_name": data.get("title"),
            "thumbnail": data.get("thumbnail_url"),
            "provider": data.get("provider_name"),
            "play_count": None,
            "album_url": None,
            "artist_url": None,
        }