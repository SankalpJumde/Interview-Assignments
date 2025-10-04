import datetime
import json
import os
import csv

OUTPUT_DIR = "outputs"
os.makedirs(OUTPUT_DIR, exist_ok=True)

def input_float(prompt, default=0.0):
    """Helper to safely input a float value"""
    while True:
        v = input(prompt).strip()
        if v == "" and default is not None:
            return float(default)
        try:
            return float(v)
        except ValueError:
            print("⚠️ Please enter a valid number.")

def input_nonempty(prompt):
    while True:
        v = input(prompt).strip()
        if v:
            return v

# ----------------- Collect Inputs -----------------

def collect_daily_expenses():
    print("\n--- Daily Expenses (per day) ---")
    daily = {
        "Food": input_float("Food (₹/day): "),
        "Travel": input_float("Travel (₹/day): "),
        "Shopping": input_float("Shopping (₹/day): "),
        "Grocery": input_float("Grocery (₹/day): "),
    }
    other_amt = input_float("Other (₹/day, 0 if none): ", 0.0)
    daily["Others"] = {}
    if other_amt > 0:
        purpose = input_nonempty("  Mention purpose (e.g., coffee, snacks): ")
        daily["Others"][purpose] = other_amt
    return daily

def collect_weekly_expenses():
    print("\n--- Weekly Expenses (per week) ---")
    weekly = {
        "Food": input_float("Food (₹/week): "),
        "Travel": input_float("Travel (₹/week): "),
        "Shopping": input_float("Shopping (₹/week): "),
        "Grocery": input_float("Grocery (₹/week): "),
    }
    other_amt = input_float("Other (₹/week, 0 if none): ", 0.0)
    weekly["Others"] = {}
    if other_amt > 0:
        purpose = input_nonempty("  Mention purpose (e.g., trip, picnic): ")
        weekly["Others"][purpose] = other_amt
    return weekly

def collect_monthly_expenses():
    print("\n--- Monthly Expenses (per month) ---")
    monthly = {
        "Mobile Recharge": input_float("Mobile recharge (₹/month): "),
        "WiFi Recharge": input_float("WiFi recharge (₹/month): "),
        "Rent": input_float("Rent (₹/month): "),
        "Grocery": input_float("Grocery (₹/month): "),
        "Entertainment": input_float("Entertainment (movies, arcade, etc.) (₹/month): "),
        "Gym Membership": input_float("Gym membership (₹/month): "),
        "Shopping": input_float("Shopping (₹/month): "),
    }
    # OTT subscriptions
    monthly["OTT"] = {}
    print("\nEnter OTT subscriptions (enter 'done' to finish):")
    while True:
        name = input("  OTT name: ").strip()
        if name.lower() in ("done", ""):
            break
        amt = input_float(f"    Amount for {name} (₹/month): ")
        monthly["OTT"][name] = amt

    # Food delivery orders
    food_delivery = input_float("Food delivery (₹/month): ")
    sub = input("Do you have subscription for food delivery? (y/n): ").strip().lower()
    monthly["Food Delivery"] = {"Orders": food_delivery}
    if sub == "y":
        sub_amt = input_float("  Subscription cost (₹/month): ")
        monthly["Food Delivery"]["Subscription"] = sub_amt

    # Other monthly
    other_amt = input_float("Other monthly (₹/month, 0 if none): ")
    monthly["Others"] = {}
    if other_amt > 0:
        purpose = input_nonempty("  Mention purpose (e.g., insurance, loan EMI): ")
        monthly["Others"][purpose] = other_amt

    return monthly

# ----------------- Computations -----------------

def compute_totals(daily, weekly, monthly):
    # Daily total
    daily_total = sum([v for k, v in daily.items() if k != "Others"])
    daily_total += sum(daily["Others"].values())

    # Weekly total
    weekly_total = sum([v for k, v in weekly.items() if k != "Others"])
    weekly_total += sum(weekly["Others"].values())

    # Monthly total
    monthly_total = 0
    for k, v in monthly.items():
        if isinstance(v, dict):
            monthly_total += sum(v.values())
        else:
            monthly_total += v

    return {
        "daily_total": daily_total,
        "weekly_total": weekly_total,
        "monthly_total": monthly_total
    }

# ----------------- Output -----------------

def print_summary(daily, weekly, monthly, totals):
    print("\n\n=== Expense Summary ===")

    print("\nDaily Expenses:")
    for k, v in daily.items():
        if k == "Others":
            for purpose, amt in v.items():
                print(f"  {k} ({purpose}): ₹{amt}")
        else:
            print(f"  {k}: ₹{v}")
    print(f"Total Daily: ₹{totals['daily_total']}")

    print("\nWeekly Expenses:")
    for k, v in weekly.items():
        if k == "Others":
            for purpose, amt in v.items():
                print(f"  {k} ({purpose}): ₹{amt}")
        else:
            print(f"  {k}: ₹{v}")
    print(f"Total Weekly: ₹{totals['weekly_total']}")

    print("\nMonthly Expenses:")
    for k, v in monthly.items():
        if isinstance(v, dict):
            for subk, amt in v.items():
                print(f"  {k} ({subk}): ₹{amt}")
        else:
            print(f"  {k}: ₹{v}")
    print(f"Total Monthly: ₹{totals['monthly_total']}")

def save_summary(daily, weekly, monthly, totals):
    ts = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
    data = {"daily": daily, "weekly": weekly, "monthly": monthly, "totals": totals}
    filename = os.path.join(OUTPUT_DIR, f"expense_summary_{ts}.json")
    with open(filename, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2, ensure_ascii=False)
    print(f"\n✅ Saved summary to {filename}")

    # Also save CSV quick summary
    csv_file = os.path.join(OUTPUT_DIR, f"expense_summary_{ts}.csv")
    with open(csv_file, "w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow(["Category", "Amount"])
        writer.writerow(["Daily Total", totals["daily_total"]])
        writer.writerow(["Weekly Total", totals["weekly_total"]])
        writer.writerow(["Monthly Total", totals["monthly_total"]])
    print(f"✅ Saved CSV to {csv_file}")

# ----------------- Main -----------------

def main():
    print("Welcome to Personal Expense Tracker\n")

    daily = collect_daily_expenses()
    weekly = collect_weekly_expenses()
    monthly = collect_monthly_expenses()

    totals = compute_totals(daily, weekly, monthly)
    print_summary(daily, weekly, monthly, totals)

    save = input("\nSave results to file? (y/n): ").strip().lower()
    if save == "y":
        save_summary(daily, weekly, monthly, totals)

if __name__ == "__main__":
    main()
