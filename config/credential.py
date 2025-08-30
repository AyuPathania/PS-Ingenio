import pytest

@pytest.fixture(scope="function")
def credentials(test_data):
    return {
    'tc_01': {
        'user': test_data['user']['tc_01'],
        'advisor': test_data['advisor']['Hubert']
    },
    'tc_02': {
        'user': test_data['user']['tc_02'],
        'advisor': test_data['advisor']['tetsLanguageOrder']
    },
    'tc_03': {
        'user': test_data['user']['tc_03'],
        'advisor': test_data['advisor']['tetsLanguageOrder']
    },
    'tc_04': {
        'user': test_data['user']['tc_04'],
        'advisor': test_data['advisor']['tetsLanguageOrder']
    },
    'tc_05': {
        'user': test_data['user']['tc_05'],
        'advisor': test_data['advisor']['tetsLanguageOrder']
    },
    'tc_06': {
        'user': test_data['user']['tc_06'],
        'advisor': test_data['advisor']['tetsLanguageOrder']
    },
    'tc_07': {
        'user': test_data['user']['tc_07'],
        'advisor': test_data['advisor']['tetsLanguageOrder']
    },
    'tc_08': {
        'user': test_data['user']['tc_08'],
        'advisor': test_data['advisor']['tetsLanguageOrder']
    },
    'tc_09': {
        'user': test_data['user']['tc_09'],
        'advisor': test_data['advisor']['tetsLanguageOrder']
    },
    'tc_10': {
        'user': test_data['user']['tc_10'],
        'advisor': test_data['advisor']['tetsLanguageOrder']
    },
    'tc_11': {
        'user': test_data['user']['tc_11'],
        'advisor': test_data['advisor']['tetsLanguageOrder']
    },
    'tc_12': {
        'user': test_data['user']['tc_12'],
        'advisor': test_data['advisor']['tetsLanguageOrder']
    },
    'tc_13': {
        'user': test_data['user']['tc_13'],
        'advisor': test_data['advisor']['tetsLanguageOrder']
    }
}