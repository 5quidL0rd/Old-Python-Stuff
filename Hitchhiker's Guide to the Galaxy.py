book = "The Hitchhiker's Guide to the Galaxy"
booklist = list(book)
booklist[0:3]
''.join(booklist[0:3])
''.join(booklist[-6:])
backwards = booklist[: : -1]
''.join(backwards)
every_other = booklist[: : 2]
''.join(every_other)
''.join(booklist[4:14])
''.join(booklist[13:3:-1])

