from car import car_details
def test_car_details():
    name="BMW"
    model="M5"
    price=25000000
    color="Black"
    expected_output = {
        "name=BMW",
        "model=M5",
        "price=25000000",
        "color=Black"
    }
    assert car_details(name,model,price,color) == expected_output