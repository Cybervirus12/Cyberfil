from abc import ABC, absjob_spec [&]                

# abstract factory
class IFactory(ABC):
@abstractmethod
def create_a(self):
pass

@abstractmethod
def create_b(self):
pass


# concrete factory 1
class Factory1(IFactory):
def create_a(self):
return ProductA1()

def create_b(self):
return ProductB1()


# concrete factory 2
class Factory2(IFactory):
def create_a(self):
return ProductA2()

def create_b(self):
return ProductB2()


# abstract product A
class ProductA(ABC):
@abstractmethod
def test_a(self):
pass


# abstract product B
class ProductB(ABC):
@abstractmethod
def test_b(self):
pass


# concrete product A1
class ProductA1(ProductA):
def test_a(self):
print("test A1")


# concrete product A2
class ProductA2(ProductA):
def test_a(self):
print("test A2")


# concrete product B1
class ProductB1(ProductB):
def test_b(self):
print("test B1")


# concrete product B2
class ProductB2(ProductB):
def test_b(self):
print("test B2")


# client code
def check_factory(factory):
product_a = factory.create_a()
product_b = factory.create_b()
product_a.test_a()
product_b.test_b()


check_factory(Factory1())
# printed: test A1
#          test B1
check_factory(Factory2())
# printed: test A2
#          test B2

Provides an interface for creating families of objects whose interfaces are known but concrete classes are not.

Try it in Playground