from tkinter import ttk 
from Table_Find_Stock_Values import column_heading_name_list

class Table_Data:
    def __init__(self):
        return 
    def createTable(self,para1):
         # Create a style object for ttk widgets
        para1.style = ttk.Style(para1.main_window)


        # Configure our custom style for the Treeview widget
        para1.style.configure("Custom.Treeview",
        font=('Calibri', 12), background="#d4f2db",
        foreground="black", rowheight=25, fieldbackground="#D3D3D3")

        para1.style.configure("Custom.Treeview.Heading", 
        font=('Calibri', 18, 'bold'), 
        foreground="green")
        

        # Create the Treeview widget with the custom style
        para1.tree_table = ttk.Treeview(para1.main_window, style="Custom.Treeview")

        para1.tree_table["columns"] = ("Column 1","Column 2","Column 3","Column 4","Column 5","Column 6","Column 7","Column 8","Column 9")
    


    def stylingTable(self,tk,para1):

        # Format the columns
        para1.tree_table.column("#0", width=0, stretch=tk.NO)
        for col in range(len(column_heading_name_list)):
            para1.tree_table.column(para1.tree_table["columns"][col], anchor=tk.W, width=150)

        # Create headings
        para1.tree_table.heading("#0", text="", anchor=tk.W)
        for col_head in range(len(column_heading_name_list)):
            para1.tree_table.heading(f"Column {col_head+1}",text=column_heading_name_list[col_head], anchor=tk.W)


TableData_obj = Table_Data()