def car_details(name,model,price,color):
    results = {
        "Name": name,
        "Model": model,
        "Price": price,
        "Color": color
    }
    return results

if __name__ == "__main__":
    name="BMW"
    model="M5"
    price=25000000
    color="Black"
    print(car_details(name,model,price,color))
