from src.parser_init import parse
from datetime import datetime
from src.entities_extractor import extract_and_save_entities
from src.clusterization import clusterization_start
from src.digest_generator import generate_digest

channel_url = "https://t.me/csu76"
channel_name = channel_url.split('/')[-1]
messages = parse(channel_url,                                                       #новости за временной период
                 datetime.strptime("2025-11-20", '%Y-%m-%d'),
                 datetime.strptime("2025-11-23", '%Y-%m-%d'),
                 channel_name)

print(generate_digest(messages))
print(extract_and_save_entities(messages))
clusterization_start()

