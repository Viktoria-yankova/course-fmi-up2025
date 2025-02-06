from statistics import quantiles

if __name__=="__main__":
    d = dict()
    d2 = {}
    print(type (d2))
    s= set()
    print(type(s))
    d3= dict([("name", "viktoria"), ("course", "up")])
    print(d3)
    ingredients = ["vodka", "rom", "orange juice,", "lemon", "menta" ]
    quantiles= [50,20,0,0,1]
    print(dict(zip(ingredients, quantiles)))