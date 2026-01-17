from car import car_details
def test_car_details():
  expected output = {
    "name=BMW",
    "model=M5",
    "price=25000000",
    "color=black"
   }
assert car_details("BMW", "M5", 25000000, "black") == expected output
