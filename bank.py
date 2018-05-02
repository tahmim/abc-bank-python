class Bank:
    def __init__(self):
        self.customers = []

    def addCustomer(self, customer):
        self.customers.append(customer)

    def customerSummary(self):
        summary = "Customer Summary"
        summary = ["{} - {} - {} account(s)".format(summary, customer, Customer(customer).numAccs())
                   for customer in self.customers]
        return summary

    def totalInterestPaid(self):
        total = 0
        for c in self.customers:
            total += c.totalInterestEarned()
        return total
    def getFirstCustomer(self):
        try:
            self.customers = None
            return self.customers[0].name
        except Exception as e:
            print(e)
            return "Error"