def calculate_marks(maths, science, marathi, english, hindi):
    print(f"maths = {maths}" )
    print(f"science = {science}" )
    print(f"marathi = {marathi}" )
    print(f"english = {english}" )
    print(f"hindi = {hindi}" )
    total_marks = maths + science + marathi + english + hindi
    print(f"Total marks are: {total_marks}")

calculate_marks(science=40, maths=50, hindi=45, marathi=70, english=50)