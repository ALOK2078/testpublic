import yaml

# Function to read and print the contents of test.yml
def read_yaml_file(file_path):
    try:
        with open(file_path, 'r') as file:
            data = yaml.safe_load(file)
            print("Contents of the YAML file:")
            print(data)
    except FileNotFoundError:
        print(f"Error: The file '{file_path}' was not found.")
    except yaml.YAMLError as e:
        print(f"Error parsing YAML file: {e}")

# Specify the path to the YAML file
yaml_file_path = 'test.yml'

# Call the function
read_yaml_file(yaml_file_path)