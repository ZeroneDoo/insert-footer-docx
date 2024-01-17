import requests

url = 'https://demo.gotenberg.dev/forms/libreoffice/convert'
files = [
    ('files', ('01. Schedule-Masking-NoFooter.docx', open('01. Schedule-Masking-NoFooter.docx', 'rb'))),
    ('files', ('02. 01234567 - Lampiran (IF ANY).xlsx', open('02. 01234567 - Lampiran (IF ANY).xlsx', 'rb'))),
    ('files', ('03. Wording-Masking-NoFooter.docx', open('03. Wording-Masking-NoFooter.docx', 'rb'))),
]
data = {
    "merge": "true"
}
response = requests.post(url, files=files, data=data)

# Accessing request details
# print(f"Request URL: {response.request.url}\n")
# print(f"Request Method: {response.request.method}\n")
# print(f"Request Headers: {response.request.headers}\n")
# print(f"Request Body: {response.request.body}\n")

# Accessing response details
# print(f"Response Status Code: {response.status_code}")
# print(f"Response Headers: {response.headers}")
# print(f"Response Content: {response.text}")

with open('out.pdf', 'wb') as output_file:
    output_file.write(response.content)