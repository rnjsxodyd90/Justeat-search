import tkinter as tk
from tkinter import ttk
from app.utils import get_restaurants  # Reuse API fetch + processing logic

# Main GUI Class
class RestaurantBrowser:
    def __init__(self, root):
        self.root = root
        self.root.title("Just Eat Restaurant Viewer")

        # Input and UI state
        self.postcode = tk.StringVar(value="M160RA")            # default postcode
        self.sort_option = tk.StringVar(value="Rating (High → Low)")  # default sort
        self.restaurants = []                                   # stores restaurant data
        self.current_index = 0                                  # used to paginate 3 at a time

        self.setup_ui()  # Build  UI

    def setup_ui(self):
        # Top input section with postcode and sort dropdown
        control_frame = ttk.Frame(self.root)
        control_frame.pack(pady=10)

        ttk.Label(control_frame, text="Postcode:").pack(side=tk.LEFT)
        ttk.Entry(control_frame, textvariable=self.postcode, width=10).pack(side=tk.LEFT, padx=5)
        ttk.Button(control_frame, text="Search", command=self.load_restaurants).pack(side=tk.LEFT, padx=5)

        ttk.Label(control_frame, text="Sort by:").pack(side=tk.LEFT, padx=(15, 0))
        sort_menu = ttk.Combobox(
            control_frame,
            textvariable=self.sort_option,
            values=[
                "Rating (High → Low)",
                "Name (A → Z)",
                "Delivery Cost (Low → High)"
            ],
            state="readonly",
            width=25
        )
        sort_menu.pack(side=tk.LEFT)

        # Main result area (cards are rendered here)
        self.result_frame = ttk.Frame(self.root)
        self.result_frame.pack(padx=10, pady=10, fill=tk.BOTH, expand=True)

        # Navigation buttons at the bottom
        nav_frame = ttk.Frame(self.root)
        nav_frame.pack(pady=10)

        self.prev_btn = ttk.Button(nav_frame, text="← Previous 3", command=self.show_previous)
        self.prev_btn.pack(side=tk.LEFT, padx=5)

        self.next_btn = ttk.Button(nav_frame, text="Next 3 →", command=self.show_next)
        self.next_btn.pack(side=tk.LEFT, padx=5)

    # Fetch and display restaurants
    def load_restaurants(self):
        self.current_index = 0
        postcode = self.postcode.get().strip().replace(" ", "")
        self.restaurants = get_restaurants(postcode)  # API call
        self.sort_restaurants()                       # sort before showing
        self.show_restaurants()

    #  Sorting based on dropdown value
    def sort_restaurants(self):
        option = self.sort_option.get()
        if option == "Rating (High → Low)":
            self.restaurants.sort(key=lambda r: r.get("rating", 0), reverse=True)
        elif option == "Name (A → Z)":
            self.restaurants.sort(key=lambda r: r.get("name", "").lower())
        elif option == "Delivery Cost (Low → High)":
            self.restaurants.sort(key=lambda r: r.get("delivery_cost", float('inf')))

    #  Render restaurant cards (3 at a time)
    def show_restaurants(self):
        for widget in self.result_frame.winfo_children():
            widget.destroy()  # 🔄 clear previous results

        #  get current page of 3 results
        sliced = self.restaurants[self.current_index:self.current_index + 3]
        if not sliced:
            ttk.Label(self.result_frame, text="No restaurants found.").pack()
            return

        for r in sliced:
            #  Create a card for each restaurant
            card = ttk.LabelFrame(self.result_frame, text=r['name'], padding=10)
            card.pack(fill="x", expand=True, pady=5)

            #  Halal with flag
            if r["halal"]:
                halal_text = "✔ Halal" + (f" {r['flag']}" if r.get("flag") else "")
                ttk.Label(card, text=halal_text, foreground="green").pack(anchor="w")

            #  Cuisines
            ttk.Label(card, text="Cuisines: " + ", ".join(r["cuisines"])).pack(anchor="w")

            #  Star rating
            stars = "⭐" * int(round(r["rating"])) + "☆" * (5 - int(round(r["rating"])))
            ttk.Label(card, text=f"Rating: {stars} ({r['rating']})").pack(anchor="w")

            #  Delivery cost
            if r.get("delivery_cost") is not None:
                ttk.Label(card, text=f"Delivery: £{r['delivery_cost']:.2f}").pack(anchor="w")

            #  Address
            ttk.Label(card, text="Address: " + r["address"]).pack(anchor="w")

    #  Go to next batch of 3 restaurants
    def show_next(self):
        if self.current_index + 3 < len(self.restaurants):
            self.current_index += 3
            self.show_restaurants()

    # Go to previous batch
    def show_previous(self):
        if self.current_index - 3 >= 0:
            self.current_index -= 3
            self.show_restaurants()


# Start the app
if __name__ == "__main__":
    root = tk.Tk()
    app = RestaurantBrowser(root)
    root.mainloop()
