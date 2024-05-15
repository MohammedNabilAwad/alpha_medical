def patient():

    return {
        "Patient": [
            {
                "fieldname": "patient_history",
                "fieldtype": "Tab Break",
                "label": "Patient History",
                "insert_after": "patient_details",
            },
            {
                "fieldname": "offspring",
                "fieldtype": "Int",
                "label": "Offspring",
                "insert_after": "patient_history",
                "ignore_user_permissions": 1,
            },
            {
                "fieldname": "special_habits_table",
                "fieldtype": "Table",
                "label": "Special Habits",
                "options": "Special Habits Table",
                "insert_after": "offspring",
                "ignore_user_permissions": 1,
            },
            {
                "fieldname": "handedness",
                "fieldtype": "Select",
                "label": "Handedness",
                "options": "\nLeft Handedness\nRight Handedness",
                "insert_after": "special_habits_table",
                "ignore_user_permissions": 1,
            },
            {
                "fieldname": "source_informaion",
                "fieldtype": "Data",
                "label": "Source of Informaion",
                "insert_after": "handedness",
                "ignore_user_permissions": 1,
            },
            {
                "fieldname": "chief_complain",
                "fieldtype": "Link",
                "label": "Chief Complaint",
                "options": "Complaint",
                "insert_after": "source_informaion",
                "ignore_user_permissions": 1,
            },
            {
                "fieldname": "since",
                "fieldtype": "Data",
                "label": "Since",
                "insert_after": "chief_complain",
                "ignore_user_permissions": 1,
            },
            {
                "fieldname": "analysis_chief_complaint",
                "fieldtype": "Text Editor",
                "label": "Analysis of Chief Complaint",
                "insert_after": "since",
                "ignore_user_permissions": 1,
            },
            {
                "fieldname": "involved_system_analysis",
                "fieldtype": "Tab Break",
                "label": "Involved system analysis",
                "insert_after": "analysis_chief_complaint",
            },
            {
                "fieldname": "cardiovascular_System",
                "fieldtype": "Table",
                "label": "Cardiovascular System",
                "options": "Cardiovascular System Table",
                "insert_after": "involved_system_analysis",
                "ignore_user_permissions": 1,
            },
            {
                "fieldname": "review_of_other_system",
                "fieldtype": "Table",
                "label": "Review of other system",
                "options": "Review of other system Table",
                "insert_after": "cardiovascular_System",
                "ignore_user_permissions": 1,
            },
            {
                "fieldname": "chronic_diseases",
                "fieldtype": "Table",
                "label": "Chronic Diseases",
                "options": "Chronic Diseases Table",
                "insert_after": "review_of_other_system",
                "ignore_user_permissions": 1,
            },
            {
                "fieldname": "past_history_tab",
                "fieldtype": "Tab Break",
                "label": "Past History",
                "insert_after": "chronic_diseases",
            },
            {
                "fieldname": "past_history",
                "fieldtype": "Table",
                "label": "Past History",
                "options": "Past History Table",
                "insert_after": "past_history_tab",
                "ignore_user_permissions": 1,
            },
            {
                "fieldname": "family_history_tab",
                "fieldtype": "Tab Break",
                "label": "Family History",
                "insert_after": "past_history",
            },
            {
                "fieldname": "family_history",
                "fieldtype": "Table",
                "label": "Family History",
                "options": "Family History Table",
                "insert_after": "family_history_tab",
                "ignore_user_permissions": 1,
            },
        ]
    }

