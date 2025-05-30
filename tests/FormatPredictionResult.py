import json
import sys

def sort_json_file(input_file, output_file=None, indent=4):
    try:
        with open(input_file, 'r', encoding='utf-8') as f:
            data = json.load(f)

        for k, v in data.items():
            data[k] = int(v)
        for i in range(0, len(data.items())):
            id = str(i)
            if id not in data:
                print(f'player {id} is not in the map')
                data[id] = -1
        if output_file:

            with open(output_file, 'w', encoding='utf-8') as f:
                json.dump(data, f, indent=indent, sort_keys=True, ensure_ascii=False)
            print(f"Formatted json file exported to {output_file}")
        else:
            print(json.dumps(data, indent=indent, sort_keys=True, ensure_ascii=False))

    except FileNotFoundError:
        print(f"Error: file '{input_file}' does not exist")
        sys.exit(1)
    except json.JSONDecodeError:
        print(f"Error: '{input_file}' is an invalid json file")
        sys.exit(1)
    except Exception as e:
        print(f"Error: {str(e)}")
        sys.exit(1)

if __name__ == "__main__":
    sort_json_file(r"C:/Users/syeda/OneDrive/Desktop/4th Year/COSC419/jersey-number-pipeline/out2/SoccerNetResults/final_results_test_masked.json", r"C:/Users/syeda/OneDrive/Desktop/4th Year/COSC419/jersey-number-pipeline/out2/SoccerNetResults/final_results_test_masked_formatted.json", 4)