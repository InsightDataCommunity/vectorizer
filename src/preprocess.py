import logging
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
import utilities

class PreprocessText():
    def __init__(self, dataframe):
        # TODO Do we want to assume this takes in a dataframe?
        self.log = logging.getLogger('Enron_email_analysis.preprocess')
        self.preprocessed_text = self.preprocess(dataframe)


    def preprocess(self, dataframe):
        # TODO: Find a way to run these all at once. Doing these individually is inefficient.
        # TODO: Consider using *args or *kwargs
        # TODO: Assuming we want to run these all right now. Use true false to indicate whether to run in future.
        # TODO: Bad naming of dataframeX below.
        # TODO: These functions still need to be fully tested.
        # TODO: Add try excepts to all functions to be able to tell what fails.
        # TODO: Add logging saying each function succeeded if it did.
        # TODO: Make all quotes same type.

        self.log.info("In preprocess function.")
        dataframe1 = self.lowercase(dataframe)
        dataframe2 = self.remove_special_characters(dataframe1)
        self.remove_stop_words(dataframe2) # Doesn't return anything for now
        dataframe3 = self.remove_website_links(dataframe2)
        dataframe4 = self.tokenize(dataframe3)

        self.log.info(f"Sample of preprocessed data: {dataframe4.head()}")

        return dataframe4

    def lowercase(self, dataframe):
        logging.info("Converting dataframe to lowercase")
        lowercase_dataframe = dataframe.apply(lambda x: x.lower())
        return lowercase_dataframe

    def remove_special_characters(self, dataframe):
        self.log.info("Removing special characters from dataframe")
        no_special_characters = dataframe.replace(r'[^A-Za-z0-9 ]+', '', regex=True)
        return no_special_characters

    def remove_numbers(self, dataframe):
        self.log.info("Removing numbers from dataframe")
        removed_numbers = dataframe.str.replace(r'\d+','')
        return removed_numbers

    def remove_whitespace(self, dataframe):
        self.log.info("Removing whitespace from dataframe")
        # replace more than 1 space with 1 space
        merged_spaces = dataframe.str.replace(r"\s\s+",' ')
        # delete beginning and trailing spaces
        trimmed_spaces = merged_spaces.apply(lambda x: x.str.strip())
        return trimmed_spaces

    def remove_stop_words(self, dataframe):
        # TODO: An option to pass in a custom list of stopwords would be cool.
        set(stopwords.words('english'))

    def remove_website_links(self, dataframe):
        self.log.info("Removing website links from dataframe")
        no_website_links = dataframe.str.replace(r"http\S+", "")
        return no_website_links

    def tokenize(self, dataframe):
        tokenized_dataframe = dataframe.apply(lambda row: word_tokenize(row))
        return tokenized_dataframe

    def remove_emails(self, dataframe):
        # TODO: Not a priority right now. Come back to it later.
        return dataframe

    def expand_contractions(self, dataframe):
        # TODO: Not a priority right now. Come back to it later.
        return dataframe
