import datetime

STUDENT = 'Student'
TEACHER = 'Teacher'
ADMIN = 'Admin'

SUBJECT_NAME_MAX_LENGTH = 30
COLOR_MAX_LENGTH = 7
COLOR_DEFAULT = '#007bff'

QUIZ_NAME_MAX_LENGTH = 30

QUESTION_MAX_LENGTH = 200

OPTIONS_MAX_LENGTH = 30
OPTION_1 = 'A'
OPTION_2 = 'B'
OPTION_3 = 'C'
OPTION_4 = 'D'

OPTIONS_MAPPER = {
    0: OPTION_1,
    1: OPTION_2,
    2: OPTION_3,
    3: OPTION_4
}

TEXT_MAX_LENGTH = 30

TIME_MIN_VALUE = 1

VALID_EVENT_DATA = {
        'title': 'Test Event',
        'description': 'Test Event Description' * 10,
        'date': datetime.datetime(3022, 1, 1, 0, 0),
    }