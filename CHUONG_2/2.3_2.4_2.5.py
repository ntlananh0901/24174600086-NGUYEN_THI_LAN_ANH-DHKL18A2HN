from xml.dom import minidom

# Đọc và phân tích file XML
doc = minidom.parse("sample.xml")
print("Phân tích thành công!")
#2.4 Lấy và in tên công ty từ file XML
company_name = doc.getElementsByTagName("name")[0].firstChild.data
print("Tên công ty:", company_name)
#2.5  in thông tin nhân viên từ file XML
staff_list = doc.getElementsByTagName("staff")

print("Danh sách nhân viên:")
for staff in staff_list:
    name = staff.getElementsByTagName("name")[0].firstChild.data
    print("-", name)