"""
Skywork AI Image Generator — IGEN VERITAS
Calls the Skywork Image API and saves the result to social-media/
Usage:
  python skywork_generate.py --prompt "..." --filename "social-media/CB-024_pain.png"
  python skywork_generate.py --prompt "..." --filename "social-media/CB-025_edu.png" --aspect-ratio 1:1 --resolution 2K
"""

import os
import sys
import json
import argparse
import requests

SKYWORK_GATEWAY_URL = os.environ.get(
    "SKYWORK_GATEWAY_URL", "https://api-tools.skywork.ai/theme-gateway"
)


def get_api_key():
    key = os.environ.get("SKYWORK_API_KEY", "")
    if not key:
        print("ERROR: SKYWORK_API_KEY environment variable is not set.")
        print("Add it to .claude/settings.local.json under 'env'.")
        sys.exit(1)
    return key


def generate_image(prompt: str, filename: str, aspect_ratio: str = "1:1", resolution: str = "2K"):
    api_key = get_api_key()

    headers = {
        "Authorization": f"Bearer {api_key}",
        "Content-Type": "application/json",
        "Accept": "text/event-stream",
    }

    payload = {
        "title": prompt[:60],
        "content": prompt,
        "style": {"aspect_ratio": aspect_ratio},
        "options": {"resolution": resolution},
        "source_platform": "claude-code",
    }

    url = f"{SKYWORK_GATEWAY_URL}/api/sse/image/create"

    print(f"\nSkywork Image Generation")
    print(f"Prompt : {prompt[:100]}...")
    print(f"Output : {filename}")
    print(f"Format : {aspect_ratio} @ {resolution}")
    print(f"Calling API — this takes ~2 minutes, please wait...\n")

    file_url = None

    try:
        with requests.post(url, headers=headers, json=payload, stream=True, timeout=300) as resp:
            resp.raise_for_status()

            for raw_line in resp.iter_lines():
                if not raw_line:
                    continue

                line = raw_line.decode("utf-8") if isinstance(raw_line, bytes) else raw_line

                if not line.startswith("data:"):
                    continue

                data_str = line[5:].strip()

                if data_str == "[DONE]":
                    break

                try:
                    data = json.loads(data_str)
                    event = data.get("event", "")

                    if event == "progress":
                        pct = data.get("data", {}).get("percent", 0)
                        msg = data.get("data", {}).get("message", "processing")
                        bar = "#" * int(pct / 5) + "-" * (20 - int(pct / 5))
                        print(f"\r  [{bar}] {pct}%  {msg}", end="", flush=True)

                    elif event == "success":
                        file_url = data.get("data", {}).get("file_url")
                        print(f"\n  Done.")
                        break

                    elif event == "error":
                        print(f"\nERROR from Skywork: {data}")
                        sys.exit(1)

                except json.JSONDecodeError:
                    pass

    except requests.exceptions.Timeout:
        print("\nERROR: Request timed out after 5 minutes.")
        sys.exit(1)
    except requests.exceptions.HTTPError as e:
        print(f"\nERROR: HTTP {e.response.status_code} — {e.response.text[:200]}")
        sys.exit(1)

    if not file_url:
        print("\nERROR: No file_url in API response.")
        sys.exit(1)

    # Download image
    print(f"\nDownloading image...")
    try:
        img_resp = requests.get(file_url, timeout=120)
        img_resp.raise_for_status()
    except Exception as e:
        print(f"ERROR downloading image: {e}")
        sys.exit(1)

    # Save to disk
    out_dir = os.path.dirname(filename)
    if out_dir:
        os.makedirs(out_dir, exist_ok=True)

    with open(filename, "wb") as f:
        f.write(img_resp.content)

    size_kb = round(len(img_resp.content) / 1024, 1)
    print(f"Saved  : {filename} ({size_kb} KB)")
    return filename


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Generate image via Skywork AI")
    parser.add_argument("--prompt", required=True, help="Detailed image generation prompt")
    parser.add_argument("--filename", required=True, help="Output path e.g. social-media/CB-024_pain.png")
    parser.add_argument(
        "--aspect-ratio",
        default="1:1",
        choices=["1:1", "3:4", "4:3", "16:9", "9:16"],
        help="Aspect ratio (default: 1:1 for Instagram feed)",
    )
    parser.add_argument(
        "--resolution",
        default="2K",
        choices=["1K", "2K", "4K"],
        help="Output resolution (default: 2K)",
    )
    args = parser.parse_args()

    generate_image(args.prompt, args.filename, args.aspect_ratio, args.resolution)
