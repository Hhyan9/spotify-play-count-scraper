thonpython
import json
import logging
import os
from pathlib import Path
from extractors.artist_parser import ArtistParser
from extractors.album_parser import AlbumParser
from extractors.track_parser import TrackParser
from outputs.exporters import Exporter

logging.basicConfig(level=logging.INFO, format='[%(levelname)s] %(message)s')

PARSERS = {
    "artist": ArtistParser(),
    "album": AlbumParser(),
    "track": TrackParser(),
}

def detect_type(url: str) -> str:
    if "/artist/" in url:
        return "artist"
    if "/album/" in url:
        return "album"
    if "/track/" in url:
        return "track"
    raise ValueError(f"Unknown Spotify URL type: {url}")

def main():
    data_dir = Path(__file__).resolve().parent.parent / "data"
    input_file = data_dir / "inputs.sample.txt"

    if not input_file.exists():
        raise FileNotFoundError(f"Missing input file: {input_file}")

    results = []

    with open(input_file, "r") as f:
        urls = [line.strip() for line in f if line.strip()]

    for url in urls:
        try:
            kind = detect_type(url)
            parser = PARSERS[kind]
            logging.info(f"Processing {kind}: {url}")
            result = parser.parse(url)
            results.append(result)
        except Exception as e:
            logging.error(f"Failed to process {url}: {e}")

    output_dir = Path(__file__).resolve().parent.parent / "data"
    json_output = output_dir / "output.json"

    Exporter.export_json(results, json_output)
    logging.info(f"Export complete → {json_output}")

if __name__ == "__main__":
    main()