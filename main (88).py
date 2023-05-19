class CoffeeShipment:
    def __init__(self, weight, destination):
        self.weight = weight
        self.destination = destination

    def calculate_shipping_cost(self):
        rate_per_kg = 5.0  # Shipping cost rate per kilogram
        return self.weight * rate_per_kg

    def calculate_shipping_time(self):
        # Assume shipping time is based on distance
        shipping_time = 2  # in days
        if self.destination == "International":
            shipping_time += 5  # Additional days for international shipments
        return shipping_time

    def print_shipping_details(self):
        shipping_cost = self.calculate_shipping_cost()
        shipping_time = self.calculate_shipping_time()

        print("Shipping Details:")
        print(f"Weight: {self.weight} kg")
        print(f"Destination: {self.destination}")
        print(f"Shipping Cost: ${shipping_cost}")
        print(f"Estimated Shipping Time: {shipping_time} days")


# Example usage
weight = float(input("Enter the weight of the coffee shipment (in kg): "))
destination = input("Enter the destination (Domestic/International): ")

shipment = CoffeeShipment(weight, destination)
shipment.print_shipping_details()

