def average(*args):
    if args:
        ave = sum(args) / len(args)
        return ave
    else:
        return None
