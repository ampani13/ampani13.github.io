AUTHOR = 'Amiya Pani'
SITENAME = 'Amiya Pani'
SITESUBTITLE = 'Data Engineer & AI Specialist'
SITEURL = ''

PATH = 'content'
TIMEZONE = 'Asia/Kolkata'
DEFAULT_LANG = 'en'

THEME = 'themes/amiya-dark'

FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

DISPLAY_PAGES_ON_MENU = False
DISPLAY_CATEGORIES_ON_MENU = False

MENUITEMS = [
    ('Home', '/'),
    ('About', '/pages/about.html'),
    ('Experience', '/pages/experience.html'),
    ('Skills', '/pages/skills.html'),
    ('Education', '/pages/education.html'),
    ('Blog', '/blog.html'),
    ('Contact', '/pages/contact.html'),
]

SOCIAL = [
    ('linkedin', 'https://www.linkedin.com/in/amiya-pani/'),
    ('github', 'https://github.com/ampani13'),
    ('envelope', 'mailto:contact@amiyapani.com'),
]

DIRECT_TEMPLATES = ['index', 'blog_index']
BLOG_INDEX_SAVE_AS = 'blog.html'
BLOG_INDEX_URL = 'blog.html'

PAGE_URL = 'pages/{slug}.html'
PAGE_SAVE_AS = 'pages/{slug}.html'

ARTICLE_URL = 'blog/{slug}.html'
ARTICLE_SAVE_AS = 'blog/{slug}.html'

DEFAULT_PAGINATION = 5
RELATIVE_URLS = True

STATIC_PATHS = ['images', 'extra']
EXTRA_PATH_METADATA = {'extra/CNAME': {'path': 'CNAME'}}
TEMPLATE_PAGES = {'404.html': '404.html'}
