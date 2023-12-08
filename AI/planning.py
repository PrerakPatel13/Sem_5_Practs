class Action:
    def __init__(self, name, preconditions, effects):
        self.name = name
        self.preconditions = preconditions
        self.effects = effects

def total_order_planning(actions, goal):
    plan = []
    current_state = set()
    while not goal <= current_state:
        added = False
        for action in actions:
            if action not in plan and action.preconditions <= current_state:
                plan.append(action)
                current_state |= action.effects
                added = True
                break
        if not added:
            print("Goal cannot be achieved.")
            return None
    return plan

# Define actions with their preconditions and effects for making a burger
burger_actions = [
    Action("Buy Burger Buns", set(), {"Burger Buns"}),
    Action("Cook Patty", set(), {"Cooked Patty"}),
    Action("Slice Tomatoes", set(), {"Sliced Tomatoes"}),
    Action("Shred Lettuce", set(), {"Shredded Lettuce"}),
    Action("Grill Onions", set(), {"Grilled Onions"}),
    Action("Add Sauce to Patty", {"Cooked Patty"}, {"Patty with Sauce"}),
    Action("Add Cheese to Patty", {"Patty with Sauce"}, {"Burger Patty with Cheese"}),
    Action("Assemble Burger", {"Burger Buns", "Burger Patty with Cheese", "Sliced Tomatoes", "Shredded Lettuce", "Grilled Onions"},
            {"Burger"}),
]

burger_goal = {"Burger"}
burger_plan = total_order_planning(burger_actions, burger_goal)

if burger_plan:
    print("Total Order Plan for Burger:")
    for action in burger_plan:
        print(action.name)
