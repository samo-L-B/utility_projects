# utility_projects

Small, standalone Python tools, collected in one repo. Each folder used to be its own repo; its full git history
was kept when it moved here (2026-11-05).

| Folder | Was | What it does | Status |
|---|---|---|---|
| [`art/`](art/) | `project-art-motherfucker` | A 5-minute daily briefing on a great artist or photographer, in the terminal. Standard library only. | in daily use |
| [`musica/`](musica/) | `project-musica` | Rolling Stone's 500 greatest albums and songs as CSV, plus scripts to browse them. | data in daily use |
| [`tts/`](tts/) | `project-tts` | Text to speech in six languages, three ways: inline text, command line, text file. | 2024, dormant |
| [`yt/`](yt/) | `project-yt` | YouTube downloader for a list of links. | 2024, superseded by [yt-dlp](https://github.com/yt-dlp/yt-dlp) |

## Quick start

```bash
python3 art/daily_art.py              # today's artist or photographer
python3 art/daily_art.py --quiz       # guess the artist from the style alone
python3 -m unittest discover -s art/tests
```

To download videos, use yt-dlp (`pacman -S yt-dlp`, `winget install yt-dlp`): `yt-dlp <url>`.
`yt/YT.py` and its link list are kept for reference.

Each folder has its own README with the details.

## Who uses what

These tools also feed two other projects, which read them from this repo's location next to them
(`~/Projects/GitHub/utility_projects`):

- **SELF-Luh** (`l`): the daily art cards from `art/`, and the record of the day from
  `musica/rolling_stone_top_500_records/rolling_stone_top_500_albums_2020.csv`.
- **project-dailydrive**: opens `art/daily_art.py` in the morning routine.

Moving or renaming `art/` or `musica/` breaks both; update their paths at the same time.
