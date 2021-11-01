def clean_object(x):
    """
    This function transforms "x" to integrers.
    Arggs:
    - x given argument.
    Returns:
     - Integrer or number.
     """
    try:
        y = int(x)
        return y
    except:
        return x