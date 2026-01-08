# Moto-Inventory-System

A comprehensive inventory management system for motorcycle shops to track all equipment quantities, prices, and categories.

## Features

- **Add Equipment**: Add new equipment with name, quantity, price, and category
- **Update Quantities**: Update equipment quantities (set to specific value or adjust by adding/removing)
- **Remove Equipment**: Remove equipment from inventory
- **View Inventory**: Display all equipment in a formatted table
- **Search**: Search for equipment by name
- **Category Management**: Filter equipment by category
- **Low Stock Alerts**: View items below a specified quantity threshold
- **Inventory Summary**: See total items, units, and inventory value
- **Data Persistence**: All data is automatically saved to a JSON file

## Requirements

- Python 3.6 or higher

## Installation

1. Clone this repository:
```bash
git clone https://github.com/itzD3L/Moto-Inventory-System.git
cd Moto-Inventory-System
```

2. No additional dependencies required - uses only Python standard library!

## Usage

### Running the System

Simply run the main script:

```bash
python3 inventory.py
```

Or make it executable and run directly:

```bash
chmod +x inventory.py
./inventory.py
```

### Main Menu Options

1. **Add new equipment** - Add a new item to the inventory
2. **Update equipment quantity** - Set quantity to a specific value
3. **Adjust quantity** - Add or remove units from current quantity
4. **Remove equipment** - Delete an item from inventory
5. **View all equipment** - Display all items in a formatted table
6. **Search equipment** - Find items by keyword in name
7. **View by category** - Filter items by category
8. **View low stock items** - See items below a quantity threshold
9. **View inventory summary** - Display summary statistics
0. **Exit** - Close the application

### Example Usage

#### Adding Equipment
```
Enter your choice: 1
Enter equipment name: Oil Filter
Enter quantity: 50
Enter price per unit: $12.99
Enter category (default: General): Filters
Added 'Oil Filter' to inventory.
```

#### Viewing All Equipment
```
Enter your choice: 5

====================================================================================================
NAME                           QUANTITY     PRICE        CATEGORY             VALUE       
====================================================================================================
Oil Filter                     50           $12.99       Filters              $649.50     
Spark Plug                     100          $8.50        Engine Parts         $850.00     
====================================================================================================
```

#### Adjusting Quantity
```
Enter your choice: 3
Enter equipment name: Oil Filter
Enter change amount (positive to add, negative to remove): -10
Updated 'Oil Filter' quantity from 50 to 40.
```

#### Low Stock Alert
```
Enter your choice: 8
Enter threshold (default: 5): 10

Low stock items (quantity <= 10):

====================================================================================================
NAME                           QUANTITY     PRICE        CATEGORY             VALUE       
====================================================================================================
Brake Pad Set                  5            $45.00       Brakes               $225.00     
====================================================================================================
```

## Data Storage

All inventory data is stored in `inventory_data.json` in the same directory as the script. This file is automatically created and updated as you use the system.

### Example inventory_data.json
```json
{
  "Oil Filter": {
    "name": "Oil Filter",
    "quantity": 50,
    "price": 12.99,
    "category": "Filters",
    "last_updated": "2026-01-08T11:45:00.000000"
  },
  "Spark Plug": {
    "name": "Spark Plug",
    "quantity": 100,
    "price": 8.50,
    "category": "Engine Parts",
    "last_updated": "2026-01-08T11:46:00.000000"
  }
}
```

## Categories

You can organize your equipment into categories such as:
- Engine Parts
- Filters
- Brakes
- Tires
- Lubricants
- Tools
- Accessories
- General

Categories help you organize and filter your inventory effectively.

## Best Practices

1. **Regular Updates**: Update quantities whenever items are sold or received
2. **Use Categories**: Organize items into logical categories for easier management
3. **Monitor Low Stock**: Regularly check low stock items to ensure you don't run out
4. **Backup Data**: Periodically backup the `inventory_data.json` file
5. **Consistent Naming**: Use consistent naming conventions for similar items

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.