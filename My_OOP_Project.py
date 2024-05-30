from abc import ABC, abstractmethod

class FamilyMember(ABC):
    def __init__(self, name, age, gender):
        self.__name = name
        self.__age = age
        self.__gender = gender
        
    def get_name(self):
        return self.__name
    
    def get_age(self):
        return self.__age
    
    def get_gender(self):
        return self.__gender
    
    @abstractmethod
    def Family_info(self):
        pass
    
    @abstractmethod
    def Role(self):
        pass

class Father(FamilyMember):
    def __init__(self, name, age, gender):
        super().__init__(name, age, gender)
        
    def Family_info(self):
        print("Name: " + self.get_name())
        print("Gender: " + self.get_gender())
        
    def Role(self):
        print("The Father")

class Mother(FamilyMember):
    def __init__(self, name, age, gender):
        super().__init__(name, age, gender)
        
    def Family_info(self):
        print("Name: " + self.get_name())
        print("Gender: " + self.get_gender())
        
    def Role(self):
        print("The Mother")

class FirstChild(FamilyMember):
    def __init__(self, name, age, gender):
        super().__init__(name, age, gender)
        
    def Family_info(self):
        print("Name: " + self.get_name())
        print("Gender: " + self.get_gender())
        
    def Role(self):
        print("The First child")

class SecondChild(FamilyMember):
    def __init__(self, name, age, gender):
        super().__init__(name, age, gender)
        
    def Family_info(self):
        print("Name: " + self.get_name())
        print("Gender: " + self.get_gender())
        
    def Role(self):
        print("The Second child")

class ThirdChild(FamilyMember):
    def __init__(self, name, age, gender):
        super().__init__(name, age, gender)
        
    def Family_info(self):
        print("Name: " + self.get_name())
        print("Gender: " + self.get_gender())
        
    def Role(self):
        print("The Third child")

# Creating instances of the subclasses
Person1 = Father("Romeo", 65, "Male")
Person2 = Mother("Maria", 57, "Female")
Person3 = FirstChild("Sam", 35, "Male")
Person4 = ThirdChild("Christine", 19, "Female")
Person5 = SecondChild("Joe", 23, "Male")

# Calling methods for each instance
print("=======================")
Person1.Family_info()
Person1.Role()
print("=======================")
print()
print("=======================")
Person2.Family_info()
Person2.Role()
print("=======================")
print()
print("=======================")
Person3.Family_info()
Person3.Role()
print("=======================")
print()
print("=======================")
Person4.Family_info()
Person4.Role()
print("=======================")
print()
print("=======================")
Person5.Family_info()
Person5.Role()
print("=======================")