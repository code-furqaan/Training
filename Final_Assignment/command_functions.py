
from Users import *
from Authors import *
from Books import *
from Reviews import *

def help(d):
    print('\n--Following are the executable commands--')
    for k, v in d.items():
        print(k)


command_functions = {}
command_functions["add_authors"] = add_author
command_functions["remove_authors"] = remove_author
command_functions["get_author_by_id"] = author_by_id
command_functions["get_all_authors"] = get_all_authors
command_functions["update_authors"] = update_author
command_functions["get_author_reviews"] = get_author_review
command_functions["add_books"] = add_book
command_functions["add_book_review"] = add_book_review
command_functions["remove_books"] = remove_book
command_functions["get_all_books"] = get_all_books
command_functions["get_book_by_authorid"] = get_books_by_authorid
command_functions["get_book_reviews"] = get_book_review
command_functions["add_book_review"] = add_book_review
command_functions["get_all_review"] = get_all_reviews
command_functions["add_user"] = add_new_user
command_functions["get_all_user"] = get_all_users
command_functions["get_user_review"] = get_user_review
command_functions["help"] = help