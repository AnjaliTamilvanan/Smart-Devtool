def is_valid_endpoint(endpoint):
    if not endpoint:
        return False

    endpoint = endpoint.lower()

    if " " in endpoint and not endpoint.startswith("/"):
        return False

    return endpoint.startswith("/") or endpoint.startswith("http")


def choose_best_endpoint(endpoints, use_case):
    if not endpoints:
        return ""

    use_case = (use_case or "").lower()

    for ep in endpoints:
        url = ep.get("url", "")
        desc = ep.get("description", "").lower()

        if not is_valid_endpoint(url):
            continue

        if use_case and (use_case in url.lower() or use_case in desc):
            return url

    for ep in endpoints:
        url = ep.get("url", "")
        if is_valid_endpoint(url):
            return url

    return ""


def replace_path_params(endpoint):
    replacements = {
        "{id}": "1",
        "{name}": "india",
        "{code}": "IN",
        "{region}": "asia",
    }

    for key, value in replacements.items():
        endpoint = endpoint.replace(key, value)

    return endpoint


def build_full_url(endpoint, base_url):
    if endpoint.startswith("http"):
        return endpoint

    if not base_url:
        return ""

    return base_url.rstrip("/") + endpoint


# 🔥 DEMO SAFE OVERRIDES (VERY IMPORTANT)
def apply_demo_overrides(base_url, use_case):
    base_url = base_url.lower()
    use_case = (use_case or "").lower()

    # 1. JSONPlaceholder
    if "jsonplaceholder.typicode.com" in base_url:
        if "todo" in use_case:
            return "/todos/1"
        return "/posts/1"

    # 2. GitHub API
    if "api.github.com" in base_url:
        if "repo" in use_case:
            return "/users/octocat/repos"
        return "/users/octocat"

    # 3. OpenWeather
    if "api.openweathermap.org" in base_url:
        return "/data/2.5/weather?q=London"

    # 4. CatFact
    if "catfact.ninja" in base_url:
        return "/fact"

    return None


def generate_code(structured_data, language, base_url=""):
    endpoints = structured_data.get("endpoints", [])
    authentication = structured_data.get("authentication", "")
    use_case = structured_data.get("use_case", "")

    # 🔥 APPLY DEMO OVERRIDE FIRST
    override_endpoint = apply_demo_overrides(base_url, use_case)

    if override_endpoint:
        endpoint = override_endpoint
    else:
        endpoint = choose_best_endpoint(endpoints, use_case)

    if not endpoint:
        return {
            "code": "⚠️ Unable to generate code: No valid endpoint found.",
            "sample_url": ""
        }

    endpoint = replace_path_params(endpoint)

    full_url = build_full_url(endpoint, base_url)

    if not full_url:
        return {
            "code": "⚠️ Unable to construct valid API URL.",
            "sample_url": ""
        }

    # 🔥 Authentication note only (no API key injection)
    auth_note = ""
    if "openweathermap" in base_url:
        auth_note = "# Note: This API requires authentication (API key needed)\n"
    elif authentication and authentication.lower() not in ["none", "no auth", ""]:
        auth_note = "# Note: This API requires authentication\n"

    code = f"""{auth_note}import requests

def call_api():
    url = "{full_url}"
    response = requests.get(url)

    if response.status_code == 200:
        return response.json()
    else:
        return {{
            "error": response.status_code,
            "message": response.text
        }}

print(call_api())
"""

    return {
        "code": code,
        "sample_url": full_url
    }