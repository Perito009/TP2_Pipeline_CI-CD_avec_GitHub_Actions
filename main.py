def hello(first_name="GitHub", last_name="Actions"):
    if not isinstance(first_name, str) or not isinstance(last_name, str):
        raise TypeError("Both first_name and last_name must be strings")
    return f"Hello, {first_name} {last_name}!"
    
