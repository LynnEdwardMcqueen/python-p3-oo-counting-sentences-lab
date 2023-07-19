#!/usr/bin/env python3

class MyString:
    def __init__(self, value = "foo"):
        self.set_value(value)
        return


    def set_value(self, value):
        if type (value) == str :
            self._value = value
        else:
            print("The value must be a string.")
        return
       
    def get_value(self):
        return self._value
        
    
    def is_sentence(self):
        return self._value[-1] == '.'
    
    def is_question(self):
        return self._value[-1] == '?'
    
    def is_exclamation(self):
        return self._value[-1] == '!'
    
    def count_sentences(self):
        if not ( self.is_sentence() or self.is_question() or self.is_exclamation() ) :
            return 0
        
        sentences = self._value.split(".")
        print(sentences)

        questions_and_sentences = []
        for potential_question in sentences:
            questions_and_sentences += potential_question.split("?")
        
        questions_and_sentences_and_exclamations = []


        for potential_exclamation in questions_and_sentences:
            questions_and_sentences_and_exclamations += potential_exclamation.split("!")

        
        total_sentences = len(questions_and_sentences_and_exclamations)
        for sentence in questions_and_sentences_and_exclamations:
            if sentence == "":
                total_sentences -= 1
        return total_sentences
      

    value = property(get_value, set_value,)
  
