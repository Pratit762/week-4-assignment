def validate_airport(code):
    return code.isalpha() and len(code) == 3
