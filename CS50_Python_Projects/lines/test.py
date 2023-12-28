def check_argv():
    if len(argv) == 1:
        exit("Too few command_line arguments")
    if len(argv) > 2:
        exit("Too many '#' command_line arguments")
    try:
        if argv[1].endswith(".py") == False: #hello
            exit("Not a python file")
    except FileNotFoundError:
        #starts with a comment

        exit("File does not exist")
        count = "#"
#hello world
             #hello

 'hello world'
        #hello