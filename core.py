#! /usr/bin/python3

def suma(a,b):
    return a + b

def resta(m,s):
    return m - s

def demon(requestCode) -> str:
    if requestCode == 1: return "+"
    if requestCode == 2: return "-"
    return "codeError"

def coreMain():
    product = demon(1)
    product = demon(2)
    product = demon("badInput")
    print(f"product: {product}")    

if __name__ == "__main__":
    
    coreMain()