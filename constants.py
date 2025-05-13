# String constants
# Note: SonarQube did not like that some strings were used multiple times, so we created variables for the strings
required_gpa_copy = "Required GPA"
scholarship_id_copy = "Scholarship ID"
applicant_pronoun_copy = "Applicant Pronoun"
applicant_first_name_copy = "Applicant First Name"
applicant_last_name_copy = "Applicant Last Name"
scholarship_name_copy = "Scholarship Name"
student_id_copy = "Student ID"
applicant_id_copy = "Applicant ID"
academic_achievements_copy = "Academic Achievements"
financial_info_copy = "Financial Info"
written_essay_copy = "Written Essay"
work_experience_copy = "Work Experience"
first_name_copy = 'First Name'
last_name_copy = 'Last Name'
email_address_copy = 'Email Address'
applicant_first_name_apos = 'Applicant First Name'
applicant_last_name_apos = 'Applicant Last Name'
scholarship_id_apos = 'Scholarship ID'
applicant_id_apos = 'Applicant ID'
arch_scholarship_html = 'archive_scholarship.html'
app_search_html = 'applicant_search.html'
full_name_copy = "Full Name"

# CSV file paths
accounts_csv = "./storage/accounts.csv"
applications_csv = "./storage/applications.csv"
scholarships_csv = "./storage/scholarships.csv"
students_csv = "./storage/students.csv"
unapproved_accounts_csv = "./storage/unapproved_accounts.csv"
decisions_csv = "./storage/decisions.csv"
archived_csv = "./storage/archivedscholarships.csv"

# File Upload constants
UPLOAD_FOLDER = "./storage/documents"
ALLOWED_EXTENSIONS = {'pdf', 'docx'}

# Email constants
EMAIL_ADDRESS = 'addemailaddresshere'
EMAIL_PASSWORD = 'addpasswordfromaccount'
SMTP_SERVER = 'smtp.example.com'
SMTP_PORT = 587

#application_fields used with filter_applications function
application_fields = [
    scholarship_id_apos, applicant_first_name_apos, applicant_last_name_apos, 'Applicant Pronoun', applicant_id_apos,
    'Applicant Net ID', 'Major', 'Minor', 'GPA', 'Year', 'Ethnicity', 'Academic Achievements',
    'Financial Info', 'Written Essay', 'Work Experience'
]