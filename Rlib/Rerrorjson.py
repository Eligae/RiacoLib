import json

def append_error(error_code: dict, file='./Rerror.json'):
    """
    Append error information to a JSON file.

    :param error_code: A dictionary containing error information.
    :param file: File path for storing error data (default is './Rerror.json').
    """
    try:
        with open(file, 'r', encoding='utf-8') as json_file:
            existing_data = json.load(json_file)
            existing_data['data'].append(error_code)
    except FileNotFoundError:
        existing_data = {'data': [error_code]}

    with open(file, 'w', encoding='utf-8') as json_file:
        json.dump(existing_data, json_file)

def handle_error(function, function_args=None, file='./Rerror.json'):
    """
    Wrap a function to handle exceptions and log errors in a JSON file.

    :param function: The function to be executed.
    :param function_args: A dictionary of arguments to be passed to the function (optional).
    :param file: File path for storing error data (default is './Rerror.json').
    :return: The result of the executed function or None in case of an error.
    """
    try:
        result = function(**function_args) if function_args else function()
        return result
    except Exception as e:
        if function_args is None:
            function_args = {}
        function_args['error'] = str(e)
        append_error(function_args, file=file)
        return None  # Return None to indicate an error occurred


__doc__ = """
Example usage:
Define your function to be wrapped and its arguments
```python
def example_function(x, y):
    return x / y

function_args = {'x': 10, 'y': 0}
```
Wrap the function to handle errors
```python
result = handle_error(example_function, function_args)
if result is not None:
    print("Result:", result)
else:
    print("An error occurred and was logged.")
```
"""