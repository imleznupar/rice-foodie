import web_scraper

# all_dishes = web_scraper.get_all_dishes()
all_dishes = {'south-servery': {'LUNCH': [], 'DINNER': ['Shredded Lettuce & Pico de Gallo', 'Tex Mex Queso', 'Corn Tortilla Chips', 'Refried Beans', 'Corn Tortilla Chips', 'Shredded Lettuce & Pico de Gallo', 'Fajita Seasoned PAOW with Peppers & Onions', 'Nacho Styled Ground Beef', 'Fajita Paow with Peppers & Onions', 'Nacho Style Ground Beef', 'Refried Beans', 'Tex-Mex Questo', 'Naan', 'Basmati', 'Spicy Masala Lentils', 'Basmati Rice', 'Spicy Masala', 'Naan', 'Tamarind and Tomato Chutneys', 'Tamarind and Tomato Chutney', 'Aloo Chole', 'Fried Chicken Samosas', 'Vegetable Samosa', 'Tandoori Chicken Dumsticks', 'Steam Vegetables', 'Jasmine Rice', 'Steamed Broccoli & Carrots', 'Jasmine', 'Honey Chili Chicken Thighs', 'Vegetables & Tofu Soup', 'Honey Chili Glazed Chicken Thighs', 'Steamed Vegetable Gyozas with Yuzu Dipping Sauce', 'Vegetable & Tofu Soup', 'Buffalo Chicken Pizza with Blue Cheeese', 'Cauliflower Crust Buffalo Chicken & Blue Cheese Pizza', 'Buffalo Chicken with Blue Cheese Pizza', 'Roasted Vegetable Medley', 'Buffalo Chicken with Blue Cheese Pizza', 'Roasted Red Potatoes', 'Fresh Vegetable Medley', 'Roasted Baby Potatoes', 'Fresh Vegetable Medley', 'Black-Eyed Pea Stew with Braised Greens', 'Baked Cod Fillets with Caper Shrimp Cream Sauce', 'Baked Cod Filets, Caper Shrimp Cream Sauce', 'Black Eyed Pea Stew with Braised Greens', 'Beef & Chicken Meatballs', 'Fresh Vegetable Medley with Spicy Plant Based Sausage Crumble ']}, 
              'seibel-servery': {'LUNCH': ['Congee', 'Miso Soup', "Chef's Choice", 'Pasta of the Day', 'Marinara', 'Alfredo', 'Grilled Chicken', 'Arroz con Gandules ', 'Roasted Vegetables', 'Fried Yucca w/ Sofrito', 'Puerto Rican Baked Chicken Quarters', 'Pita Bread', 'Levant Salad/Yogurt Sauce', 'Lamb Beef Gyro ', 'Falafel (chickpea fritter)', '3 Cheese Pizza', 'Pepperoni', 'Roasted Vegetables', 'Ranchero Beans', 'Cheese Enchiladas', 'Pork Tamales'], 'DINNER': ['Congee', 'Miso Soup', "Chef's Choice", 'Pasta of the Day', 'Marinara', 'Alfredo', 'Grilled Chicken', 'Jollof Rice', 'Nigerian Eggplant Stew', 'Chakalaka', 'Piri Piri Chicken', 'Pita Bread', 'Levant Salad/Yogurt Sauce', 'Falafel (chickpea fritter)', 'Lamb Beef Gyro', '3 Cheese Pizza', 'Pepperoni', 'Chicken and Waffles', 'Bacon', 'Hash Browns', 'Scrambled Eggs']}, 
              'west-servery': {'LUNCH': [], 'DINNER': []}, 
              'north-servery': {'LUNCH': ['Baked Beans', 'Fresh Vegetables', 'Corn on The Cob', 'Mac & Cheese', 'BBQ Chicken Drumsticks', 'Vegetable of The Day', 'Jasmine Rice', 'Teriyaki Tofu Cutlets', 'Chicken Potstickers', 'Sweet & Sour Chicken', 'Jasmine Rice', 'Spicy PAOW Stir-Fry', 'Basmati Rice', 'Fresh Vegetables', 'Papadum', 'Lentil Masala', 'Garlic Naan', 'Swai Masala', 'Steamed Rice', 'Vegetable of The Day', 'Tortilla', 'Ranchero Beams', 'Beef Barbacoa', 'Pepperoni Pizza', 'Cheese Pizza', 'Gluten-Free Pizza', 'Assorted Cookies'], 'DINNER': ['Vegetable of The Day', 'Dinner Roll', 'Baked Beans', 'Smoked Pork Loins', 'Mac & Cheese', 'Vegetable of The Day', 'Jasmine Rice', 'Lime Soy Vinaigrette Tilapia', 'Teriyaki Meatball', 'WOK STATION CLOSED', 'Basmati Rice', 'Lentil Stew', 'Vegetable of The Day', 'Papadum', 'Garlic Naan', 'Butter Chicken', 'Pepperoni Pizza', 'Cheese Pizza', 'Supreme Pizza', 'Steamed Rice', 'Vegetable of The Day', 'Refried Beans', 'Beef Taquitos', 'Housemade Italian Bread', 'TX Roadhouse Styled Cinnamon Butter Spread', 'Assorted Desserts']}, 
              'baker-college-kitchen': {'LUNCH': [], 'DINNER': []}} #example

database = [["Tom", ["south-servery","seibel-servery", "west-servery", "north-servery", "baker-college-kitchen"], 
             ["potstickers"], 2027]] #name, serveries, keywords, grad

def single_user_dishes(entry):
    lst = []
    for servery in entry[1]:
        for keyword in entry[2]:
            if any(keyword in s.lower() for s in all_dishes[servery]["LUNCH"]):
                lst.append("There's "+keyword+" at "+servery+" for lunch.")
            if any(keyword in s.lower() for s in all_dishes[servery]["DINNER"]):
                lst.append("There's "+keyword+" at "+servery+" for dinner.")
    return lst

for entry in database:
    print(single_user_dishes(entry))
            