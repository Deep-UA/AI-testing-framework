
def test_ai_first(gemini_client, time_tracker):
    actual_response = gemini_client.ask('List all the useful features of Pytest? Answer in 2 sentences')
    expected_words = ['fixtures', 'assertion', 'test', 'parameterization']
    key_words_found = []
    counter = 0
    for words in actual_response.lower().split():
        if words in expected_words:
            counter += 1
            key_words_found.append(words)
    missing_words = [word for word in expected_words if word not in key_words_found]
    assert counter >=3, f"More than one keyword is missing:{missing_words}"

def test_single_sentence_answer(gemini_client):
    actual_response = gemini_client.ask('What is Pytest? Answer in 1 sentence')
    end_marks = actual_response.count('.') + actual_response.count('!') + actual_response.count('?')
    assert end_marks == 1, f"Expected 1 sentence, but found {end_marks}"
