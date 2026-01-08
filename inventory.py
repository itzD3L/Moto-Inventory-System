#!/usr/bin/env python3
"""
Moto Shop Inventory System
A system to track all motorcycle shop equipment quantities
"""

import json
import os
from typing import Dict, List, Optional
from datetime import datetime


class InventoryItem:
    """Represents an item in the inventory"""
    
    def __init__(self, name: str, quantity: int, price: float, category: str = "General"):
        self.name = name
        self.quantity = quantity
        self.price = price
        self.category = category
        self.last_updated = datetime.now().isoformat()
    
    def to_dict(self) -> dict:
        """Convert item to dictionary for JSON serialization"""
        return {
            'name': self.name,
            'quantity': self.quantity,
            'price': self.price,
            'category': self.category,
            'last_updated': self.last_updated
        }
    
    @classmethod
    def from_dict(cls, data: dict) -> 'InventoryItem':
        """Create item from dictionary"""
        item = cls(data['name'], data['quantity'], data['price'], data.get('category', 'General'))
        item.last_updated = data.get('last_updated', datetime.now().isoformat())
        return item


class MotoInventorySystem:
    """Main inventory management system"""
    
    def __init__(self, data_file: str = "inventory_data.json"):
        self.data_file = data_file
        self.inventory: Dict[str, InventoryItem] = {}
        self.load_inventory()
    
    def load_inventory(self):
        """Load inventory from JSON file"""
        if os.path.exists(self.data_file):
            try:
                with open(self.data_file, 'r') as f:
                    data = json.load(f)
                    self.inventory = {
                        name: InventoryItem.from_dict(item_data)
                        for name, item_data in data.items()
                    }
                print(f"Loaded {len(self.inventory)} items from {self.data_file}")
            except Exception as e:
                print(f"Error loading inventory: {e}")
                self.inventory = {}
        else:
            print("No existing inventory file found. Starting with empty inventory.")
    
    def save_inventory(self):
        """Save inventory to JSON file"""
        try:
            data = {name: item.to_dict() for name, item in self.inventory.items()}
            with open(self.data_file, 'w') as f:
                json.dump(data, f, indent=2)
            print(f"Inventory saved to {self.data_file}")
        except Exception as e:
            print(f"Error saving inventory: {e}")
    
    def add_item(self, name: str, quantity: int, price: float, category: str = "General") -> bool:
        """Add a new item to inventory"""
        if name in self.inventory:
            print(f"Item '{name}' already exists. Use update_quantity to modify it.")
            return False
        
        if quantity < 0:
            print("Quantity cannot be negative.")
            return False
        
        if price < 0:
            print("Price cannot be negative.")
            return False
        
        self.inventory[name] = InventoryItem(name, quantity, price, category)
        self.save_inventory()
        print(f"Added '{name}' to inventory.")
        return True
    
    def update_quantity(self, name: str, quantity: int) -> bool:
        """Update the quantity of an existing item"""
        if name not in self.inventory:
            print(f"Item '{name}' not found in inventory.")
            return False
        
        if quantity < 0:
            print("Quantity cannot be negative.")
            return False
        
        old_quantity = self.inventory[name].quantity
        self.inventory[name].quantity = quantity
        self.inventory[name].last_updated = datetime.now().isoformat()
        self.save_inventory()
        print(f"Updated '{name}' quantity from {old_quantity} to {quantity}.")
        return True
    
    def adjust_quantity(self, name: str, change: int) -> bool:
        """Adjust quantity by a relative amount (positive or negative)"""
        if name not in self.inventory:
            print(f"Item '{name}' not found in inventory.")
            return False
        
        new_quantity = self.inventory[name].quantity + change
        if new_quantity < 0:
            print(f"Cannot adjust quantity. Result would be negative ({new_quantity}).")
            return False
        
        return self.update_quantity(name, new_quantity)
    
    def remove_item(self, name: str) -> bool:
        """Remove an item from inventory"""
        if name not in self.inventory:
            print(f"Item '{name}' not found in inventory.")
            return False
        
        del self.inventory[name]
        self.save_inventory()
        print(f"Removed '{name}' from inventory.")
        return True
    
    def get_item(self, name: str) -> Optional[InventoryItem]:
        """Get a specific item from inventory"""
        return self.inventory.get(name)
    
    def list_all_items(self) -> List[InventoryItem]:
        """Get all items in inventory"""
        return list(self.inventory.values())
    
    def search_items(self, keyword: str) -> List[InventoryItem]:
        """Search for items by keyword in name"""
        keyword_lower = keyword.lower()
        return [
            item for name, item in self.inventory.items()
            if keyword_lower in name.lower()
        ]
    
    def get_items_by_category(self, category: str) -> List[InventoryItem]:
        """Get all items in a specific category"""
        return [
            item for item in self.inventory.values()
            if item.category.lower() == category.lower()
        ]
    
    def get_low_stock_items(self, threshold: int = 5) -> List[InventoryItem]:
        """Get items with quantity below threshold"""
        return [
            item for item in self.inventory.values()
            if item.quantity <= threshold
        ]
    
    def get_total_inventory_value(self) -> float:
        """Calculate total value of all inventory"""
        return sum(item.quantity * item.price for item in self.inventory.values())
    
    def display_summary(self):
        """Display inventory summary"""
        if not self.inventory:
            print("\nInventory is empty.")
            return
        
        print(f"\n{'='*80}")
        print(f"INVENTORY SUMMARY")
        print(f"{'='*80}")
        print(f"Total Items: {len(self.inventory)}")
        print(f"Total Units: {sum(item.quantity for item in self.inventory.values())}")
        print(f"Total Value: ${self.get_total_inventory_value():.2f}")
        print(f"{'='*80}\n")


def main():
    """Main function for CLI interface"""
    system = MotoInventorySystem()
    
    while True:
        print("\n" + "="*50)
        print("MOTO SHOP INVENTORY SYSTEM")
        print("="*50)
        print("1. Add new equipment")
        print("2. Update equipment quantity")
        print("3. Adjust quantity (add/remove)")
        print("4. Remove equipment")
        print("5. View all equipment")
        print("6. Search equipment")
        print("7. View by category")
        print("8. View low stock items")
        print("9. View inventory summary")
        print("0. Exit")
        print("="*50)
        
        choice = input("\nEnter your choice: ").strip()
        
        if choice == "1":
            # Add new equipment
            name = input("Enter equipment name: ").strip()
            try:
                quantity = int(input("Enter quantity: ").strip())
                price = float(input("Enter price per unit: $").strip())
                category = input("Enter category (default: General): ").strip() or "General"
                system.add_item(name, quantity, price, category)
            except ValueError:
                print("Invalid input. Please enter valid numbers for quantity and price.")
        
        elif choice == "2":
            # Update quantity
            name = input("Enter equipment name: ").strip()
            try:
                quantity = int(input("Enter new quantity: ").strip())
                system.update_quantity(name, quantity)
            except ValueError:
                print("Invalid input. Please enter a valid number for quantity.")
        
        elif choice == "3":
            # Adjust quantity
            name = input("Enter equipment name: ").strip()
            try:
                change = int(input("Enter change amount (positive to add, negative to remove): ").strip())
                system.adjust_quantity(name, change)
            except ValueError:
                print("Invalid input. Please enter a valid number.")
        
        elif choice == "4":
            # Remove equipment
            name = input("Enter equipment name to remove: ").strip()
            confirm = input(f"Are you sure you want to remove '{name}'? (yes/no): ").strip().lower()
            if confirm == "yes":
                system.remove_item(name)
            else:
                print("Removal cancelled.")
        
        elif choice == "5":
            # View all equipment
            items = system.list_all_items()
            if items:
                print(f"\n{'='*100}")
                print(f"{'NAME':<30} {'QUANTITY':<12} {'PRICE':<12} {'CATEGORY':<20} {'VALUE':<12}")
                print(f"{'='*100}")
                for item in sorted(items, key=lambda x: x.name):
                    value = item.quantity * item.price
                    print(f"{item.name:<30} {item.quantity:<12} ${item.price:<11.2f} {item.category:<20} ${value:<11.2f}")
                print(f"{'='*100}")
            else:
                print("\nNo items in inventory.")
        
        elif choice == "6":
            # Search equipment
            keyword = input("Enter search keyword: ").strip()
            items = system.search_items(keyword)
            if items:
                print(f"\nFound {len(items)} item(s):")
                print(f"\n{'='*100}")
                print(f"{'NAME':<30} {'QUANTITY':<12} {'PRICE':<12} {'CATEGORY':<20} {'VALUE':<12}")
                print(f"{'='*100}")
                for item in items:
                    value = item.quantity * item.price
                    print(f"{item.name:<30} {item.quantity:<12} ${item.price:<11.2f} {item.category:<20} ${value:<11.2f}")
                print(f"{'='*100}")
            else:
                print(f"\nNo items found matching '{keyword}'.")
        
        elif choice == "7":
            # View by category
            category = input("Enter category name: ").strip()
            items = system.get_items_by_category(category)
            if items:
                print(f"\nItems in category '{category}':")
                print(f"\n{'='*100}")
                print(f"{'NAME':<30} {'QUANTITY':<12} {'PRICE':<12} {'CATEGORY':<20} {'VALUE':<12}")
                print(f"{'='*100}")
                for item in items:
                    value = item.quantity * item.price
                    print(f"{item.name:<30} {item.quantity:<12} ${item.price:<11.2f} {item.category:<20} ${value:<11.2f}")
                print(f"{'='*100}")
            else:
                print(f"\nNo items found in category '{category}'.")
        
        elif choice == "8":
            # View low stock items
            try:
                threshold = input("Enter threshold (default: 5): ").strip()
                threshold = int(threshold) if threshold else 5
                items = system.get_low_stock_items(threshold)
                if items:
                    print(f"\nLow stock items (quantity <= {threshold}):")
                    print(f"\n{'='*100}")
                    print(f"{'NAME':<30} {'QUANTITY':<12} {'PRICE':<12} {'CATEGORY':<20} {'VALUE':<12}")
                    print(f"{'='*100}")
                    for item in sorted(items, key=lambda x: x.quantity):
                        value = item.quantity * item.price
                        print(f"{item.name:<30} {item.quantity:<12} ${item.price:<11.2f} {item.category:<20} ${value:<11.2f}")
                    print(f"{'='*100}")
                else:
                    print(f"\nNo low stock items found.")
            except ValueError:
                print("Invalid threshold value.")
        
        elif choice == "9":
            # View summary
            system.display_summary()
        
        elif choice == "0":
            # Exit
            print("\nThank you for using Moto Shop Inventory System!")
            break
        
        else:
            print("\nInvalid choice. Please try again.")


if __name__ == "__main__":
    main()
