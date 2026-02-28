<<<<<<< Updated upstream
\"\"\"\nConstants for LMArenaBridge.\nAll hardcoded values should be defined here.\n\"\"\"\n\nimport os\n\n# ============================================================\n# APPLICATION CONFIGURATION\n# ============================================================\n\n# Set to True for detailed logging, False for minimal logging\nDEBUG = True\n\n# Port to run the server on\nPORT = int(os.environ.get("PORT", 7860))\n\n# Default config and models file paths\nCONFIG_FILE = "config.json"\nMODELS_FILE = "models.json"\n\n# ============================================================\n# HTTP STATUS CODES\n# ============================================================\n\nclass HTTPStatus:\n    \"\"\"HTTP Status Codes\"\"\"\n    # 1xx Informational\n    CONTINUE = 100\n    SWITCHING_PROTOCOLS = 101\n    PROCESSING = 102\n    EARLY_HINTS = 103\n    \n    # 2xx Success\n    OK = 200\n    CREATED = 201\n    ACCEPTED = 202\n    NON_AUTHORITATIVE_INFORMATION = 203\n    NO_CONTENT = 204\n    RESET_CONTENT = 205\n    PARTIAL_CONTENT = 206\n    MULTI_STATUS = 207\n    \n    # 3xx Redirection\n    MULTIPLE_CHOICES = 300\n    MOVED_PERMANENTLY = 301\n    MOVED_TEMPORARILY = 302\n    SEE_OTHER = 303\n    NOT_MODIFIED = 304\n    USE_PROXY = 305\n    TEMPORARY_REDIRECT = 307\n    PERMANENT_REDIRECT = 308\n    \n    # 4xx Client Errors\n    BAD_REQUEST = 400\n    UNAUTHORIZED = 401\n    PAYMENT_REQUIRED = 402\n    FORBIDDEN = 403\n    NOT_FOUND = 404\n    METHOD_NOT_ALLOWED = 405\n    NOT_ACCEPTABLE = 406\n    PROXY_AUTHENTICATION_REQUIRED = 407\n    REQUEST_TIMEOUT = 408\n    CONFLICT = 409\n    GONE = 410\n    LENGTH_REQUIRED = 411\n    PRECONDITION_FAILED = 412\n    REQUEST_TOO_LONG = 413\n    REQUEST_URI_TOO_LONG = 414\n    UNSUPPORTED_MEDIA_TYPE = 415\n    REQUESTED_RANGE_NOT_SATISFIABLE = 416\n    EXPECTATION_FAILED = 417\n    IM_A_TEAPOT = 418\n    INSUFFICIENT_SPACE_ON_RESOURCE = 419\n    METHOD_FAILURE = 420\n    MISDIRECTED_REQUEST = 421\n    UNPROCESSABLE_ENTITY = 422\n    LOCKED = 423\n    FAILED_DEPENDENCY = 424\n    UPGRADE_REQUIRED = 426\n    PRECONDITION_REQUIRED = 428\n    TOO_MANY_REQUESTS = 429\n    REQUEST_HEADER_FIELDS_TOO_LARGE = 431\n    UNAVAILABLE_FOR_LEGAL_REASONS = 451\n    \n    # 5xx Server Errors\n    INTERNAL_SERVER_ERROR = 500\n    NOT_IMPLEMENTED = 501\n    BAD_GATEWAY = 502\n    SERVICE_UNAVAILABLE = 503\n    GATEWAY_TIMEOUT = 504\n    HTTP_VERSION_NOT_SUPPORTED = 505\n    INSUFFICIENT_STORAGE = 507\n    NETWORK_AUTHENTICATION_REQUIRED = 511\n\n\n# Status code descriptions for logging\nSTATUS_MESSAGES = {\n    100: \"Continue\",\n    101: \"Switching Protocols\",\n    102: \"Processing\",\n    103: \"Early Hints\",\n    200: \"OK - Success\",\n    201: \"Created\",\n    202: \"Accepted\",\n    203: \"Non-Authoritative Information\",\n    204: \"No Content\",\n    205: \"Reset Content\",\n    206: \"Partial Content\",\n    207: \"Multi-Status\",\n    300: \"Multiple Choices\",\n    301: \"Moved Permanently\",\n    302: \"Moved Temporarily\",\n    303: \"See Other\",\n    304: \"Not Modified\",\n    305: \"Use Proxy\",\n    307: \"Temporary Redirect\",\n    308: \"Permanent Redirect\",\n    400: \"Bad Request - Invalid request syntax\",\n    401: \"Unauthorized - Invalid or expired token\",\n    402: \"Payment Required\",\n    403: \"Forbidden - Access denied\",\n    404: \"Not Found - Resource doesn't exist\",\n    405: \"Method Not Allowed\",\n    406: \"Not Acceptable\",\n    407: \"Proxy Authentication Required\",\n    408: \"Request Timeout\",\n    409: \"Conflict\",\n    410: \"Gone - Resource permanently deleted\",\n    411: \"Length Required\",\n    412: \"Precondition Failed\",\n    413: \"Request Too Long - Payload too large\",\n    414: \"Request URI Too Long\",\n    415: \"Unsupported Media Type\",\n    416: \"Requested Range Not Satisfiable\",\n    417: \"Expectation Failed\",\n    418: \"I'm a Teapot\",\n    419: \"Insufficient Space on Resource\",\n    420: \"Method Failure\",\n    421: \"Misdirected Request\",\n    422: \"Unprocessable Entity\",\n    423: \"Locked\",\n    424: \"Failed Dependency\",\n    426: \"Upgrade Required\",\n    428: \"Precondition Required\",\n    429: \"Too Many Requests - Rate limit exceeded\",\n    431: \"Request Header Fields Too Large\",\n    451: \"Unavailable For Legal Reasons\",\n    500: \"Internal Server Error\",\n    501: \"Not Implemented\",\n    502: \"Bad Gateway\",\n    503: \"Service Unavailable\",\n    504: \"Gateway Timeout\",\n    505: \"HTTP Version Not Supported\",\n    507: \"Insufficient Storage\",\n    511: \"Network Authentication Required\"\n}\n\n# ============================================================\n# RECAPTCHA CONSTANTS\n# ============================================================\n\n# Default reCAPTCHA sitekey and action from gpt4free/g4f/Provider/needs_auth/LMArena.py\nRECAPTCHA_SITEKEY = \"6Led_uYrAAAAAKjxDIF58fgFtX3t8loNAK85bW9I\"\nRECAPTCHA_ACTION = \"chat_submit\"\n\n# reCAPTCHA Enterprise v2 sitekey used when v3 scoring fails and LMArena prompts a checkbox challenge\nRECAPTCHA_V2_SITEKEY = \"6Ld7ePYrAAAAAB34ovoFoDau1fqCJ6IyOjFEQaMn\"\n\n# Cloudflare Turnstile sitekey used by LMArena to mint anonymous-user signup tokens\nTURNSTILE_SITEKEY = \"0x4AAAAAAA65vWDmG-O_lPtT\"\n\n# ============================================================\n# ARENA ORIGINS\n# ============================================================\n\nLMARENA_ORIGIN = \"https://lmarena.ai\"\nARENA_ORIGIN = \"https://arena.ai\"\n\nARENA_HOST_TO_ORIGIN = {\n    \"lmarena.ai\": LMARENA_ORIGIN,\n    \"www.lmarena.ai\": LMARENA_ORIGIN,\n    \"arena.ai\": ARENA_ORIGIN,\n    \"www.arena.ai\": ARENA_ORIGIN,\n}\n\n# ============================================================\n# BROWSER FETCH MODELS\n# ============================================================\n\n# Models that should always use the in-browser (Chrome fetch) transport for streaming\nSTRICT_CHROME_FETCH_MODELS = {\n    \"gemini-3-pro-grounding\",\n    \"gemini-exp-1206\",\n}\n\n# ============================================================\n# TIMEOUTS AND LIMITS\n# ============================================================\n\n# Default timeout for requests (seconds)\nDEFAULT_REQUEST_TIMEOUT = 120\n\n# reCAPTCHA timeout settings (milliseconds)\nGRECAPTCHA_TIMEOUT_MS = 60000\nGRECAPTCHA_POLL_MS = 250\n\n# Token expiry margins (seconds)\nTOKEN_EXPIRY_SKEW_SECONDS = 30\nRECAPTCHA_TOKEN_EXPIRY_SECONDS = 110\nRECAPTCHA_V3_TOKEN_LIFETIME_SECONDS = 120\n\n# Background refresh interval (seconds)\nPERIODIC_REFRESH_INTERVAL_SECONDS = 1800  # 30 minutes\n\n# Rate limiting\nRATE_LIMIT_WINDOW_SECONDS = 60\nDEFAULT_RATE_LIMIT_RPM = 60\n\n# ============================================================\n# USERSCRIPT PROXY SETTINGS\n# ============================================================\n\nDEFAULT_USERSCRIPT_PROXY_POLL_TIMEOUT_SECONDS = 25\nDEFAULT_USERSCRIPT_PROXY_JOB_TTL_SECONDS = 90\nUSERSCRIPT_PROXY_ACTIVE_WINDOW_BUFFER_SECONDS = 10\nUSERSCRIPT_PROXY_JOB_TTL_MAX_SECONDS = 600\n\n# ============================================================\n# BACKOFF SETTINGS\n# ============================================================\n\n# Exponential backoff for rate limit responses (429)\ndef get_rate_limit_backoff_seconds(retry_after: str | None, attempt: int) -> int:\n    \"\"\"Compute backoff seconds for upstream 429 responses.\"\"\"\n    if retry_after:\n        try:\n            value = int(float(retry_after.strip()))\n        except Exception:\n            value = 0\n        if value > 0:\n            return min(value, 3600)\n    \n    attempt = max(0, int(attempt))\n    return min(5 * (2 ** attempt), 300)\n\n\ndef get_general_backoff_seconds(attempt: int) -> int:\n    \"\"\"Compute general exponential backoff seconds.\"\"\"\n    attempt = max(0, int(attempt))\n    return min(2 * (2 ** attempt), 30)\n\n# ============================================================\n# BROWSER SETTINGS\n# ============================================================\n\n# Default browser window modes\nDEFAULT_CAMOUFOX_PROXY_WINDOW_MODE = \"hide\"\nDEFAULT_CAMOUFOX_FETCH_WINDOW_MODE = \"hide\"\nDEFAULT_CHROME_FETCH_WINDOW_MODE = \"hide\"\n\n# Window mode valid values\nVALID_WINDOW_MODES = {\"hide\", \"hidden\", \"minimize\", \"minimized\", \"offscreen\", \"off-screen\", \"moveoffscreen\", \"move-offscreen\", \"visible\"}\n\n# Chrome/Edge executable paths (Windows)\nCHROME_PATH_CANDIDATES = [\n    r\"C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe\",\n    r\"C:\\Program Files (x86)\\Google\\Chrome\\Application\\chrome.exe\",\n]\nEDGE_PATH_CANDIDATES = [\n    r\"C:\\Program Files\\Microsoft\\Edge\\Application\\msedge.exe\",\n    r\"C:\\Program Files (x86)\\Microsoft\\Edge\\Application\\msedge.exe\",\n]\n\n# Browser user agent\nDEFAULT_USER_AGENT = (\n    \"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) \"\n    \"Chrome/120.0.0.0 Safari/537.36\"\n)\n\n# ============================================================\n# IMAGE UPLOAD SETTINGS\n# ============================================================\n\nMAX_IMAGE_SIZE_BYTES = 10 * 1024 * 1024  # 10MB\n\n# Supported MIME types for image upload\nSUPPORTED_IMAGE_MIME_TYPES = {\n    \"image/png\",\n    \"image/jpeg\",\n    \"image/gif\",\n    \"image/webp\",\n    \"image/svg+xml\",\n}\n\n# ============================================================\n# CLOUDFLARE COOKIE NAMES\n# ============================================================\n\nCF_CLEARANCE_COOKIE = \"cf_clearance\"\nCF_BM_COOKIE = \"__cf_bm\"\nCF_UVID_COOKIE = \"_cfuvid\"\nPROVISIONAL_USER_ID_COOKIE = \"provisional_user_id\"\nARENA_AUTH_COOKIE = \"arena-auth-prod-v1\"\nGRECAPTCHA_COOKIE = \"_GRECAPTCHA\"\n\n# Cookie domains\nARENA_COOKIE_DOMAINS = (\".lmarena.ai\", \".arena.ai\")\n\n# ============================================================\n# API ENDPOINTS\n# ============================================================\n\nARENA_DIRECT_MODE_URL = \"https://lmarena.ai/?mode=direct\"\nNEXTJS_API_SIGNUP = \"/nextjs-api/sign-up\"\n\n# ============================================================\n# CONTENT TYPES\n# ============================================================\n\nCONTENT_TYPE_TEXT_PLAIN_UTF8 = \"text/plain;charset=UTF-8\"\nCONTENT_TYPE_APPLICATION_JSON = \"application/json\"\n\n# ============================================================\n# TURNSTILE SELECTORS\n# ============================================================\n\nTURNSTILE_SELECTORS = [\n    '#lm-bridge-turnstile',\n    '#lm-bridge-turnstile iframe',\n    '#cf-turnstile', \n    'iframe[src*=\"challenges.cloudflare.com\"]',\n    '[style*=\"display: grid\"] iframe'\n]\n\nTURNSTILE_INNER_SELECTORS = [\n    \"input[type='checkbox']\",\n    \"div[role='checkbox']\",\n    \"label\",\n]\n\n# ============================================================\n# HTTP HEADERS\n# ============================================================\n\nARENA_ORIGIN_HEADER = \"https://lmarena.ai\"\nARENA_REFERER_HEADER = \"https://lmarena.ai/?mode=direct\"\n\n# ============================================================\n# SUPABASE\n# ============================================================\n\n# Regex pattern for finding Supabase JWT\nSUPABASE_JWT_PATTERN = r\"eyJ[a-zA-Z0-9_-]+\\.[a-zA-Z0-9_-]+\\.[a-zA-Z0-9_-]+\"\n\n# ============================================================\n# TURNSTILE / CLOUDFLARE\n# ============================================================\n\nCLOUDFLARE_CHALLENGE_TITLE = \"Just a moment\"\n
=======
"""
Constants for LMArenaBridge.
All hardcoded values should be defined here.
"""

import os

# ============================================================
# APPLICATION CONFIGURATION
# ============================================================

# Set to True for detailed logging, False for minimal logging
DEBUG = True

# Port to run the server on
PORT = int(os.environ.get("PORT", 7860))

# Default config and models file paths
CONFIG_FILE = "config.json"
MODELS_FILE = "models.json"

# ============================================================
# HTTP STATUS CODES
# ============================================================

class HTTPStatus:
    """HTTP Status Codes"""
    # 1xx Informational
    CONTINUE = 100
    SWITCHING_PROTOCOLS = 101
    PROCESSING = 102
    EARLY_HINTS = 103
    
    # 2xx Success
    OK = 200
    CREATED = 201
    ACCEPTED = 202
    NON_AUTHORITATIVE_INFORMATION = 203
    NO_CONTENT = 204
    RESET_CONTENT = 205
    PARTIAL_CONTENT = 206
    MULTI_STATUS = 207
    
    # 3xx Redirection
    MULTIPLE_CHOICES = 300
    MOVED_PERMANENTLY = 301
    MOVED_TEMPORARILY = 302
    SEE_OTHER = 303
    NOT_MODIFIED = 304
    USE_PROXY = 305
    TEMPORARY_REDIRECT = 307
    PERMANENT_REDIRECT = 308
    
    # 4xx Client Errors
    BAD_REQUEST = 400
    UNAUTHORIZED = 401
    PAYMENT_REQUIRED = 402
    FORBIDDEN = 403
    NOT_FOUND = 404
    METHOD_NOT_ALLOWED = 405
    NOT_ACCEPTABLE = 406
    PROXY_AUTHENTICATION_REQUIRED = 407
    REQUEST_TIMEOUT = 408
    CONFLICT = 409
    GONE = 410
    LENGTH_REQUIRED = 411
    PRECONDITION_FAILED = 412
    REQUEST_TOO_LONG = 413
    REQUEST_URI_TOO_LONG = 414
    UNSUPPORTED_MEDIA_TYPE = 415
    REQUESTED_RANGE_NOT_SATISFIABLE = 416
    EXPECTATION_FAILED = 417
    IM_A_TEAPOT = 418
    INSUFFICIENT_SPACE_ON_RESOURCE = 419
    METHOD_FAILURE = 420
    MISDIRECTED_REQUEST = 421
    UNPROCESSABLE_ENTITY = 422
    LOCKED = 423
    FAILED_DEPENDENCY = 424
    UPGRADE_REQUIRED = 426
    PRECONDITION_REQUIRED = 428
    TOO_MANY_REQUESTS = 429
    REQUEST_HEADER_FIELDS_TOO_LARGE = 431
    UNAVAILABLE_FOR_LEGAL_REASONS = 451
    
    # 5xx Server Errors
    INTERNAL_SERVER_ERROR = 500
    NOT_IMPLEMENTED = 501
    BAD_GATEWAY = 502
    SERVICE_UNAVAILABLE = 503
    GATEWAY_TIMEOUT = 504
    HTTP_VERSION_NOT_SUPPORTED = 505
    INSUFFICIENT_STORAGE = 507
    NETWORK_AUTHENTICATION_REQUIRED = 511


# Status code descriptions for logging
STATUS_MESSAGES = {
    100: "Continue",
    101: "Switching Protocols",
    102: "Processing",
    103: "Early Hints",
    200: "OK - Success",
    201: "Created",
    202: "Accepted",
    203: "Non-Authoritative Information",
    204: "No Content",
    205: "Reset Content",
    206: "Partial Content",
    207: "Multi-Status",
    300: "Multiple Choices",
    301: "Moved Permanently",
    302: "Moved Temporarily",
    303: "See Other",
    304: "Not Modified",
    305: "Use Proxy",
    307: "Temporary Redirect",
    308: "Permanent Redirect",
    400: "Bad Request - Invalid request syntax",
    401: "Unauthorized - Invalid or expired token",
    402: "Payment Required",
    403: "Forbidden - Access denied",
    404: "Not Found - Resource doesn't exist",
    405: "Method Not Allowed",
    406: "Not Acceptable",
    407: "Proxy Authentication Required",
    408: "Request Timeout",
    409: "Conflict",
    410: "Gone - Resource permanently deleted",
    411: "Length Required",
    412: "Precondition Failed",
    413: "Request Too Long - Payload too large",
    414: "Request URI Too Long",
    415: "Unsupported Media Type",
    416: "Requested Range Not Satisfiable",
    417: "Expectation Failed",
    418: "I'm a Teapot",
    419: "Insufficient Space on Resource",
    420: "Method Failure",
    421: "Misdirected Request",
    422: "Unprocessable Entity",
    423: "Locked",
    424: "Failed Dependency",
    426: "Upgrade Required",
    428: "Precondition Required",
    429: "Too Many Requests - Rate limit exceeded",
    431: "Request Header Fields Too Large",
    451: "Unavailable For Legal Reasons",
    500: "Internal Server Error",
    501: "Not Implemented",
    502: "Bad Gateway",
    503: "Service Unavailable",
    504: "Gateway Timeout",
    505: "HTTP Version Not Supported",
    507: "Insufficient Storage",
    511: "Network Authentication Required"
}

# ============================================================
# RECAPTCHA CONSTANTS
# ============================================================

# Default reCAPTCHA sitekey and action from gpt4free/g4f/Provider/needs_auth/LMArena.py
RECAPTCHA_SITEKEY = "6Led_uYrAAAAAKjxDIF58fgFtX3t8loNAK85bW9I"
RECAPTCHA_ACTION = "chat_submit"

# reCAPTCHA Enterprise v2 sitekey used when v3 scoring fails and LMArena prompts a checkbox challenge
RECAPTCHA_V2_SITEKEY = "6Ld7ePYrAAAAAB34ovoFoDau1fqCJ6IyOjFEQaMn"

# Cloudflare Turnstile sitekey used by LMArena to mint anonymous-user signup tokens
TURNSTILE_SITEKEY = "0x4AAAAAAA65vWDmG-O_lPtT"

# ============================================================
# ARENA ORIGINS
# ============================================================

LMARENA_ORIGIN = "https://lmarena.ai"
ARENA_ORIGIN = "https://arena.ai"

ARENA_HOST_TO_ORIGIN = {
    "lmarena.ai": LMARENA_ORIGIN,
    "www.lmarena.ai": LMARENA_ORIGIN,
    "arena.ai": ARENA_ORIGIN,
    "www.arena.ai": ARENA_ORIGIN,
}

# ============================================================
# BROWSER FETCH MODELS
# ============================================================

# Models that should always use the in-browser (Chrome fetch) transport for streaming
STRICT_CHROME_FETCH_MODELS = {
    "gemini-3-pro-grounding",
    "gemini-exp-1206",
}

# ============================================================
# TIMEOUTS AND LIMITS
# ============================================================

# Default timeout for requests (seconds)
DEFAULT_REQUEST_TIMEOUT = 120

# reCAPTCHA timeout settings (milliseconds)
GRECAPTCHA_TIMEOUT_MS = 60000
GRECAPTCHA_POLL_MS = 250

# Token expiry margins (seconds)
TOKEN_EXPIRY_SKEW_SECONDS = 30
RECAPTCHA_TOKEN_EXPIRY_SECONDS = 110
RECAPTCHA_V3_TOKEN_LIFETIME_SECONDS = 120

# Background refresh interval (seconds)
PERIODIC_REFRESH_INTERVAL_SECONDS = 1800  # 30 minutes

# Rate limiting
RATE_LIMIT_WINDOW_SECONDS = 60
DEFAULT_RATE_LIMIT_RPM = 60

# ============================================================
# USERSCRIPT PROXY SETTINGS
# ============================================================

DEFAULT_USERSCRIPT_PROXY_POLL_TIMEOUT_SECONDS = 25
DEFAULT_USERSCRIPT_PROXY_JOB_TTL_SECONDS = 90
USERSCRIPT_PROXY_ACTIVE_WINDOW_BUFFER_SECONDS = 10
USERSCRIPT_PROXY_JOB_TTL_MAX_SECONDS = 600

# ============================================================
# BACKOFF SETTINGS
# ============================================================

# Exponential backoff for rate limit responses (429)
def get_rate_limit_backoff_seconds(retry_after: str | None, attempt: int) -> int:
    """Compute backoff seconds for upstream 429 responses."""
    if retry_after:
        try:
            value = int(float(retry_after.strip()))
        except Exception:
            value = 0
        if value > 0:
            return min(value, 3600)
    
    attempt = max(0, int(attempt))
    return min(5 * (2 ** attempt), 300)


def get_general_backoff_seconds(attempt: int) -> int:
    """Compute general exponential backoff seconds."""
    attempt = max(0, int(attempt))
    return min(2 * (2 ** attempt), 30)

# ============================================================
# BROWSER SETTINGS
# ============================================================

# Default browser window modes
DEFAULT_CAMOUFOX_PROXY_WINDOW_MODE = "hide"
DEFAULT_CAMOUFOX_FETCH_WINDOW_MODE = "hide"
DEFAULT_CHROME_FETCH_WINDOW_MODE = "hide"

# Window mode valid values
VALID_WINDOW_MODES = {"hide", "hidden", "minimize", "minimized", "offscreen", "off-screen", "moveoffscreen", "move-offscreen", "visible"}

# Chrome/Edge executable paths (Windows)
CHROME_PATH_CANDIDATES = [
    r"C:\Program Files\Google\Chrome\Application\chrome.exe",
    r"C:\Program Files (x86)\Google\Chrome\Application\chrome.exe",
]
EDGE_PATH_CANDIDATES = [
    r"C:\Program Files\Microsoft\Edge\Application\msedge.exe",
    r"C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe",
]

# Browser user agent
DEFAULT_USER_AGENT = (
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) "
    "Chrome/120.0.0.0 Safari/537.36"
)

# ============================================================
# IMAGE UPLOAD SETTINGS
# ============================================================

MAX_IMAGE_SIZE_BYTES = 10 * 1024 * 1024  # 10MB

# Supported MIME types for image upload
SUPPORTED_IMAGE_MIME_TYPES = {
    "image/png",
    "image/jpeg",
    "image/gif",
    "image/webp",
    "image/svg+xml",
}

# ============================================================
# CLOUDFLARE COOKIE NAMES
# ============================================================

CF_CLEARANCE_COOKIE = "cf_clearance"
CF_BM_COOKIE = "__cf_bm"
CF_UVID_COOKIE = "_cfuvid"
PROVISIONAL_USER_ID_COOKIE = "provisional_user_id"
ARENA_AUTH_COOKIE = "arena-auth-prod-v1"
GRECAPTCHA_COOKIE = "_GRECAPTCHA"

# Cookie domains
ARENA_COOKIE_DOMAINS = (".lmarena.ai", ".arena.ai")

# ============================================================
# API ENDPOINTS
# ============================================================

ARENA_DIRECT_MODE_URL = "https://lmarena.ai/?mode=direct"
NEXTJS_API_SIGNUP = "/nextjs-api/sign-up"

# ============================================================
# CONTENT TYPES
# ============================================================

CONTENT_TYPE_TEXT_PLAIN_UTF8 = "text/plain;charset=UTF-8"
CONTENT_TYPE_APPLICATION_JSON = "application/json"

# ============================================================
# TURNSTILE SELECTORS
# ============================================================

TURNSTILE_SELECTORS = [
    '#lm-bridge-turnstile',
    '#lm-bridge-turnstile iframe',
    '#cf-turnstile', 
    'iframe[src*="challenges.cloudflare.com"]',
    '[style*="display: grid"] iframe'
]

TURNSTILE_INNER_SELECTORS = [
    "input[type='checkbox']",
    "div[role='checkbox']",
    "label",
]

# ============================================================
# HTTP HEADERS
# ============================================================

ARENA_ORIGIN_HEADER = "https://lmarena.ai"
ARENA_REFERER_HEADER = "https://lmarena.ai/?mode=direct"

# ============================================================
# SUPABASE
# ============================================================

# Regex pattern for finding Supabase JWT
SUPABASE_JWT_PATTERN = r"eyJ[a-zA-Z0-9_-]+\.[a-zA-Z0-9_-]+\.[a-zA-Z0-9_-]+"

# ============================================================
# TURNSTILE / CLOUDFLARE
# ============================================================

CLOUDFLARE_CHALLENGE_TITLE = "Just a moment"
>>>>>>> Stashed changes
