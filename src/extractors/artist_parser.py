thonpython
import requests
import logging

OEMBED_URL = "https://open.spotify.com/oembed"

class ArtistParser:
    def parse(self, url: str) -> dict:
        """Extract artist metadata using Spotify oEmbed."""
        try:
            resp = requests.get(OEMBED_URL, params={"url": url}, timeout=10)
            resp.raise_for_status()
            data = resp.json()
        except Exception as e:
            logging.error(f"OEmbed fetch failed for {url}: {e}")
            raise

        return {
            "type": "artist",
            "artist_url": url,
            "artist_name": data.get("title"),
            "thumbnail": data.get("thumbnail_url"),
            "provider": data.get("provider_name"),
            "followers": None,
            "monthlyListeners": None,
            "worldRank": None,
            "topCities": [],
            "albums": [],
            "singles": [],
            "popularReleases": [],
            "biography": None,
            "externalLinks": [],
        }