import pandas

excel_data = pandas.read_excel('Recipients data.xlsx', sheet_name='Recipients')

count = 0

input("Press ENTER after login into Whatsapp Web and your chats are visiable.")
for column in excel_data['Contact'].tolist():
    name = excel_data['Name'][count]
    number = f"+98{str(excel_data['Contact'][count])}"
    message = f"hello {name} to {number}"
    print(message)