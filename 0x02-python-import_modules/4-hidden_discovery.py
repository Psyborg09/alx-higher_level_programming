#!/usr/bin/python3

if __name__ == "__main__":
    """Prints all names in hidden_4."""
    import hidden_4

    name = dir(hidden_4)
    for n in name:
        if n[:2] != "__":
            print("{}".format(n)) 
