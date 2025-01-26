from datasets import load_dataset
import json
import os

def get_template():
    train = load_dataset("cmotions/Beatles_lyrics", split='dataset_cleaned[:90%]')
    test = load_dataset("cmotions/Beatles_lyrics", split='dataset_cleaned[:10%]')
    dataset_splits = {"train": train, "test": test}

    if not os.path.exists("data"):
        os.mkdir("data")

    with open("data/config.json", "w") as f:
        config = {
            "chat_template": (
                "{% for message in messages %}"
                "{{ message['content'] }}"
                "{% endfor %}"
            )
        }
        f.write(json.dumps(config))

    for key, ds in dataset_splits.items():
        with open(f"data/{key}.jsonl", "w") as f:
            for item in ds:
                i = {"messages": [
                    {"content": item['lyrics']},
                ]}
                f.write(json.dumps(i) + "\n")
