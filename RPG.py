#  File: RPG.py
#  Description: Creates a simple RPG game
#  Student's Name: Zi Zhou Wang
#  Student's UT EID: zw3948
#  Course Name: CS 313E
#  Unique Number: 86940
#
#  Date Created: 6/10/2017
#  Date Last Modified: 6/10/2017

# defines a Python class called Weapon
# @param name identifies the weapon's type
# each weapon type will do a specific amount of damage when striking an opponent


class Weapon:
    def __init__(self, name):
        self.type = name
        if name == "dagger":
            self.damage = 4
        elif name == "axe" or name == "staff":
            self.damage = 6
        elif name == "sword":
            self.damage = 10
        else:
            self.damage = 1

# defines a Python class called Armor
# @param name identifies the armor's type
# each armor type will offer a specific amount of protection or AC


class Armor:
    def __init__(self, name):
        self.type = name
        if name == "plate":
            self.AC = 2
        elif name == "chain":
            self.AC = 5
        elif name == "leather":
            self.AC = 8
        else:
            self.AC = 10

# defines a Python class called RPGCharacter
# this class serves as a template class for more specialized characters


class RPGCharacter:
    # defines the initialization method
    # @param name identifies and character's name
    def __init__(self, name):
        self.name = name
        self.armor = Armor("none")
        self.weapon = Weapon("none")
        self.health = 0
        self.spell = 0

    # removes any weapons the character is currently wielding

    def unwield(self):
        print(self.name, "is no longer wielding anything.")
        self.weapon = Weapon("none")

    # removes any armor the character is currently wearing

    def takeOffArmor(self):
        print("NAME is no longer wearing anything.")
        self.armor = Armor("none")
    # defines a method for which a character object can fight another
    # @param other the character to fight

    def fight(self, other):
        print(self.name, "attacks", other.name, "with a(n)", self.weapon.type)
        other.health -= self.weapon.damage
        print(self.name, "does", self.weapon.damage, "damage to", other.name)
        print(other.name, "is now down to", other.health, "health")
        other.checkForDefeat()

    # defines a method that checks if the character has been defeated

    def checkForDefeat(self):
        if self.health <= 0:
            print(self.name, "has been defeated!")

    # prints a formatted version of the character's stats

    def show(self):
        print()
        print(" " + self.name)
        print("   Current Health:", self.health)
        print("   Current Spell Points:", self.spell)
        print("   Wielding:", self.weapon.type)
        print("   Wearing:", self.armor.type)
        print("   Armor class:", self.armor.AC)
        print()

# defines a Python class called Fighter
# the Fighter class is a subclass of RPGCharacter


class Fighter(RPGCharacter):
    # defines the initialization method
    # @param name the name of the character
    def __init__(self, name):
        super().__init__(name)
        self.health = 40
    # weapons and armor usable by the Fighter class
    weapons = ["dagger", "axe", "staff", "sword", "none"]
    armors = ["plate", "chain", "leather", "none"]

    # equipts a specified weapon onto a Fighter
    # @param weapon the weapon to equipt

    def wield(self, weapon):
        if weapon.type in self.weapons:
            print(self.name, "is now wielding a(n)", weapon.type)
            self.weapon = weapon
        else:
            print("Weapon not allowed for this character class.")

    # equipts a specific armor onto a Fighter
    # @param armor the armor to equipt

    def putOnArmor(self, armor):
        if armor.type in self.armors:
            print(self.name, "is now wearing", armor.type)
            self.armor = armor
        else:
            print("Armor not allowed for this character class.")

# defines a Python class called Wizard
# the Wizard class is a subclass of RPGCharacter


class Wizard(RPGCharacter):
    # defines the initialization method
    def __init__(self, name):
        super().__init__(name)
        self.health = 16
        self.spell = 20

    # weapons and armor usable by the Wizard class
    weapons = ["dagger", "staff", "none"]
    armors = ["none"]

    # equipts a specified weapon onto a Wizard
    # @param weapon the weapon to equipt

    def wield(self, weapon):
        if weapon.type in self.weapons:
            print(self.name, "is now wielding a(n)", weapon.type)
            self.weapon = weapon
        else:
            print("Weapon not allowed for this character class.")

    # equipts a specified armor onto a Wizard
    # @param armor the armor to equipt

    def putOnArmor(self, armor):
        if armor in self.armors:
            print(self.name, "is now wearing", armor.type)
            self.armor = armor
        else:
            print("Armor not allowed for this character class.")

    # defines a method the allows a Wizard to cast spells
    # @param spell the spell to cast
    # @param character is the character to cast the spell on

    def castSpell(self, spell, character):
        if spell == "Fireball" or spell == "Lightning Bolt" or spell == "Heal":
            print(self.name, "casts", spell, "at", character.name)
            if spell == "Fireball":
                if self.spell < 3:
                    print("Insufficient spell points")
                    return
                else:
                    character.health -= 5
                    self.spell -= 3
                    print(self.name, "does 5 damage to", character.name)
                    print(character.name, "is now down to", character.health, "health")
            elif spell == "Lightning Bolt":
                if self.spell < 10:
                    print("Insufficient spell points")
                    return
                else:
                    character.health -= 10
                    self.spell -= 10
                    print(self.name, "does 10 damage to", character.name)
                    print(character.name, "is now down to", character.health, "health")
            else:
                if self.spell < 6:
                    print("Insufficient spell points")
                    return
                else:
                    character.health += 6
                    self.spell -= 6
                    print(self.name, "heals", character.name, "for 6 health points")
                    print(character.name, "is now at", character.health, "health")
        else:
            print("Unknown spell name. Spell failed.")
            return


def main():
    chainMail = Armor("chain")
    sword = Weapon("sword")
    staff = Weapon("staff")
    axe = Weapon("axe")

    harry = Wizard("Harry Potter")
    harry.wield(staff)

    aragorn = Fighter("Aragorn")
    aragorn.putOnArmor(chainMail)
    aragorn.wield(axe)

    harry.show()
    aragorn.show()

    harry.castSpell("Fireball", aragorn)
    aragorn.fight(harry)

    harry.show()
    aragorn.show()

    harry.castSpell("Lightning Bolt", aragorn)
    aragorn.wield(sword)

    harry.show()
    aragorn.show()

    harry.castSpell("Heal", harry)
    aragorn.fight(harry)

    harry.fight(aragorn)
    aragorn.fight(harry)

    harry.show()
    aragorn.show()


main()