import pandas as pd
import re
from pathlib import Path


# ==========================================
# INPUT AND OUTPUT FOLDER
# ==========================================

input_folder = Path("Input")
output_folder = Path("Output")


# ==========================================
# REQUIRED COLUMNS
# ==========================================

required_columns = [
    "First Name",
    "Last Name",
    "Email",
    "Phone Number"
]


# ==========================================
# NAME VALIDATION
# ==========================================

def validate_name(first_name, last_name):

    if pd.isna(first_name) or str(first_name).strip() == "":
        return "Name Missing"

    if pd.isna(last_name) or str(last_name).strip() == "":
        return "Name Missing"

    return "Valid"


# ==========================================
# EMAIL VALIDATION
# ==========================================

def validate_email(email):

    if pd.isna(email) or str(email).strip() == "":
        return "Email Missing"

    email = str(email).strip()

    pattern = r"^[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}$"

    if re.fullmatch(pattern, email):
        return "Valid"

    return "Invalid Email"


# ==========================================
# MOBILE VALIDATION
# ==========================================

def validate_mobile(phone):

    if pd.isna(phone) or str(phone).strip() == "":
        return "Mobile Missing"

    phone = str(phone).strip()

    # Exactly 10 digits
    # First digit must be 6, 7, 8 or 9
    if re.fullmatch(r"[6-9][0-9]{9}", phone):
        return "Valid"

    return "Invalid Mobile"


# ==========================================
# FIND ALL EXCEL FILES
# ==========================================

excel_files = list(input_folder.rglob("*.xlsx"))

print("Total Excel files:", len(excel_files))


# ==========================================
# PROCESS EACH FILE
# ==========================================

for file in excel_files:

    print("\n========================================")
    print("Processing:", file)
    print("========================================")

    try:

        # ==================================
        # READ EXCEL
        # ==================================

        df = pd.read_excel(file)

        # Clean column names
        df.columns = df.columns.str.strip()


        # ==================================
        # CHECK REQUIRED COLUMNS
        # ==================================

        missing_columns = [
            column
            for column in required_columns
            if column not in df.columns
        ]

        if missing_columns:

            print("\nMISSING COLUMNS:")
            print(missing_columns)

            print("\nFILE STATUS: INVALID")

            continue


        # ==================================
        # NAME VALIDATION
        # ==================================

        df["Name Validation"] = df.apply(
            lambda row: validate_name(
                row["First Name"],
                row["Last Name"]
            ),
            axis=1
        )


        # ==================================
        # EMAIL VALIDATION
        # ==================================

        df["Email Validation"] = df["Email"].apply(
            validate_email
        )


        # ==================================
        # MOBILE VALIDATION
        # ==================================

        df["Mobile Validation"] = df["Phone Number"].apply(
            validate_mobile
        )


        # ==================================
        # COUNT VALID / INVALID
        # ==================================

        total_records = len(df)

        valid_names = (
            df["Name Validation"] == "Valid"
        ).sum()

        invalid_names = (
            df["Name Validation"] != "Valid"
        ).sum()

        valid_emails = (
            df["Email Validation"] == "Valid"
        ).sum()

        invalid_emails = (
            df["Email Validation"] != "Valid"
        ).sum()

        valid_mobiles = (
            df["Mobile Validation"] == "Valid"
        ).sum()

        invalid_mobiles = (
            df["Mobile Validation"] != "Valid"
        ).sum()


        # ==================================
        # FILE STATUS
        # ==================================

        all_valid = (
            invalid_names == 0
            and
            invalid_emails == 0
            and
            invalid_mobiles == 0
        )


        # ==================================
        # PRINT SUMMARY
        # ==================================

        print("\nVALIDATION SUMMARY")
        print("-----------------------------")

        print("Total Records :", total_records)

        print(
            "Name          :",
            valid_names,
            "Valid |",
            invalid_names,
            "Invalid"
        )

        print(
            "Email         :",
            valid_emails,
            "Valid |",
            invalid_emails,
            "Invalid"
        )

        print(
            "Mobile        :",
            valid_mobiles,
            "Valid |",
            invalid_mobiles,
            "Invalid"
        )


        # ==================================
        # FINAL FILE STATUS
        # ==================================

        if all_valid:

            print("\n=============================")
            print("FILE STATUS: VALID")
            print("=============================")

        else:

            print("\n=============================")
            print("FILE STATUS: INVALID")
            print("=============================")


        # ==================================
        # CREATE OUTPUT FOLDER
        # ==================================

        relative_path = file.relative_to(input_folder)

        output_dir = (
            output_folder /
            relative_path.parent
        )

        output_dir.mkdir(
            parents=True,
            exist_ok=True
        )


        # ==================================
        # SAVE VALIDATED FILE
        # ==================================

        validated_file = (
            output_dir /
            f"{file.stem}_validated.xlsx"
        )

        df.to_excel(
            validated_file,
            index=False
        )

        print(
            "\nValidated file:",
            validated_file
        )


        # ==================================
        # FIND INVALID RECORDS
        # ==================================

        invalid_records = df[
            (df["Name Validation"] != "Valid")
            |
            (df["Email Validation"] != "Valid")
            |
            (df["Mobile Validation"] != "Valid")
        ]


        # ==================================
        # SAVE INVALID RECORDS
        # ==================================

        if not invalid_records.empty:

            invalid_file = (
                output_dir /
                f"{file.stem}_invalid.xlsx"
            )

            invalid_records.to_excel(
                invalid_file,
                index=False
            )

            print(
                "Invalid records:",
                invalid_file
            )

        else:

            print(
                "No invalid records found."
            )


    except Exception as error:

        print("\nERROR processing file:")
        print(file)

        print("Reason:", error)

        print("\nFILE STATUS: INVALID")


# ==========================================
# COMPLETE
# ==========================================

print("\n========================================")
print("All Excel files processed!")
print("========================================")