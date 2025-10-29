"""
Object-Oriented Programming (OOP) Concepts
Comprehensive demonstration of OOP principles in Python including:
- Classes and Objects
- Inheritance
- Encapsulation
- Polymorphism
- Abstract Classes
- Class Methods and Static Methods
- Property Decorators
- Magic Methods (Dunder methods)
"""

from abc import ABC, abstractmethod
from datetime import datetime
from typing import List, Optional


# ============================================================================
# 1. Basic Class with Encapsulation
# ============================================================================

class BankAccount:
    """Demonstrates encapsulation with private attributes."""
    
    def __init__(self, account_number: str, owner: str, balance: float = 0.0):
        """
        Initialize a bank account.
        
        Args:
            account_number: Unique account identifier
            owner: Account owner name
            balance: Initial balance (default: 0.0)
        """
        self.__account_number = account_number  # Private attribute
        self.__owner = owner
        self.__balance = balance
        self.__transactions = []
    
    # Property decorator - getter
    @property
    def balance(self) -> float:
        """Get current balance."""
        return self.__balance
    
    @property
    def owner(self) -> str:
        """Get account owner."""
        return self.__owner
    
    def deposit(self, amount: float):
        """Deposit money into account."""
        if amount <= 0:
            raise ValueError("Deposit amount must be positive")
        
        self.__balance += amount
        self.__transactions.append(f"Deposit: +${amount:.2f}")
        print(f"✓ Deposited ${amount:.2f}. New balance: ${self.__balance:.2f}")
    
    def withdraw(self, amount: float):
        """Withdraw money from account."""
        if amount <= 0:
            raise ValueError("Withdrawal amount must be positive")
        
        if amount > self.__balance:
            raise ValueError("Insufficient funds")
        
        self.__balance -= amount
        self.__transactions.append(f"Withdrawal: -${amount:.2f}")
        print(f"✓ Withdrew ${amount:.2f}. New balance: ${self.__balance:.2f}")
    
    def get_transaction_history(self) -> List[str]:
        """Get list of all transactions."""
        return self.__transactions.copy()
    
    def __str__(self) -> str:
        """String representation of the account."""
        return f"Account({self.__account_number}, {self.__owner}, ${self.__balance:.2f})"
    
    def __repr__(self) -> str:
        """Developer-friendly representation."""
        return f"BankAccount('{self.__account_number}', '{self.__owner}', {self.__balance})"


# ============================================================================
# 2. Inheritance - Single and Multi-level
# ============================================================================

class Vehicle(ABC):
    """Abstract base class for vehicles."""
    
    def __init__(self, brand: str, model: str, year: int):
        self.brand = brand
        self.model = model
        self.year = year
        self._mileage = 0
    
    @abstractmethod
    def start_engine(self):
        """Abstract method - must be implemented by subclasses."""
        pass
    
    def drive(self, distance: float):
        """Drive the vehicle a certain distance."""
        self._mileage += distance
        print(f"Drove {distance} km. Total mileage: {self._mileage} km")
    
    def __str__(self) -> str:
        return f"{self.year} {self.brand} {self.model}"


class Car(Vehicle):
    """Car class inheriting from Vehicle."""
    
    def __init__(self, brand: str, model: str, year: int, num_doors: int):
        super().__init__(brand, model, year)
        self.num_doors = num_doors
        self._engine_running = False
    
    def start_engine(self):
        """Implementation of abstract method."""
        self._engine_running = True
        print(f"🚗 {self.brand} {self.model} engine started: Vroom!")
    
    def honk(self):
        """Car-specific method."""
        print("🔊 Beep beep!")


class ElectricCar(Car):
    """Electric car - multi-level inheritance."""
    
    def __init__(self, brand: str, model: str, year: int, num_doors: int, 
                 battery_capacity: float):
        super().__init__(brand, model, year, num_doors)
        self.battery_capacity = battery_capacity
        self._battery_level = 100
    
    def start_engine(self):
        """Override parent method."""
        self._engine_running = True
        print(f"⚡ {self.brand} {self.model} powered on silently...")
    
    def charge(self, hours: float):
        """Electric car specific method."""
        charge_rate = 10  # % per hour
        charge_amount = min(hours * charge_rate, 100 - self._battery_level)
        self._battery_level += charge_amount
        print(f"🔋 Charged {charge_amount:.1f}%. Battery: {self._battery_level}%")


class Motorcycle(Vehicle):
    """Motorcycle class inheriting from Vehicle."""
    
    def __init__(self, brand: str, model: str, year: int, has_sidecar: bool = False):
        super().__init__(brand, model, year)
        self.has_sidecar = has_sidecar
    
    def start_engine(self):
        """Implementation of abstract method."""
        print(f"🏍️  {self.brand} {self.model} engine started: VRROOOOM!")
    
    def wheelie(self):
        """Motorcycle-specific method."""
        print("🏍️  Performing a wheelie! 🎪")


# ============================================================================
# 3. Polymorphism
# ============================================================================

def test_vehicle(vehicle: Vehicle):
    """Demonstrates polymorphism - works with any Vehicle subclass."""
    print(f"\nTesting: {vehicle}")
    vehicle.start_engine()
    vehicle.drive(50)


# ============================================================================
# 4. Class Methods and Static Methods
# ============================================================================

class Employee:
    """Demonstrates class methods and static methods."""
    
    # Class variable
    company_name = "Tech Corp"
    employee_count = 0
    
    def __init__(self, name: str, salary: float, department: str):
        self.name = name
        self.salary = salary
        self.department = department
        Employee.employee_count += 1
    
    @classmethod
    def from_string(cls, employee_string: str):
        """
        Class method - alternative constructor.
        Create employee from string format: "Name,Salary,Department"
        """
        name, salary, department = employee_string.split(',')
        return cls(name, float(salary), department)
    
    @classmethod
    def set_company_name(cls, name: str):
        """Class method to modify class variable."""
        cls.company_name = name
    
    @staticmethod
    def is_valid_salary(salary: float) -> bool:
        """Static method - utility function related to the class."""
        return salary > 0 and salary < 1_000_000
    
    def give_raise(self, percentage: float):
        """Instance method."""
        if not 0 < percentage <= 50:
            raise ValueError("Raise must be between 0 and 50%")
        
        old_salary = self.salary
        self.salary *= (1 + percentage / 100)
        print(f"💰 {self.name}'s salary: ${old_salary:,.2f} → ${self.salary:,.2f}")
    
    def __str__(self) -> str:
        return f"Employee({self.name}, {self.department}, ${self.salary:,.2f})"


# ============================================================================
# 5. Magic Methods (Dunder Methods)
# ============================================================================

class Vector:
    """Demonstrates magic methods for operator overloading."""
    
    def __init__(self, x: float, y: float):
        self.x = x
        self.y = y
    
    def __add__(self, other):
        """Override + operator."""
        return Vector(self.x + other.x, self.y + other.y)
    
    def __sub__(self, other):
        """Override - operator."""
        return Vector(self.x - other.x, self.y - other.y)
    
    def __mul__(self, scalar):
        """Override * operator for scalar multiplication."""
        return Vector(self.x * scalar, self.y * scalar)
    
    def __eq__(self, other):
        """Override == operator."""
        return self.x == other.x and self.y == other.y
    
    def __str__(self) -> str:
        """String representation."""
        return f"Vector({self.x}, {self.y})"
    
    def __repr__(self) -> str:
        return f"Vector({self.x}, {self.y})"
    
    def __len__(self) -> int:
        """Override len() function."""
        return 2
    
    def magnitude(self) -> float:
        """Calculate vector magnitude."""
        return (self.x ** 2 + self.y ** 2) ** 0.5


# ============================================================================
# 6. Composition (Has-A relationship)
# ============================================================================

class Address:
    """Address class for composition example."""
    
    def __init__(self, street: str, city: str, country: str):
        self.street = street
        self.city = city
        self.country = country
    
    def __str__(self) -> str:
        return f"{self.street}, {self.city}, {self.country}"


class Person:
    """Person class demonstrating composition."""
    
    def __init__(self, name: str, age: int, address: Address):
        self.name = name
        self.age = age
        self.address = address  # Composition: Person HAS-A Address
    
    def __str__(self) -> str:
        return f"{self.name}, {self.age} years old, lives at {self.address}"


# ============================================================================
# Demonstrations
# ============================================================================

def demonstrate_oop_concepts():
    """Demonstrate all OOP concepts."""
    
    print("=" * 70)
    print("Object-Oriented Programming Concepts in Python")
    print("=" * 70)
    
    # 1. Encapsulation
    print("\n1. ENCAPSULATION - Bank Account Example:")
    print("-" * 70)
    
    account = BankAccount("123456", "Alice", 1000)
    print(account)
    account.deposit(500)
    account.withdraw(200)
    print(f"Current balance: ${account.balance:.2f}")
    print(f"Transaction history: {account.get_transaction_history()}")
    
    # 2. Inheritance
    print("\n2. INHERITANCE - Vehicle Hierarchy:")
    print("-" * 70)
    
    car = Car("Toyota", "Camry", 2023, 4)
    electric = ElectricCar("Tesla", "Model 3", 2024, 4, 75)
    motorcycle = Motorcycle("Harley-Davidson", "Street 750", 2023)
    
    print(f"Created: {car}")
    print(f"Created: {electric}")
    print(f"Created: {motorcycle}")
    
    # 3. Polymorphism
    print("\n3. POLYMORPHISM - Same method, different behavior:")
    print("-" * 70)
    
    vehicles = [car, electric, motorcycle]
    for vehicle in vehicles:
        test_vehicle(vehicle)
    
    # 4. Electric car specific features
    print("\n4. SUBCLASS SPECIFIC FEATURES:")
    print("-" * 70)
    
    electric.charge(3)
    car.honk()
    motorcycle.wheelie()
    
    # 5. Class Methods and Static Methods
    print("\n5. CLASS METHODS & STATIC METHODS:")
    print("-" * 70)
    
    emp1 = Employee("Bob", 75000, "Engineering")
    emp2 = Employee.from_string("Charlie,65000,Marketing")
    
    print(f"Company: {Employee.company_name}")
    print(f"Total employees: {Employee.employee_count}")
    print(emp1)
    print(emp2)
    
    emp1.give_raise(10)
    
    print(f"Is $80,000 valid? {Employee.is_valid_salary(80000)}")
    
    # 6. Magic Methods
    print("\n6. MAGIC METHODS - Operator Overloading:")
    print("-" * 70)
    
    v1 = Vector(3, 4)
    v2 = Vector(1, 2)
    
    print(f"v1 = {v1}")
    print(f"v2 = {v2}")
    print(f"v1 + v2 = {v1 + v2}")
    print(f"v1 - v2 = {v1 - v2}")
    print(f"v1 * 2 = {v1 * 2}")
    print(f"v1 == v2? {v1 == v2}")
    print(f"Magnitude of v1: {v1.magnitude():.2f}")
    
    # 7. Composition
    print("\n7. COMPOSITION - Person with Address:")
    print("-" * 70)
    
    address = Address("123 Main St", "New York", "USA")
    person = Person("David", 30, address)
    print(person)


if __name__ == "__main__":
    demonstrate_oop_concepts()
