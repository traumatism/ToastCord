import argparse

from toastcord import version

parser = argparse.ArgumentParser()

parser.add_argument(
    "-t", "--token",
    required=True,
    help="Your Discord API token",
    dest="token",
    metavar="<value>"
)

http_options = parser.add_argument_group("HTTP Options")

http_options.add_argument(
    "--user-agent",
    default=f"toastcord/{version}",
    help="User-Agent header",
    dest="user_agent",
    metavar="<value>"
)

api_options = parser.add_argument_group("Discord API options")

api_options.add_argument(
    "--api-backend",
    default="https://canary.discord.com/api/",
    help="Discord API backend to use",
    dest="api_backend",
    metavar="<value>"
)

api_options.add_argument(
    "--api-version",
    default="v9",
    help="Discord API version to use",
    dest="api_version",
    metavar="<value>"
)

arguments = parser.parse_args()
