import tkinter as tk
from tkinter import messagebox

# List to store contact data
contacts = []

def insert_window():
    insert_win = tk.Toplevel(root)
    insert_win.title("Insert Contact")

    # Entry fields for contact details
    name_label = tk.Label(insert_win, text="Name:")
    name_entry = tk.Entry(insert_win)
    tel_label = tk.Label(insert_win, text="Telephone:")
    tel_entry = tk.Entry(insert_win)
    mobile_label = tk.Label(insert_win, text="Mobile:")
    mobile_entry = tk.Entry(insert_win)
    email_label = tk.Label(insert_win, text="Email:")
    email_entry = tk.Entry(insert_win)

    def save_contact():
        name = name_entry.get()
        tel = tel_entry.get()
        mobile = mobile_entry.get()
        email = email_entry.get()
        contacts.append((name, tel, mobile, email))
        messagebox.showinfo("Contact Saved", f"Contact saved for {name}")
        insert_win.destroy()  # Close the insert window
        display_contacts()  # Update the list of contacts in the main window

    save_button = tk.Button(insert_win, text="Save", command=save_contact)
    cancel_button = tk.Button(insert_win, text="Cancel", command=insert_window)

    # Grid layout
    name_label.grid(row=0, column=0)
    name_entry.grid(row=0, column=1)
    tel_label.grid(row=1, column=0)
    tel_entry.grid(row=1, column=1)
    mobile_label.grid(row=2, column=0)
    mobile_entry.grid(row=2, column=1)
    email_label.grid(row=3, column=0)
    email_entry.grid(row=3, column=1)
    save_button.grid(row=4, columnspan=2)
    cancel_button.grid(row=5, columnspan=2)

def sort_contacts():
    
    contacts.sort(key=lambda x: x[0])  # Sort by name
    display_contacts()

def search_window():
    search_win = tk.Toplevel(root)
    search_win.title("Search Contact")

    search_label = tk.Label(search_win, text="Enter Name:")
    search_entry = tk.Entry(search_win)

    def search_contact():
        name_to_search = search_entry.get()
        found_contacts = [c for c in contacts if c[0].lower() == name_to_search.lower()]
        if found_contacts:
            contact = found_contacts[0]
            messagebox.showinfo("Contact Details", f"Name: {contact[0]}\nTelephone: {contact[1]}\nMobile: {contact[2]}\nEmail: {contact[3]}")
        else:
            messagebox.showinfo("Contact Not Found", f"No contact found for {name_to_search}")

    search_button = tk.Button(search_win, text="Search", command=search_contact)

    search_label.grid(row=0, column=0)
    search_entry.grid(row=0, column=1)
    search_button.grid(row=1, columnspan=2)

def delete_contact():
    selected_contact = contacts_listbox.curselection()
    if selected_contact:
        index = selected_contact[0]
        del contacts[index]
        display_contacts()

def display_contacts():
    contacts_listbox.delete(0, tk.END)
    for contact in contacts:
        contacts_listbox.insert(tk.END, contact[0])

# Create the main window
root = tk.Tk()
root.title("Phone NoteBook")

# Listbox to display contacts
contacts_listbox = tk.Listbox(root, selectmode=tk.SINGLE)
contacts_listbox.grid(row=0, column=0, rowspan=4)

# Buttons for insert, search, sort, and delete
insert_button = tk.Button(root, text="Insert", command=insert_window)
search_button = tk.Button(root, text="Search", command=search_window)
sort_button = tk.Button(root, text="Sort", command=sort_contacts)
delete_button = tk.Button(root, text="Delete", command=delete_contact)

insert_button.grid(row=0, column=1)
search_button.grid(row=1, column=1)
sort_button.grid(row=2, column=1)
delete_button.grid(row=3, column=1)

root.mainloop()