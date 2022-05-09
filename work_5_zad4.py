class Employee:

    def __int__(self, id, first_name, last_name):
        self.id = id
        self.first_name = first_name
        self.last_name = last_name
        self.salary = None

    def set_salary(self, salary):
        try:
            salary = float(salary)
            if salary > 0
                self._salary()
