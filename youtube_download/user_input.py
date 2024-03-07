from utility import *
import file_operations as f
import os

def mode_select(modes: dict) -> str:

    question = f"\nPlease select mode (1 - {len(modes)})"
    for i, name in enumerate(modes):
        question += f"\n({i + 1}) {name}"

    question += "\n(-1) Quit\n>"

    while True:

        try:
            mode = int(input(question))

            if mode == -1:
                quit()

            elif mode >= 1 and mode <= len(modes):
                return list(modes)[mode-1]

        except ValueError:
            print("\nMode not found. Please try again")


# def selection_single(text: str, number_of_items: int, array: list, selection: list, selected_indexs: set) -> None:
#     n = int(text)

#     if check_num_range(n, 1, number_of_items):
#         i = n-1
#         if i not in selected_indexs:
#             selection.append(array[i])
#             selected_indexs.add(i)


# def selection_range(text: str, number_of_items: int, array: list, selection: list, selected_indexs: set) -> None:
#     start, end = text.split("-")

#     try:
#         start_i = int(start)
#         end_i = int(end)

#     except ValueError:
#         # add a statment here
#         pass

#     if start_i < end_i and check_num_range(start_i, 1, number_of_items) and check_num_range(end_i, 1, number_of_items):
#         start_i -= 1
#         index_range = range(start_i, end_i)
#         for i in index_range:
#             if i in selected_indexs:
#                 continue
#             else:
#                 selection.append(array[i])
#                 selected_indexs.add(i)


# def get_selection(array) -> list:

#     selected_indexs: set[int]
#     selection: list

#     selected_indexs = set()
#     number_of_items = len(array)
#     selection = []
#     answer = get_input("Enter selection (1-10 5)",
#                        default="all").lower().strip()

#     if answer == "all":
#         return array

#     answer = answer.split()

#     # print(answer)

#     for text in answer:

#         if len(text.split("-")) == 2:
#             selection_range(text, number_of_items, array,
#                             selection, selected_indexs)

#         elif text.isdigit():

#             selection_single(text, number_of_items, array,
#                              selection, selected_indexs)

#     return selection


class SelectionFromNumber:
    def __init__(self, array) -> None:
        self.array = array
        self.length = len(self.array)
        self.selection: list = []
        self.selected_index: set[int] = set()
        self.all = False

    def prompt(self) -> None:
        self.answer = get_input("Enter selection (1-10 5)",
                                default="all").lower().strip().split()

    def selection_range(self, string):
        start, end = string.split("-")

        if not (start.isdigit() and end.isdigit()):
            return

        start_i = int(start) - 1
        end_i = int(end) - 1

        if start_i < end_i and check_num_range(start_i, 0, self.length-1) and \
                check_num_range(end_i, 0, self.length-1):
            self.selected_index.update(
                set([i for i in range(start_i, end_i+1)]))

    def selection_single(self, string):
        number = int(string)

        if check_num_range(number, 1, self.length):
            i = number - 1
            self.selected_index.add(i)

    def prompt_process(self) -> None:
        if self.answer[0] == "all" and len(self.answer) == 1:
            self.all = True
            return

        for item in self.answer:
            if len(item.split("-")) == 2:
                self.selection_range(item)

            elif item.isdigit():
                self.selection_single(item)

    def make_selection(self):
        if self.all:
            self.selection = self.array
            return

        else:
            indexs = list(self.selected_index)
            indexs.sort()
            self.selection = [self.array[i] for i in indexs]


def get_selection(array) -> list:
    sel = SelectionFromNumber(array)
    sel.prompt()
    sel.prompt_process()
    sel.make_selection()

    return sel.selection


def get_input(question, default=None):

    if default is not None:
        question += f". Default is {str(default)}."

    question = "\n" + question + "\n>"
    while True:

        answer = input(question)
        if answer:
            return answer

        if default is not None:
            return default


def get_num(question, default=None):

    while True:
        answer = get_input(question, default)
        if answer.isdigit():
            return answer
        else:
            print("Enter a positve integer")


def get_confirm(question, default=None):

    question += " [y/n]"

    while True:
        answer = get_input(question, default)

        if answer.lower().strip() in ["yes", "y"]:
            return True

        elif answer.lower().strip() in ["no", "n"]:
            return False

# change to path.lib library and use relative path
def get_download_dir(folder_name):

    while True:
        # anwser = get_input(
        #     "Enter download directory",
        #     os.path.join(os.path.expanduser("~"), "Videos")
        # )
        # implemant path checking


        download_dir = f.get_dir("Enter download path", os.path.join(os.path.expanduser("~"), "Videos"))

        
        if download_dir is None:
            print(f"Error. Folder not found")
            continue

        if folder_name:
            created_path = os.path.join(download_dir, folder_name)
            if get_confirm(f"Create folder for playlist at({created_path})"):
                os.mkdir(created_path)

                download_dir = created_path



        print(f"saving to {download_dir}")

        if get_confirm("Confirm location", "y"):
    
            return download_dir



def get_links():
    links = get_input("Enter links sperated by space")
    return links.split()
