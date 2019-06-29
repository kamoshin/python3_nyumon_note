def yen2doller(yen, rate, charge = 0):
    doller = yen / (rate + charge)
    return doller

def doller2yen(doller, rate, charge = 0):
    yen = doller * (rate - charge)
    return yen
