def hello(first_name="GitHub Actions", last_name=None):
    if not isinstance(first_name, str) or (
        last_name is not None and not isinstance(last_name, str)
    ):
        raise TypeError("Name must be a string")

    if last_name:
        return f"Hello, {first_name} {last_name}!"
    return f"Hello, {first_name}!"
