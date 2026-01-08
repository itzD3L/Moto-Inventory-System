#!/usr/bin/env python3
"""
Example usage of the Moto Shop Inventory System
This script demonstrates how to use the system programmatically
"""

from inventory import MotoInventorySystem


def populate_sample_data():
    """Populate the inventory with sample motorcycle shop equipment"""
    
    print("="*60)
    print("MOTO SHOP INVENTORY SYSTEM - Example Usage")
    print("="*60)
    
    # Create inventory system instance
    system = MotoInventorySystem('example_inventory.json')
    
    print("\n[1] Adding sample equipment to inventory...")
    
    # Engine Parts
    system.add_item('Oil Filter - Standard', 50, 12.99, 'Engine Parts')
    system.add_item('Oil Filter - Premium', 30, 18.99, 'Engine Parts')
    system.add_item('Spark Plug - NGK', 100, 8.50, 'Engine Parts')
    system.add_item('Air Filter', 25, 24.99, 'Engine Parts')
    system.add_item('Piston Ring Set', 15, 89.99, 'Engine Parts')
    
    # Brakes
    system.add_item('Brake Pad Set - Front', 20, 45.00, 'Brakes')
    system.add_item('Brake Pad Set - Rear', 20, 42.00, 'Brakes')
    system.add_item('Brake Fluid - DOT4', 40, 12.50, 'Brakes')
    system.add_item('Brake Line Kit', 8, 65.00, 'Brakes')
    
    # Tires & Wheels
    system.add_item('Front Tire - Sport', 12, 145.00, 'Tires')
    system.add_item('Rear Tire - Sport', 12, 165.00, 'Tires')
    system.add_item('Tire Valve Stems', 100, 2.50, 'Tires')
    system.add_item('Wheel Bearing Kit', 10, 35.00, 'Tires')
    
    # Lubricants
    system.add_item('Chain Lube', 20, 9.99, 'Lubricants')
    system.add_item('Engine Oil - 10W40', 60, 25.99, 'Lubricants')
    system.add_item('Fork Oil', 15, 18.99, 'Lubricants')
    
    # Tools & Accessories
    system.add_item('Chain Breaker Tool', 5, 79.99, 'Tools')
    system.add_item('Torque Wrench', 3, 159.99, 'Tools')
    system.add_item('Motorcycle Stand', 8, 89.99, 'Tools')
    
    print("\n[2] Displaying all equipment...")
    items = system.list_all_items()
    print(f"\n{'='*100}")
    print(f"{'NAME':<35} {'QUANTITY':<12} {'PRICE':<12} {'CATEGORY':<20} {'VALUE':<12}")
    print(f"{'='*100}")
    for item in sorted(items, key=lambda x: x.category + x.name):
        value = item.quantity * item.price
        print(f"{item.name:<35} {item.quantity:<12} ${item.price:<11.2f} {item.category:<20} ${value:<11.2f}")
    print(f"{'='*100}")
    
    print("\n[3] Checking low stock items (threshold: 10)...")
    low_stock = system.get_low_stock_items(10)
    if low_stock:
        print(f"Found {len(low_stock)} low stock item(s):")
        for item in sorted(low_stock, key=lambda x: x.quantity):
            print(f"  - {item.name}: {item.quantity} units")
    
    print("\n[4] Searching for 'brake' items...")
    brake_items = system.search_items('brake')
    print(f"Found {len(brake_items)} item(s) matching 'brake':")
    for item in brake_items:
        print(f"  - {item.name}: {item.quantity} @ ${item.price}")
    
    print("\n[5] Viewing Engine Parts category...")
    engine_parts = system.get_items_by_category('Engine Parts')
    print(f"Engine Parts category has {len(engine_parts)} item(s):")
    for item in engine_parts:
        print(f"  - {item.name}: {item.quantity} @ ${item.price}")
    
    print("\n[6] Inventory Summary...")
    system.display_summary()
    
    print("\n[7] Simulating sales (adjusting quantities)...")
    system.adjust_quantity('Oil Filter - Standard', -5)
    system.adjust_quantity('Spark Plug - NGK', -12)
    system.adjust_quantity('Chain Lube', -3)
    
    print("\n[8] Updated summary after sales...")
    system.display_summary()
    
    print("\n" + "="*60)
    print("Example completed successfully!")
    print(f"Data saved to: example_inventory.json")
    print("="*60)


if __name__ == "__main__":
    populate_sample_data()
