from __future__ import unicode_literals

from .common import InfoExtractor
from ..utils import int_or_none


_translation_table = {
    'a': 'h', 'd': 'e', 'e': 'v', 'f': 'o', 'g': 'f', 'i': 'd', 'l': 'n',
    'm': 'a', 'n': 'm', 'p': 'u', 'q': 't', 'r': 's', 'v': 'p', 'x': 'r',
    'y': 'l', 'z': 'i',
    '$': ':', '&': '.', '(': '=', '^': '&', '=': '/',
}


def _decode(s):
    return ''.join(_translation_table.get(c, c) for c in s)


class CliphunterIE(InfoExtractor):
    IE_NAME = 'cliphunter'

    _VALID_URL = r'''(?x)http://(?:www\.)?cliphunter\.com/w/
        (?P<id>[0-9]+)/
        (?P<seo>.+?)(?:$|[#\?])
    '''
    _TEST = {
        'url': 'http://www.cliphunter.com/w/1012420/Fun_Jynx_Maze_solo',
        'md5': 'b7c9bbd4eb3a226ab91093714dcaa480',
        'info_dict': {
            'id': '1012420',
            'ext': 'flv',
            'title': 'Fun Jynx Maze solo',
            'thumbnail': 're:^https?://.*\.jpg$',
            'age_limit': 18,
        }
    }

    def _real_extract(self, url):
        video_id = self._match_id(url)
        webpage = self._download_webpage(url, video_id)

        video_title = self._search_regex(
            r'mediaTitle = "([^"]+)"', webpage, 'title')

        gexo_files = self._parse_json(
            self._search_regex(
                r'var\s+gexoFiles\s*=\s*({.+?});', webpage, 'gexo files'),
            video_id)

        formats = []
        for format_id, f in gexo_files.items():
            video_url = f.get('url')
            if not video_url:
                continue
            fmt = f.get('fmt')
            height = f.get('h')
            format_id = '%s_%sp' % (fmt, height) if fmt and height else format_id
            formats.append({
                'url': _decode(video_url),
                'format_id': format_id,
                'width': int_or_none(f.get('w')),
                'height': int_or_none(height),
                'tbr': int_or_none(f.get('br')),
            })
        self._sort_formats(formats)

        thumbnail = self._search_regex(
            r"var\s+mov_thumb\s*=\s*'([^']+)';",
            webpage, 'thumbnail', fatal=False)

        return {
            'id': video_id,
            'title': video_title,
            'formats': formats,
            'age_limit': self._rta_search(webpage),
            'thumbnail': thumbnail,
        }
