from django.http import HttpResponse
from openpyxl import Workbook

def generate_excel(query):
  #fetch data from query 
  data = query

  # Create a new workbook
  wb = Workbook()
  ws = wb.active

    # Add headers
  ws.append(["Nomor Dokumen", "Column 2", "Column 3"])

    # Add data to the sheet
  for item in data:
      ws.append([item.field1, item.field2, item.field3])

    # Save the workbook
  response = HttpResponse(content_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet')
  response['Content-Disposition'] = 'attachment; filename=report.xlsx'
  wb.save(response)

  return response