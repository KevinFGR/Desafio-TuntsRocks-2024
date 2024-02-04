import gspread

def main():
    file_key = 'key-file.json'
    google_account = gspread.service_account(filename = file_key)

    sheet_key = '13PW1hgkXhSs-qpwBvibQeXXT_q7cOWcPr3dAaV00k14'
    sheet = google_account.open_by_key(sheet_key)

    work_sheet = sheet.worksheet('engenharia_de_software')
    # getting all the values of the sheet page
    sheet_cells = work_sheet.get_all_values()

    # Get the information of the first column's cell in the second row
    total_classes = sheet_cells[1][0]
    # Separate the number of the text and remove possible spaces
    total_classes = total_classes.split(':')[1].strip()
    # finaly convert the inforamtion to integer
    total_classes = int(total_classes)

    # It means the start row of the values of the studants
    sheet_row = 4

    try:
        # updating the sheet's cells
        for row in sheet_cells[3:]:
            if(absence_rejected(total_classes ,row)):
                work_sheet.update_cell(sheet_row, 7, 'Reprovado por Falta')
                work_sheet.update_cell(sheet_row, 8, '0')
            else:
                new_values = grade_aproved(row)
                work_sheet.update_cell(sheet_row, 7, new_values[0])
                work_sheet.update_cell(sheet_row, 8, new_values[1])
            
            sheet_row += 1

        print('Worksheet successfully modified')

    except Exception as e:
        print('Something went wrong running the code. ')
        print(e)

# Calculates if the studant was rejected by being absence in more than 25% of classes
def absence_rejected(classes, row):
    #calculating the minimum of classes the studant had to be present
    minimun_presence = classes*0.25

    if int(row[2]) > minimun_presence:
        return True
    else:
        return False
        

# Calculates if the studant was aproved basing on his grade
def grade_aproved(row):
    # getting the grades and converting than to integer
    grades = row[3:6]
    # grades = row

    for i in range(len(grades)):
        grades[i] = int(grades[i])

    average = sum(grades)/3

    if average < 50:
        return ['Reprovado por Nota', '0']

    elif 50 <= average and  average < 70:
        grade_for_aprovation = 100 - average
        
        # Checking if the grade_for_aprovation needs to be rounded
        if (grade_for_aprovation*10)%10 != 0:
            grade_for_aprovation = str(int(grade_for_aprovation)+1)
        else:
            grade_for_aprovation = str(int(grade_for_aprovation))

        return ['Exame Final', grade_for_aprovation]

    elif average >= 70:
        return ['Aprovado','0']

    else:
        return ['ERROR','0']


if __name__ == "__main__":
    main()