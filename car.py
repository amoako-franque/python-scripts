class Car:
  def __init__(self, model, year, color, for_sale):
    self.model = model
    self.year = year
    self.color = color
    self.for_sale = for_sale

  def drive(self):
    print(f"vroom vroom {self.model}")

  def stop(self):
    print(f"car stop when the stop button is pressed {self.model}")

  def describe(self):
    print(f"model: {self.model}, year: {self.year}, color: {self.color}, for sale: {self.for_sale}")