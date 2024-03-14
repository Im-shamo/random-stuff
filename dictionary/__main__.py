import sys
sys.path.insert(0,"C:\\Users\\shamo\Github\\random-stuff")
print(sys.path)


from PyMultiDictionary import MultiDictionary
from youtube_download import user_input as usr

class Dict:
    def prompt(self):
        answer = usr.get_input("Enter words")
        self.words: list[str] = answer.strip().split()

    def meaning_en(self):
        self.dict: list[dict[str]] = []
        for word in self.words:
            dictionary = MultiDictionary()
            meaning = dictionary.meaning("en", word)
            self.dict.append({"word": word, "en":meaning})


    

def main():
    dict=Dict()
    dict.prompt()
    dict.meaning_en()
    print(f"{dict.dict=}")

if __name__ == "__main__":
    main()