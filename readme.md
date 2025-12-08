# ascendance-engine (Python OOP Battle Arena) ⚔️

A text-based turn-based strategy game that simulates a battle between two characters. This project demonstrates core Object-Oriented Programming (OOP) principles in Python, including Inheritance, Encapsulation, and Polymorphism.

## 📋 Features

  * **Interactive Setup:** Players select two fighters from three distinct classes to battle against each other.
  * **Unique Class Mechanics:** Each character class has unique stats and special abilities (Shields, Magic, Evasion).
  * **RNG Elements:** Critical mechanics like blocking and dodging are based on probability, making every battle unique.
  * **Turn-Based Logic:** A robust loop that handles turns, health tracking, and win conditions.

## 🛠️ Technical Concepts

This project serves as a practical example of:

  * **Encapsulation:** Uses private attributes (e.g., `__hp`, `__mana`) and `@property` decorators to protect data integrity.
  * **Inheritance:** All specific classes (`Warrior`, `Mage`, `Rogue`) inherit from the abstract `Character` base class.
  * **Polymorphism:** The game loop calls `.attack()` on the objects without needing to know their specific class; each object handles the logic differently.
  * **Abstract Base Classes (ABC):** Enforces a strict blueprint for all character types.

## 🦸 Character Classes

### 1\. The Warrior 🛡️

  * **Role:** Tank
  * **Stats:** High HP (150), Moderate Attack (15).
  * **Special Ability:** **Block**. Has a 20% chance to raise a shield after attacking. If the shield is up, the next incoming damage is reduced by 50%.

### 2\. The Mage 🔮

  * **Role:** Glass Cannon (High Damage, Low Health)
  * **Stats:** Low HP (90), High Attack (25).
  * **Special Ability:** **Arcane Blast**. Uses Mana to deal double damage.
  * **Fallback:** If Mana runs out, the Mage performs a weak attack but regenerates Mana.

### 3\. The Rogue 🗡️

  * **Role:** Gambler / Evasion Tank
  * **Stats:** Moderate HP (110), Moderate Attack (20).
  * **Special Ability:** **Evasion**. Has a 30% chance to vanish into shadows after attacking. If hidden, the next incoming attack is completely dodged (0 Damage).

## 🚀 How to Run

1.  Ensure you have Python installed.
2.  Save the script to a file (e.g., `main.py`).
3.  Run the script in your terminal:

<!-- end list -->

```bash
python main.py
```

## 🎮 Usage Example

When you run the program, you will be prompted to select two characters:

```text
Game Start
Enter your character:
1 = Warrior
2 = Mage
3 = Rogue
> 1
Enter your character:
1 = Warrior
2 = Mage
3 = Rogue
> 3

--- Round 1 ---
Warrior swings a heavy axe at Rogue!
 > Rogue takes 15 damage! (HP: 95/110)
Rogue strikes Warrior from the shadows!
 > Warrior takes 20 damage! (HP: 130/150)
 * Rogue vanishes into the shadows! (Next attack will miss)

--- Round 2 ---
Warrior swings a heavy axe at Rogue!
 * Rogue dodges the attack completely!
 > Rogue takes 0 damage! (HP: 95/110)
...
```
