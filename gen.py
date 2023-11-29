import json


def process_json(input_file):
    with open(input_file, "r") as file:
        try:
            data = json.load(file)
        except json.JSONDecodeError as e:
            return f"Error: Invalid JSON file - {e}"

    output_dict = {}
    for item in data:
        if "name" in item:
            if item.get("type") == "dropDown" and "options" in item and item["options"]:
                output_dict[item["name"]] = item["options"][0].get("value")
            elif "default" in item:
                output_dict[item["name"]] = item["default"]
    return json.dumps(output_dict)


def write_to_file(output, output_file):
    with open(output_file, "w") as file:
        file.write(f'"""{output}"""')


if __name__ == "__main__":
    processed_json = process_json("updatedParams.json")
    write_to_file(processed_json, "defaultsAsJSONstring.txt")


def get_values(*names):
            import json
            _all_values = json.loads("""JSON_STRING""")
            return [_all_values[n] for n in names]