import json
import os

# File to store complaints
FILE_NAME = "complaints.json"

# Load existing complaints
def load_complaints():
    if os.path.exists(FILE_NAME):
        with open(FILE_NAME, "r") as f:
            try:
                return json.load(f)
            except json.JSONDecodeError:
                return {}
    return {}

# Save complaints
def save_complaints(data):
    with open(FILE_NAME, "w") as f:
        json.dump(data, f, indent=4)

# Register a new complaint
def register_complaint(data):
    complaint_id = str(len(data) + 1)
    name = input("Enter your name: ")

    print("\nChoose Complaint Category:")
    print("1. Academic")
    print("2. Hostel")
    print("3. Technical")
    print("4. Other")
    choice = input("Enter choice: ")
    categories = {"1": "Academic", "2": "Hostel", "3": "Technical", "4": "Other"}
    category = categories.get(choice, "Other")

    complaint_text = input("Enter your complaint: ")

    data[complaint_id] = {
        "Name": name,
        "Category": category,
        "Complaint": complaint_text,
        "Status": "Pending"
    }

    save_complaints(data)
    print(f"\n✅ Complaint registered successfully! Your Complaint ID is {complaint_id}\n")

# View all complaints
def view_complaints(data):
    if not data:
        print("\nNo complaints found.\n")
        return
    
    print("\n📋 All Complaints:\n")
    for cid, details in data.items():
        print(f"ID: {cid} | Name: {details['Name']} | Category: {details['Category']} | "
              f"Complaint: {details['Complaint']} | Status: {details['Status']}")

# Update complaint status (Admin use)
def update_status(data):
    cid = input("Enter Complaint ID to update: ")
    if cid in data:
        print("Choose new status:")
        print("1. Pending")
        print("2. In Progress")
        print("3. Resolved")
        choice = input("Enter choice: ")

        status_map = {"1": "Pending", "2": "In Progress", "3": "Resolved"}
        data[cid]["Status"] = status_map.get(choice, "Pending")
        
        save_complaints(data)
        print("\n✅ Status updated successfully!\n")
    else:
        print("\n❌ Complaint ID not found!\n")

# Main Menu
def main():
    complaints = load_complaints()
    
    while True:
        print("\n====== Complaint Portal ======")
        print("1. Register Complaint")
        print("2. View Complaints")
        print("3. Update Complaint Status (Admin)")
        print("4. Exit")
        
        choice = input("Enter your choice: ")
        
        if choice == "1":
            register_complaint(complaints)
        elif choice == "2":
            view_complaints(complaints)
        elif choice == "3":
            update_status(complaints)
        elif choice == "4":
            print("👋 Exiting Complaint Portal. Goodbye!")
            break
        else:
            print("❌ Invalid choice. Please try again.")

# ✅ Correct main entry point
if __name__ == "_main_":
    main()